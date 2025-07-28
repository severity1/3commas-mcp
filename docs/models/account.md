# Account Models

This document describes the Pydantic models used for account management operations in the 3Commas MCP server.

## Overview

Account models provide validation and structure for account-related API requests. These models ensure data integrity for request parameters. API responses are returned as unvalidated `APIResponse = Dict[str, Any]` following our established pattern.

## Request Models

### GetConnectedExchangesRequest

**Purpose:** Request model for the get_connected_exchanges_and_wallets endpoint.

**Used by:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Fields:** No parameters required for this endpoint.

**Validation:** Inherits from BaseModelConfig for consistent configuration.

**Safety:** Simple model with no parameters, ensuring safe endpoint access.

## API Response Handling

Following our established pattern, API responses from account endpoints are returned as unvalidated `APIResponse = Dict[str, Any]`. This provides flexibility to handle varying response structures from the 3Commas API without validation overhead.

Response data includes exchange account information, balance data, trading permissions, and connection status, but is not validated at the model level.

## Validation Patterns

### Request Parameter Validation
No validation patterns required for this endpoint as it accepts no parameters.

## Trading Safety Considerations

- **Read-only Operations:** Account detail retrieval has minimal trading risk
- **Authentication Required:** All requests require proper API authentication
- **Rate Limiting:** Respects 3Commas API rate limits for account operations
- **Data Privacy:** Response filtering removes sensitive account information

## Integration Examples

### Request Validation
```python
# Validate request parameters (none required for this endpoint)
try:
    request = GetConnectedExchangesRequest()
    exchanges = await get_connected_exchanges_and_wallets()
    # exchanges is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid request parameters: {e}")
```

## Related Documentation

- **Tools:** [Account Management Tools](../tools/account.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common model patterns and configuration
- **API Reference:** [3Commas Account API](https://developers.3commas.io/account)
- **Conversations:** [Account Management Examples](../conversations/account-management-conversation.md)