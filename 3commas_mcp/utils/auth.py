"""HMAC-SHA256 authentication utilities for 3Commas API"""

import hashlib
import hmac
from typing import Dict, Any, Optional
from urllib.parse import urlencode


def generate_signature(query_string: str, secret: str) -> str:
    """Generate HMAC-SHA256 signature for 3Commas API authentication.
    
    Args:
        query_string: URL-encoded query string or request body
        secret: 3Commas API secret key
        
    Returns:
        HMAC-SHA256 signature as hexadecimal string
        
    Example:
        >>> secret = "my_secret_key"
        >>> query = "account_id=123&pair=BTCUSDT"
        >>> signature = generate_signature(query, secret)
    """
    return hmac.new(
        secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


def build_query_string(params: Optional[Dict[str, Any]]) -> str:
    """Build properly formatted query string for signature generation.
    
    Args:
        params: Dictionary of parameters to encode
        
    Returns:
        URL-encoded query string sorted by key for consistent signatures
        
    Example:
        >>> params = {"account_id": 123, "pair": "BTCUSDT", "amount": 10.5}
        >>> query = build_query_string(params)
        >>> # Returns: "account_id=123&amount=10.5&pair=BTCUSDT"
    """
    if not params:
        return ""
    
    # Sort parameters by key for consistent signature generation
    sorted_params = sorted(params.items())
    return urlencode(sorted_params)


def create_auth_headers(api_key: str, signature: str) -> Dict[str, str]:
    """Create authentication headers for 3Commas API requests.
    
    Args:
        api_key: 3Commas API key
        signature: HMAC-SHA256 signature generated from request data
        
    Returns:
        Dictionary containing APIKEY and APISIGN headers
        
    Example:
        >>> headers = create_auth_headers("my_api_key", "signature_hash")
        >>> # Returns: {"APIKEY": "my_api_key", "APISIGN": "signature_hash"}
    """
    return {
        "APIKEY": api_key,
        "APISIGN": signature
    }


def sign_request(
    api_key: str, 
    secret: str, 
    params: Optional[Dict[str, Any]] = None,
    body: Optional[str] = None
) -> Dict[str, str]:
    """Generate complete authentication headers for a 3Commas API request.
    
    Args:
        api_key: 3Commas API key
        secret: 3Commas API secret key
        params: Query parameters (for GET requests)
        body: Request body (for POST/PATCH requests)
        
    Returns:
        Dictionary containing authentication headers
        
    Example:
        >>> # For GET request with query parameters
        >>> headers = sign_request(api_key, secret, params={"account_id": 123})
        
        >>> # For POST request with body
        >>> headers = sign_request(api_key, secret, body='{"name": "My Bot"}')
    """
    # Use body if provided, otherwise build query string from params
    data_to_sign = body if body else build_query_string(params)
    signature = generate_signature(data_to_sign, secret)
    return create_auth_headers(api_key, signature)


def validate_credentials(api_key: Optional[str], secret: Optional[str]) -> bool:
    """Validate that API credentials are present and properly formatted.
    
    Args:
        api_key: 3Commas API key to validate
        secret: 3Commas API secret to validate
        
    Returns:
        True if credentials appear valid, False otherwise
    """
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