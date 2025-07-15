# Contributing Guide

Thank you for your interest in contributing to the 3Commas MCP server project! This guide will help you understand our development process and standards.

## Getting Started

### Prerequisites
- Python 3.12 or higher
- 3Commas account with API access
- Basic understanding of cryptocurrency trading concepts
- Familiarity with MCP (Model Context Protocol) concepts

### Development Setup
1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/3commas-mcp.git
   cd 3commas-mcp
   ```

2. **Set up development environment**
   ```bash
   # Install dependencies
   uv pip install -e .[dev]
   
   # Set up environment variables
   cp env.example .env
   # Edit .env with your 3Commas API credentials (for testing)
   ```

3. **Verify setup**
   ```bash
   # Run quality checks
   ruff format . && ruff check . && mypy . && pytest
   ```

## Development Standards

### Code Quality Requirements
All contributions must meet these quality standards:
- **Formatting**: Code must be formatted with `ruff format .`
- **Linting**: Code must pass `ruff check .` without errors
- **Type Checking**: Code must pass `mypy .` without errors
- **Testing**: All new code must include comprehensive tests
- **Documentation**: All public APIs must be documented

### Trading Safety Standards
Given the nature of cryptocurrency trading, all contributions must prioritize safety:
- **Parameter Validation**: All trading parameters must be validated thoroughly
- **Account Safety**: Verify account permissions and trading capabilities
- **Destructive Operations**: Require explicit confirmation for risky operations
- **Error Handling**: Provide clear, actionable error messages with trading context
- **Security**: Never log or expose API credentials or sensitive trading data

## Contribution Process

### 1. Issue Discussion
Before starting work on a significant feature:
1. Check existing issues to avoid duplication
2. Create a new issue describing your proposed changes
3. Discuss the approach with maintainers
4. Wait for approval before beginning implementation

### 2. Development Workflow
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Follow component guidance**
   - Use CLAUDE.md files in each directory for component-specific guidance
   - Follow established patterns for tools, models, and utilities
   - Maintain consistency with existing code style

3. **Implement with safety first**
   - Include comprehensive input validation
   - Add appropriate error handling
   - Follow 3Commas API authentication requirements
   - Test with both valid and invalid inputs

4. **Update documentation**
   - Update relevant CLAUDE.md files if adding new patterns
   - Add or update docs/ files following the 4-layer structure
   - Update TASKS.md and API_REFERENCES.md implementation status
   - Include code docstrings with trading context

### 3. Testing Requirements
All contributions must include comprehensive testing:

#### Required Test Coverage
- **Authentication Tests**: Test HMAC-SHA256 signature generation and validation
- **API Tests**: Test API connectivity and request/response handling
- **Trading Safety Tests**: Test validation logic for trading parameters
- **Error Handling Tests**: Test error scenarios and edge cases

#### Test Structure
```python
def test_create_dca_bot_success():
    """Test successful DCA bot creation with valid parameters."""
    # Arrange: Set up valid bot configuration
    # Act: Create bot using the tool
    # Assert: Verify bot created with correct parameters

def test_create_dca_bot_invalid_params():
    """Test DCA bot creation with invalid parameters."""
    # Arrange: Set up invalid bot configuration
    # Act: Attempt to create bot
    # Assert: Verify appropriate error handling
