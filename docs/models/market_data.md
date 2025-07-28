# Market Data Models

This document describes the Pydantic models used for market data operations in the 3Commas MCP server.

## Overview

Market data models provide validation and structure for market data API requests. These models ensure data integrity for request parameters. API responses are returned as unvalidated `APIResponse = Dict[str, Any]` following our established pattern.

## Request Models

### GetAllMarketPairsRequest

**Purpose:** Request parameters for retrieving all available trading pairs.

**Used by:** [get_all_market_pairs](../tools/market_data.md#get-all-market-pairs)

**Fields:**
- `market_code: Optional[str]` - Optional market code filter with length constraints (1-50)

**Validation:** Market code has length constraints when provided.

**Safety:** Simple parameter validation ensures safe API requests.

### GetCurrencyRatesRequest

**Purpose:** Request parameters for retrieving currency rates and limits.

**Used by:** [get_currency_rates_and_limits](../tools/market_data.md#get-currency-rates-and-limits)

**Fields:**
- `market_code: str` - Exchange market code (required, length 1-50)
- `pair: str` - Trading pair in BASE_QUOTE format (required, pattern validation)
- `limit_type: Optional[LimitType]` - Optional limit type enum

**Validation:** Market code and pair have length and pattern constraints respectively.

**Safety:** Validates trading pair format to prevent invalid API requests.

### GetSupportedMarketsRequest

**Purpose:** Request model for getting supported markets.

**Used by:** [get_supported_markets](../tools/market_data.md#get-supported-markets)

**Fields:** No parameters required for this endpoint.

**Safety:** Simple model with no parameters, ensuring safe endpoint access.

## API Response Handling

Following our established pattern, API responses from market data endpoints are returned as unvalidated `APIResponse = Dict[str, Any]`. This provides flexibility to handle varying response structures from the 3Commas API without validation overhead.

Response data includes trading pairs, currency rates, exchange information, and market capabilities, but is not validated at the model level.

## Validation Patterns

### Market Code Field Constraints
Market codes use Field constraints for length validation:
```python
market_code: Optional[str] = Field(
    None, min_length=1, max_length=50,
    description="Optional market code to filter pairs by exchange"
)
```

### Trading Pair Field Constraints
Trading pairs use Field constraints for format validation:
```python
pair: str = Field(
    ..., min_length=3, max_length=20,
    pattern=r"^[A-Z0-9]+_[A-Z0-9]+$",
    description="Trading pair in BASE_QUOTE format"
)
```

### Enum Field Constraints
Optional enums use proper typing:
```python
limit_type: Optional[LimitType] = Field(
    None, description="Optional limit type for specific trading contexts"
)
```

## Trading Safety Considerations

- **Request Parameter Validation:** Validates trading pair format and market codes to prevent invalid API calls
- **Read-only Operations:** Market data retrieval has minimal trading risk
- **Authentication Required:** All requests require proper API authentication
- **Rate Limiting:** Respects 3Commas API rate limits for market data operations

## Integration Examples

### Request Validation
```python
# Validate request parameters before API call
try:
    request = GetCurrencyRatesRequest(
        market_code="binance", 
        pair="BTC_USDT", 
        limit_type=LimitType.BOT
    )
    rates = await get_currency_rates_and_limits(
        request.market_code, request.pair, request.limit_type
    )
    # rates is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid request parameters: {e}")
```

### Market Pairs Request
```python
# Validate market code parameter
try:
    request = GetAllMarketPairsRequest(market_code="binance")
    pairs = await get_all_market_pairs(request.market_code)
    # pairs is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid market code: {e}")
```

## Related Documentation

- **Tools:** [Market Data Tools](../tools/market_data.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common model patterns and configuration
- **API Reference:** [3Commas Market Data API](https://developers.3commas.io/market-data)
- **Conversations:** [Market Data Examples](../conversations/market-data-conversation.md)