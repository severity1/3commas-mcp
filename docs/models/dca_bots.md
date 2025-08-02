# DCA Bot Models

This document describes the Pydantic models used for DCA (Dollar Cost Averaging) bot operations in the 3Commas MCP server.

## Overview

DCA bot models provide validation and structure for bot-related API requests. These models ensure data integrity for request parameters. API responses are returned as unvalidated `APIResponse = Dict[str, Any]` following our established pattern.

## Request Models

### GetDCABotDetailsRequest

**Purpose:** Request model for retrieving DCA bot details and configuration information.

**Used by:** [get_dca_bot_details](../tools/dca_bots.md#get-dca-bot-details)

**Fields:**
- `bot_id: str` - DCA bot unique identifier (numeric string)
- `include_events: bool` - Include related events in response (default: False)

**API Mapping:**
- `bot_id` -> `{bot_id}` (path parameter)
- `include_events` -> `include_events` (query parameter)

**Validation Rules:**
- Bot ID must be non-empty string with pattern validation (^\d+$)
- Include events is optional boolean with false default

**Safety:** Validates bot ID format to prevent invalid API requests and ensure proper bot identification.

**Example:**
```python
request = GetDCABotDetailsRequest(
    bot_id="12345678",
    include_events=True
)
```

### GetDCABotListRequest

**Purpose:** Request model for retrieving list of DCA bots with filtering and sorting capabilities.

**Used by:** [get_dca_bot_list](../tools/dca_bots.md#get-dca-bot-list)

**Fields:**
- `account_id: int` - Filter bots by specific 3Commas exchange account ID (0 = all accounts, default: 0)
- `strategy: StrategyType | None` - Filter by trading strategy ("long" or "short", optional)
- `order_direction: str` - Sort order ("ASC" or "DESC", default: "DESC")
- `limit: int` - Maximum number of bots to return (1-1000, default: 50)
- `offset: int` - Number of bots to skip for pagination (default: 0)
- `from_date: str | None` - Filter bots created from this date (ISO format, optional)
- `scope: str | None` - Filter scope for bot selection (optional)
- `sort_by: str | None` - Field to sort by (optional)
- `quote: str | None` - Filter by quote currency (optional)

**API Mapping:**
- `account_id` -> `account_id` (query parameter)
- `strategy` -> `strategy` (query parameter)
- `order_direction` -> `order_direction` (query parameter)
- `limit` -> `limit` (query parameter)
- `offset` -> `offset` (query parameter)
- `from_date` -> `from` (query parameter)
- `scope` -> `scope` (query parameter)
- `sort_by` -> `sort_by` (query parameter)
- `quote` -> `quote` (query parameter)

**Validation Rules:**
- Account ID must be ≥1 if provided
- Strategy must be valid StrategyType ("long" or "short") if provided
- Order direction must match pattern (ASC|DESC)
- Limit must be between 1-1000 if provided
- Offset must be ≥0 if provided
- All parameters except order_direction are optional

**Safety:** Validates parameter ranges and formats to prevent invalid API requests and ensure proper portfolio filtering.

**Example:**
```python
# Basic request for all bots
request = GetDCABotListRequest()

# Filtered request with pagination
request = GetDCABotListRequest(
    account_id=12345,
    strategy="long",
    limit=50,
    offset=0,
    quote="USDT"
)
```

### GetAvailableStrategyListRequest

**Purpose:** Request model for retrieving available DCA bot trading strategies.

**Used by:** [get_available_strategy_list](../tools/dca_bots.md#get-available-strategy-list)

**Fields:** No additional fields beyond the base `response_filter` from `APIRequest`.

**API Mapping:** No query parameters beyond response filtering.

**Validation Rules:** Uses default APIRequest validation (response_filter only).

**Safety:** Simple read-only operation with no trading risks.

**Example:**
```python
request = GetAvailableStrategyListRequest()
```

The simplest request model with no parameters, demonstrating the minimal APIRequest inheritance pattern.

### GetDCABotProfitDataRequest

**Purpose:** Validates parameters for retrieving DCA bot profit analytics over specified time periods.

**Used by:** [get_dca_bot_profit_data](../tools/dca_bots.md#get-dca-bot-profit-data)

**Fields:**
- `bot_id: str` - DCA bot identifier (numeric string pattern, required)
- `days: int` - Number of days for profit data (1-365 range, default: 30)

**API Mapping:**
- `bot_id` → Path parameter `/bots/{bot_id}/profit_by_day`
- `days` → Query parameter `?days={days}`

**Validation Rules:**
- `bot_id`: Must be numeric string format (validates 3Commas bot ID format)
- `days`: Range validation (1-365) ensures reasonable time period requests

**Safety:** Read-only operation with no trading risks. Time period validation prevents excessive API load, and bot ID validation ensures proper request format.

**Example:**
```python
# Default 30-day profit data
request = GetDCABotProfitDataRequest(bot_id="12345678")

# Custom time period
request = GetDCABotProfitDataRequest(bot_id="12345678", days=90)
```

## API Response Handling

Following our established pattern, API responses from DCA bot endpoints are returned as unvalidated `APIResponse = Dict[str, Any]`. This provides flexibility to handle varying response structures from the 3Commas API without validation overhead.

Response data includes bot configuration, active deals, performance metrics, and operational status, but is not validated at the model level.

## Validation Patterns

### Bot ID Validation
Bot IDs use Field constraints for format validation:
```python
bot_id: str = Field(
    ..., min_length=1, pattern=r"^\d+$",
    description="DCA bot unique identifier (numeric string)"
)
```

### Boolean Parameter Validation
Optional parameters use Field constraints with defaults:
```python
include_events: bool = Field(
    default=False, description="Include related events in response"
)
```

### Integer Range Validation
Numeric parameters use Field constraints with meaningful defaults:
```python
account_id: int = Field(
    default=0, ge=0,
    description="Filter bots by specific 3Commas exchange account ID (0 = all accounts)"
)

limit: int = Field(
    default=50, ge=1, le=1000,
    description="Maximum number of bots to return (1-1000)"
)
```

### Enum Validation
Strategy parameters use StrategyType enum for validation:
```python
strategy: StrategyType | None = Field(
    default=None,
    description="Filter by trading strategy (long or short positions)"
)
```

## Trading Safety Considerations

### Request Parameter Validation
- **Bot ID Format:** Ensures bot ID is numeric string format to prevent invalid API calls
- **Parameter Types:** Validates boolean parameters with appropriate defaults
- **Input Sanitization:** Pattern validation prevents malformed bot identifiers
- **Range Validation:** Ensures numeric parameters are within acceptable API limits
- **Enum Constraints:** Strategy types are validated against allowed values
- **Pagination Safety:** Validates limit and offset ranges for safe pagination

### Risk Assessment
- **Read-only Operations:** DCA bot retrieval operations have minimal trading risk
- **Authentication Required:** All requests require proper API authentication
- **Rate Limiting:** Respects 3Commas API rate limits for bot operations
- **Portfolio Access:** List operations only return bots owned by authenticated account

## Integration Examples

### Request Validation
```python
# Validate bot details request parameters before API call
try:
    request = GetDCABotDetailsRequest(bot_id="12345678", include_events=True)
    bot_details = await get_dca_bot_details(request.bot_id, request.include_events)
    # bot_details is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid bot request parameters: {e}")

# Validate bot list request with filtering
try:
    request = GetDCABotListRequest(
        account_id=12345,
        strategy="long",
        limit=50,
        offset=0
    )
    bot_list = await get_dca_bot_list(**request.dict())
    # bot_list is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid bot list parameters: {e}")
```

### Error Handling
```python
# Handle validation errors for bot ID format
try:
    request = GetDCABotDetailsRequest(bot_id="invalid_id")  # Will fail validation
except ValidationError as e:
    logger.error(f"Bot ID must be numeric string: {e}")

# Handle validation errors for list parameters
try:
    request = GetDCABotListRequest(
        account_id=0,  # Will fail validation (must be ≥1)
        limit=2000     # Will fail validation (must be ≤1000)
    )
except ValidationError as e:
    logger.error(f"Invalid list parameters: {e}")
```

## Related Documentation

- **Tools:** [DCA Bot Management Tools](../tools/dca_bots.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common base classes and configuration
- **API Reference:** [3Commas DCA Bot API](https://developers.3commas.io/dca-bot)
- **Conversations:** [DCA Bot Management Examples](../conversations/dca-bot-management-conversation.md)

## Development Guidelines

### Adding New DCA Bot Request Models
When extending DCA bot model functionality:
1. **Inherit from BaseModelConfig** for all request models
2. **Include comprehensive validation** for request parameters
3. **Use pattern validation** for structured fields (bot IDs, pairs)
4. **Document API parameter mappings** to 3Commas endpoints
5. **Add request safety considerations** for parameter validation
6. **Update this documentation** with new request patterns

### Validation Best Practices
- **Request Safety First:** Validate all request parameters comprehensively
- **Pattern Validation:** Use regex patterns for structured identifiers
- **Type Safety:** Use appropriate Field constraints for parameter types
- **Clear Error Messages:** Provide actionable validation error messages
- **API Compatibility:** Ensure request parameters match 3Commas API expectations