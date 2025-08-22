---
allowed-tools: TodoWrite, Read, Grep, LS, Bash
argument-hint: "[api-name, identifier, or task]"
description: Generate implementation plan for 3Commas MCP APIs with validation
---

# API Implementation Plan: $ARGUMENTS

## Phase 1: Analysis & Validation

### API Discovery
Examine project context and identify API details:
- Check `docs/MVP_GET_APIS.md` for priority, phase, and endpoint details
- Review `docs/API_REFERENCES.md` for current implementation status
- Analyze `TASKS.md` for progress context and next logical steps
- Identify best reference implementation to copy patterns from

### Parameter Validation
Validate API using testing scripts:
- Test endpoint: `python scripts/test_api.py <endpoint>` with realistic parameters
- **Parameter Testing**: Identify required vs optional parameters, valid parameter names, correct value formats and types, parameter constraints
- **Request/Response Validation**: Confirm request method and parameter location, test parameter variations, verify actual vs documented response structure
- **Error Testing**: Test invalid parameters to understand error responses
- Document actual response structure and exact parameter names
- Verify token count < 25,000 for MCP efficiency

## Phase 2: Implementation

### Setup & Model Creation
1. **TodoWrite**: Create todos for implementation and documentation phases
2. **Pydantic Model** (`models/{domain}.py`):
   - Use ONLY script-validated parameter names, types, and constraints
   - Follow @docs/PATTERNS.md model patterns exactly
   - Inherit from APIRequest with proper field validation

### Tool Function & Registration  
3. **Tool Function** (`tools/{domain}.py`):
   - Follow @docs/PATTERNS.md tool patterns exactly
   - Use @handle_api_errors decorator
   - Include response_filter parameter with "display" default
   - Use validated endpoint path and parameters from testing
4. **Registration**: Add `mcp.tool()(domain.function_name)` to `server.py`

### Quality Assurance
5. **Validation**: Run all quality checks: `uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`
6. **Final Test**: Verify implemented function matches script validation results

## Phase 3: Documentation

### Status & Documentation Updates
1. **Progress Tracking**: Update TASKS.md counters, change docs/API_REFERENCES.md status (⏸️ → ✅)
2. **Tool Documentation**: Create/update `docs/tools/{domain}.md`
3. **Model Documentation**: Create/update `docs/models/{domain}.md`  
4. **Conversation Examples**: Create/update `docs/conversations/{domain}-conversation.md`
5. **Project Updates**: Update `README.md` and `docs/PATTERNS.md` if needed
6. **Cross-References**: Verify all documentation layers reference each other

### Requirements
- **Trading Safety**: Validate operations before execution
- **Parameter Validation**: Use ONLY script-tested parameters, types, and constraints  
- **Pattern Compliance**: Follow @docs/PATTERNS.md exactly
- **Privacy**: Use dummy data only (bot ID 12345678, $245.67 profit)

---

## Execution

Starting analysis for: `$ARGUMENTS`