# Model Documentation

Pydantic models for 3Commas API functionality - **4 model domains implemented** (request validation only).

## Available Models

### Base Models ([base.md](base.md))
- `BaseModelConfig` - Foundation configuration for all Pydantic models
- `APIRequest` - Base class for all API request models
- `APIResponse` - Type alias for API response data
- `ResponseFilter` - Response filtering options enum
- Common enums: `BotType`, `DealStatus`, `StrategyType`

### Account Models ([account.md](account.md))
- `GetConnectedExchangesRequest` - Connected exchanges listing parameters
- `GetAccountInfoRequest` - Account details and summary parameters
- `GetBalanceHistoryRequest` - Balance history filtering parameters

### DCA Bot Models ([dca_bots.md](dca_bots.md))
- `GetDCABotListRequest` - Bot portfolio filtering and pagination
- `GetDCABotDetailsRequest` - Individual bot details parameters
- `GetAvailableStrategyListRequest` - Strategy listing parameters
- `GetDCABotProfitDataRequest` - Profit analytics parameters
- `GetBlacklistOfPairsRequest` - Trading restrictions parameters

### Market Data Models ([market_data.md](market_data.md))
- `GetAllMarketPairsRequest` - Trading pairs filtering parameters
- `GetCurrencyRatesRequest` - Currency rates and limits parameters
- `GetSupportedMarketsRequest` - Market listing parameters

All models include `response_filter` parameter validation and inherit from `APIRequest` base class.