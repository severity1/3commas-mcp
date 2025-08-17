# Account Management Tools

## Available Tools

### health_check

**Function:** `health_check() -> APIResponse`

**Description:** Tests API connectivity and authentication status with 3Commas.

**Parameters:** None

**Returns:** Health status with API base URL and credentials configuration status.

### get_connected_exchanges_and_wallets

**Function:** `get_connected_exchanges_and_wallets(response_filter: str = "display") -> APIResponse`

**Description:** Retrieves all connected exchange accounts and wallet information.

**Parameters:**
- `response_filter`: Response detail level ("full" or "display")

**Returns:** List of connected exchanges with account details and balances.

### get_account_info

**Function:** `get_account_info(account_id: Union[str, int] = "summary", response_filter: str = "display") -> APIResponse`

**Description:** Retrieves account information for a specific account or aggregated summary.

**Parameters:**
- `account_id`: Account ID or "summary" for aggregated data
- `response_filter`: Response detail level ("full" or "display")

**Returns:** Account information including balance, profit metrics, and trading settings.

### get_balance_history_data

**Function:** `get_balance_history_data(date_from: str, account_id: Union[str, int] = "summary", date_to: Optional[str] = None, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves account balance history over time.

**Parameters:**
- `date_from`: Start date in ISO 8601 format (required)
- `account_id`: Account ID or "summary" for aggregated data
- `date_to`: End date in ISO 8601 format (optional)
- `response_filter`: Response detail level ("full" or "display")

**Returns:** Historical balance data with timestamps and USD/BTC values.