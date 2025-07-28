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

## Trading Safety Considerations

### Request Parameter Validation
- **Bot ID Format:** Ensures bot ID is numeric string format to prevent invalid API calls
- **Parameter Types:** Validates boolean parameters with appropriate defaults
- **Input Sanitization:** Pattern validation prevents malformed bot identifiers

### Risk Assessment
- **Read-only Operations:** DCA bot detail retrieval has minimal trading risk
- **Authentication Required:** All requests require proper API authentication
- **Rate Limiting:** Respects 3Commas API rate limits for bot operations

## Integration Examples

### Request Validation
```python
# Validate request parameters before API call
try:
    request = GetDCABotDetailsRequest(bot_id="12345678", include_events=True)
    bot_details = await get_dca_bot_details(request.bot_id, request.include_events)
    # bot_details is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid bot request parameters: {e}")
```

### Error Handling
```python
# Handle validation errors for bot ID format
try:
    request = GetDCABotDetailsRequest(bot_id="invalid_id")  # Will fail validation
except ValidationError as e:
    logger.error(f"Bot ID must be numeric string: {e}")
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