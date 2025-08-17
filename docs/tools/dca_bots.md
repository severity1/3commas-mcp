# DCA Bot Tools

## Available Tools

### get_dca_bot_details

**Function:** `get_dca_bot_details(bot_id: str, include_events: bool = False, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves comprehensive information about a specific DCA bot.

**Parameters:**
- `bot_id`: DCA bot unique identifier (required)
- `include_events`: Include related events in response
- `response_filter`: Response detail level ("full" or "display")

**Returns:** DCA bot details including configuration, active deals, and performance data.

### get_dca_bot_list

**Function:** `get_dca_bot_list(account_id: int = 0, strategy: str | None = None, order_direction: str = "DESC", limit: int = 50, offset: int = 0, from_date: str | None = None, scope: str | None = None, sort_by: str | None = None, quote: str | None = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves the user's DCA bot portfolio with filtering and sorting options.

**Parameters:**
- `account_id`: Filter by exchange account ID (0 = all accounts)
- `strategy`: Filter by trading strategy ("long" or "short")
- `order_direction`: Sort order ("ASC" or "DESC")
- `limit`: Maximum number of bots to return (1-1000)
- `offset`: Number of bots to skip for pagination
- `from_date`: Filter bots created from this date (ISO format)
- `scope`: Filter scope for bot selection
- `sort_by`: Field to sort by
- `quote`: Filter by quote currency
- `response_filter`: Response detail level ("full" or "display")

**Returns:** List of DCA bots with configuration, status, and performance data.

### get_available_strategy_list

**Function:** `get_available_strategy_list(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all available DCA bot trading strategies.

**Parameters:**
- `response_filter`: Response detail level ("full" or "display")

**Returns:** Available strategies with configuration options and compatibility information.

### get_dca_bot_profit_data

**Function:** `get_dca_bot_profit_data(bot_id: str, days: int = 30, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves daily profit/loss data for a specific DCA bot.

**Parameters:**
- `bot_id`: DCA bot unique identifier (required)
- `days`: Number of days for profit data (1-365)
- `response_filter`: Response detail level ("full" or "display")

**Returns:** Daily profit analytics with BTC/USD amounts and timestamps.

### get_blacklist_of_pairs

**Function:** `get_blacklist_of_pairs(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves blacklisted trading pairs for DCA bots.

**Parameters:**
- `response_filter`: Response detail level ("full" or "display")

**Returns:** List of blacklisted trading pairs with restrictions and configurations.