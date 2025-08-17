# Market Data Tools

## Available Tools

### get_all_market_pairs

**Function:** `get_all_market_pairs(market_code: str = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all available trading pairs across markets or for a specific market.

**Parameters:**
- `market_code`: Optional market code to filter pairs
- `response_filter`: Response detail level ("full" or "display")

**Returns:** List of trading pairs with symbols, availability, and trading parameters.

### get_currency_rates_and_limits

**Function:** `get_currency_rates_and_limits(market_code: str, pair: str, limit_type: LimitType = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves current exchange rates and trading limits for currencies.

**Parameters:**
- `market_code`: Exchange market code (required)
- `pair`: Trading pair (required)
- `limit_type`: Optional limit type (LimitType.BOT or LimitType.SMART_TRADE)
- `response_filter`: Response detail level ("full" or "display")

**Returns:** Exchange rates, trading limits, precision, and fee information.

### get_supported_markets

**Function:** `get_supported_markets(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves the complete list of supported trading markets and exchanges.

**Parameters:**
- `response_filter`: Response detail level ("full" or "display")

**Returns:** List of supported markets with names, features, and compatibility information.