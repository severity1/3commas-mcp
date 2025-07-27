# CLAUDE.md for utils/

## Context Activation
Activates when working in `utils/` directory implementing authentication, error handling, and validation utilities.

**Companions**: api/ (HTTP client), models/ (validation), tools/ (usage)

## Implemented Utilities

### Authentication (auth.py)
- `generate_signature()` - HMAC-SHA256 for 3Commas API
- `build_query_string()` - Parameter encoding for signatures
- `create_auth_headers()` - APIKEY and APISIGN headers
- `sign_request()` - Complete request signing utility

### Error Handling (decorators.py)
- `@handle_api_errors` - Consistent error formatting
- `@rate_limit_retry` - Exponential backoff for 3Commas limits
- `@validate_trading_context` - Pre-flight safety checks
- `RateLimiter` - Sliding window rate limiting (official 3Commas limits: 100 global, 120 deals, 40 smart_trades/10s)

### Environment (env.py)
- `get_3commas_credentials()` - Secure API key/secret access
- `should_enable_destructive_ops()` - Safety controls for dangerous operations
- `get_rate_limits()` - Configurable limits per endpoint type
- `validate_environment()` - Environment variable validation

### Response Filtering (response_filter.py)
- `filter_response()` - Main filtering with layered approach
- Security filter: Always removes `url_secret`, `account_id`
- Display filter: 85% token reduction vs full responses
- Filter types: `"full"` (editing) vs `"display"` (default)

## Implementation Requirements

### Essential Patterns
1. **Security first** - Never log credentials or sensitive data
2. **Error context** - Include trading context in error messages
3. **Validation comprehensive** - Validate all trading parameters
4. **Reusable design** - Utilities work across all components

### Authentication Standards
```python
def generate_signature(query_string: str, secret: str) -> str:
    """Generate HMAC-SHA256 signature for 3Commas API"""
    # Follow 3Commas authentication specification
```

### Error Handling Standards
```python
@handle_api_errors
async def trading_operation():
    """Trading operation with comprehensive error handling"""
    # Implementation with trading-specific error context
```

## Development Workflow

### Implementation Steps
1. Define utility purpose with clear trading context
2. Implement core logic following security standards
3. Add comprehensive error handling with trading context
4. Add parameter validation with trading safety checks
5. Test: valid/invalid scenarios, edge cases, security scenarios

### Quality Checklist
- [ ] Comprehensive type hints and documentation
- [ ] Security practices for credential/data handling
- [ ] Error handling with trading context
- [ ] Trading safety validation logic
- [ ] Tests cover security scenarios and edge cases