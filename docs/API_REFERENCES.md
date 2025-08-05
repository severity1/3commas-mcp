# 3Commas API References

This document contains links to all available 3Commas API reference documentation and tracks implementation status for the 3Commas MCP server.

## Implementation Status

✅ = Implemented and tested  
🚧 = In progress  
⏸️ = Not yet implemented  
💰 = Requires paid 3Commas tier  
⚠️ = High risk operation requiring special handling

## Documentation Cross-References

For each implemented API, documentation is available in multiple layers:
- **Tools**: [docs/tools/](tools/) - Function signatures and usage examples
- **Models**: [docs/models/](models/) - Data models and validation
- **Conversations**: [docs/conversations/](conversations/) - Real-world usage scenarios
- **Implementation**: Source code with comprehensive docstrings

## API Documentation

### Core/Quick Start (Foundation)
- [Overview](https://developers.3commas.io/quick-start/overview)
- [Security and Permission Types](https://developers.3commas.io/quick-start/security-and-permission-types)
- [How to Start](https://developers.3commas.io/quick-start/how-to-start)
- [How to create an RSA Key pair](https://developers.3commas.io/quick-start/how-to-create-an-rsa-key-pair)
- [Signing a Request Using RSA](https://developers.3commas.io/quick-start/signing-a-request-using-rsa)
- [Signing a Request Using HMAC SHA256](https://developers.3commas.io/quick-start/signing-a-request-using-hmac-sha256)
- [Dates and times](https://developers.3commas.io/quick-start/dates-and-times)
- [Errors](https://developers.3commas.io/quick-start/errors)
- [Limits](https://developers.3commas.io/quick-start/limits)

### Account APIs (Account Management)
- [Account Entity](https://developers.3commas.io/account/account-entity) - Account data structure and field definitions
- [⏸️] `GET` [Available Market Subtypes](https://developers.3commas.io/account/available-market-subtypes) - Get supported market types for exchanges
- [⏸️] `POST` [Add Exchange Account](https://developers.3commas.io/account/add-exchange-account) - Connect new exchange account
- [✅] `GET` [Get Account Info](https://developers.3commas.io/account/get-account-info) - Retrieve current account information
- [⏸️] `POST` [Edit Exchange Account](https://developers.3commas.io/account/edit-exchange-account) - Modify exchange account settings
- [✅] `GET` [List Connected Exchanges and Wallets](https://developers.3commas.io/account/list-of-connected-exchanges-and-wallets) - Get all connected exchange accounts
- [⏸️] `GET` [Get List of Active Entities](https://developers.3commas.io/account/get-the-list-of-active-entities) - Retrieve active trading entities
- [⏸️] `POST` [Rename Exchange Account](https://developers.3commas.io/account/rename-exchange-account) - Update exchange account name
- [⏸️] `GET` [Balance History Data](https://developers.3commas.io/account/balance-history-data) - Historical balance changes over time
- [⏸️] `POST` [Load Balances for Specified Exchange](https://developers.3commas.io/account/load-balances-for-specified-exchange) - Refresh balance data from exchange
- [⏸️⚠️] `POST` [Sell All to BTC](https://developers.3commas.io/account/sell-all-to-btc) - Convert all holdings to BTC **[High Risk]**
- [⏸️⚠️] `POST` [Sell All to USD](https://developers.3commas.io/account/sell-all-to-usd) - Convert all holdings to USD **[High Risk]**
- [⏸️] `POST` [Account Leverage Information](https://developers.3commas.io/account/account-leverage-information) - Retrieve leverage settings and limits
- [⏸️] `GET` [Deposit or Withdraw Networks Info](https://developers.3commas.io/account/deposit-or-withdraw-networks-info) - Available networks for deposits/withdrawals
- [⏸️] `GET` [User Deposit Data](https://developers.3commas.io/account/user-deposit-data) - Deposit address and transaction history
- [⏸️⚠️] `POST` [Delete Exchange Account](https://developers.3commas.io/account/delete-an-exchange-account) - Remove exchange account **[Destructive]**
- [⏸️] `POST` [User Balances for Pie Chart](https://developers.3commas.io/account/user-balances-for-pie-chart-visualization) - Balance data formatted for pie chart display
- [⏸️] `POST` [User Balances for Table Chart](https://developers.3commas.io/account/user-balances-for-table-chart-visualization) - Balance data formatted for table display
- [⏸️] `POST` [Convert Dust Coins to BNB](https://developers.3commas.io/account/convert-dust-coins-to-bnb) - Convert small balances to BNB
- [⏸️] `GET` [Get Daily Trading Volume](https://developers.3commas.io/account/get-volume-daily) - Daily trading volume statistics
- [⏸️] `GET` [Get Monthly Trading Volume](https://developers.3commas.io/account/get-volume-monthly) - Monthly trading volume statistics
- [⏸️] `GET` [Get All-Time Trading Volume](https://developers.3commas.io/account/get-volume-total) - Total historical trading volume

### Market Data APIs (Market Information)
- [✅] `GET` [Supported Markets List](https://developers.3commas.io/market-data/supported_markets_list) - Get list of supported trading markets and exchanges
- [✅] `GET` [All Market Pairs](https://developers.3commas.io/market-data/all-market-pairs) - Retrieve all available trading pairs across markets
- [✅] `GET` [Currency Rates and Limits](https://developers.3commas.io/market-data/currency-rates-and-limits) - Get exchange rates and trading limits for currencies
- [⏸️] `GET` [Currency Rates and Limits with Leverage Data](https://developers.3commas.io/market-data/currency-rates-and-limits-with-leverage-data) - Get rates, limits, and leverage information

### Simple Trading APIs (Manual Trading)
- [Trade Entity](https://developers.3commas.io/simple-trading/trade-entity) - Trade data structure and field definitions
- [⏸️] `POST` [Create Trade](https://developers.3commas.io/simple-trading/create-trade) - Create new manual trade order
- [⏸️] `GET` [Get Trade](https://developers.3commas.io/simple-trading/get-trade) - Retrieve specific trade details
- [⏸️] `GET` [Get Active Trades](https://developers.3commas.io/simple-trading/get-active-trades) - List all currently active trades
- [⏸️] `GET` [Trades History](https://developers.3commas.io/simple-trading/get-trades-history) - Get historical trade records
- [⏸️⚠️] `POST` [Cancel Trade](https://developers.3commas.io/simple-trading/cancel-trade) - Cancel active trade **[High Risk]**

### DCA Bot APIs (Automated Trading - DCA Strategy)
- [DCA Bot Entity](https://developers.3commas.io/dca-bot/dca-bot-entity) - DCA bot data structure and field definitions
- [✅] `GET` [Available Strategy List](https://developers.3commas.io/dca-bot/available-strategy-list) - Get list of available trading strategies
- [⏸️] `POST` [Create DCA Bot](https://developers.3commas.io/dca-bot/create-dca-bot) - Create new DCA trading bot
- [⏸️] `PATCH` [Edit DCA Bot](https://developers.3commas.io/dca-bot/edit-dca-bot) - Modify existing DCA bot configuration
- [✅] `GET` [Get DCA Bot](https://developers.3commas.io/dca-bot/get-dca-bot) - Retrieve specific DCA bot details
- [✅] `GET` [Get List of DCA Bots](https://developers.3commas.io/dca-bot/get-the-list-of-dca-bots) - List all DCA bots for account
- [⏸️] `POST` [Disable DCA Bot](https://developers.3commas.io/dca-bot/disable-dca-bot) - Stop DCA bot trading
- [⏸️] `POST` [Enable DCA Bot](https://developers.3commas.io/dca-bot/enable-dca-bot) - Start DCA bot trading
- [⏸️] `POST` [Copy DCA Bot](https://developers.3commas.io/dca-bot/copy-dca-bot) - Duplicate existing DCA bot configuration
- [⏸️⚠️] `POST` [Close DCA Bot at Market Price](https://developers.3commas.io/dca-bot/close-dca-bot-at-market-price) - Force close bot positions at market price **[High Risk]**
- [⏸️⚠️] `POST` [Cancel DCA Bot](https://developers.3commas.io/dca-bot/cancel-dca-bot) - Cancel DCA bot and all active deals **[High Risk]**
- [⏸️] `POST` [Add Pairs to Blacklist](https://developers.3commas.io/dca-bot/add-pairs-to-blacklist) - Add trading pairs to blacklist
- [✅] `GET` [Get Blacklist of Pairs](https://developers.3commas.io/dca-bot/get-blacklist-of-pairs) - Retrieve blacklisted trading pairs
- [✅] `GET` [Get DCA Bot Profit Data](https://developers.3commas.io/dca-bot/get-dca-bot-profit-data) - Retrieve bot profit analytics
- [⏸️] `GET` [Get DCA Bot Stats](https://developers.3commas.io/dca-bot/get-dca-bot-stats) - Get bot performance statistics
- [⏸️] `GET` [Get DCA Bot Stats by Date](https://developers.3commas.io/dca-bot/get-dca-bot-stats-by-date) - Get bot stats for specific date range
- [⏸️⚠️] `POST` [Delete DCA Bot](https://developers.3commas.io/dca-bot/delete-dca-bot) - Permanently remove DCA bot **[Destructive]**
- [⏸️] `GET` [DCA Bot Deals Stats](https://developers.3commas.io/dca-bot/dca-bot-deals-stats) - Statistics for bot deals and trades

### Grid Bot APIs (Automated Trading - Grid Strategy) **[EXCLUDED FROM MVP]**
*Grid Bot APIs are not included in the current MVP scope as they are not actively used.*

- [Grid Bot Entity](https://developers.3commas.io/grid-bot/grid-bot-entity) - Grid bot data structure and field definitions
- [❌] `POST` [Create Grid Bot](https://developers.3commas.io/grid-bot/create-grid-bot) - Create new grid trading bot **[Not in MVP]**
- [❌] `PATCH` [Edit Grid Bot](https://developers.3commas.io/grid-bot/edit-grid-bot) - Modify existing grid bot configuration **[Not in MVP]**
- [❌] `GET` [Get Grid Bot](https://developers.3commas.io/grid-bot/get-grid-bot) - Retrieve specific grid bot details **[Not in MVP]**
- [❌] `GET` [Get List of Grid Bots](https://developers.3commas.io/grid-bot/get-the-list-of-grid-bots) - List all grid bots for account **[Not in MVP]**
- [❌] `GET` [Get Profit Details](https://developers.3commas.io/grid-bot/get-profit-details) - Retrieve grid bot profit analytics **[Not in MVP]**
- [❌] `POST` [Disable Grid Bot](https://developers.3commas.io/grid-bot/disable-grid-bot) - Stop grid bot trading **[Not in MVP]**
- [❌] `POST` [Enable Grid Bot](https://developers.3commas.io/grid-bot/enable_grid_bot) - Start grid bot trading **[Not in MVP]**
- [❌] `DELETE` [Delete Grid Bot](https://developers.3commas.io/grid-bot/delete-grid-bot) - Permanently remove grid bot **[Not in MVP]**
- [❌] `POST` [Set Note to Grid Bot](https://developers.3commas.io/grid-bot/set-a-note-to-grid-bot) - Add or update grid bot notes **[Not in MVP]**
- [❌] `GET` [Required Balances for Launch](https://developers.3commas.io/grid-bot/required-balances-for-launch) - Get minimum balance requirements **[Not in MVP]**
- [❌] `GET` [Grid Bot Events](https://developers.3commas.io/grid-bot/grid-bot-events) - Retrieve grid bot activity events **[Not in MVP]**
- [❌] `GET` [Get Market Orders of Grid Bot](https://developers.3commas.io/grid-bot/get-market-orders-of-grid-bot) - List grid bot market orders **[Not in MVP]**

### Smart Trading APIs (Advanced Manual Trading)
- [SmartTrade Entity](https://developers.3commas.io/smart-trade/smart-trade-entity) - SmartTrade data structure and field definitions
- [⏸️] `POST` [Create SmartTrade](https://developers.3commas.io/smart-trade/create-smart-trade) - Create new smart trade order
- [⏸️] `PATCH` [Edit SmartTrade](https://developers.3commas.io/smart-trade/edit-smart-trade) - Modify existing smart trade configuration
- [⏸️] `GET` [Get SmartTrade](https://developers.3commas.io/smart-trade/get-smart-trade) - Retrieve specific smart trade details
- [⏸️] `GET` [Get List of SmartTrades](https://developers.3commas.io/smart-trade/get-the-list-of-smart-trade) - List all smart trades for account
- [⏸️] `POST` [Add Funds for SmartTrades](https://developers.3commas.io/smart-trade/add-funds-for-smart-trade) - Increase smart trade position size
- [⏸️] `GET` [Available Reduce Funds](https://developers.3commas.io/smart-trade/available-reduce-funds) - Get reducible fund amounts
- [⏸️] `POST` [Reduce Funds for SmartTrade](https://developers.3commas.io/smart-trade/reduce-funds-for-smart-trade) - Decrease smart trade position size
- [⏸️⚠️] `POST` [Close SmartTrade at Market Price](https://developers.3commas.io/smart-trade/close-smart-trade-at-market-price) - Force close smart trade at market price **[High Risk]**
- [⏸️] `POST` [Add Note to SmartTrade](https://developers.3commas.io/smart-trade/add-a-note-to-smart-trade) - Add or update smart trade notes
- [⏸️⚠️] `DELETE` [Cancel SmartTrade](https://developers.3commas.io/smart-trade/cancel_smart-trade) - Cancel active smart trade **[High Risk]**
- [⏸️] `POST` [Force Start SmartTrade](https://developers.3commas.io/smart-trade/force-start-smart-trade) - Manually trigger smart trade execution

#### Smart Trade Execution APIs
- [Trade Entity](https://developers.3commas.io/smart-trade/trades/trade-entity) - Trade data structure and field definitions
- [⏸️] `GET` [Get Trades of SmartTrade](https://developers.3commas.io/smart-trade/trades/get-trades-of-smart-trade) - Retrieve trades for specific smart trade
- [⏸️⚠️] `POST` [Close Trade by Market](https://developers.3commas.io/smart-trade/trades/closes-trade-by-market) - Force close trade at market price **[High Risk]**
- [⏸️⚠️] `DELETE` [Cancel Trade](https://developers.3commas.io/smart-trade/trades/cancel-trade) - Cancel active trade **[High Risk]**

## Endpoints Summary

### Base URL
```
https://api.3commas.io/public/api
```

## Authentication
All requests require:
- `APIKEY` header with your API key
- `APISIGN` header with request signature


## Safety Classifications

### Low Risk Operations
- Read-only operations (get, list)
- Market data retrieval
- Strategy information lookup
- Account balance queries

### Medium Risk Operations
- Bot creation and configuration
- Bot enable/disable operations
- Safety order management
- Deal parameter updates

### High Risk Operations ⚠️
- Bot deletion (permanent)
- Deal cancellation (potential profit loss)
- Panic sell operations (market price execution)
- Account deletion (permanent)

## Implementation Guidelines

### For Developers
- **MVP Priority**: Focus on bot management and strategy configuration first
- **Safety First**: Implement comprehensive validation for all medium/high risk operations
- **Documentation**: Update this file as APIs are implemented
- **Testing**: Ensure thorough testing for all risk levels

### Safety Requirements
- **High Risk Operations**: Require explicit user confirmation
- **Parameter Validation**: Comprehensive validation before API calls
- **Error Handling**: Clear error messages with trading context
- **Rate Limiting**: Respect 3Commas rate limits to protect user accounts

### Cross-Reference Updates
When implementing APIs, ensure updates to:
- [ ] This API reference status
- [ ] Tool documentation in docs/tools/
- [ ] Model documentation in docs/models/
- [ ] Conversation examples in docs/conversations/
- [ ] TASKS.md implementation status