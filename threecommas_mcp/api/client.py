"""3Commas API client"""

import asyncio
import logging
from typing import Optional, Dict, TypeVar, Union, Any
import httpx
from pydantic import BaseModel

from ..utils import (
    get_3commas_credentials,
    get_api_base_url,
    validate_environment,
    sign_request,
    handle_api_errors,
)
from ..utils.decorators import _rate_limiter

logger = logging.getLogger(__name__)

# Type variable for generic request models
ReqT = TypeVar("ReqT", bound=BaseModel)


def detect_endpoint_type(path: str, method: str) -> str:
    """Detect endpoint type for rate limiting based on official 3Commas limits.

    Official rate limits from https://developers.3commas.io/quick-start/limits:
    - Global: 100 req/min
    - /ver1/deals: 120 req/min
    - /ver1/smart_trades: 40 req/10 seconds
    - /ver1/deals/:deal_id/show: 120 req/min
    """
    # Specific endpoint patterns with higher limits
    if "/ver1/deals" in path and not path.endswith("/show"):
        return "deals"

    if "/ver1/smart_trades" in path:
        return "smart_trades"

    if "/ver1/deals/" in path and path.endswith("/show"):
        return "deals_show"

    # Default to global limit (100 req/min)
    return "global"


@handle_api_errors
async def api_request(
    path: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Union[Dict[str, Any], BaseModel, None] = None,
    endpoint_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Make a request to the 3Commas API with proper authentication and rate limiting."""
    # Validate environment
    missing_vars = validate_environment()
    if missing_vars:
        return {
            "error": f"Missing required environment variables: {', '.join(missing_vars)}"
        }

    # Get credentials and base URL
    api_key, secret = get_3commas_credentials()
    if not api_key or not secret:
        return {"error": "API credentials not configured"}

    base_url = get_api_base_url()

    # Determine endpoint type for rate limiting
    if endpoint_type is None:
        endpoint_type = detect_endpoint_type(path, method)

    # Rate limiting check
    if not _rate_limiter.can_make_request(endpoint_type):
        wait_time = _rate_limiter.get_wait_time(endpoint_type)
        logger.info(
            f"Rate limit reached for {endpoint_type} endpoints. Waiting {wait_time:.2f}s"
        )
        await asyncio.sleep(wait_time)

    # Convert Pydantic models to dict
    request_data = None
    if data is not None:
        request_data = (
            data.model_dump(exclude_unset=True) if isinstance(data, BaseModel) else data
        )

    # Prepare request parameters
    request_params = params or {}
    json_body = None

    # For POST/PATCH requests, data goes in body
    if method in ("POST", "PATCH") and request_data:
        json_body = request_data
        request_params = params or {}
    # For GET/DELETE requests, data goes in query params
    elif request_data:
        request_params.update(request_data)

    try:
        # Generate authentication headers
        import json

        auth_headers = sign_request(
            api_key,
            secret,
            path,
            params=request_params if method in ("GET", "DELETE") else None,
            body=json.dumps(json_body) if json_body else None,
        )

        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            **auth_headers,  # Apikey and Signature headers
        }

        # Make the request
        async with httpx.AsyncClient(timeout=30.0) as client:
            url = f"{base_url}/{path}"

            kwargs: Dict[str, Any] = {
                "headers": headers,
                "params": request_params if method in ("GET", "DELETE") else None,
            }

            if json_body:
                kwargs["json"] = json_body

            logger.debug(
                f"Making {method} request to {url} (endpoint_type: {endpoint_type})"
            )
            response = await client.request(method, url, **kwargs)

            # Record successful request for rate limiting
            _rate_limiter.record_request(endpoint_type)

            # Handle 204 No Content responses
            if response.status_code == 204:
                return {"status": "success", "status_code": 204}

            # Handle successful responses with content
            if 200 <= response.status_code < 300:
                try:
                    json_data = response.json()
                    # Ensure we return a dict as specified in the function signature
                    if not isinstance(json_data, dict):
                        json_data = {"data": json_data}
                    return json_data
                except ValueError:
                    # If JSON parsing fails but status is success, return the text
                    return {"content": response.text}

            # Handle API errors
            try:
                error_data = response.json()
                if isinstance(error_data, dict) and "error" in error_data:
                    return {"error": f"API error: {error_data['error']}"}
                return {"error": f"API error {response.status_code}: {error_data}"}
            except ValueError:
                return {"error": f"API error {response.status_code}: {response.text}"}

    except httpx.RequestError as e:
        logger.error(f"Network error while making request to {path}: {e}")
        return {"error": f"Network error: {str(e)}"}
    except ValueError as e:
        logger.error(f"Failed to parse JSON response from {path}: {e}")
        return {"error": f"Failed to parse JSON response: {str(e)}"}
    except Exception as e:
        logger.error(f"Unexpected error while making request to {path}: {e}")
        return {"error": f"Unexpected error: {str(e)}"}


async def health_check() -> Dict[str, Any]:
    """Perform a health check by testing API connectivity."""
    try:
        # Test with a simple endpoint that doesn't require trading permissions
        response = await api_request("ver1/accounts", method="GET")

        if "error" in response:
            return {"status": "unhealthy", "error": response["error"]}

        return {
            "status": "healthy",
            "api_base_url": get_api_base_url(),
            "credentials_configured": validate_environment() == [],
        }

    except Exception as e:
        return {"status": "unhealthy", "error": f"Health check failed: {str(e)}"}
