# Utility Patterns

**Context**: Core utilities for error handling, response filtering, and authentication

## Component Focus
- **Error handling** - @handle_api_errors decorator from decorators.py
- **Response filtering** - filter_response() from response_filter.py for token optimization
- **Environment validation** - validate_environment() from env.py

## Required Patterns
1. **Use @handle_api_errors decorator** - Consistent error formatting for all tools
2. **Apply filter_response()** - Before returning data (85% token reduction on display)
3. **Environment validation** - Automatic validation on import

## Available Utilities
- **decorators.py**: handle_api_errors() with consistent {"error": "message"} formatting
- **response_filter.py**: filter_response() with security and token optimization
- **auth.py**: sign_request() for HMAC-SHA256 authentication (automatic via api_request)
- **env.py**: validate_environment() and credential management

## Code Examples
```python
# Error handling decorator
from ..utils.decorators import handle_api_errors

@handle_api_errors
async def tool_function():
    # Catches ValueError, Exception, returns {"error": "message"}
    # Maintains type safety with proper Dict[str, Any] return

# Response filtering
from ..utils.response_filter import filter_response

filtered = filter_response(api_response, "display")
# - Removes sensitive fields (url_secret, account_id)
# - Optimizes arrays and objects for display (85% token reduction)

# Environment validation (automatic)
from ..utils import validate_environment  # Validates on import
```

## Integration Requirements
- All MCP tools use @handle_api_errors as first decorator
- All responses filtered with filter_response() before return
- Authentication handled automatically via api_request() (no manual HMAC)
- Environment validated automatically on module import