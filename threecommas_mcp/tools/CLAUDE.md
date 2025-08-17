# Tool Patterns

**Context**: MCP tool functions for 3Commas API with consistent error handling and filtering

## Component Focus
- **Function signatures** - Standard async functions with response_filter parameter
- **Error handling** - @handle_api_errors decorator from utils.decorators  
- **Request validation** - Pydantic models with to_query_params() method

## Required Patterns
1. **Use @handle_api_errors decorator** - First decorator for consistent error handling
2. **Include response_filter parameter** - Default "display" for token optimization
3. **Pydantic request models** - Instantiate with function parameters
4. **Apply filter_response()** - Before returning API response

## Import Pattern
```python
from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse
from ..models.dca_bots import GetDCABotListRequest
```

## Code Examples
```python
@handle_api_errors
async def get_dca_bot_list(
    account_id: int = 0, 
    strategy: str | None = None,
    response_filter: str = "display"
) -> APIResponse:
    """Get all DCA bots with status and configuration."""
    
    request = GetDCABotListRequest(
        account_id=account_id,
        strategy=strategy, 
        response_filter=response_filter
    )
    response = await api_request("ver1/bots", params=request.to_query_params())
    return filter_response(response, request.response_filter)
```

## Integration Requirements
- All tool functions use @handle_api_errors as first decorator
- All functions include response_filter: str = "display" parameter
- Use request model to_query_params() for API parameter building
- Apply filter_response() before returning data to optimize tokens