"""Environment variable management for 3Commas MCP"""

import os
from typing import Optional, Tuple


def get_3commas_credentials() -> Tuple[Optional[str], Optional[str]]:
    """Get 3Commas API credentials from environment.
    
    Returns:
        Tuple of (api_key, secret_key) from environment variables
        
    Environment Variables:
        3COMMAS_API_KEY: Your 3Commas API key
        3COMMAS_SECRET_KEY: Your 3Commas secret key
    """
    api_key = os.getenv("3COMMAS_API_KEY")
    secret_key = os.getenv("3COMMAS_SECRET_KEY")
    return api_key, secret_key


def should_enable_destructive_ops() -> bool:
    """Check if destructive operations should be enabled.
    
    Destructive operations include:
    - Bot deletion
    - Deal cancellation
    - Emergency panic sell operations
    
    Returns:
        True if destructive operations are enabled, False otherwise
        
    Environment Variables:
        3COMMAS_ENABLE_DESTRUCTIVE: Set to "true", "1", "yes", or "on" to enable
    """
    env_value = os.getenv("3COMMAS_ENABLE_DESTRUCTIVE", "false").lower().strip()
    return env_value in ("true", "1", "yes", "on")


def get_rate_limits() -> dict[str, int]:
    """Get 3Commas API rate limits configuration.
    
    Returns:
        Dictionary with rate limits per endpoint type
        
    Environment Variables:
        3COMMAS_RATE_LIMIT_STANDARD: Standard endpoints (default: 300 req/min)
        3COMMAS_RATE_LIMIT_TRADING: Trading endpoints (default: 60 req/min)  
        3COMMAS_RATE_LIMIT_STATS: Statistics endpoints (default: 120 req/min)
    """
    return {
        "standard": int(os.getenv("3COMMAS_RATE_LIMIT_STANDARD", "300")),
        "trading": int(os.getenv("3COMMAS_RATE_LIMIT_TRADING", "60")),
        "stats": int(os.getenv("3COMMAS_RATE_LIMIT_STATS", "120")),
    }


def validate_environment() -> list[str]:
    """Validate that required environment variables are set.
    
    Returns:
        List of missing environment variable names, empty if all present
    """
    missing = []
    api_key, secret_key = get_3commas_credentials()
    
    if not api_key:
        missing.append("3COMMAS_API_KEY")
    if not secret_key:
        missing.append("3COMMAS_SECRET_KEY")
        
    return missing


def get_api_base_url() -> str:
    """Get 3Commas API base URL.
    
    Returns:
        Base URL for 3Commas API
        
    Environment Variables:
        3COMMAS_API_BASE_URL: Override default base URL (default: https://api.3commas.io)
    """
    return os.getenv("3COMMAS_API_BASE_URL", "https://api.3commas.io")