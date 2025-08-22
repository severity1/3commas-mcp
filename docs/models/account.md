# Account Models

## Available Models

### GetConnectedExchangesRequest

**Purpose:** Request parameters for retrieving connected exchange accounts and wallets.

**Used by:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Key Fields:** No parameters required for this endpoint.

**Validation:** Inherits from APIRequest base class.

### GetAccountInfoRequest

**Purpose:** Request parameters for retrieving account information and summary data.

**Used by:** [get_account_info](../tools/account.md#get-account-info)

**Key Fields:**
- `account_id`: Account ID (integer) or "summary" for aggregated data (default: "summary")

**Validation:** Accepts both integer account IDs and "summary" string.

### GetBalanceHistoryRequest

**Purpose:** Request parameters for retrieving historical balance data over time.

**Used by:** [get_balance_history_data](../tools/account.md#get-balance-history-data)

**Key Fields:**
- `date_from`: Start date in ISO 8601 format (required)
- `account_id`: Account ID or "summary" for aggregated data (default: "summary")
- `date_to`: End date in ISO 8601 format (optional)

**Validation:** ISO 8601 date format validation with regex patterns.