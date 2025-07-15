# 3Commas API References

This document contains links to all available 3Commas API reference documentation.

## Implementation Status

✅ = Implemented and tested  
⏸️ = Not yet implemented  
💰 = Requires paid 3Commas tier

## API Documentation

### Core
- [Overview](https://developers.3commas.io/) - Main API documentation
- [Authentication](https://developers.3commas.io/#authentication) - API key and signature setup
- [Rate Limits](https://developers.3commas.io/#rate-limiting) - Request limits and throttling

### DCA Bot APIs
- [⏸️] [Create Bot](https://developers.3commas.io/dca-bot/#create-bot) - Create new DCA bot
- [⏸️] [Update Bot](https://developers.3commas.io/dca-bot/#update-bot) - Modify existing bot configuration
- [⏸️] [Get Bot Details](https://developers.3commas.io/dca-bot/#get-bot-details) - Retrieve specific bot information
- [⏸️] [List Bots](https://developers.3commas.io/dca-bot/#list-bots) - Get all bots for account
- [⏸️] [Delete Bot](https://developers.3commas.io/dca-bot/#delete-bot) - Permanently remove bot
- [⏸️] [Enable Bot](https://developers.3commas.io/dca-bot/#enable-bot) - Activate bot trading
- [⏸️] [Disable Bot](https://developers.3commas.io/dca-bot/#disable-bot) - Pause bot trading
- [⏸️] [Cancel All Deals](https://developers.3commas.io/dca-bot/#cancel-all-deals) - Cancel active deals
- [⏸️] [Panic Sell All Deals](https://developers.3commas.io/dca-bot/#panic-sell-all-deals) - Emergency sell all positions
- [⏸️] [Get Bot Stats](https://developers.3commas.io/dca-bot/#get-bot-stats) - Bot performance statistics
- [⏸️] [Get Bot Profit](https://developers.3commas.io/dca-bot/#get-bot-profit) - Daily profit data
- [⏸️] [Get Deals Stats](https://developers.3commas.io/dca-bot/#deals-stats) - Deal statistics and metrics

### Grid Bot APIs
- [⏸️] [Create Grid Bot](https://developers.3commas.io/grid-bot/#create-grid-bot) - Create new grid bot
- [⏸️] [Update Grid Bot](https://developers.3commas.io/grid-bot/#update-grid-bot) - Modify grid bot settings
- [⏸️] [Get Grid Bot Details](https://developers.3commas.io/grid-bot/#get-grid-bot-details) - Retrieve grid bot info
- [⏸️] [List Grid Bots](https://developers.3commas.io/grid-bot/#list-grid-bots) - Get all grid bots
- [⏸️] [Delete Grid Bot](https://developers.3commas.io/grid-bot/#delete-grid-bot) - Remove grid bot
- [⏸️] [Enable Grid Bot](https://developers.3commas.io/grid-bot/#enable-grid-bot) - Activate grid bot
- [⏸️] [Disable Grid Bot](https://developers.3commas.io/grid-bot/#disable-grid-bot) - Pause grid bot

### Smart Trade APIs
- [⏸️] [Create Smart Trade](https://developers.3commas.io/smart-trade/#create-smart-trade) - Create manual trade
- [⏸️] [Update Smart Trade](https://developers.3commas.io/smart-trade/#update-smart-trade) - Modify trade parameters
- [⏸️] [Get Smart Trade](https://developers.3commas.io/smart-trade/#get-smart-trade) - Retrieve trade details
- [⏸️] [List Smart Trades](https://developers.3commas.io/smart-trade/#list-smart-trades) - Get all smart trades
- [⏸️] [Cancel Smart Trade](https://developers.3commas.io/smart-trade/#cancel-smart-trade) - Cancel active trade
- [⏸️] [Close Smart Trade](https://developers.3commas.io/smart-trade/#close-smart-trade) - Force close trade

### Strategy APIs
- [⏸️] [Get Strategy List](https://developers.3commas.io/strategies/#strategy-list) - Available trading strategies
- [⏸️] [QFL Strategy](https://developers.3commas.io/strategies/#qfl) - QFL configuration options
- [⏸️] [RSI Strategy](https://developers.3commas.io/strategies/#rsi) - RSI indicator settings
- [⏸️] [Bollinger Bands Strategy](https://developers.3commas.io/strategies/#bollinger-bands) - BB parameters
- [⏸️] [MACD Strategy](https://developers.3commas.io/strategies/#macd) - MACD configuration
- [⏸️] [Moving Average Strategy](https://developers.3commas.io/strategies/#moving-average) - MA settings
- [⏸️] [Custom Signals](https://developers.3commas.io/strategies/#custom-signals) - External signal integration

### Account APIs
- [⏸️] [Get Accounts](https://developers.3commas.io/accounts/#get-accounts) - List exchange accounts
- [⏸️] [Create Account](https://developers.3commas.io/accounts/#create-account) - Add exchange account
- [⏸️] [Update Account](https://developers.3commas.io/accounts/#update-account) - Modify account settings
- [⏸️] [Delete Account](https://developers.3commas.io/accounts/#delete-account) - Remove exchange account
- [⏸️] [Get Account Balance](https://developers.3commas.io/accounts/#account-balance) - Current balance info
- [⏸️] [Account Load Balances](https://developers.3commas.io/accounts/#load-balances) - Refresh balance data

### Pairs Management APIs
- [⏸️] [Get Pairs Blacklist](https://developers.3commas.io/pairs/#pairs-blacklist) - Blacklisted trading pairs
- [⏸️] [Update Pairs Blacklist](https://developers.3commas.io/pairs/#update-blacklist) - Modify blacklist
- [⏸️] [Get Market Pairs](https://developers.3commas.io/pairs/#market-pairs) - Available trading pairs
- [⏸️] [Currency Rates](https://developers.3commas.io/pairs/#currency-rates) - Exchange rates data

### Deals APIs
- [⏸️] [Get Deals](https://developers.3commas.io/deals/#get-deals) - List all deals
- [⏸️] [Get Deal](https://developers.3commas.io/deals/#get-deal) - Specific deal details
- [⏸️] [Cancel Deal](https://developers.3commas.io/deals/#cancel-deal) - Cancel active deal
- [⏸️] [Panic Sell Deal](https://developers.3commas.io/deals/#panic-sell-deal) - Emergency sell deal
- [⏸️] [Update Deal](https://developers.3commas.io/deals/#update-deal) - Modify deal parameters
- [⏸️] [Add Safety Order](https://developers.3commas.io/deals/#add-safety-order) - Manual safety order

### Portfolio APIs
- [⏸️] [Get Portfolio Stats](https://developers.3commas.io/portfolio/#portfolio-stats) - Overall performance
- [⏸️] [Get Profit Stats](https://developers.3commas.io/portfolio/#profit-stats) - Profit/loss analytics
- [⏸️] [Get Balance Stats](https://developers.3commas.io/portfolio/#balance-stats) - Balance distribution
- [⏸️] [Portfolio Pie Chart](https://developers.3commas.io/portfolio/#pie-chart) - Asset allocation data

### Marketplace APIs 💰
- [⏸️] [Get Marketplace Items](https://developers.3commas.io/marketplace/#marketplace-items) 💰 - Available strategies
- [⏸️] [Subscribe to Strategy](https://developers.3commas.io/marketplace/#subscribe) 💰 - Copy trading signals
- [⏸️] [Unsubscribe Strategy](https://developers.3commas.io/marketplace/#unsubscribe) 💰 - Stop copying signals
- [⏸️] [My Subscriptions](https://developers.3commas.io/marketplace/#my-subscriptions) 💰 - Active subscriptions

### Webhooks APIs
- [⏸️] [Create Webhook](https://developers.3commas.io/webhooks/#create-webhook) - Setup external signals
- [⏸️] [Update Webhook](https://developers.3commas.io/webhooks/#update-webhook) - Modify webhook config
- [⏸️] [Delete Webhook](https://developers.3commas.io/webhooks/#delete-webhook) - Remove webhook
- [⏸️] [List Webhooks](https://developers.3commas.io/webhooks/#list-webhooks) - Get all webhooks
- [⏸️] [Test Webhook](https://developers.3commas.io/webhooks/#test-webhook) - Validate webhook setup

### Trading View Integration
- [⏸️] [TradingView Signals](https://developers.3commas.io/tradingview/#tradingview-signals) - Custom signal format
- [⏸️] [Signal Processing](https://developers.3commas.io/tradingview/#signal-processing) - How signals are handled
- [⏸️] [Webhook URL Format](https://developers.3commas.io/tradingview/#webhook-format) - Required URL structure

### User Management APIs
- [⏸️] [Get User Info](https://developers.3commas.io/users/#user-info) - Current user details
- [⏸️] [Update User](https://developers.3commas.io/users/#update-user) - Modify user settings
- [⏸️] [Change Password](https://developers.3commas.io/users/#change-password) - Update password
- [⏸️] [Get Permissions](https://developers.3commas.io/users/#permissions) - API key permissions

### Notification APIs
- [⏸️] [Get Notifications](https://developers.3commas.io/notifications/#get-notifications) - User notifications
- [⏸️] [Mark as Read](https://developers.3commas.io/notifications/#mark-read) - Update notification status
- [⏸️] [Notification Settings](https://developers.3commas.io/notifications/#settings) - Configure alerts

## Endpoints Summary

### Base URL
```
https://api.3commas.io
```

### Common Endpoints
- `GET /ver1/bots` - List all bots
- `POST /ver1/bots/create_bot` - Create new bot  
- `GET /ver1/bots/:id/show` - Get bot details
- `PATCH /ver1/bots/:id/update` - Update bot
- `POST /ver1/bots/:id/delete` - Delete bot
- `POST /ver1/bots/:id/enable` - Enable bot
- `POST /ver1/bots/:id/disable` - Disable bot
- `GET /ver1/deals` - List all deals
- `GET /ver1/accounts` - List accounts
- `GET /ver1/bots/strategy_list` - Available strategies
- `GET /ver1/bots/pairs_black_list` - Blacklisted pairs

## Authentication
All requests require:
- `APIKEY` header with your API key
- `APISIGN` header with request signature

## Rate Limits
- Standard endpoints: 300 requests/minute
- Trading endpoints: 60 requests/minute  
- Statistics endpoints: 120 requests/minute