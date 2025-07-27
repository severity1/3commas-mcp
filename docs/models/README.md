# Model Documentation

This directory contains documentation for all Pydantic models used in the 3Commas MCP server, organized by trading domain.

## Model Categories

### Bot Models
Documentation for DCA and Grid bot configuration models:
- **Bot Configuration**: Models for creating and updating bots
- **Bot Status**: Models for bot state and performance tracking
- **Bot Filters**: Models for bot listing and search operations

### Strategy Models  
Documentation for trading strategy configuration models:
- **Technical Indicators**: RSI, MACD, Bollinger Bands, Moving Average models
- **QFL Strategy**: Quick Fingers Luc strategy configuration
- **Custom Signals**: External signal webhook configuration models

### Deal Models
Documentation for deal and safety order management models:
- **Deal Configuration**: Models for deal creation and management
- **Safety Orders**: Models for safety order configuration and limits
- **Deal Status**: Models for deal tracking and profit/loss calculation

### Account Models
Documentation for exchange account and market data models:
- **Account Configuration**: Exchange account setup and permissions
- **Account Balance**: Balance tracking and trading limits
- **Market Data**: Trading pairs, currency rates, and market information

## Documentation Structure

Each model documentation file follows a consistent template:

### Model Overview
- **Purpose**: What the model validates and its trading context
- **Used By**: Links to tools that use this model
- **API Mapping**: How model fields map to 3Commas API fields
- **Safety Considerations**: Trading safety requirements and constraints

### Field Documentation
- **Field Descriptions**: Detailed description of each model field
- **Validation Rules**: Pydantic validation rules and trading constraints
- **Type Information**: Complete type hints and optional/required status
- **Examples**: Sample valid and invalid field values

### Usage Examples
- **Creation Examples**: How to create model instances
- **Validation Examples**: Common validation scenarios
- **Error Handling**: Common validation errors and solutions
- **Integration Examples**: How models integrate with tools and API client

## Model Files

### Available Model Documentation

#### Base Models (`base.md`) ✅
- `BaseModelConfig`: Foundation configuration for all Pydantic models
- `APIRequest`: Base class for all API request models  
- `APIResponse`: Type alias for all API response data
- `BotType`, `DealStatus`, `StrategyType`: Common enums for trading operations
- `ReqT`: Generic type variable for API request models

### Planned Model Documentation

#### Bot Models (`bots.md`)
- `DCABotConfig`: DCA bot creation and configuration
- `GridBotConfig`: Grid bot setup and parameters
- `BotStatus`: Bot state, performance, and operational status
- `BotFilters`: Bot listing and search parameters
- `BotUpdate`: Bot modification and update parameters

#### Strategy Models (`strategies.md`)
- `QFLStrategy`: Quick Fingers Luc strategy configuration
- `RSIStrategy`: RSI indicator strategy parameters
- `BollingerBandsStrategy`: Bollinger Bands strategy settings
- `MACDStrategy`: MACD strategy configuration
- `MovingAverageStrategy`: Moving Average strategy parameters
- `CustomSignalStrategy`: External signal webhook configuration

#### Deal Models (`deals.md`)
- `DealConfig`: Deal creation and management parameters
- `SafetyOrderConfig`: Safety order configuration and constraints
- `DealStatus`: Deal state and profit/loss tracking
- `DealFilters`: Deal listing and search parameters
- `DealUpdate`: Deal modification parameters

#### Account Models (`accounts.md`)
- `AccountConfig`: Exchange account configuration
- `AccountBalance`: Balance and trading limit information
- `AccountPermissions`: Account trading capabilities and restrictions
- `AccountFilters`: Account listing and search parameters

#### Market Models (`pairs.md`)
- `TradingPair`: Trading pair configuration and market data
- `PairBlacklist`: Blacklisted pairs management
- `CurrencyRates`: Exchange rate and conversion data
- `MarketFilters`: Market data filtering parameters

## Cross-References

### Integration with Other Documentation Layers
- **Tools Documentation**: Each model links to tools that use it - [Base Models](base.md) used by [DCA Bot Tools](../tools/dca_bots.md)
- **Conversation Examples**: Models reference usage scenarios - [Base Models](base.md) patterns shown in [DCA Bot Management](../conversations/dca-bot-management-conversation.md)
- **Code Implementation**: Models link to actual implementation files - [Base Models](base.md) implemented in `threecommas_mcp/models/base.py`
- **API Reference**: Models reference corresponding 3Commas API endpoints

### Model Relationships
- **Inheritance**: Base model relationships and shared patterns
- **Composition**: Models that include other models as fields
- **Dependencies**: Models that depend on other models for validation
- **Usage Patterns**: Common model usage patterns across tools

## Development Guidelines

### Adding New Models
When adding new model documentation:
1. **Follow Template**: Use the established model documentation template
2. **Include Safety**: Document trading safety considerations
3. **Cross-Reference**: Link to related tools, conversations, and API docs
4. **Validate Examples**: Ensure all examples are valid and tested
5. **Update Index**: Add new models to this README

### Maintenance
- **Keep Current**: Update documentation when models change
- **Validate Links**: Ensure all cross-references remain valid
- **Test Examples**: Verify all code examples work correctly
- **Safety Review**: Regularly review safety documentation for accuracy

## Trading Safety Focus

All model documentation emphasizes trading safety:
- **Parameter Validation**: Clear documentation of trading parameter constraints
- **Risk Assessment**: Risk level indicators for model usage
- **Safety Warnings**: Explicit warnings for high-risk operations
- **Validation Examples**: Examples of proper validation for trading safety

This model documentation ensures that developers understand not just how to use the models, but how to use them safely in trading contexts.