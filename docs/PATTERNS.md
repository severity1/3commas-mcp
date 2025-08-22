# Implementation Patterns Reference

Implementation patterns for 3Commas MCP server APIs.

## Core Patterns

### 1. Model Definition Pattern
**Reference**: `threecommas_mcp/models/dca_bots.py:42-116` (GetDCABotListRequest)

- Inherit from `APIRequest`
- Concise docstring: `"""Request parameters for [domain] [action]."""`
- Field validation with Pydantic `Field()`
- Enum integration for type safety
- Range/pattern validation for constraints

### 2. Tool Function Pattern
**Reference**: `threecommas_mcp/tools/dca_bots.py:69-110` (get_dca_bot_list)

- `@handle_api_errors` decorator (first)
- Modern type hints (str | None, defaults)
- `response_filter: str = "display"` parameter
- Pydantic model validation
- `request.to_query_params()` for parameters
- `filter_response()` before return

### 3. Docstring Pattern
**Model**: `"""Request parameters for [domain] [action]."""`
**Tool**: Brief description + Args + Returns only

### 4. File Structure Pattern
- Standard imports from base
- Module docstring with API reference
- Consistent naming: `Get{Domain}{Action}Request`
- Function naming: `get_{domain}_{action}`

## Quick Implementation

1. **Copy model** from GetDCABotListRequest
2. **Copy tool** from get_dca_bot_list()
3. **Register in server.py**
4. **Update 4-layer docs**:
   - `docs/API_REFERENCES.md`
   - `docs/tools/{domain}.md`
   - `docs/models/{domain}.md`
   - `docs/conversations/{domain}-conversation.md`

## Essential Checklist

### Model
- [ ] Inherits from `APIRequest`
- [ ] Uses `Field()` validation
- [ ] Concise docstring pattern

### Tool
- [ ] `@handle_api_errors` decorator
- [ ] `response_filter` parameter
- [ ] Uses Pydantic validation
- [ ] Uses `to_query_params()`
- [ ] Uses `filter_response()`

### Documentation
- [ ] API status updated
- [ ] 4-layer docs complete
- [ ] Cross-references maintained
- [ ] **Use dummy data ONLY when documenting** (bot ID 12345678, $245.67 profit)

## Cross-References

- **Models**: `threecommas_mcp/models/CLAUDE.md`
- **Tools**: `threecommas_mcp/tools/CLAUDE.md`
- **Development**: `docs/DEVELOPMENT.md`
- **Progress**: `TASKS.md`, `docs/API_REFERENCES.md`