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

### GetAccountInfoRequest

**Purpose:** Request model for the get_account_info endpoint to retrieve detailed account information.

**Used by:** [get_account_info](../tools/account.md#get-account-info)

**API Endpoint:** `/ver1/accounts/{account_id}`

**Fields:**
- `account_id` (Optional[Union[str, int]]): Account ID or "summary" for aggregated data
  - **Default:** "summary"
  - **Type:** Can be integer account ID or string "summary"
  - **Description:** Specifies which account to retrieve or "summary" for all accounts
  - **Example:** 31337503 or "summary"

**Validation:**
- Inherits from APIRequest base class with response_filter support
- Flexible account_id field accepts both numeric IDs and "summary" string
- Automatically validates response_filter parameter ("full" or "display")

**Script Validation Results:**
- **Tested endpoint:** `/ver1/accounts/summary` and `/ver1/accounts/31337503`
- **Response size:** 587 tokens (summary), 633 tokens (specific account)
- **API compatibility:** Confirmed working with both account ID and summary modes

**Safety:** Read-only operation with parameter validation for account access.

## API Response Handling

Following our established pattern, API responses from account endpoints are returned as unvalidated `APIResponse = Dict[str, Any]`. This provides flexibility to handle varying response structures from the 3Commas API without validation overhead.

Response data includes exchange account information, balance data, trading permissions, and connection status, but is not validated at the model level.

## Validation Patterns

### Request Parameter Validation

**GetConnectedExchangesRequest:** No validation patterns required as it accepts no parameters.

**GetAccountInfoRequest:** Validates account_id parameter with flexible typing:
- Accepts integer account IDs (e.g., 31337503)
- Accepts string "summary" for aggregated data
- Defaults to "summary" if not specified
- Inherits response_filter validation from APIRequest base class

## Trading Safety Considerations

- **Read-only Operations:** Account detail retrieval has minimal trading risk
- **Authentication Required:** All requests require proper API authentication
- **Rate Limiting:** Respects 3Commas API rate limits for account operations
- **Data Privacy:** Response filtering removes sensitive account information

## Integration Examples

### Request Validation
```python
# GetConnectedExchangesRequest - no parameters required
try:
    request = GetConnectedExchangesRequest()
    exchanges = await get_connected_exchanges_and_wallets()
    # exchanges is APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid request parameters: {e}")

# GetAccountInfoRequest - with account ID validation
try:
    # Summary request (default)
    summary_request = GetAccountInfoRequest()
    summary = await get_account_info()
    
    # Specific account request
    account_request = GetAccountInfoRequest(account_id=31337503)
    account = await get_account_info(account_id=31337503)
    
    # Both return APIResponse = Dict[str, Any] (unvalidated)
except ValidationError as e:
    logger.error(f"Invalid account_id parameter: {e}")
```

## Related Documentation

- **Tools:** [Account Management Tools](../tools/account.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common model patterns and configuration
- **API Reference:** [3Commas Account API](https://developers.3commas.io/account)
- **Conversations:** [Account Management Examples](../conversations/account-management-conversation.md)