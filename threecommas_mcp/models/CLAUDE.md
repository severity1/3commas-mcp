# CLAUDE.md for models/

## Context Activation
Activates when creating Pydantic validation models for 3Commas API structures.

## Current Implementation Status
**5 Request models implemented (all inherit from APIRequest):**
- `account.py` - GetConnectedExchangesRequest (28 lines)
- `market_data.py` - GetAllMarketPairsRequest, GetCurrencyRatesRequest, GetSupportedMarketsRequest (87 lines)
- `dca_bots.py` - GetDCABotDetailsRequest (39 lines)
- `base.py` - APIRequest, ResponseFilter, common enums (185 lines)

**Exports**: Clean __init__.py with base models and enums

## Established Patterns (from actual code)
- **All models inherit from `APIRequest`** (verified in all 5 models)
- **Field validation using `Field()`** (consistent pattern, no @validator found yet)
- **API mapping in docstrings** (comprehensive documentation)
- **Response filter automatic** (inherited from APIRequest base)

## Model Structure (from market_data.py:14-36)
```python
class GetAllMarketPairsRequest(APIRequest):
    """Request model for getting all market pairs.

    Request parameters for retrieving all available trading pairs,
    optionally filtered by market code.

    API Mapping:
        market_code -> market_code (optional query parameter)

    API Endpoint: GET /ver1/accounts/market_pairs
    """

    market_code: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Optional market code to filter pairs by exchange",
        examples=["binance", "okex", "bybit_spot"],
    )
```

## Base Architecture (base.py)
- **ResponseFilter enum** (DISPLAY="display", FULL="full")
- **APIRequest base class** (automatic response_filter field)
- **Common enums** - BotType, DealStatus, StrategyType, LimitType, MarketCode
- **APIResponse type alias** - Dict[str, Any] for unvalidated responses

## Quality Standards (verified in current code)
- [ ] Inherits from `APIRequest` (automatic response_filter)
- [ ] Field validation using `Field()` with constraints
- [ ] API endpoint and mapping documented in docstring
- [ ] Comprehensive type hints and descriptions
- [ ] Optional fields properly typed with `Optional[Type]`