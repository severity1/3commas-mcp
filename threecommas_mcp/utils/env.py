"""Environment variable management for 3Commas MCP"""

import os


def get_3commas_credentials() -> tuple[str | None, str | None]:
    """Get 3Commas API credentials from environment."""
    api_key = os.getenv("3COMMAS_API_KEY")
    secret_key = os.getenv("3COMMAS_SECRET_KEY")
    return api_key, secret_key


def should_enable_destructive_ops() -> bool:
    """Check if destructive operations should be enabled."""
    env_value = os.getenv("3COMMAS_ENABLE_DESTRUCTIVE", "false").lower().strip()
    return env_value in ("true", "1", "yes", "on")


def get_rate_limits() -> dict[str, dict[str, int]]:
    """Get 3Commas API rate limits configuration based on official limits.

    Returns rate limits with time windows in seconds and request counts.
    Official limits from https://developers.3commas.io/quick-start/limits
    """
    return {
        "global": {
            "requests": int(os.getenv("3COMMAS_RATE_LIMIT_GLOBAL", "100")),
            "window": 60,  # 100 requests per minute
        },
        "deals": {
            "requests": int(os.getenv("3COMMAS_RATE_LIMIT_DEALS", "120")),
            "window": 60,  # 120 requests per minute
        },
        "smart_trades": {
            "requests": int(os.getenv("3COMMAS_RATE_LIMIT_SMART_TRADES", "40")),
            "window": 10,  # 40 requests per 10 seconds
        },
        "deals_show": {
            "requests": int(os.getenv("3COMMAS_RATE_LIMIT_DEALS_SHOW", "120")),
            "window": 60,  # 120 requests per minute
        },
    }


def validate_environment() -> list[str]:
    """Validate that required environment variables are set."""
    missing = []
    api_key, secret_key = get_3commas_credentials()

    if not api_key:
        missing.append("3COMMAS_API_KEY")
    if not secret_key:
        missing.append("3COMMAS_SECRET_KEY")

    return missing


def get_api_base_url() -> str:
    """Get 3Commas API base URL."""
    return os.getenv("3COMMAS_API_BASE_URL", "https://api.3commas.io/public/api")
