# CLAUDE.md for tools/

## Context Activation
Activates when implementing MCP functions for 3Commas API trading operations.

## Current Implementation Status
**5 functions implemented across 3 modules:**
- `account.py` - 1 function: get_connected_exchanges_and_wallets
- `market_data.py` - 3 functions: get_all_market_pairs, get_currency_rates_and_limits, get_supported_markets  
- `dca_bots.py` - 1 function: get_dca_bot_details

**Exports**: Only `dca_bots` module exposed in __init__.py

## Established Patterns (from actual code)
- Use `@handle_api_errors` decorator (consistently applied)
- Include `response_filter: str = "display"` parameter (all functions)
- Pass response_filter string directly to model (simplified validation)
- Create Pydantic models for validation (all use APIRequest inheritance)
- Apply `filter_response()` before returning (consistent pattern)

## Function Structure (from market_data.py:21-69)
```python
@handle_api_errors
async def get_all_market_pairs(
    market_code: Optional[str] = None, 
    response_filter: str = "display"
) -> APIResponse:
    request = GetAllMarketPairsRequest(
        market_code=market_code, 
        response_filter=response_filter
    )
    params = {}
    if request.market_code:
        params["market_code"] = request.market_code
    response = await api_request("ver1/accounts/market_pairs", params=params, method="GET")
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)
    return response
```

## Quality Standards (verified in current code)
- [ ] Uses `@handle_api_errors` decorator
- [ ] Includes `response_filter: str = "display"` parameter  
- [ ] Uses corresponding Pydantic request model
- [ ] Calls `filter_response()` before returning
- [ ] Follows established import patterns

## MVP Implementation Tracking
When implementing new tool functions, update:
1. `TASKS.md` - Change ⏸️ to ✅ in MVP phase tables
2. `docs/MVP_GET_APIS.md` - Mark completed in priority tables  
3. `docs/API_REFERENCES.md` - Update status marker
4. `threecommas_mcp/tools/__init__.py` - Add module to exports if needed