# Development Guide

This document provides comprehensive development standards and workflows for the 3Commas MCP server project.

## Quick Start

### Environment Setup
```bash
# Install dependencies
uv pip install -e .

# Install development dependencies
uv pip install -e .[dev]

# Set up environment variables
cp env.example .env
# Edit .env with your 3Commas API credentials
```

### Development Workflow
```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type check
mypy .

# Run tests
pytest

# Run all quality checks
ruff format . && ruff check . && mypy . && pytest
```

## Project Structure

### Core Architecture
```
3commas_mcp/
├── __init__.py
├── server.py                 # Main MCP server entry point
├── api/
│   ├── __init__.py
│   ├── CLAUDE.md            # API client guidance
│   └── client.py            # 3Commas API client with HMAC-SHA256 auth
├── models/
│   ├── __init__.py
│   ├── CLAUDE.md            # Model validation guidance
│   ├── base.py              # Base models and config
│   ├── bots.py              # DCA/Grid bot models
│   ├── strategies.py        # Trading strategy models
│   ├── deals.py             # Deal and safety order models
│   ├── accounts.py          # Account and exchange models
│   └── pairs.py             # Market pairs and blacklist models
├── tools/
│   ├── __init__.py
│   ├── CLAUDE.md            # Tool implementation guidance
│   ├── bots.py              # Bot creation/management tools
│   ├── strategies.py        # Strategy configuration tools
│   ├── deals.py             # Deal analysis and safety orders
│   ├── accounts.py          # Account and exchange tools
│   └── pairs.py             # Market data and pair management tools
└── utils/
    ├── __init__.py
    ├── CLAUDE.md            # Utility function guidance
    ├── auth.py              # 3Commas HMAC-SHA256 authentication
    ├── decorators.py        # Error handling decorators
    ├── env.py               # Environment configuration
    └── validation.py        # Trading parameter validation
```

## Development Standards

### Code Quality
- **Formatting**: Use `ruff format .` for consistent code formatting
- **Linting**: Use `ruff check .` for code quality and style checks
- **Type Checking**: Use `mypy .` for static type analysis
- **Testing**: Use `pytest` for comprehensive test coverage

### Trading Safety Standards
- **Parameter Validation**: All trading parameters must be validated before API calls
- **Account Verification**: Verify exchange account permissions before bot operations
- **Destructive Operations**: Require explicit confirmation for delete/disable operations
- **Error Handling**: Include trading context in all error messages
- **Logging Safety**: Never log API keys, secrets, or sensitive trading data

### Code Style Requirements
- **Type Hints**: All functions must include comprehensive type hints
- **Docstrings**: All public functions must include docstrings with trading context
- **Error Handling**: Use `@handle_api_errors` decorator for all API operations
- **Async Patterns**: All API calls must be async using httpx
- **Security**: Follow secure coding practices for credential handling

## 3Commas Integration Standards

### Authentication
- **HMAC-SHA256**: All API requests require signature authentication
- **Environment Variables**: Store API credentials securely in environment variables
- **Header Format**: Include APIKEY and APISIGN headers for all authenticated requests
- **Query String**: Properly format query strings for signature generation

### Rate Limiting
3Commas enforces different rate limits by endpoint type:
- **Standard endpoints**: 300 requests/minute (accounts, bots list)
- **Trading endpoints**: 60 requests/minute (create/update/delete bots)
- **Statistics endpoints**: 120 requests/minute (bot stats, deals)
- **Retry Logic**: Implement exponential backoff for 429 rate limit responses

### API Error Handling
- **Authentication Errors**: Handle 401 responses with credential validation
- **Rate Limiting**: Handle 429 responses with exponential backoff
- **Trading Errors**: Handle bot/deal specific errors with trading context
- **Network Errors**: Handle timeouts and connection failures gracefully

## Testing Standards

