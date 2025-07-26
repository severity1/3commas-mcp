"""Decorators and utility functions for 3Commas MCP"""

import asyncio
import time
from functools import wraps
from typing import Callable, Any, Dict, Awaitable, cast

from .env import validate_environment


def handle_api_errors(
    func: Callable[..., Awaitable[Dict[str, Any]]],
) -> Callable[..., Awaitable[Dict[str, Any]]]:
    """Decorator to handle API errors consistently.

    Provides consistent error formatting for all API operations.
    Catches common exceptions and returns them in standard format.

    Returns:
        {"error": "error message"} for failures
        Original response for successful operations
    """

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Dict[str, Any]:
        try:
            result = await func(*args, **kwargs)
            # Cast ensures type safety when func might return subclass of Dict
            return cast(Dict[str, Any], result)
        except ValueError as e:
            return {"error": f"Validation error: {str(e)}"}
        except ConnectionError as e:
            return {"error": f"Connection error: {str(e)}"}
        except TimeoutError as e:
            return {"error": f"Request timeout: {str(e)}"}
        except Exception as e:
            # Never expose sensitive information in error messages
            return {"error": f"API operation failed: {str(e)}"}

    return wrapper


def rate_limit_retry(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
) -> Callable[
    [Callable[..., Awaitable[Dict[str, Any]]]], Callable[..., Awaitable[Dict[str, Any]]]
]:
    """Decorator to handle rate limiting with exponential backoff.
    Automatically retries requests when rate limited (HTTP 429) using exponential backoff.
    """

    def decorator(
        func: Callable[..., Awaitable[Dict[str, Any]]],
    ) -> Callable[..., Awaitable[Dict[str, Any]]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Dict[str, Any]:
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    result = await func(*args, **kwargs)

                    # Check if result indicates rate limiting
                    if isinstance(result, dict) and "error" in result:
                        error_msg = result["error"].lower()
                        if "rate limit" in error_msg or "429" in error_msg:
                            if attempt < max_retries:
                                delay = min(
                                    base_delay * (exponential_base**attempt), max_delay
                                )
                                await asyncio.sleep(delay)
                                continue

                    return result

                except Exception as e:
                    last_exception = e
                    # Check if it's a rate limiting exception
                    if hasattr(e, "status_code") and e.status_code == 429:
                        if attempt < max_retries:
                            delay = min(
                                base_delay * (exponential_base**attempt), max_delay
                            )
                            await asyncio.sleep(delay)
                            continue
                    # For non-rate-limit errors, don't retry
                    raise e

            # If we get here, all retries failed
            if last_exception:
                raise last_exception
            return {"error": "Max retries exceeded for rate limited request"}

        return wrapper

    return decorator


def validate_trading_context(
    func: Callable[..., Awaitable[Dict[str, Any]]],
) -> Callable[..., Awaitable[Dict[str, Any]]]:
    """Decorator to validate trading context before API operations."""

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Dict[str, Any]:
        # Check if credentials are available
        missing_vars = validate_environment()
        if missing_vars:
            return {
                "error": f"Missing required environment variables: {', '.join(missing_vars)}"
            }

        # Check if this appears to be a destructive operation
        func_name = func.__name__.lower()
        destructive_operations = ["delete", "cancel", "panic", "disable"]

        if any(op in func_name for op in destructive_operations):
            from .env import should_enable_destructive_ops

            if not should_enable_destructive_ops():
                return {
                    "error": f"Destructive operation '{func.__name__}' is disabled. "
                    f"Set 3COMMAS_ENABLE_DESTRUCTIVE=true to enable."
                }

        # Call the original function
        return await func(*args, **kwargs)

    return wrapper


class RateLimiter:
    """Rate limiter for 3Commas API endpoints."""

    def __init__(self) -> None:
        self._requests: Dict[str, list[float]] = {
            "standard": [],
            "trading": [],
            "stats": [],
        }
        from .env import get_rate_limits

        self._limits = get_rate_limits()

    def can_make_request(self, endpoint_type: str = "standard") -> bool:
        """Check if a request can be made without exceeding rate limits."""
        if endpoint_type not in self._limits:
            endpoint_type = "standard"

        current_time = time.time()
        window_start = current_time - 60  # 1-minute window

        # Clean old requests outside the window
        self._requests[endpoint_type] = [
            req_time
            for req_time in self._requests[endpoint_type]
            if req_time > window_start
        ]

        # Check if we're under the limit
        return len(self._requests[endpoint_type]) < self._limits[endpoint_type]

    def record_request(self, endpoint_type: str = "standard") -> None:
        """Record that a request was made."""
        if endpoint_type not in self._limits:
            endpoint_type = "standard"

        self._requests[endpoint_type].append(time.time())

    def get_wait_time(self, endpoint_type: str = "standard") -> float:
        """Get time to wait before next request can be made."""
        if self.can_make_request(endpoint_type):
            return 0.0

        # Find the oldest request in the current window
        current_time = time.time()
        window_start = current_time - 60

        old_requests = [
            req_time
            for req_time in self._requests[endpoint_type]
            if req_time > window_start
        ]

        if not old_requests:
            return 0.0

        # Wait until the oldest request falls outside the window
        oldest_request = min(old_requests)
        return max(0.0, (oldest_request + 60) - current_time)


# Global rate limiter instance
_rate_limiter = RateLimiter()
