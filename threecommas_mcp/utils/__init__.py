"""Utility functions for 3Commas MCP."""

# Environment and configuration utilities
from .env import (
    get_3commas_credentials,
    should_enable_destructive_ops,
    get_rate_limits,
    validate_environment,
    get_api_base_url,
)

# Authentication utilities
from .auth import (
    generate_signature,
    build_query_string,
    create_auth_headers,
    sign_request,
    validate_credentials,
)

# Decorators for error handling and rate limiting
from .decorators import (
    handle_api_errors,
    rate_limit_retry,
    validate_trading_context,
    RateLimiter,
)

__all__ = [
    # Environment utilities
    "get_3commas_credentials",
    "should_enable_destructive_ops",
    "get_rate_limits",
    "validate_environment",
    "get_api_base_url",
    # Authentication utilities
    "generate_signature",
    "build_query_string",
    "create_auth_headers",
    "sign_request",
    "validate_credentials",
    # Decorators and rate limiting
    "handle_api_errors",
    "rate_limit_retry",
    "validate_trading_context",
    "RateLimiter",
]
