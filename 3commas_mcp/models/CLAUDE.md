# CLAUDE.md for models/

This file provides guidance for Pydantic model implementations that validate 3Commas API data structures and trading parameters.

## Context Activation
This guidance activates when:
- Working in `3commas_mcp/models/` directory
- Creating/editing Pydantic model files (*.py)
- Implementing validation for 3Commas API structures
- Adding trading parameter validation or bot configuration models

**Companion directories**: tools/ (for usage), api/ (for requests), utils/ (for validation helpers)

## Model Architecture

### Directory Structure
- **__init__.py**: Model imports and exports
- **base.py**: Base models, common patterns, and trading validation utilities
- **Domain modules**: bots.py, strategies.py, deals.py, accounts.py, pairs.py, safety_orders.py

### Implementation Standards
- **Trading validation**: All models include trading safety validation
- **3Commas mapping**: Models map to 3Commas API field structures
- **Type safety**: Comprehensive type hints for all trading data
- **Configuration validation**: Bot and strategy parameters validated against 3Commas requirements

## Model Organization

### Domain Categories
- **Bot Models**: DCA bot configuration, grid bot settings, bot status and performance
- **Strategy Models**: QFL, RSI, Bollinger Bands, MACD, Moving Average configurations
- **Deal Models**: Deal creation, safety orders, deal status and profit tracking
- **Account Models**: Exchange account configuration, permissions, balance data
- **Market Models**: Trading pairs, currency rates, blacklist management

### File Organization Rules
- **Add to existing**: Model fits domain and file has < 10 models (trading complexity)
- **Create new file**: New domain OR existing file ≥ 10 models
- **Split file**: When file exceeds 12 models, split by logical sub-domains
- **Domain boundaries**: Create new domain for ≥ 3 conceptually distinct model groups
- **Naming**: Use descriptive names matching 3Commas terminology (e.g., DCABot, SafetyOrder)

## Implementation Requirements

### Essential Patterns
1. **Inherit from BaseModel**: All models extend Pydantic BaseModel
2. **Field validation**: Use Pydantic validators for trading parameter validation
3. **API mapping**: Include field mappings to 3Commas API structure
4. **Documentation**: Comprehensive docstrings with trading context
5. **Safety validation**: Trading-specific validation for bot and strategy parameters

### Trading Validation Standards
- **Bot Configuration**: Validate base_order_volume, safety_order_volume, max_safety_orders
- **Strategy Parameters**: Validate strategy-specific parameters against 3Commas requirements
- **Account Validation**: Verify exchange account permissions and trading capabilities
- **Pair Validation**: Validate trading pairs against account permissions and market availability
- **Deal Validation**: Validate deal parameters and safety order configurations

### Field Mapping Patterns
Models must include clear mapping between Python field names and 3Commas API fields:
```python
class DCABotConfig(BaseModel):
    account_id: int  # -> account_id
    pair: str        # -> pair
    base_order_volume: Decimal  # -> base_order_volume
    safety_order_volume: Decimal  # -> safety_order_volume
    
    class Config:
        # 3Commas API field mappings if different
        alias_generator = None  # Use exact field names for 3Commas
```

### Validation Patterns
Include comprehensive validation for trading parameters:
```python
@validator('base_order_volume')
def validate_base_order_volume(cls, v):
    if v <= 0:
        raise ValueError('Base order volume must be positive')
    # Additional trading-specific validation
    return v
```

## Model Categories

### Bot Configuration Models
- **DCABotConfig**: DCA bot creation and update parameters
- **GridBotConfig**: Grid bot configuration and settings
- **BotStatus**: Bot state, performance metrics, and operational status
- **BotFilters**: Filtering parameters for bot listing operations

### Strategy Configuration Models
- **QFLStrategy**: Quick Fingers Luc strategy parameters
- **RSIStrategy**: RSI indicator strategy configuration
- **BollingerBandsStrategy**: Bollinger Bands strategy settings
- **MACDStrategy**: MACD strategy parameters
- **MovingAverageStrategy**: Moving Average strategy configuration
- **CustomSignalStrategy**: External signal webhook configuration

### Deal and Safety Order Models
- **DealConfig**: Deal creation and management parameters
- **SafetyOrderConfig**: Safety order configuration and limits
- **DealStatus**: Deal state, profit/loss tracking, and completion status
- **DealFilters**: Filtering parameters for deal operations

### Account and Market Models
- **AccountConfig**: Exchange account configuration and permissions
- **AccountBalance**: Account balance and trading limits
- **TradingPair**: Trading pair configuration and market data
- **PairBlacklist**: Blacklisted pairs management
- **CurrencyRates**: Exchange rate data for profit calculations

## Development Standards

### Quality Checks
- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type Check**: `mypy .`
- **Test**: `pytest`

### Model Requirements
- All models must include comprehensive type hints
- Apply trading parameter validation using Pydantic validators
- Include docstrings with trading context and usage examples
- Map fields to 3Commas API structure with clear documentation
- Test validation logic with valid/invalid trading scenarios

### Integration Standards

### Tool Integration
When models are used in tools:
- Models provide validation for all tool parameters
- Include trading safety validation before API calls
- Apply proper error messages for validation failures
- Ensure model serialization matches 3Commas API expectations

### API Integration
When models work with API client:
- Models serialize to proper 3Commas API format
- Include field mappings for API compatibility
- Handle 3Commas response deserialization
- Apply proper type conversion for trading data

### Utility Integration
When models work with utilities:
- Use validation utilities for complex trading logic
- Apply common validation patterns across models
- Include utility functions for model transformation
- Use shared validation functions for consistency

## Implementation Workflow

### New Model Development Process
1. **Define API structure**: Analyze 3Commas API documentation for field requirements
2. **Create base model**: Extend BaseModel with proper field definitions
3. **Add validation**: Implement trading-specific validation logic
4. **Map API fields**: Document field mappings to 3Commas API
5. **Add documentation**: Include comprehensive docstrings with trading context
6. **Test validation**: Create tests for valid/invalid scenarios
7. **Update documentation**: Implementation status tracking

### Quality Validation Checklist
For each model implementation:
- [ ] Model extends BaseModel with proper type hints
- [ ] Trading parameter validation implemented using Pydantic validators
- [ ] Field mappings to 3Commas API documented clearly
- [ ] Comprehensive docstrings with trading context included
- [ ] Quality checks passed: format, lint, type check
- [ ] Tests cover validation scenarios: valid inputs, invalid inputs, edge cases
- [ ] Documentation updated: implementation status tracking

### 3Commas-Specific Model Patterns
- **Decimal precision**: Use Decimal for all financial values (volumes, prices, profits)
- **Enum validation**: Use Enums for strategy types, bot states, deal statuses
- **Required fields**: Clearly distinguish required vs optional parameters
- **Validation order**: Validate individual fields before cross-field validation
- **Error messages**: Provide clear, trading-context error messages for validation failures