### Test Categories
- **Authentication Tests**: Test HMAC-SHA256 signature generation and validation
- **API Tests**: Test API connectivity and request/response handling
- **Trading Safety Tests**: Test validation logic for trading parameters
- **Performance Tests**: Test rate limiting compliance and response times

### Test Structure
```python
def test_function_name():
    """Test description with trading context."""
    # Arrange: Set up test data and scenarios
    # Act: Execute the function under test
    # Assert: Verify expected results and trading safety
```

### Testing Approach
- **API Responses**: Validate 3Commas API response handling
- **Rate Limiting**: Test rate limiting compliance and backoff behavior
- **Authentication**: Test authentication scenarios and error conditions
- **Trading Safety**: Validate trading parameter safety checks

## Component Guidelines

### Tool Implementation
- **Function Signatures**: Follow (routing_params, trading_params, optional_params) pattern
- **Validation**: Use Pydantic models for all input validation
- **Safety Checks**: Include trading safety validation before operations
- **Registration**: Register tools in server.py with appropriate destructiveness classification

### Model Implementation
- **Base Classes**: Extend Pydantic BaseModel for all data models
- **Field Validation**: Use validators for trading parameter validation
- **API Mapping**: Document field mappings to 3Commas API structure
- **Type Safety**: Use comprehensive type hints for all fields

### Utility Implementation
- **Reusability**: Design utilities for use across all components
- **Security**: Prioritize secure credential and data handling
- **Error Context**: Include trading context in all error handling
- **Documentation**: Provide comprehensive usage documentation

## Environment Configuration

### Required Environment Variables
```bash
# 3Commas API Credentials
3COMMAS_API_KEY=your_api_key_here
3COMMAS_SECRET_KEY=your_secret_key_here

# Feature Flags
3COMMAS_ENABLE_DESTRUCTIVE=false  # Enable bot disable/delete operations

# Development Settings
DEBUG=false
LOG_LEVEL=INFO
```

### Security Considerations
- **Credential Storage**: Store credentials in environment variables only
- **Feature Flags**: Use feature flags to control destructive operations
- **Logging**: Configure safe logging that excludes sensitive data
- **Validation**: Validate all environment variables on startup

## Documentation Standards

### Code Documentation
- **Docstrings**: Include comprehensive docstrings with trading context
- **Type Hints**: Use complete type hints for all parameters and returns
- **Examples**: Include usage examples in docstrings where appropriate
- **Safety Warnings**: Include trading safety warnings where applicable

### Documentation Structure
- **4-Layer Pattern**: conversations/, models/, tools/, code docstrings
- **Cross-References**: Maintain bidirectional links between all layers
- **Trading Context**: Include trading scenarios and safety considerations
- **API References**: Link to 3Commas API documentation

## Troubleshooting

### Common Issues
- **Authentication Failures**: Verify API key and secret configuration
- **Rate Limiting**: Check rate limit compliance and backoff implementation
- **Bot Creation Errors**: Validate trading parameters and account permissions
- **Deal Management Issues**: Verify deal state and safety order configuration

### Debugging Tools
- **Logging**: Use structured logging with trading context
- **Error Messages**: Include detailed error information with trading context
- **Validation**: Use comprehensive validation with clear error messages
- **Testing**: Use comprehensive test coverage for debugging support

## Quality Assurance

### Pre-commit Checklist
- [ ] Code formatted with `ruff format .`
- [ ] Linting passed with `ruff check .`
- [ ] Type checking passed with `mypy .`
- [ ] Tests passed with `pytest`
- [ ] Trading safety validation included
- [ ] Documentation updated for new features
- [ ] Environment variables configured correctly

### Continuous Integration
- **Automated Testing**: All tests must pass in CI/CD pipeline
- **Quality Checks**: All quality checks must pass before merge
- **Security Scanning**: Scan for security vulnerabilities and credential exposure
- **Documentation**: Ensure documentation is updated with code changes