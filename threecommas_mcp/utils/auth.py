"""HMAC-SHA256 authentication utilities for 3Commas API"""

import hashlib
import hmac
from typing import Dict, Any
from urllib.parse import urlencode


def generate_signature(query_string: str, secret: str) -> str:
    """Generate HMAC-SHA256 signature for 3Commas API authentication."""
    return hmac.new(
        secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()


def build_query_string(params: Dict[str, Any] | None) -> str:
    """Build URL-encoded query string sorted by key for consistent signatures."""
    if not params:
        return ""

    # Sort parameters by key for consistent signature generation
    sorted_params = sorted(params.items())
    return urlencode(sorted_params)


def create_auth_headers(api_key: str, signature: str) -> Dict[str, str]:
    """Create Apikey and Signature headers for 3Commas API requests."""
    return {"Apikey": api_key, "Signature": signature}


def sign_request(
    api_key: str,
    secret: str,
    path: str,
    params: Dict[str, Any] | None = None,
    body: str | None = None,
) -> Dict[str, str]:
    """Generate complete authentication headers for a 3Commas API request."""
    # For GET requests, sign path + query string
    # For POST/PATCH requests, sign path + body
    # 3Commas requires signature to include full API path including /public/api prefix
    full_path = f"/public/api/{path.lstrip('/')}"

    if body:
        data_to_sign = full_path + body
    else:
        query_string = build_query_string(params)
        data_to_sign = full_path + (f"?{query_string}" if query_string else "")

    signature = generate_signature(data_to_sign, secret)
    return create_auth_headers(api_key, signature)


def validate_credentials(api_key: str | None, secret: str | None) -> bool:
    """Validate that API credentials are present and properly formatted."""
    if not api_key or not secret:
        return False

    # Basic format validation - 3Commas keys are typically 32+ chars
    if len(api_key) < 32 or len(secret) < 32:
        return False

    # Check for common placeholder values
    placeholder_values = ["your_api_key", "your_secret_key", "test", "example"]
    if api_key.lower() in placeholder_values or secret.lower() in placeholder_values:
        return False

    return True
