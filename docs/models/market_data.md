# Market Data Models

## Available Models

### GetAllMarketPairsRequest

**Purpose:** Request parameters for retrieving all available trading pairs.

**Used by:** [get_all_market_pairs](../tools/market_data.md#get-all-market-pairs)

**Key Fields:**
- `market_code`: Optional market code filter (length 1-50)

**Validation:** Market code length constraints when provided.

### GetCurrencyRatesRequest

**Purpose:** Request parameters for retrieving currency rates and trading limits.

**Used by:** [get_currency_rates_and_limits](../tools/market_data.md#get-currency-rates-and-limits)

**Key Fields:**
- `market_code`: Exchange market code (required, length 1-50)
- `pair`: Trading pair in BASE_QUOTE format (required, pattern validation)
- `limit_type`: Optional limit type enum (LimitType.BOT or LimitType.SMART_TRADE)

**Validation:** Market code length and trading pair format validation with regex pattern.

### GetSupportedMarketsRequest

**Purpose:** Request parameters for retrieving supported trading markets and exchanges.

**Used by:** [get_supported_markets](../tools/market_data.md#get-supported-markets)

**Key Fields:** No additional fields beyond response_filter from APIRequest.

**Validation:** Inherits from APIRequest base class.