```

### 4. Pull Request Process
1. **Pre-submission checklist**
   - [ ] Code formatted with `ruff format .`
   - [ ] Linting passed with `ruff check .`
   - [ ] Type checking passed with `mypy .`
   - [ ] All tests pass with `pytest`
   - [ ] Documentation updated
   - [ ] Trading safety validated

2. **Submit pull request**
   - Use descriptive title summarizing the change
   - Include detailed description of changes
   - Reference related issues
   - Include screenshots for UI changes (if applicable)

3. **Review process**
   - Maintainers will review code quality and trading safety
   - Address feedback promptly and thoroughly
   - Update tests and documentation as requested
   - Maintain focus on trading safety throughout review

## Component-Specific Guidelines

### API Client (`3commas_mcp/api/`)
- **Authentication**: Implement proper HMAC-SHA256 signature generation
- **Rate Limiting**: Include exponential backoff for rate limit compliance
- **Error Handling**: Handle 3Commas-specific error formats
- **Security**: Never log API credentials or sensitive data

### Tools (`3commas_mcp/tools/`)
- **Function Signatures**: Follow (routing_params, trading_params, optional_params) pattern
- **Validation**: Use Pydantic models for comprehensive input validation
- **Safety Checks**: Include trading safety validation before operations
- **Registration**: Register tools with appropriate destructiveness classification

### Models (`3commas_mcp/models/`)
- **Validation**: Include comprehensive trading parameter validation
- **API Mapping**: Document field mappings to 3Commas API structure
- **Type Safety**: Use complete type hints for all fields
- **Documentation**: Include trading context in model documentation

### Utilities (`3commas_mcp/utils/`)
- **Security**: Prioritize secure credential and data handling
- **Reusability**: Design for use across all components
- **Error Context**: Include trading context in error handling
- **Testing**: Comprehensive test coverage for utility functions

## Documentation Standards

### Code Documentation
- **Docstrings**: Include comprehensive docstrings with trading context
- **Type Hints**: Use complete type hints for all parameters and returns
- **Examples**: Include usage examples where appropriate
- **Safety Warnings**: Include trading safety warnings where applicable

### Project Documentation
When adding new features, update relevant documentation:
- **TASKS.md**: Mark features as completed
- **docs/API_REFERENCES.md**: Update implementation status
- **docs/models/**: Add model documentation following templates
- **docs/tools/**: Add tool documentation with trading examples
- **docs/conversations/**: Add usage examples with trading scenarios

## Trading Safety Guidelines

### Critical Safety Considerations
- **Bot Operations**: Always validate bot configuration and account permissions
- **Deal Management**: Include safety checks for deal cancellation and modifications
- **Strategy Configuration**: Validate strategy parameters against 3Commas requirements
- **Account Validation**: Verify exchange account capabilities before operations

### Risk Assessment
All contributions involving trading operations must include risk assessment:
- **Low Risk**: Read-only operations (get bot details, list accounts)
- **Medium Risk**: Bot creation and configuration changes
- **High Risk**: Bot deletion, deal cancellation, panic sell operations

### Error Handling for Trading
- **Clear Messages**: Provide actionable error messages with trading context
- **Safety Context**: Include information about potential trading impact
- **Recovery Options**: Suggest recovery steps for common error scenarios
- **Logging**: Log errors safely without exposing sensitive trading data

## Communication

### Getting Help
- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check CLAUDE.md files for component-specific guidance

### Reporting Issues
When reporting issues:
1. **Use issue templates** if available
2. **Include trading context** for trading-related issues
3. **Provide reproduction steps** with sample parameters (anonymized)
4. **Include environment information** (Python version, OS, etc.)
5. **Never include** API credentials or sensitive trading data

## Code of Conduct

### Our Standards
- **Professional Communication**: Maintain respectful and constructive communication
- **Trading Safety Focus**: Prioritize user safety and responsible trading practices
- **Collaborative Spirit**: Help others learn and contribute effectively
- **Security Awareness**: Be mindful of security implications in all contributions

### Enforcement
- Issues will be addressed by project maintainers
- Serious violations may result in contribution restrictions
- Focus remains on building a safe and reliable trading tool

## Release Process

### Version Management
- **Semantic Versioning**: Follow semver for version numbering
- **Change Documentation**: Update CHANGELOG.md for all releases
- **Breaking Changes**: Clearly document any breaking changes
- **Migration Guides**: Provide migration instructions for major version changes

### Quality Gates
All releases must pass:
- [ ] All automated tests
- [ ] Manual testing with live 3Commas API (testnet)
- [ ] Documentation review and updates
- [ ] Security review for credential handling
- [ ] Trading safety validation

Thank you for contributing to the 3Commas MCP server project! Your contributions help make cryptocurrency trading more accessible and safer for everyone.