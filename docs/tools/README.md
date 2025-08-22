# Tool Documentation

MCP tools for 3Commas API functionality - **12 tools implemented** (read-only operations only).

## Available Tools

### Account Management ([account.md](account.md))
- `health_check()` - API connectivity and authentication testing
- `get_account_info()` - Account details, balance, and profit metrics
- `get_connected_exchanges_and_wallets()` - Connected exchange accounts
- `get_balance_history_data()` - Historical balance tracking

### Market Data ([market_data.md](market_data.md))
- `get_supported_markets()` - Supported trading markets and exchanges
- `get_all_market_pairs()` - Available trading pairs across markets
- `get_currency_rates_and_limits()` - Exchange rates, limits, and precision

### DCA Bot Management ([dca_bots.md](dca_bots.md))
- `get_dca_bot_list()` - DCA bot portfolio with filtering
- `get_dca_bot_details()` - Comprehensive bot configuration and performance
- `get_available_strategy_list()` - Available trading strategies
- `get_dca_bot_profit_data()` - Daily profit analytics
- `get_blacklist_of_pairs()` - Trading restrictions and blacklisted pairs

All tools include `response_filter` parameter (`"display"` for essential data, `"full"` for complete response).