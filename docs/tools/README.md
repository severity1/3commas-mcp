# Tool Documentation

This directory contains documentation for all MCP tools that expose 3Commas API functionality, organized by trading domain.

## Tool Categories

### Bot Management Tools
Documentation for DCA and Grid bot management operations:
- **Bot Creation**: Tools for creating new bots with validated configurations
- **Bot Management**: Tools for updating, enabling, disabling, and deleting bots
- **Bot Monitoring**: Tools for retrieving bot status, performance, and statistics
- **Bot Operations**: Tools for cloning bots and managing bot portfolios

### Strategy Configuration Tools
Documentation for trading strategy setup and management:
- **Strategy Discovery**: Tools for listing available strategies and parameters
- **Strategy Configuration**: Tools for configuring technical indicator strategies
- **Custom Signals**: Tools for setting up external signal webhooks
- **Strategy Optimization**: Tools for analyzing and optimizing strategy performance

### Deal Management Tools
Documentation for deal and safety order operations:
- **Deal Monitoring**: Tools for listing and analyzing active deals
- **Deal Operations**: Tools for canceling, updating, and managing deals
- **Safety Orders**: Tools for adding and configuring safety orders
- **Deal Analysis**: Tools for deal performance tracking and profit calculation

### Account Management Tools
Documentation for exchange account and market data operations:
- **Account Setup**: Tools for managing exchange account connections
- **Account Monitoring**: Tools for checking account balances and permissions
- **Market Data**: Tools for retrieving trading pairs and market information
- **Pair Management**: Tools for managing trading pair blacklists

## Documentation Structure

Each tool documentation file follows a consistent template:

### Tool Overview
- **Purpose**: What the tool does and its trading context
- **Safety Level**: Risk assessment (Low/Medium/High)
- **Prerequisites**: Account permissions and setup requirements
- **Related Models**: Links to models used by this tool

### Function Reference
- **Function Signature**: Complete function signature with type hints
- **Parameters**: Detailed parameter descriptions with trading constraints
- **Returns**: Return value structure and trading data
- **Errors**: Common error scenarios and handling
- **Examples**: Usage examples with realistic trading parameters

### Trading Safety
- **Safety Considerations**: Trading safety requirements and warnings
- **Risk Assessment**: Potential trading risks and mitigation strategies
- **Validation Requirements**: Required parameter validation
- **Error Handling**: Safe error handling patterns

### Integration Examples
- **Basic Usage**: Simple tool usage examples
- **Advanced Scenarios**: Complex trading scenarios using the tool
- **Error Handling**: Proper error handling in trading contexts
- **Cross-Tool Integration**: Using multiple tools together

## Tool Files

### Planned Tool Documentation

#### Bot Management (`bots.md`)
- `create_dca_bot`: Create new DCA bot with validated configuration
- `create_grid_bot`: Create new Grid bot with market parameters
- `get_bot_details`: Retrieve bot configuration and status
- `list_bots`: List bots with filtering and pagination
- `update_bot_config`: Modify bot configuration safely
- `enable_bot`: Activate bot trading with safety checks
- `disable_bot`: Pause bot trading operations
- `delete_bot`: Permanently remove bot (destructive)
- `clone_bot`: Duplicate successful bot configurations
- `get_bot_stats`: Retrieve bot performance metrics

#### Strategy Configuration (`strategies.md`)
- `get_strategy_list`: List available trading strategies
- `get_qfl_strategy`: Configure QFL strategy parameters
- `get_rsi_strategy`: Configure RSI strategy settings
- `get_bollinger_strategy`: Configure Bollinger Bands strategy
- `get_macd_strategy`: Configure MACD strategy parameters
- `get_moving_average_strategy`: Configure MA strategy settings
- `create_custom_signal`: Set up external signal webhooks
- `test_strategy_config`: Validate strategy configurations

#### Deal Management (`deals.md`)
- `get_deal_details`: Retrieve specific deal information
- `list_deals`: List deals with filtering options
- `cancel_deal`: Cancel active deal safely
- `update_deal`: Modify deal parameters
- `add_safety_order`: Add manual safety order
- `get_deal_safety_orders`: List deal safety orders
- `panic_sell_deal`: Emergency sell deal (high risk)
- `get_deals_stats`: Overall deal statistics

#### Account Management (`accounts.md`)
- `list_accounts`: List exchange accounts
- `get_account_details`: Retrieve account information
- `get_account_balance`: Check account balances
- `validate_account_permissions`: Verify trading permissions
- `load_account_balances`: Refresh balance data
- `get_account_trading_info`: Get trading capabilities

#### Market Data (`pairs.md`)
- `get_market_pairs`: List available trading pairs
- `get_currency_rates`: Retrieve exchange rates
- `get_pairs_blacklist`: List blacklisted pairs
- `update_pairs_blacklist`: Modify pair blacklist
- `validate_trading_pair`: Verify pair availability
- `get_pair_market_data`: Retrieve pair market information

## Cross-References

### Integration with Other Documentation Layers
- **Model Documentation**: Links to models used by each tool
- **Conversation Examples**: References to usage scenarios
- **Code Implementation**: Links to actual tool implementation
- **API Reference**: Links to corresponding 3Commas API endpoints

### Tool Relationships
- **Workflow Integration**: Tools that work together in trading workflows
- **Dependency Chains**: Tools that depend on other tools for data
- **Safety Dependencies**: Tools that require safety validation from other tools
- **Performance Integration**: Tools used together for performance optimization

## Development Guidelines

### Adding New Tools
When adding new tool documentation:
1. **Follow Template**: Use the established tool documentation template
2. **Include Safety**: Document trading safety considerations and risks
3. **Cross-Reference**: Link to related models, conversations, and implementation
4. **Test Examples**: Ensure all examples are valid and tested
5. **Update Index**: Add new tools to this README

### Maintenance
- **Keep Current**: Update documentation when tool signatures change
- **Validate Examples**: Ensure all code examples work correctly
- **Safety Review**: Regularly review safety documentation for accuracy
- **Cross-Reference**: Maintain valid links to all related documentation

## Trading Safety Focus

All tool documentation emphasizes trading safety:
- **Risk Classification**: Clear risk level indicators (Low/Medium/High)
- **Safety Warnings**: Explicit warnings for destructive operations
- **Parameter Validation**: Documentation of required validation
- **Error Handling**: Safe error handling patterns for trading contexts
- **Permission Requirements**: Clear documentation of required account permissions

## Usage Patterns

### Common Tool Workflows
- **Bot Setup Workflow**: Account validation → Strategy selection → Bot creation → Monitoring
- **Deal Management Workflow**: Deal monitoring → Safety order management → Performance analysis
- **Strategy Optimization Workflow**: Strategy analysis → Parameter tuning → Performance comparison
- **Risk Management Workflow**: Account monitoring → Position sizing → Safety order configuration

### Integration Examples
- **Multi-Bot Management**: Coordinating multiple bots for portfolio management
- **Strategy Backtesting**: Using historical data tools for strategy validation
- **Performance Monitoring**: Combining bot stats with deal analysis for optimization
- **Risk Assessment**: Using account and market data for risk management

This tool documentation ensures that developers understand not just how to use the tools, but how to use them safely and effectively in real trading scenarios.