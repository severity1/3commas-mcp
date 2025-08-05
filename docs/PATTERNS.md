# Implementation Patterns Reference

This document provides the definitive reference for all established implementation patterns in the 3Commas MCP server. Use this as your single source of truth when implementing new APIs.

## Overview

Our patterns prioritize **scalability**, **maintainability**, and **trading safety** while following **DRY** and **KISS** principles. Every API follows identical patterns, making the codebase predictable and easy to extend.

## Established Patterns

### 1. Model Definition Pattern

**Reference Implementation**: `threecommas_mcp/models/dca_bots.py:42-116`  
**Example**: `GetDCABotListRequest` class

**Key Pattern Elements:**
- ✅ **Inherit from `APIRequest`** - Automatic `response_filter` field
- ✅ **Comprehensive docstring** - Include API mapping and endpoint reference  
- ✅ **Field validation** - Use Pydantic `Field()` with comprehensive constraints
- ✅ **Trading context** - Include trading-specific validation and safety considerations
- ✅ **Enum integration** - Use base enums (StrategyType, etc.) for type safety
- ✅ **Range validation** - Use `ge`, `le` constraints for numeric parameters
- ✅ **Pattern validation** - Use regex patterns for structured fields
- ✅ **Field aliases** - Use `alias` for API parameter mapping when needed

### 2. Tool Function Pattern

**Reference Implementation**: `threecommas_mcp/tools/dca_bots.py:69-110`  
**Example**: `get_dca_bot_list()` function

**Key Pattern Elements:**
- ✅ **`@handle_api_errors` decorator** - Always first decorator for consistent error handling
- ✅ **Type hints** - Modern Python union types (str | None, int with defaults)
- ✅ **`response_filter: str = "display"`** - Always include with default value
- ✅ **Concise docstring** - Brief description + Args + Returns (see docstring pattern below)
- ✅ **Pydantic validation** - Use request model for input validation with proper enum types
- ✅ **Automatic parameter building** - Use `request.to_query_params()` for automatic conversion
- ✅ **API request** - Call `api_request()` with endpoint and params
- ✅ **Response filtering** - Always apply `filter_response()` before return
- ✅ **Security filtering** - Automatic removal of sensitive fields (`api_key_invalid`, `api_keys_state`, `customer_id`)
- ✅ **Error context** - Include trading context in error descriptions

### 3. Docstring Pattern

**Reference Implementation**: `threecommas_mcp/models/dca_bots.py:13-15` and `threecommas_mcp/tools/dca_bots.py:24-33`

**Model Class Docstring Pattern:**
```python
class GetModelNameRequest(APIRequest):
    """Request parameters for [domain] [action] [with optional filtering]."""
```

**Tool Function Docstring Pattern:**
```python
async def get_domain_action(...) -> APIResponse:
    """Brief description of what the function does.

    Args:
        param_name: Parameter description
        optional_param: Optional parameter description (default: value)
        response_filter: Response detail level ("full" or "display")

    Returns:
        Brief description of return data structure and key fields.
    """
```

**Key Docstring Elements:**
- ✅ **Concise format** - No API endpoint details, permissions, or implementation notes
- ✅ **Standard Args section** - One line per parameter with type and description
- ✅ **Standard Returns section** - Brief description of return data structure
- ✅ **No verbose sections** - Avoid Raises, See, API Mapping, Script Validation sections
- ✅ **Consistent terminology** - Use established domain language (bots, pairs, accounts)

### 4. File Structure Pattern

**Model File**: `threecommas_mcp/models/dca_bots.py:1-11` (header pattern)  
**Tool File**: `threecommas_mcp/tools/dca_bots.py:1-11` (imports pattern)

**Key Pattern Elements:**
- ✅ **Standard imports** - APIRequest, ResponseFilter, relevant enums from base
- ✅ **Module docstring** - Include domain description and API reference link
- ✅ **Consistent naming** - `Get{Domain}{Action}Request` for model classes
- ✅ **Function naming** - `get_{domain}_{action}` for tool functions

## Implementation Templates

### Reference Existing Code

**For new API implementation, copy patterns from:**

