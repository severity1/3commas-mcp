# CLAUDE.md for utils/

This file provides guidance for utility functions that support 3Commas API integration and trading operations.

## Context Activation
This guidance activates when:
- Working in `3commas_mcp/utils/` directory
- Creating/editing utility function files (*.py)
- Implementing authentication, error handling, or validation utilities
- Adding trading-specific helper functions for 3Commas operations

**Companion directories**: api/ (for client), models/ (for validation), tools/ (for usage)

## Utility Architecture

### Directory Structure
- **__init__.py**: Utility imports and exports
- **auth.py**: HMAC-SHA256 authentication and signature generation
- **decorators.py**: Error handling decorators for trading operations
- **env.py**: Environment configuration and credential management
- **validation.py**: Trading parameter validation utilities
- **filters.py**: Response filtering for trading data optimization

### Implementation Standards
- **Security focused**: All utilities prioritize secure credential handling
- **Trading safety**: Validation utilities include trading safety checks
- **Error handling**: Comprehensive error handling with trading context
- **Reusability**: Utilities designed for use across all components

## Utility Categories

### Authentication Utilities (auth.py)
- **HMAC-SHA256 signature generation**: Core authentication for 3Commas API
- **Query string formatting**: Proper parameter formatting for signature generation
- **Request header creation**: APIKEY and APISIGN header generation
- **Credential validation**: API key and secret validation utilities

### Error Handling Utilities (decorators.py)
- **@handle_api_errors**: Comprehensive error handling decorator for API calls
- **@handle_trading_errors**: Trading-specific error handling with safety context
- **@validate_trading_params**: Parameter validation decorator for trading operations
- **@rate_limit_retry**: Exponential backoff decorator for rate limiting

### Environment Utilities (env.py)
- **Credential management**: Secure API key and secret handling
- **Feature flags**: Destructive operation controls (enable/disable)
- **Configuration validation**: Environment variable validation
- **Security settings**: Trading safety configuration options

### Validation Utilities (validation.py)
- **Trading parameter validation**: Bot, strategy, and deal parameter validation
- **Account permission validation**: Exchange account capability checks
- **Market data validation**: Trading pair and currency validation
- **Safety constraint validation**: Risk management and safety order validation

### Response Filtering (filters.py)
- **Trading data filtering**: Optimize response data while preserving critical trading information
- **Audit trail preservation**: Maintain essential data for trading audit requirements
- **Performance optimization**: Reduce token usage while maintaining trading safety
- **Configurable filtering**: Flexible filtering based on trading context

## Implementation Requirements

### Essential Patterns
1. **Security first**: All utilities prioritize secure credential and data handling
2. **Error context**: Include trading context in all error messages
3. **Validation comprehensive**: Validate all trading parameters thoroughly
4. **Logging safe**: Never log sensitive trading data or credentials
5. **Reusable design**: Utilities usable across all components

### Authentication Standards
HMAC-SHA256 signature generation following 3Commas requirements:
```python
def generate_signature(query_string: str, secret: str) -> str:
    """Generate HMAC-SHA256 signature for 3Commas API authentication"""
    # Implementation following 3Commas authentication spec
```

### Error Handling Standards
Comprehensive error handling with trading context:
```python
@handle_api_errors
async def trading_operation():
    """Trading operation with comprehensive error handling"""
    # Implementation with trading-specific error handling
```

### Validation Standards
Trading parameter validation with safety checks:
```python
def validate_bot_config(config: DCABotConfig) -> ValidationResult:
    """Validate bot configuration with trading safety checks"""
    # Implementation with comprehensive validation
```

## Development Standards

### Quality Checks
- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type Check**: `mypy .`
- **Test**: `pytest`

### Utility Requirements
- All utilities must include comprehensive type hints
- Apply secure coding practices for credential handling
- Include comprehensive error handling with trading context
- Test with valid/invalid scenarios and edge cases
- Document usage patterns and integration requirements

### Integration Standards

### API Integration
When utilities are used with API client:
- Provide authentication utilities for all API requests
- Include error handling for API-specific failures
- Apply rate limiting utilities for 3Commas compliance
- Ensure secure credential handling throughout request lifecycle

### Tool Integration
When utilities are used in tools:
- Provide validation utilities for all tool parameters
- Include error handling decorators for consistent error management
- Apply trading safety validation before operations
- Ensure utilities handle tool-specific requirements

### Model Integration
When utilities work with models:
- Provide validation utilities for model validation
- Include transformation utilities for API compatibility
- Apply consistent validation patterns across models
- Ensure utilities support model serialization/deserialization

## Implementation Workflow

### New Utility Development Process
1. **Define utility purpose**: Clear scope and trading context
2. **Implement core logic**: Following security and safety standards
3. **Add error handling**: Comprehensive error handling with trading context
4. **Add validation**: Parameter validation with trading safety checks
5. **Test thoroughly**: Valid/invalid scenarios, edge cases, security scenarios
6. **Document usage**: Integration patterns and usage examples
7. **Update documentation**: Implementation status tracking

### Quality Validation Checklist
For each utility implementation:
- [ ] Utility includes comprehensive type hints and documentation
- [ ] Security practices followed for credential and data handling
- [ ] Error handling includes trading context and appropriate error messages
- [ ] Validation logic includes trading safety checks
- [ ] Quality checks passed: format, lint, type check
- [ ] Tests cover all scenarios: valid inputs, invalid inputs, edge cases, security
- [ ] Documentation updated: implementation status tracking

### 3Commas-Specific Utility Patterns
- **Signature generation**: HMAC-SHA256 with proper query string formatting
- **Rate limiting**: Exponential backoff with 3Commas-specific limits (300/60/120 req/min)
- **Error handling**: 3Commas error format handling and translation
- **Trading validation**: Bot/strategy/deal parameter validation with 3Commas requirements
- **Security**: API key/secret handling with proper environment variable management

### Security Requirements
- **Credential handling**: Never log or expose API keys/secrets
- **Environment variables**: Secure loading and validation of credentials
- **Error messages**: Redact sensitive information from error messages
- **Validation**: Validate all inputs before processing
- **Logging**: Safe logging practices for trading operations without exposing sensitive data