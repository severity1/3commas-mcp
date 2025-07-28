# Market Data Tools

This document describes the market data tools available in the 3Commas MCP server.

## Overview

Market data tools provide read-only access to trading pairs, currency rates, exchange information, and market availability. These tools are essential for bot configuration, trading decisions, and understanding exchange compatibility.

## Available Tools

### get_all_market_pairs

**Function:** `get_all_market_pairs(market_code: str = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all available trading pairs across markets or for a specific market. This is essential for bot configuration as it provides the complete list of tradeable pairs, their symbols, and market availability.

**Parameters:**
- `market_code`: Optional market code to filter pairs (e.g., "binance", "okx")
- `response_filter`: Filter type for response ("full" or "display", default: "display")

**Returns:** List of all available trading pairs including:
- Pair symbols (base/quote currencies)
- Market availability and status
- Trading parameters and restrictions
- Volume and liquidity information

**Safety:** Read-only operation with no trading risks. Essential data for safe bot configuration.

**API Details:**
- **Endpoint:** `GET /ver1/market_pairs`
- **Security:** SIGNED (requires API key + HMAC signature)
- **Permission:** NONE (public data with authentication)

**Models:** [TradingPair](../models/market_data.md#tradingpair)

**Examples:** [Market Data Conversation](../conversations/market-data-conversation.md#get-all-market-pairs)

### get_currency_rates_and_limits

**Function:** `get_currency_rates_and_limits(market_code: str, pair: str, limit_type: LimitType = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves current exchange rates and trading limits for currencies. This is required for trading decisions as it provides essential pricing and limit information needed for order calculations and risk management.

**Parameters:**
- `market_code` (str, required): Exchange market code (string from supported markets)
- `pair` (str, required): Trading pair to get specific rates (e.g., "BTC_USDT")
- `limit_type` (LimitType, optional): Optional limit type (LimitType.BOT or LimitType.SMART_TRADE)
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** Currency rates and limits including:
- Current exchange rates between currencies
- Minimum and maximum trading limits
- Price precision and step sizes
- Trading fees and commission rates

**Safety:** Read-only market data essential for safe trading calculations and risk management.

**API Details:**
- **Endpoint:** `GET /ver1/accounts/currency_rates`
- **Security:** NONE (no authentication required)
- **Permission:** NONE (public data)

**Models:** [CurrencyRate](../models/market_data.md#currencyrate)

**Examples:** [Market Data Conversation](../conversations/market-data-conversation.md#get-currency-rates)

### get_supported_markets

**Function:** `get_supported_markets(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves the complete list of supported trading markets and exchanges. This provides exchange compatibility information needed to understand which markets are available for trading operations and bot deployment.

**Parameters:**
- `response_filter`: Filter type for response ("full" or "display", default: "display")

**Returns:** List of supported markets including:
- Market names and codes
- Exchange compatibility status
- Available trading features
- Market-specific limitations
- Connection requirements

**Safety:** Read-only information essential for understanding exchange compatibility and capabilities.

**API Details:**
- **Endpoint:** `GET /ver1/accounts/market_list`
- **Security:** SIGNED (requires API key + HMAC signature)
- **Permission:** NONE (public data with authentication)

**Models:** [SupportedMarket](../models/market_data.md#supportedmarket)

**Examples:** [Market Data Conversation](../conversations/market-data-conversation.md#get-supported-markets)

## Usage Patterns

### Basic Market Research
```python
# Get all available trading pairs
pairs = await get_all_market_pairs()

# Get pairs for specific exchange
binance_pairs = await get_all_market_pairs(market_code="binance")

# Get currency rates for specific pair
btc_rates = await get_currency_rates_and_limits(market_code="binance", pair="BTC_USDT", limit_type=LimitType.BOT)

# Get all supported markets
markets = await get_supported_markets()
```

### Bot Configuration Workflow
```python
# 1. Check supported markets
markets = await get_supported_markets()

# 2. Get available pairs for chosen market
pairs = await get_all_market_pairs(market_code="binance")

# 3. Get rate and limit information for chosen pair
limits = await get_currency_rates_and_limits(market_code="binance", pair="BTC_USDT", limit_type=LimitType.BOT)

# 4. Use data for safe bot configuration
```

## Trading Safety Considerations

- **Read-only operations**: No financial risk as these endpoints only retrieve market information
- **Bot configuration safety**: Essential data for validating trading pairs and limits before bot creation
- **Rate limiting**: Respects 3Commas API rate limits for market data endpoints
- **Data freshness**: Market data should be refreshed regularly for accurate trading decisions

## Error Handling

All market data tools use the `@handle_api_errors` decorator for consistent error handling:

- **API Errors**: Automatically handled with descriptive error messages
- **Invalid Parameters**: Validation errors for malformed market codes or trading pairs
- **Rate Limiting**: Exponential backoff when rate limits are exceeded
- **Market Unavailability**: Clear errors when markets are temporarily unavailable

## Related Documentation

- **Models:** [Market Data Models](../models/market_data.md) - Data structures and validation
- **API Reference:** [3Commas Market Data API](https://developers.3commas.io/market-data)
- **Bot Configuration:** [DCA Bot Tools](dca_bots.md) - Using market data for bot setup
- **Authentication:** [HMAC-SHA256 Authentication](../DEVELOPMENT.md#authentication)