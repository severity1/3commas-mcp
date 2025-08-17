# DCA Bot Models

## Available Models

### GetDCABotDetailsRequest

**Purpose:** Request parameters for retrieving DCA bot details and configuration information.

**Used by:** [get_dca_bot_details](../tools/dca_bots.md#get-dca-bot-details)

**Key Fields:**
- `bot_id`: DCA bot unique identifier (numeric string, required)
- `include_events`: Include related events in response (default: False)

**Validation:** Bot ID format validation with regex pattern (^\d+$).

### GetDCABotListRequest

**Purpose:** Request parameters for retrieving DCA bot portfolio with filtering and sorting.

**Used by:** [get_dca_bot_list](../tools/dca_bots.md#get-dca-bot-list)

**Key Fields:**
- `account_id`: Filter by exchange account ID (0 = all accounts, default: 0)
- `strategy`: Filter by trading strategy ("long" or "short", optional)
- `order_direction`: Sort order ("ASC" or "DESC", default: "DESC")
- `limit`: Maximum bots to return (1-1000, default: 50)
- `offset`: Pagination offset (default: 0)
- `from_date`: Filter bots created from date (ISO format, optional)
- `scope`, `sort_by`, `quote`: Additional filtering options (optional)

**Validation:** Parameter ranges, StrategyType enum validation, pagination safety checks.

### GetAvailableStrategyListRequest

**Purpose:** Request parameters for retrieving available DCA bot trading strategies.

**Used by:** [get_available_strategy_list](../tools/dca_bots.md#get-available-strategy-list)

**Key Fields:** No additional fields beyond response_filter from APIRequest.

**Validation:** Inherits from APIRequest base class.

### GetDCABotProfitDataRequest

**Purpose:** Request parameters for retrieving DCA bot profit analytics over time periods.

**Used by:** [get_dca_bot_profit_data](../tools/dca_bots.md#get-dca-bot-profit-data)

**Key Fields:**
- `bot_id`: DCA bot identifier (numeric string, required)
- `days`: Number of days for profit data (1-365 range, default: 30)

**Validation:** Bot ID format validation, time period range validation.

### GetBlacklistOfPairsRequest

**Purpose:** Request parameters for retrieving blacklisted trading pairs for DCA bots.

**Used by:** [get_blacklist_of_pairs](../tools/dca_bots.md#get-blacklist-of-pairs)

**Key Fields:** No additional fields beyond response_filter from APIRequest.

**Validation:** Inherits from APIRequest base class.