1. **Model**: Copy `threecommas_mcp/models/dca_bots.py:42-116` (GetDCABotListRequest) or `threecommas_mcp/models/account.py:20-38` (GetAccountInfoRequest) and modify for your parameters
2. **Tool Function**: Copy `threecommas_mcp/tools/dca_bots.py:69-161` (get_dca_bot_list) or `threecommas_mcp/tools/account.py:42-91` (get_account_info) and modify endpoint/parameters  
3. **File Structure**: Follow `threecommas_mcp/models/dca_bots.py:1-11` for file headers
4. **Imports**: Follow `threecommas_mcp/tools/dca_bots.py:7-11` for import patterns
5. **Server Registration**: Follow `threecommas_mcp/server.py:29-30` for MCP tool registration

### Quick Implementation Steps

1. **Create model** - Copy `GetDCABotListRequest` and modify fields for your API
2. **Create tool function** - Copy `get_dca_bot_list()` and modify endpoint/parameters
3. **Register in server** - Add `mcp.tool()(your_module.your_function)` to server.py
4. **Update documentation** - Follow 4-layer documentation pattern:
   - API status in `docs/API_REFERENCES.md`
   - Function docs in `docs/tools/{domain}.md`
   - Model docs in `docs/models/{domain}.md`
   - Conversation examples in `docs/conversations/{domain}-conversation.md`
5. **Update progress** - Mark completed in `TASKS.md` and update progress counters

## Pattern Compliance Checklist

When implementing a new API, verify:

### Model Compliance
- [ ] Model inherits from `APIRequest`
- [ ] Concise docstring following pattern: `"""Request parameters for [domain] [action]."""`
- [ ] Field validation using `Field()` with appropriate constraints
- [ ] Use enums for type safety (StrategyType, etc.)
- [ ] Range validation for numeric parameters (ge, le)
- [ ] Pattern validation for structured fields (regex)
- [ ] Field aliases for API parameter mapping when needed
- [ ] Trading safety validation where applicable

### Tool Compliance
- [ ] Uses `@handle_api_errors` decorator as first decorator
- [ ] Modern Python type hints (str | None, int with defaults)
- [ ] Includes `response_filter: str = "display"` parameter
- [ ] Uses proper enum types in function signature
- [ ] Uses Pydantic model for input validation
- [ ] Uses `request.to_query_params()` for automatic parameter building
- [ ] Calls `api_request()` with correct endpoint and params
- [ ] Calls `filter_response(response, request.response_filter)` before return
- [ ] Concise docstring with brief description + Args + Returns sections only

### Documentation Compliance
- [ ] API status updated in `docs/API_REFERENCES.md` (⏸️ → ✅)
- [ ] Model documented in `docs/models/{domain}.md`
- [ ] Tool documented in `docs/tools/{domain}.md`
- [ ] Usage examples in `docs/conversations/{domain}-conversation.md`
- [ ] Cross-references between documentation layers
- [ ] Progress updated in `TASKS.md`

### Quality Compliance
- [ ] Full type hints for all parameters and returns
- [ ] Trading safety considerations included in documentation
- [ ] Error handling covers all scenarios (ValueError, APIError)
- [ ] All quality checks pass (ruff format, ruff check, mypy)
- [ ] MCP server loads without errors

## Benefits of This Pattern

### Scalability
- **Linear growth**: Each new API requires ~60-80 lines of code (20% reduction from automatic param building)
- **Zero setup**: All infrastructure (auth, errors, filtering, parameters) automatic
- **Consistent interface**: Predictable function signatures across all APIs
- **Pattern replication**: Copy-paste-modify approach for rapid development

### Maintainability
- **Single change points**: Common changes affect one location
- **Pattern consistency**: Easy to understand and modify any API
- **Documentation alignment**: All docs follow same structure

### Quality Assurance
- **Type safety**: Pydantic models catch errors early
- **Error handling**: Consistent error responses via decorators
- **Token optimization**: Universal response filtering
- **Trading safety**: Validation patterns prevent unsafe operations
- **Parameter automation**: Automatic query parameter building eliminates manual errors

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

## Pattern Evolution

This pattern has evolved through multiple API implementations. Key improvements include:

- **Enhanced type safety**: Full union types and enum integration
- **Comprehensive validation**: Range, pattern, and enum constraints
- **Automatic parameter building**: Pydantic-powered query parameter generation
- **Documentation integration**: 4-layer documentation system
- **Quality assurance**: Complete toolchain integration

## Next Steps

With the pattern now fully established, additional APIs can be implemented rapidly using this exact template, ensuring consistent quality and maintainability across the entire codebase.

This pattern reference ensures consistent, maintainable, and scalable implementation across all planned GET APIs and future API additions.