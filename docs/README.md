# Documentation

This directory contains comprehensive documentation for the 3Commas MCP server project, organized in a multi-layer structure to support development, usage, and maintenance.

## Documentation Structure

### Core Documentation
- **[PATTERNS.md](PATTERNS.md)**: Implementation patterns reference and compliance checklist
- **[DEVELOPMENT.md](DEVELOPMENT.md)**: Development standards, workflow, and quality requirements
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contributing guidelines with trading safety focus
- **[API_REFERENCES.md](API_REFERENCES.md)**: 3Commas API reference links and implementation status
- **[MVP_GET_APIS.md](MVP_GET_APIS.md)**: MVP implementation plan and progress tracking

### Multi-Layer Documentation System

This project uses a 4-layer documentation pattern to provide comprehensive coverage:

#### Layer 1: Conversations (`conversations/`)
Real-world usage examples and interaction patterns for trading scenarios:
- **Bot Management**: Creating, updating, and managing DCA bots
- **Strategy Configuration**: Setting up and optimizing trading strategies  
- **Deal Operations**: Managing deals and safety orders
- **Account Management**: Exchange account setup and validation
- **Risk Management**: Trading safety and risk assessment scenarios

#### Layer 2: Models (`models/`)
Pydantic model documentation with validation rules and API mappings:
- **Bot Models**: DCA bot configuration, grid bot settings, bot status
- **Strategy Models**: QFL, RSI, Bollinger Bands, MACD, Moving Average configurations
- **Deal Models**: Deal creation, safety orders, deal status tracking
- **Account Models**: Exchange account configuration and permissions
- **Market Models**: Trading pairs, currency rates, blacklist management

#### Layer 3: Tools (`tools/`)
API tool reference with signatures, parameters, and trading safety scenarios:
- **Bot Tools**: Bot creation, management, and performance tracking
- **Strategy Tools**: Strategy configuration and optimization
- **Deal Tools**: Deal analysis, safety orders, and risk management
- **Account Tools**: Account validation and exchange integration
- **Market Tools**: Market data and trading pair management

#### Layer 4: Code Docstrings
Implementation-level documentation with cross-references embedded in the codebase.

## Cross-Reference System

All documentation layers are bidirectionally linked:
- **Code** → **Tools**: Docstrings reference tool documentation
- **Tools** ↔ **Models**: Tool docs link to model validation, models link to usage
- **Tools** → **Conversations**: Tool docs reference usage scenarios
- **Conversations** → **Tools/Models**: Examples reference specific implementations

## Trading Context Documentation

### Safety-Focused Documentation
All documentation includes trading safety considerations:
- **Risk Assessment**: Low/Medium/High risk classification for operations
- **Safety Warnings**: Explicit warnings for destructive operations
- **Parameter Validation**: Documentation of trading parameter constraints
- **Account Requirements**: Exchange account permission requirements

### Trading Scenario Coverage
Documentation covers realistic trading scenarios:
- **Beginner Bot Setup**: Basic DCA bot creation and management
- **Advanced Strategies**: Complex strategy configurations and optimizations
- **Risk Management**: Safety order configuration and deal management
- **Portfolio Management**: Multi-bot coordination and performance tracking

## Documentation Templates

### Usage Templates
Standardized templates ensure consistency across all documentation:
- **Tool Documentation**: Function signatures, parameters, safety considerations
- **Model Documentation**: Field descriptions, validation rules, API mappings
- **Conversation Examples**: Realistic scenarios with safety context
- **Code Docstrings**: Implementation details with cross-references

### Trading-Specific Templates
Specialized templates for trading contexts:
- **Bot Operation Templates**: Including safety checks and validation
- **Strategy Configuration Templates**: With parameter constraints and requirements
- **Deal Management Templates**: Including risk assessment and safety orders
- **Account Management Templates**: With permission and capability validation

## Getting Started

### For Developers
1. **Start with [DEVELOPMENT.md](DEVELOPMENT.md)** for development setup and standards
2. **Review [CONTRIBUTING.md](CONTRIBUTING.md)** for contribution guidelines
3. **Use component CLAUDE.md files** in each directory for specific guidance
4. **Follow the 4-layer documentation pattern** when adding new features

### For Users
1. **Check conversations/** for usage examples in your trading context
2. **Review tools/** for API reference and function signatures  
3. **Consult models/** for parameter validation and requirements
4. **Refer to API_REFERENCES.md** for 3Commas API implementation status

### For AI Development
1. **CLAUDE.md files** provide context-aware guidance for each component
2. **Subtree discovery system** automatically loads relevant documentation
3. **Cross-reference system** maintains consistency across all layers
4. **Trading safety focus** ensures responsible development practices

## Documentation Maintenance

### Regular Updates
- **Implementation Status**: Update API_REFERENCES.md as features are implemented
- **Usage Examples**: Add new conversation examples for new features
- **Cross-References**: Maintain bidirectional links between documentation layers
- **Safety Documentation**: Update safety warnings and risk assessments

### Quality Assurance
- **Link Validation**: Ensure all cross-references are valid and accessible
- **Template Consistency**: Follow established templates for all documentation
- **Trading Context**: Maintain focus on trading safety and risk management
- **Comprehensive Coverage**: Ensure all 4 layers are updated for new features

## Future Documentation Plans

### Planned Additions
- **Advanced Trading Strategies**: Documentation for complex multi-bot strategies
- **Integration Guides**: Documentation for TradingView and webhook integrations
- **Troubleshooting Guides**: Common issues and solutions for trading scenarios
- **Performance Optimization**: Guidelines for optimizing bot performance

### Community Contributions
- **Usage Examples**: Community-contributed trading scenarios and strategies
- **Best Practices**: Proven trading patterns and risk management approaches
- **Integration Examples**: Real-world integration patterns and use cases
- **Safety Guidelines**: Community-driven safety recommendations and warnings

This documentation structure ensures that whether you're developing, using, or maintaining the 3Commas MCP server, you have access to comprehensive, safety-focused guidance at the appropriate level of detail.