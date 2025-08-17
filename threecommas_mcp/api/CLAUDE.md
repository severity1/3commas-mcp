# API Client Patterns

**Context**: 3Commas API client with HMAC-SHA256 authentication and rate limiting

## Component Focus
- **API request function** - Single api_request() interface for all endpoints
- **Rate limiting** - Automatic endpoint detection and limit application
- **Authentication** - HMAC-SHA256 signing with credential protection

## Required Patterns
1. **Use api_request() exclusively** - Never implement direct HTTP calls
2. **Endpoint format** - Use "ver1/bots" format (exclude base URL)
3. **Rate limit compliance** - Automatic detection based on endpoint patterns

## Rate Limiting Specifics
- **Global endpoints**: 100 requests/minute (default)
- **Deals endpoints** (/ver1/deals): 120 requests/minute  
- **SmartTrades endpoints** (/ver1/smart_trades): 40 requests/10 seconds
- **Deal details** (/ver1/deals/:id/show): 120 requests/minute

## Code Examples
```python
from ..api.client import api_request

# Standard API call
response = await api_request(
    "ver1/bots",
    params={"account_id": 123, "strategy": "long"}
)

# Endpoint detection automatically applies rate limits
response = await api_request("ver1/deals/123/show")  # 120/min limit
response = await api_request("ver1/smart_trades")    # 40/10s limit
```

## Integration Requirements
- Always use api_request() function from api.client
- Authentication handled automatically via HMAC-SHA256
- Rate limiting applied automatically via detect_endpoint_type()
- Credentials never logged or exposed in responses