# Market Data Models

This document describes the Pydantic models used for market data operations in the 3Commas MCP server.

## Overview

Market data models provide validation and structure for market information, trading pairs, currency rates, and exchange data. These models ensure data integrity and provide clear documentation of expected data formats for market operations.

## Models

### TradingPair

**Purpose:** Model representing a trading pair as returned by the 3Commas API.

**Used by:** [get_all_market_pairs](../tools/market_data.md#get-all-market-pairs)

**Fields:**
- `pair: str` - Trading pair symbol (BTC_USDT)
- `base_currency: str` - Base currency symbol (BTC)
- `quote_currency: str` - Quote currency symbol (USDT)
- `market_code: str` - Exchange market code
- `min_volume: Optional[Decimal]` - Minimum trading volume
- `max_volume: Optional[Decimal]` - Maximum trading volume
- `volume_precision: Optional[int]` - Volume decimal precision
- `price_precision: Optional[int]` - Price decimal precision

**API Mapping:**
- `pair` -> `trading_pair_symbol`
- `base_currency` -> `base`
- `quote_currency` -> `quote`
- `market_code` -> `exchange_market_code`

**Validation Rules:**
- Trading pair must be in BASE_QUOTE format with underscore separator
- Currency symbols are normalized to uppercase
- Volume values must be positive when specified
- Pair format validated to prevent configuration errors

**Safety:** Strict validation ensures only valid trading pairs are accepted, preventing bot configuration errors.

**Example:**
```python
pair = TradingPair(
    pair="BTC_USDT",
    base_currency="BTC",
    quote_currency="USDT",
    market_code="binance",
    min_volume=Decimal("0.001")
)
```

### CurrencyRate

**Purpose:** Model representing currency exchange rate and trading limit information.

**Used by:** [get_currency_rates_and_limits](../tools/market_data.md#get-currency-rates-and-limits)

**Fields:**
- `currency_code: str` - Currency symbol (BTC, ETH, etc.)
- `rate_to_usd: Decimal` - Exchange rate to USD
- `min_trading_amount: Optional[Decimal]` - Minimum trading amount
- `max_trading_amount: Optional[Decimal]` - Maximum trading amount
- `trading_fee: Optional[Decimal]` - Trading fee percentage
- `precision: Optional[int]` - Decimal precision for amounts

**API Mapping:**
- `currency_code` -> `currency`
- `rate_to_usd` -> `usd_rate`
- `min_trading_amount` -> `min_amount`
- `max_trading_amount` -> `max_amount`

**Validation Rules:**
- Currency code normalized to uppercase and cannot be empty
- Exchange rate must be positive
- Trading amounts must be positive when specified
- Uses Decimal type for precise financial calculations

**Safety:** Ensures accurate rate and limit data for safe trading calculations and risk management.

**Example:**
```python
rate = CurrencyRate(
    currency_code="BTC",
    rate_to_usd=Decimal("45000.50"),
    min_trading_amount=Decimal("0.001"),
    trading_fee=Decimal("0.1")
)
```

### SupportedMarket

**Purpose:** Model representing information about supported exchanges and their capabilities.

**Used by:** [get_supported_markets](../tools/market_data.md#get-supported-markets)

**Fields:**
- `market_name: str` - Human-readable market name
- `market_code: str` - Market code identifier
- `market_type: str` - Market type (spot, futures, etc.)
- `is_active: bool` - Whether market is active (default: True)
- `supported_features: Optional[List[str]]` - Available features

**API Mapping:**
- `market_name` -> `name`
- `market_code` -> `code`
- `market_type` -> `type`

**Validation Rules:**
- All market fields are required and cannot be empty
- Field values are stripped of whitespace
- Supports feature list for capability tracking

**Safety:** Validates market information to ensure compatibility and feature availability.

**Example:**
```python
market = SupportedMarket(
    market_name="Binance",
    market_code="binance",
    market_type="spot",
    is_active=True,
    supported_features=["dca_bots", "grid_bots"]
)
```

### Request Models

#### GetAllMarketPairsRequest

**Purpose:** Request parameters for retrieving all available trading pairs.

**Used by:** [get_all_market_pairs](../tools/market_data.md#get-all-market-pairs)

**Fields:**
- `market_code: Optional[str]` - Optional market code filter

**Validation:** Market code normalized to lowercase if provided.

#### GetCurrencyRatesRequest

**Purpose:** Request parameters for retrieving currency rates and limits.

**Used by:** [get_currency_rates_and_limits](../tools/market_data.md#get-currency-rates-and-limits)

**Fields:**
- `pair: Optional[str]` - Optional trading pair filter

**Validation:** Trading pair format validated if provided.

#### GetSupportedMarketsRequest

**Purpose:** Request model for getting supported markets.

**Used by:** [get_supported_markets](../tools/market_data.md#get-supported-markets)

**Fields:** No parameters required for this endpoint.

## Validation Patterns

### Trading Pair Format Validation
```python
@validator('pair')
def validate_pair_format(cls, v):
    if not v or not v.strip():
        raise ValueError("Trading pair cannot be empty")
    
    pair = v.strip().upper()
    if '_' not in pair:
        raise ValueError("Trading pair must contain underscore separator")
    
    parts = pair.split('_')
    if len(parts) != 2 or not all(parts):
        raise ValueError("Trading pair must be in BASE_QUOTE format")
    
    return pair
```

### Financial Data Validation
```python
@validator('rate_to_usd')
def validate_rate_positive(cls, v):
    if v <= 0:
        raise ValueError("Exchange rate must be positive")
    return v
```

### Currency Code Normalization
```python
@validator('currency_code')
def validate_currency_code(cls, v):
    if not v or not v.strip():
        raise ValueError("Currency code cannot be empty")
    return v.strip().upper()
```

## Trading Safety Considerations

- **Pair Validation:** Strict format validation prevents invalid trading pair configurations
- **Financial Precision:** Decimal types used for all monetary values to prevent floating-point errors
- **Rate Validation:** Exchange rates validated to ensure positive values
- **Market Compatibility:** Validation ensures only supported markets and features are used

## Integration Examples

### Trading Pair Validation
```python
# Validate trading pair before bot configuration
try:
    pair = TradingPair(**pair_data)
    if pair.min_volume and volume < pair.min_volume:
        raise ValueError("Volume below minimum requirement")
except ValidationError as e:
    logger.error(f"Invalid trading pair: {e}")
```

### Rate Checking
```python
# Validate currency rates for trading calculations
try:
    rate = CurrencyRate(**rate_data)
    usd_value = amount * rate.rate_to_usd
except ValidationError as e:
    logger.error(f"Invalid rate data: {e}")
```

### Market Compatibility
```python
# Validate market support before operations
try:
    market = SupportedMarket(**market_data)
    if not market.is_active:
        raise ValueError("Market is not currently active")
    if "dca_bots" not in market.supported_features:
        raise ValueError("DCA bots not supported on this market")
except ValidationError as e:
    logger.error(f"Market compatibility issue: {e}")
```

## Related Documentation

- **Tools:** [Market Data Tools](../tools/market_data.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common model patterns and configuration
- **API Reference:** [3Commas Market Data API](https://developers.3commas.io/market-data)
- **Conversations:** [Market Data Examples](../conversations/market-data-conversation.md)