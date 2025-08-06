# Tool Patterns

**Context**: MCP function implementation for 3Commas API operations

## Component Focus
- **MCP function signatures** - Standard async function patterns
- **Decorators** - @handle_api_errors for consistent error handling
- **Response handling** - filter_response() application before return

## Required Patterns
1. **Use @handle_api_errors decorator** - Consistent error handling
2. **Include response_filter parameter** - Token optimization
3. **Pydantic validation** - Use request models for input validation
4. **Apply filter_response()** - Before returning data

## Pattern Example
```python
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..api.client import api_request

@handle_api_errors
async def get_data(param: str, response_filter: str = "display"):
    request = RequestModel(param=param, response_filter=response_filter)
    response = await api_request("ver1/endpoint", params=request.to_query_params())
    return filter_response(response, request.response_filter)
```