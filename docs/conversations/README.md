# Conversation Examples

This directory contains real-world usage examples and interaction patterns for the 3Commas MCP server, organized by trading scenarios.

## Conversation Categories

### Bot Management Conversations
Real-world examples of bot creation, configuration, and management:
- **Getting Started**: First-time bot setup and basic configuration
- **Advanced Configuration**: Complex bot setups with multiple strategies
- **Bot Optimization**: Performance tuning and strategy adjustments
- **Portfolio Management**: Managing multiple bots for diversified trading

### Strategy Development Conversations
Examples of strategy configuration and optimization:
- **Strategy Selection**: Choosing appropriate strategies for market conditions
- **Parameter Tuning**: Optimizing strategy parameters for better performance
- **Signal Integration**: Setting up external signal sources and webhooks
- **Backtesting**: Analyzing strategy performance with historical data

### Deal Management Conversations
Examples of deal monitoring and safety order management:
- **Deal Monitoring**: Tracking active deals and performance
- **Safety Order Management**: Configuring and adjusting safety orders
- **Risk Management**: Managing deal risks and position sizing
- **Emergency Scenarios**: Handling market volatility and emergency situations

### Account Setup Conversations
Examples of account configuration and validation:
- **Initial Setup**: Connecting exchange accounts and validating permissions
- **Multi-Exchange Setup**: Managing multiple exchange connections
- **Security Configuration**: Setting up secure trading parameters
- **Troubleshooting**: Resolving common account and permission issues

## Documentation Structure

Each conversation example follows a realistic interaction pattern:

### Conversation Header
- **Scenario**: Brief description of the trading scenario
- **Participants**: User and Claude interaction
- **Tools Used**: List of MCP tools used in the conversation
- **Models Referenced**: Pydantic models involved in validation
- **Risk Level**: Trading risk assessment (Low/Medium/High)
- **Prerequisites**: Required account setup and permissions

### Interaction Flow
- **Natural Language**: Realistic user requests and Claude responses
- **Tool Calls**: Actual MCP tool invocations with parameters
- **Validation**: Parameter validation and safety checks
- **Results**: Tool responses and data interpretation
- **Follow-up**: Additional questions and refinements

### Safety Considerations
- **Risk Warnings**: Explicit warnings for high-risk operations
- **Validation Steps**: Required safety validation before operations
- **Error Scenarios**: How errors are handled safely
- **Recovery Options**: Steps to recover from common issues

## Conversation Files

### Planned Conversation Examples

#### Bot Management (`bot-management-conversation.md`)
- **Creating Your First DCA Bot**: Step-by-step bot creation with safety validation
- **Optimizing Bot Performance**: Analyzing and improving bot configurations
- **Managing Multiple Bots**: Portfolio-level bot coordination and management
- **Bot Troubleshooting**: Common issues and solutions for bot operations

#### Strategy Configuration (`strategy-conversation.md`)
- **Choosing the Right Strategy**: Strategy selection based on market conditions
- **RSI Strategy Setup**: Configuring RSI-based trading strategies
- **QFL Strategy Configuration**: Setting up Quick Fingers Luc strategies
- **Custom Signal Integration**: Connecting external signal sources

#### Deal Operations (`deal-management-conversation.md`)
- **Monitoring Active Deals**: Tracking deal progress and performance
- **Safety Order Management**: Adding and configuring safety orders
- **Deal Optimization**: Adjusting deals for better performance
- **Emergency Deal Management**: Handling volatile market conditions

#### Account Setup (`account-setup-conversation.md`)
- **Initial Account Configuration**: Setting up exchange connections
- **Permission Validation**: Verifying trading permissions and capabilities
- **Multi-Exchange Setup**: Managing multiple trading accounts
- **Security Best Practices**: Secure account configuration guidelines

#### Risk Management (`risk-management-conversation.md`)
- **Position Sizing**: Calculating appropriate position sizes
- **Portfolio Risk Assessment**: Evaluating overall portfolio risk
- **Stop Loss Configuration**: Setting up protective stop losses
- **Diversification Strategies**: Managing risk across multiple positions

