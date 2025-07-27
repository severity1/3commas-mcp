# CLAUDE.md for api/

## Context Activation
Activates when working in `api/` directory implementing HTTP client for 3Commas API integration.

**Companions**: tools/ (usage), models/ (requests), utils/ (auth/helpers)

## Implementation Overview

### Core Components
- **client.py**: `api_request()` function with complete 3Commas integration
- **Authentication**: HMAC-SHA256 signature via utils/auth.py
- **Rate limiting**: Integration with utils/decorators.py RateLimiter
- **Health check**: `health_check()` for API connectivity validation

## Implementation Requirements

### API Request Pattern
The `api_request()` function handles all API interactions:
- **Path/Method**: API endpoint path and HTTP method
- **Authentication**: Automatic signature generation
- **Parameters**: Query parameters and request body for trading operations
- **Rate limiting**: Built-in compliance with exponential backoff

### 3Commas Authentication
Required header format:
- **Apikey**: API key header for request identification
- **Signature**: HMAC-SHA256 signature of query string
- **Content-Type**: application/json for POST/PATCH requests

### Response Handling
- **Success**: 200/201 return API data; 204 returns success status
- **Error handling**: HTTP status errors, auth failures, rate limiting
- **Security**: Never logs API keys/secrets, proper error redaction

### Rate Limiting Compliance
3Commas limits by endpoint type:
- **Standard endpoints**: 300 requests/minute
- **Trading endpoints**: 60 requests/minute  
- **Statistics endpoints**: 120 requests/minute
- **Exponential backoff**: Required for 429 responses

## Integration Requirements

### Usage Standards
- Always use with `@handle_api_errors` decorator
- Environment management via `get_3commas_credentials()`
- Payload creation using utils/payload.py utilities
- Signature generation via utils/auth.py

### Trading Safety
- **Bot operations**: Validate configuration before creation/modification
- **Deal operations**: Safety checks for cancellation and modifications
- **Destructive operations**: Require explicit confirmation
- **Account validation**: Verify exchange permissions before operations

## Development Workflow

### Implementation Steps
1. Define request patterns following 3Commas authentication requirements
2. Implement HMAC-SHA256 signature generation
3. Add error handling with trading context
4. Handle rate limiting with exponential backoff
5. Test: success, error, rate limiting, authentication scenarios

### Quality Checklist
- [ ] HMAC-SHA256 authentication and signature generation
- [ ] Rate limiting compliance with exponential backoff
- [ ] Security guidelines for API key/secret management
- [ ] Tests cover success, error, rate limiting, authentication failures