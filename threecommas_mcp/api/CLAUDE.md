# CLAUDE.md for api/

## Context Activation
Activates when implementing HTTP client for 3Commas API integration.

## Current Implementation Status
**200 lines in client.py module:**
- `api_request()` - Main HTTP client function (used by all tools)
- `health_check()` - API connectivity validation
- `detect_endpoint_type()` - Endpoint classification for rate limiting

**Exports**: 3 functions in clean __init__.py interface

## Core Function: api_request() (from client.py)
```python
async def api_request(
    path: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    method: str = "GET"
) -> Dict[str, Any]:
```

**Features implemented:**
- Automatic HMAC-SHA256 signature generation via utils/auth.py
- Built-in rate limiting compliance with exponential backoff  
- Endpoint type detection for rate limit classification
- Error handling for HTTP status codes, auth failures, rate limiting
- Security: Never logs API keys/secrets

## Authentication Integration
- Uses `get_3commas_credentials()` from utils/env.py
- Uses `sign_request()` from utils/auth.py for HMAC-SHA256
- Headers: APIKEY and APISIGN for all authenticated requests

## Rate Limiting Implementation
Official 3Commas limits (implemented via detect_endpoint_type):
- **Global**: 100 requests/minute (default)
- **/ver1/deals**: 120 requests/minute  
- **/ver1/smart_trades**: 40 requests per 10 seconds
- **Exponential backoff**: Integrated with utils/decorators.py

## Integration Pattern (verified in tools)
```python
# All tools use this pattern:
response = await api_request("ver1/accounts/market_pairs", params=params, method="GET")
```

## Quality Standards (verified in implementation)
- [ ] HMAC-SHA256 authentication implemented
- [ ] Rate limiting compliance with endpoint detection
- [ ] Security practices (no credential logging)
- [ ] Used consistently by all 5 tool functions