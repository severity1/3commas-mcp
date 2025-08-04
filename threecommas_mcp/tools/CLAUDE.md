# MCP Tool Implementation Patterns

**Context**: MCP function implementation for 3Commas API trading operations  
**When to Use**: After completing Root CLAUDE.md Phase 1 (validation) and Phase 2 decision tree

## Specific Implementation Pattern
1. **Function Signature** (use exact parameter names from script output):
   ```python
   @handle_api_errors
   async def function_name(
       required_param: str,  # From script output, not docs
       optional_param: bool = False,
       response_filter: str = "display"
   ) -> APIResponse:
   ```

2. **Implementation Steps**:
   ```python
   # Step 1: Validate using Pydantic model (based on script findings)
   request = RequestModel(
       required_param=required_param,
       optional_param=optional_param,
       response_filter=ResponseFilter(response_filter)
   )
   
   # Step 2: Build endpoint from script testing
   endpoint = f"ver1/endpoint/{request.required_param}"  # Exact format from scripts
   
   # Step 3: Make authenticated API call
   response = await api_request(endpoint, params=request.to_query_params(), method="GET")
   
   # Step 4: Apply response filtering
   if isinstance(response, dict) and "error" not in response:
       response = filter_response(response, request.response_filter)
   
   return response
   ```

3. **Required Imports**
   ```python
   from typing import Dict, Any
   from ..models.{domain} import RequestModel
   from ..api.client import api_request
   from ..utils.decorators import handle_api_errors
   from ..utils.response_filter import filter_response
   ```

## Reference Examples
- **Complete implementation**: dca_bots.py:20 (get_dca_bot_details)
- **Concise docstring style**: market_data.py:52 (get_currency_rates_and_limits)

## Integration Notes
- Always use script-validated parameter names from Root CLAUDE.md Phase 1
- Return to Root CLAUDE.md for Phase 3 (documentation) after implementation