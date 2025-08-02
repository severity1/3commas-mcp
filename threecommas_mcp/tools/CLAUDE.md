# CLAUDE.md for tools/

## Context Activation
**Triggers**: Implementing MCP functions for 3Commas API trading operations
**Usage**: Referenced during root CLAUDE.md steps 3-4 (tool implementation)

## Required Implementation Structure
1. **Function Signature**
   ```python
   @handle_api_errors
   async def function_name(
       request_param: RequestModel,
       response_filter: str = "display"
   ) -> Dict[str, Any]:
   ```

2. **Standard Implementation Pattern**
   ```python
   # Validate request using Pydantic model
   request = RequestModel(**locals())
   
   # Make authenticated API call
   response = await api_request("endpoint", request.dict())
   
   # Filter and return response
   return filter_response(response, response_filter)
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

## Documentation Requirements
After implementation, follow root CLAUDE.md step 6 for documentation workflow.