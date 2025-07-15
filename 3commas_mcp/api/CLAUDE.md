# CLAUDE.md for api/

This file provides guidance about the 3Commas API client implementation.

## Context Activation
This guidance activates when:
- Working in `3commas_mcp/api/` directory
- Creating/editing API client files (*.py)
- Implementing HTTP request handling or 3Commas authentication
- Adding signature generation or response processing for trading APIs

**Companion directories**: tools/ (for usage), models/ (for requests), utils/ (for helpers)

## API Client Architecture

The API client provides core functionality for 3Commas API integration:
- **Authentication**: 3Commas API key + HMAC-SHA256 signature management
- **Request handling**: Formatting, submission, and response processing
- **Error management**: Consistent error handling across all trading API calls
- **Rate limiting**: Compliance with 3Commas rate limits (300/60/120 req/min)

### Core Components
- **client.py**: `api_request()` main function and signature authentication
- **Authentication**: HMAC-SHA256 signature generation for all requests

## Implementation Standards

### Request Function Pattern
The `api_request()` function handles all API interactions with:
- **Path/Method**: API endpoint path and HTTP method (GET, POST, PATCH, DELETE)
- **Authentication**: Automatic signature generation via utils/auth.py
- **Parameters**: Query parameters and request body handling for trading operations
- **Rate limiting**: Built-in rate limit compliance and exponential backoff

### 3Commas Authentication Requirements
3Commas authentication requires specific header format:
- **APIKEY**: API key header for request identification
- **APISIGN**: HMAC-SHA256 signature of query string using secret key
- **Query string**: Properly formatted parameters for signature generation
- **Content-Type**: application/json for POST/PATCH requests

### Response Handling Standards
- **Success responses**: 200/201 return raw API data; 204 returns success status
- **Trading responses**: Bot/deal/strategy data with 3Commas-specific structure
- **Error handling**: HTTP status errors, authentication failures, rate limiting
- **Security**: Never logs API keys/secrets, validates inputs, proper error redaction

### Rate Limiting Compliance
3Commas enforces different rate limits by endpoint type:
- **Standard endpoints** (accounts, bots list): 300 requests/minute
- **Trading endpoints** (create/update/delete bots): 60 requests/minute
- **Statistics endpoints** (bot stats, deals): 120 requests/minute
- **Exponential backoff**: Required for 429 rate limit responses

## Usage Standards

### Integration Requirements
- **Error handling**: Always use with `@handle_api_errors` decorator from utils/decorators.py
- **Environment management**: API key/secret handling via `get_3commas_credentials()` from utils/env.py
- **Payload creation**: Convert Pydantic models using utils/payload.py utilities
- **Signature generation**: Use utils/auth.py for HMAC-SHA256 authentication

### Trading Safety Requirements
- **Bot operations**: Validate bot configuration before creation/modification
- **Deal operations**: Include safety checks for deal cancellation and modifications
- **Destructive operations**: Require explicit confirmation for delete/disable operations
- **Account validation**: Verify exchange account permissions before bot operations

## Development Standards

### Quality Checks
- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type Check**: `mypy .`
- **Test**: `pytest`

### API Client Requirements
- All functions must include proper HMAC-SHA256 authentication
- Apply rate limiting compliance with exponential backoff
- Follow established patterns for request formatting and response processing
- Test with comprehensive coverage of success, error, rate limiting, and authentication scenarios

### Integration Guidelines

### Tool Integration
When API client is used in tools:
- Always use with `@handle_api_errors` decorator
- Apply proper payload creation using utility functions
- Handle rate limiting appropriately for trading operations
- Use centralized credential management with signature generation

### Model Integration
When API client works with models:
- Convert Pydantic models using payload utilities
- Apply proper request validation before API calls
- Handle model validation errors appropriately for trading contexts
- Ensure proper type safety throughout request pipeline

### Utility Integration
When API client works with utilities:
- Use environment management for secure credential handling
- Apply payload creation utilities for 3Commas API compliance
- Use error handling decorators consistently
- Apply security practices for trading API credentials

## Implementation Workflow

### API Client Enhancement Process
1. **Define request patterns**: Follow 3Commas authentication requirements
2. **Implement authentication**: Use HMAC-SHA256 signature generation
3. **Add error handling**: Apply consistent response formats with trading context
4. **Handle rate limiting**: Implement exponential backoff for 3Commas limits
5. **Test thoroughly**: Cover success, error, rate limiting, and authentication scenarios
6. **Update documentation**: Implementation status tracking

### Quality Validation Checklist
For each API client enhancement:
- [ ] Function includes proper HMAC-SHA256 authentication and signature generation
- [ ] Rate limiting compliance applied with exponential backoff for 3Commas limits
- [ ] Security guidelines followed for API key and secret management
- [ ] Quality checks passed: format, lint, type check
- [ ] Tests cover all scenarios: success, error, rate limiting, authentication failures
- [ ] Documentation updated: implementation status tracking

### 3Commas-Specific Patterns
- **Base URL**: Always use https://api.3commas.io
- **API Versioning**: Use /ver1/ prefix for all endpoints
- **Error Format**: Handle 3Commas error response structure consistently
- **Success Indicators**: Recognize 3Commas success response patterns
- **Trading Context**: Include bot/deal/strategy identifiers in request logging (without sensitive data)