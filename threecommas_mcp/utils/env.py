"""Environment variable management for 3Commas MCP"""

import os
from typing import Optional, Tuple


def get_3commas_credentials() -> Tuple[Optional[str], Optional[str]]:
    """Get 3Commas API credentials from environment."""
    api_key = os.getenv("3COMMAS_API_KEY")
    secret_key = os.getenv("3COMMAS_SECRET_KEY")
    return api_key, secret_key


def should_enable_destructive_ops() -> bool:
    """Check if destructive operations should be enabled."""
    env_value = os.getenv("3COMMAS_ENABLE_DESTRUCTIVE", "false").lower().strip()
    return env_value in ("true", "1", "yes", "on")


def get_rate_limits() -> dict[str, int]:
    """Get 3Commas API rate limits configuration."""
    return {
        "standard": int(os.getenv("3COMMAS_RATE_LIMIT_STANDARD", "300")),
        "trading": int(os.getenv("3COMMAS_RATE_LIMIT_TRADING", "60")),
        "stats": int(os.getenv("3COMMAS_RATE_LIMIT_STATS", "120")),
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
