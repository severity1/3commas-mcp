# HTTP Client Integration Patterns

**Context**: HTTP client for 3Commas API integration  
**When to Use**: During Root CLAUDE.md Phase 2 implementation for API calls

## Required Usage Pattern
1. **Standard API Call**
   ```python
   from ..api.client import api_request
   
   # Always use api_request() - never implement direct HTTP calls
   response = await api_request(
       endpoint="ver1/bots",
       params={"account_id": 123, "strategy": "long"}
   )
   # Returns: Dict[str, Any] with JSON response
   ```

2. **Endpoint Format**
   ```python
   # Correct endpoint formats:
   endpoint = "ver1/bots"           # Global endpoints
   endpoint = "ver1/deals/123"      # Deal-specific  
   endpoint = "ver1/smart_trades"   # SmartTrade endpoints
   
   # Do NOT include base URL or full path
   ```

3. **Authentication & Security**
   ```python
   # Authentication handled automatically via HMAC-SHA256
   # Rate limiting applied automatically based on endpoint type
   # Credentials never logged or exposed
   ```

## Available Features
- **Authentication**: Automatic HMAC-SHA256 signing
- **Rate Limiting**: Global (100/min), Deals (120/min), SmartTrades (40/10s)  
- **Endpoint Detection**: Automatic classification and rate limit application
- **Response Handling**: JSON/text parsing with error handling
- **Security**: Credential protection and safe logging

## Reference Examples
- **Complete implementation**: client.py:48 (api_request function)

## Integration Notes
- Always use api_request() - never implement direct HTTP calls
- Endpoint format excludes base URL (use "ver1/bots" not full path)
- Authentication and rate limiting handled automatically