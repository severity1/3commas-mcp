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
uv run -m ruff format .

# Lint code
uv run -m ruff check .

# Type check
uv run -m mypy .

# Run all quality checks
uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .
```

## Project Structure

Core architecture: `3commas_mcp/` with `api/`, `models/`, `tools/`, `utils/` components.

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

## Implementation Patterns

### Pattern Reference
All API implementations must follow established patterns documented in:
- **`docs/PATTERNS.md`** - Complete implementation reference and templates
- **Component CLAUDE.md files** - Component-specific guidance and standards

### Component Guidelines

### Tool Implementation
- **Function Signatures**: Follow (routing_params, trading_params, optional_params) pattern
- **Validation**: Use Pydantic models for all input validation
- **Response Filter**: Include `response_filter: str = "display"` parameter (pass string directly)
- **Safety Checks**: Include trading safety validation before operations
- **Registration**: Register tools in server.py with appropriate destructiveness classification

### Model Implementation
- **Base Classes**: Inherit from `APIRequest` (not BaseModel) for automatic `response_filter` field
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

## Documentation Standards

### Required Documentation
- Include docstrings with trading context and complete type hints
- Follow 4-layer pattern: conversations/, models/, tools/, code docstrings
- Maintain cross-references between documentation layers
- Include trading safety warnings where applicable
- **Use dummy data ONLY when documenting** (bot ID 12345678, $245.67 profit)

## Quality Assurance

### Required Checks
- [ ] `black .` - code formatting
- [ ] `ruff format .` - additional formatting
- [ ] `ruff check .` - linting
- [ ] `mypy .` - type checking  
- [ ] `pytest` - tests
- [ ] Documentation updated
- [ ] Pattern compliance verified (see `docs/PATTERNS.md`)