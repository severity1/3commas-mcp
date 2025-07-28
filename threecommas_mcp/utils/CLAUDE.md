# CLAUDE.md for utils/

## Context Activation
Activates when implementing authentication, error handling, and validation utilities.

## Current Implementation Status
**557 lines across 4 utility modules:**
- `auth.py` (68 lines) - HMAC-SHA256 authentication 
- `decorators.py` (203 lines) - Error handling and rate limiting
- `env.py` (61 lines) - Environment and configuration
- `response_filter.py` (178 lines) - Response filtering and token optimization

**Exports**: 15 functions in clean __init__.py interface

## Implemented Functions (from __init__.py exports)

### Environment utilities (env.py)
- `get_3commas_credentials` - Secure API key/secret access
- `should_enable_destructive_ops` - Safety controls for dangerous operations
- `get_rate_limits` - Configurable limits per endpoint type
- `validate_environment` - Environment variable validation
- `get_api_base_url` - API base URL configuration

### Authentication utilities (auth.py)  
- `generate_signature` - HMAC-SHA256 signature generation
- `build_query_string` - Parameter encoding for signatures
- `create_auth_headers` - APIKEY and APISIGN headers
- `sign_request` - Complete request signing utility
- `validate_credentials` - Credential validation

### Decorators and rate limiting (decorators.py)
- `handle_api_errors` - Consistent error formatting (used by all tools)
- `rate_limit_retry` - Exponential backoff for 3Commas limits
- `validate_trading_context` - Pre-flight safety checks
- `RateLimiter` - Rate limiting class

### Response filtering (response_filter.py)
- `filter_response()` - Main filtering function (used by all tools)
- Accepts string "display"/"full" (simplified validation)
- Security filter: Always removes `url_secret`, `account_id`
- Display filter: 85% token reduction

## Quality Standards (verified in implementation)
- [ ] Security practices implemented (no credential logging)
- [ ] Error handling with trading context
- [ ] Comprehensive type hints and documentation  
- [ ] All functions actively used by tools/ module