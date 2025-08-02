# DCA Bot Tools

This document provides reference documentation for DCA bot management tools in the 3Commas MCP server.

## Overview

DCA (Dollar Cost Averaging) bot tools provide functionality for managing and monitoring DCA bots through the 3Commas API. These tools enable Claude to help users retrieve bot information, analyze performance, and manage bot configurations.

## Functions

### get_dca_bot_details

**Function:** `get_dca_bot_details(bot_id: str, include_events: bool = False, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves comprehensive information about a specific DCA bot including configuration, active deals, trading parameters, and performance data.

**API Endpoint:** `GET /ver1/bots/{bot_id}/show`  
**Security:** SIGNED (requires API key + HMAC signature)  
**Permission:** BOTS_READ

**Parameters:**
- `bot_id` (str, required): DCA bot unique identifier (3Commas bot ID)
- `include_events` (bool, optional): Include related events in response (default: False)
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** Complete DCA bot details including:
- Bot configuration (trading pair, order volumes, strategy settings)
- Active deals information and status
- Trading parameters and safety order configuration
- Performance metrics and profit/loss data
- Bot status (enabled/disabled) and operational state

**Safety:** Read-only operation with no trading risks

**Examples:** [DCA Bot Management Conversation](../conversations/dca-bot-management-conversation.md#retrieving-bot-details)

### get_dca_bot_list

**Function:** `get_dca_bot_list(account_id: int = 0, strategy: str | None = None, order_direction: str = "DESC", limit: int = 50, offset: int = 0, from_date: str | None = None, scope: str | None = None, sort_by: str | None = None, quote: str | None = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves the user's DCA bot portfolio with optional filtering and sorting capabilities. Provides an overview of all DCA bots including their status, configuration, and performance data.

**API Endpoint:** `GET /ver1/bots`  
**Security:** SIGNED (requires API key + HMAC signature)  
**Permission:** BOTS_READ

**Parameters:**
- `account_id` (int, optional): Filter bots by specific 3Commas exchange account ID (0 = all accounts, default: 0)
- `strategy` (str | None, optional): Filter by trading strategy ("long" or "short")
- `order_direction` (str, optional): Sort order ("ASC" or "DESC", default: "DESC")
- `limit` (int, optional): Maximum number of bots to return (1-1000, default: 50)
- `offset` (int, optional): Number of bots to skip for pagination (default: 0)
- `from_date` (str | None, optional): Filter bots created from this date (ISO format)
- `scope` (str | None, optional): Filter scope for bot selection
- `sort_by` (str | None, optional): Field to sort by (created_at, updated_at, etc.)
- `quote` (str | None, optional): Filter by quote currency (e.g., "USDT", "BTC")
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** List of DCA bots including:
- Bot configuration (trading pairs, order volumes, strategy settings)
- Status and enabled state for each bot
- Active deals information and statistics
- Performance metrics and profit/loss data
- Trading parameters and safety order configuration

**Safety:** Read-only operation with no trading risks

**Examples:** [DCA Bot Management Conversation](../conversations/dca-bot-management-conversation.md#listing-dca-bots)

### get_available_strategy_list

**Function:** `get_available_strategy_list(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all available DCA bot trading strategies from 3Commas. Provides comprehensive catalog of strategy options including configuration parameters, compatibility information, and strategy-specific settings for bot creation and configuration.

**API Endpoint:** `GET /ver1/bots/strategy_list`  
**Security:** SIGNED (requires API key + HMAC signature)  
**Permission:** BOTS_READ

**Parameters:**
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** Available strategies including:
- Strategy names and identifiers
- Configuration options and parameters for each strategy  
- Compatibility information with different exchanges
- Strategy-specific requirements and constraints
- Strategy description and trading logic information

**Safety:** Read-only operation with no trading risks

**Examples:** [DCA Bot Management Conversation](../conversations/dca-bot-management-conversation.md#strategy-configuration)

### get_dca_bot_profit_data

**Function:** `get_dca_bot_profit_data(bot_id: str, days: int = 30, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves daily profit/loss data for a specific DCA bot over a specified time period. Provides historical performance analytics with profit amounts in both BTC and USD for tracking bot profitability.

**API Endpoint:** `GET /ver1/bots/{bot_id}/profit_by_day`  
**Security:** SIGNED (requires API key + HMAC signature)  
**Permission:** BOTS_READ

**Parameters:**
- `bot_id` (str, required): DCA bot unique identifier (3Commas bot ID)
- `days` (int, optional): Number of days for profit data (1-365 days, default: 30)
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** Daily profit data including:
- Daily profit/loss amounts in BTC and USD
- Date timestamps (both string format and Unix timestamp)  
- Historical performance data for specified period
- Profit trend analysis over time

**Safety:** Read-only operation with no trading risks

**Examples:** [DCA Bot Management Conversation](../conversations/dca-bot-management-conversation.md#analyzing-bot-performance)

## Usage Patterns

### Basic Bot Information Retrieval
```python
# Get basic bot details
bot_details = await get_dca_bot_details("12345678")

# Get bot details with events
detailed_bot = await get_dca_bot_details("12345678", include_events=True)
```

### DCA Bot Portfolio Management
```python
# Get all DCA bots
all_bots = await get_dca_bot_list()

# Get bots for specific exchange account
binance_bots = await get_dca_bot_list(account_id=12345)

# Get only long strategy bots
long_bots = await get_dca_bot_list(strategy="long")

# Get recent bots with pagination
recent_bots = await get_dca_bot_list(limit=20, sort_by="created_at", order_direction="DESC")

# Filter by quote currency
usdt_bots = await get_dca_bot_list(quote="USDT")
```

### Strategy Configuration
```python
# Get all available strategies
strategies = await get_available_strategy_list()

# Get strategies with full details
detailed_strategies = await get_available_strategy_list(response_filter="full")
```

### Bot Performance Analysis
```python
# Get 30-day profit data (default)
profit_data = await get_dca_bot_profit_data("12345678")

# Get 7-day profit data for recent performance
recent_profit = await get_dca_bot_profit_data("12345678", days=7)

# Get quarterly profit data for long-term analysis
quarterly_profit = await get_dca_bot_profit_data("12345678", days=90)

# Get full response for detailed analysis
detailed_profit = await get_dca_bot_profit_data("12345678", days=30, response_filter="full")
```

### Bot Status Monitoring
The functions are commonly used for:
- Checking bot configuration before making changes
- Monitoring active deals and performance
- Analyzing bot strategy effectiveness
- Troubleshooting bot issues
- Preparing bot update parameters
- Portfolio overview and analysis
- Finding specific bots by criteria

## Error Handling

**Common Errors:**
- `ValueError`: Empty or invalid bot_id parameter (get_dca_bot_details, get_dca_bot_profit_data)
- `ValueError`: Invalid parameter values (account_id, limit, offset ranges, days: 1-365)
- `APIError`: Bot not found (invalid bot_id for get_dca_bot_details, get_dca_bot_profit_data)
- `AuthenticationError`: Invalid API credentials
- `PermissionError`: Insufficient API key permissions (missing BOTS_READ)

**Error Prevention:**
- Ensure bot_id is valid and belongs to your account (get_dca_bot_details, get_dca_bot_profit_data)
- Verify API key has BOTS_READ permission
- Use proper bot ID format (numeric string)
- Validate parameter ranges (limit: 1-1000, offset: ≥0, account_id: ≥1, days: 1-365)
- Use valid strategy values ("long" or "short")
- Ensure proper date format for from_date (ISO format)

## Integration

### Related Tools
- `get_dca_bot_list()` - Get all DCA bots for portfolio overview ✅
- `get_dca_bot_details()` - Get detailed information for specific bot ✅
- `get_available_strategy_list()` - Get available DCA bot trading strategies ✅
- `get_dca_bot_profit_data()` - Get daily profit analytics for specific bot ✅
- Future: `update_dca_bot()` - Modify bot configuration
- Future: `get_dca_bot_stats()` - Detailed performance statistics

### Cross-References
- **Models:** [Base Models](../models/base.md#apiresponse) (APIResponse return type)
- **Conversations:** [DCA Bot Management](../conversations/dca-bot-management-conversation.md)
- **API Reference:** [3Commas DCA Bot API](https://developers.3commas.io/dca-bot/get-dca-bot)

## Security Considerations

- **Read-only operation:** No trading or configuration risks
- **Authentication required:** Uses API key + HMAC signature
- **Rate limiting:** Respects 3Commas BOTS_READ rate limits
- **Data access:** Only returns data for bots owned by authenticated account