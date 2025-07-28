# Implementation Patterns Reference

This document provides the definitive reference for all established implementation patterns in the 3Commas MCP server. Use this as your single source of truth when implementing new APIs.

## Overview

Our patterns prioritize **scalability**, **maintainability**, and **trading safety** while following **DRY** and **KISS** principles. Every API follows identical patterns, making the codebase predictable and easy to extend.

## Established Patterns

### 1. Model Definition Pattern

**Reference Implementation**: `threecommas_mcp/models/market_data.py:14-36`  
**Example**: `GetAllMarketPairsRequest` class

**Key Pattern Elements:**
- ✅ **Inherit from `APIRequest`** - Automatic `response_filter` field
- ✅ **Comprehensive docstring** - Include API mapping and endpoint reference  
- ✅ **Field validation** - Use Pydantic `Field()` with constraints
- ✅ **Trading context** - Include trading-specific validation where applicable

### 2. Tool Function Pattern

**Reference Implementation**: `threecommas_mcp/tools/market_data.py:21-69`  
**Example**: `get_all_market_pairs()` function

**Key Pattern Elements:**
- ✅ **`@handle_api_errors` decorator** - Line 20, consistent error handling
- ✅ **`response_filter: str = "display"`** - Line 22, always include with default
- ✅ **String validation** - Line 53, pass response_filter directly to model (no enum conversion)
- ✅ **Pydantic validation** - Line 53, use request model for input validation
- ✅ **Response filtering** - Line 67, always apply `filter_response()` before return
- ✅ **Comprehensive docstring** - Lines 24-50, include API details and trading context

### 3. File Structure Pattern

**Model File**: `threecommas_mcp/models/market_data.py:1-11` (header pattern)  
**Tool File**: `threecommas_mcp/tools/market_data.py:1-17` (imports pattern)

**Standard imports and structure established in existing files**

## Implementation Templates

### Reference Existing Code

**For new API implementation, copy patterns from:**

1. **Model**: Copy `threecommas_mcp/models/market_data.py:14-36` and modify for your parameters
2. **Tool Function**: Copy `threecommas_mcp/tools/market_data.py:21-69` and modify endpoint/parameters  
3. **File Structure**: Follow `threecommas_mcp/models/market_data.py:1-11` for file headers
4. **Imports**: Follow `threecommas_mcp/tools/market_data.py:7-17` for import patterns

### Quick Implementation Steps

1. **Create model** - Copy existing request model and modify fields
2. **Create tool function** - Copy existing tool function and modify endpoint/params
3. **Register in server** - Add to tool list following existing registration pattern

## Pattern Compliance Checklist

When implementing a new API, verify:

### Model Compliance
- [ ] Model inherits from `APIRequest`
- [ ] Comprehensive docstring with API mapping
- [ ] Field validation using `Field()` with constraints
- [ ] Trading safety validation where applicable

### Tool Compliance
- [ ] Uses `@handle_api_errors` decorator
- [ ] Includes `response_filter: str = "display"` parameter
- [ ] Passes string directly to model (no enum conversion)
- [ ] Uses Pydantic model for input validation
- [ ] Calls `filter_response(response, request.response_filter)`
- [ ] Comprehensive docstring with trading context

### Documentation Compliance
- [ ] Model documented in `docs/models/{domain}.md`
- [ ] Tool documented in `docs/tools/{domain}.md`
- [ ] Usage examples in `docs/conversations/{domain}-conversation.md`
- [ ] Cross-references between documentation layers

### Quality Compliance
- [ ] Type hints for all parameters and returns
- [ ] Trading safety considerations included
- [ ] Error handling covers all scenarios
- [ ] Tests cover success, error, and validation cases

## Benefits of This Pattern

### Scalability
- **Linear growth**: Each new API requires ~70 lines of code
- **Zero setup**: All infrastructure (auth, errors, filtering) automatic
- **Consistent interface**: Predictable function signatures across all APIs

### Maintainability
- **Single change points**: Common changes affect one location
- **Pattern consistency**: Easy to understand and modify any API
- **Documentation alignment**: All docs follow same structure

### Quality Assurance
- **Type safety**: Pydantic models catch errors early
- **Error handling**: Consistent error responses via decorators
- **Token optimization**: Universal response filtering
- **Trading safety**: Validation patterns prevent unsafe operations

## Cross-References

### Component Documentation
- **Models**: See `threecommas_mcp/models/CLAUDE.md` for model-specific patterns
- **Tools**: See `threecommas_mcp/tools/CLAUDE.md` for tool-specific patterns
- **Utils**: See `threecommas_mcp/utils/CLAUDE.md` for utility patterns
- **API**: See `threecommas_mcp/api/CLAUDE.md` for client patterns

### Development Documentation
- **Development Guide**: `docs/DEVELOPMENT.md` - Development workflow and standards
- **Contributing Guide**: `docs/CONTRIBUTING.md` - Contribution process and requirements
- **Implementation Plan**: `docs/MVP_GET_APIS.md` - API implementation roadmap

### Implementation Status
- **Task Tracking**: `TASKS.md` - Current implementation progress
- **API Reference**: `docs/API_REFERENCES.md` - Complete API status and reference

This pattern reference ensures consistent, maintainable, and scalable implementation across all 35 planned GET APIs and future API additions.