## Conversation Patterns

### Common Interaction Flows

#### Bot Creation Flow
1. **Account Validation**: Verify exchange account permissions
2. **Strategy Selection**: Choose appropriate trading strategy
3. **Parameter Configuration**: Set bot parameters with validation
4. **Safety Checks**: Validate configuration for trading safety
5. **Bot Creation**: Create bot with confirmed parameters
6. **Monitoring Setup**: Set up performance monitoring

#### Deal Management Flow
1. **Deal Discovery**: List and filter active deals
2. **Performance Analysis**: Analyze deal profit/loss status
3. **Safety Assessment**: Evaluate deal risk and safety orders
4. **Optimization Actions**: Adjust parameters or add safety orders
5. **Monitoring**: Continue tracking deal performance

#### Strategy Optimization Flow
1. **Performance Review**: Analyze current strategy performance
2. **Parameter Analysis**: Evaluate current parameter effectiveness
3. **Market Condition Assessment**: Consider current market conditions
4. **Parameter Adjustment**: Modify strategy parameters
5. **Validation**: Test new parameters before implementation
6. **Implementation**: Apply optimized strategy configuration

### Error Handling Patterns

#### Validation Errors
- **Parameter Validation Failures**: Clear explanation of validation requirements
- **Account Permission Issues**: Steps to resolve permission problems
- **Market Condition Warnings**: Alerts about unfavorable market conditions
- **Safety Constraint Violations**: Explanation of safety requirements

#### Recovery Scenarios
- **Failed Bot Creation**: Steps to identify and fix configuration issues
- **Deal Management Errors**: Recovery options for deal operation failures
- **Strategy Configuration Issues**: Troubleshooting strategy setup problems
- **Account Connection Problems**: Resolving exchange connectivity issues

## Cross-References

### Integration with Other Documentation Layers
- **Tool Documentation**: Links to detailed tool reference documentation
- **Model Documentation**: References to model validation requirements
- **Code Examples**: Links to implementation details and patterns
- **API Reference**: References to 3Commas API documentation

### Realistic Context
- **Market Scenarios**: Examples based on real market conditions
- **Trading Strategies**: Proven trading approaches and configurations
- **Risk Management**: Real-world risk management scenarios
- **Performance Optimization**: Actual optimization techniques and results

## Development Guidelines

### Adding New Conversations
When adding new conversation examples:
1. **Realistic Scenarios**: Base examples on real trading situations
2. **Safety Focus**: Include trading safety considerations throughout
3. **Complete Flows**: Show complete interaction flows from start to finish
4. **Error Handling**: Include examples of error scenarios and recovery
5. **Cross-Reference**: Link to related tools, models, and documentation

### Maintenance
- **Market Relevance**: Update examples to reflect current market conditions
- **Tool Updates**: Update conversations when tool signatures change
- **Safety Review**: Regularly review safety considerations and warnings
- **Validation**: Ensure all examples still work with current implementation

## Trading Safety Focus

All conversation examples emphasize trading safety:
- **Risk Assessment**: Clear indication of trading risks for each scenario
- **Safety Validation**: Examples of proper parameter validation
- **Error Prevention**: Proactive error handling and prevention
- **Recovery Guidance**: Clear steps for recovering from issues
- **Best Practices**: Demonstration of safe trading practices

## Usage Guidelines

### For Developers
- **Implementation Patterns**: Learn common implementation patterns from examples
- **Error Handling**: Understand proper error handling in trading contexts
- **Safety Validation**: See examples of comprehensive safety validation
- **User Experience**: Understand how users interact with trading tools

### For Users
- **Getting Started**: Step-by-step guidance for new users
- **Advanced Usage**: Complex scenarios for experienced traders
- **Troubleshooting**: Solutions for common problems and issues
- **Best Practices**: Proven approaches for safe and effective trading

This conversation documentation ensures that both developers and users understand how to interact with the 3Commas MCP server safely and effectively in real trading scenarios.