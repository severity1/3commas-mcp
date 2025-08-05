# Account Management Tools

This document describes the account management tools available in the 3Commas MCP server.

## Overview

Account management tools provide read-only access to user account information, connected exchanges, and wallet data. These tools are essential for understanding account capabilities and available trading resources.

## Available Tools

### get_connected_exchanges_and_wallets

**Function:** `get_connected_exchanges_and_wallets(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all connected exchange accounts and wallet information for the user. This provides core account information needed for trading operations, including exchange names, account types, trading permissions, and connection status.

**Parameters:**
- `response_filter`: Filter type for response ("full" or "display", default: "display")
  - `"display"`: Returns filtered response optimized for display (85% token reduction)
  - `"full"`: Returns complete API response with all fields

**Returns:** List of connected exchanges and wallets including:
- Exchange names and account IDs
- Account types (spot, futures, etc.)
- Trading permissions and status
- Connection health and configuration
- Available balance summaries

**Safety:** This is a read-only operation with no trading risks. All credential information is filtered from responses for security.

**API Details:**
- **Endpoint:** `GET /ver1/accounts`
- **Security:** SIGNED (requires API key + HMAC signature)
- **Permission:** ACCOUNTS_READ

**Models:** 
- [ConnectedExchange](../models/account.md#connectedexchange) - Individual exchange account data
- [ExchangeBalance](../models/account.md#exchangebalance) - Balance information for exchanges

**Examples:** [Account Management Conversation](../conversations/account-management-conversation.md#get-connected-exchanges)

### get_account_info

**Function:** `get_account_info(account_id: Union[str, int] = "summary", response_filter: str = "display") -> APIResponse`

**Description:** Retrieves detailed account information for a specific account or aggregated summary data from all accounts. Provides comprehensive balance, profit metrics, trading settings, and exchange configurations.

**Parameters:**
- `account_id`: Account ID (integer) or "summary" for aggregated data (default: "summary")
- `response_filter`: Filter type for response ("full" or "display", default: "display")
  - `"display"`: Returns filtered response optimized for display (token reduction)
  - `"full"`: Returns complete API response with all fields

**Returns:** Account information including:
- Account settings and configurations
- Balance and profit metrics (BTC, USD, percentage)
- Trading permissions and features
- Exchange-specific details and status
- Auto-balance settings and errors

**Safety:** This is a read-only operation with no trading risks. All sensitive information is filtered appropriately.

**API Details:**
- **Endpoint:** `GET /ver1/accounts/{account_id}`
- **Security:** SIGNED (requires API key + HMAC signature)  
- **Permission:** ACCOUNTS_READ

**Models:**
- [GetAccountInfoRequest](../models/account.md#getaccountinforequest) - Request parameters and validation

**Examples:** [Account Management Conversation](../conversations/account-management-conversation.md#get-account-info)

## Usage Patterns

### Basic Account Information
```python
# Get all connected exchanges with filtered response
exchanges = await get_connected_exchanges_and_wallets()

# Get complete account information
full_data = await get_connected_exchanges_and_wallets(response_filter="full")

# Get account summary with aggregated data
summary = await get_account_info()

# Get specific account details
account = await get_account_info(account_id=31337503)

# Get complete account information without filtering
detailed_account = await get_account_info(account_id="summary", response_filter="full")
```

### Trading Safety Considerations

- **Read-only operation**: No financial risk as this endpoint only retrieves information
- **Credential security**: All sensitive account information is automatically filtered from responses
- **Rate limiting**: Respects 3Commas API rate limits (300 requests per minute)
- **Account validation**: Returned data can be used to validate trading permissions before bot operations

## Error Handling

All account management tools use the `@handle_api_errors` decorator for consistent error handling:

- **API Errors**: Automatically handled with descriptive error messages
- **Authentication Errors**: Clear indication when API credentials are invalid
- **Rate Limiting**: Exponential backoff when rate limits are exceeded
- **Network Errors**: Retry logic for transient network issues

## Related Documentation

- **Models:** [Account Models](../models/account.md) - Data structures and validation
- **API Reference:** [3Commas Account API](https://developers.3commas.io/account)
- **Authentication:** [HMAC-SHA256 Authentication](../DEVELOPMENT.md#authentication)
- **Rate Limiting:** [API Rate Limits](../DEVELOPMENT.md#rate-limiting)