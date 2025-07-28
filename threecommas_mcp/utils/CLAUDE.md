# CLAUDE.md for @utils/

## Context Activation
Activates when implementing authentication, error handling, and validation utilities.

## Core Functions (used by all tools)
- `handle_api_errors` (@threecommas_mcp/utils/decorators.py:11) - Error handling decorator
- `filter_response()` (@threecommas_mcp/utils/response_filter.py:13) - Token optimization, 85% reduction
- Authentication via `api_request()` integration (@threecommas_mcp/utils/auth.py exports)

## Key Utilities
### Error Handling (@threecommas_mcp/utils/decorators.py:11-40)
- Consistent error formatting: `{"error": "message"}`
- Security: Never exposes sensitive information

### Response Filtering (@threecommas_mcp/utils/response_filter.py:13-41)  
- Security filter: Always removes `url_secret`, `account_id` (line 49)
- Display filter: Removes crypto_widget, reduces arrays (line 59-87)

### Rate Limiting (@threecommas_mcp/utils/decorators.py:135-204)
- Global: 100/min, Deals: 120/min, SmartTrades: 40/10s (line 146-147)
- Exponential backoff for rate limit handling