# 3Commas MCP Development

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Quality**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

## Core Implementation Patterns
- **Trading safety first** - Always validate bot/deal operations before execution
- **Consistent tool structure** - All tools use `@handle_api_errors` (@threecommas_mcp/utils/decorators.py:11), Pydantic models, and `filter_response()` (@threecomas_mcp/utils/response_filter.py:13)
- **Security practices** - Never log credentials, always filter sensitive data in responses
- **Component-based architecture** - Each subtree (@threecommas_mcp/tools/, @threecommas_mcp/models/, @threecommas_mcp/utils/, @threecommas_mcp/api/) has focused responsibilities

## Development Workflow
### Implementing New MCP Tools
1. Create Pydantic request model in `models/{domain}.py` (inherit from APIRequest @threecommas_mcp/models/base.py:52)
2. Implement tool function in `tools/{domain}.py`:
   - Use `@handle_api_errors` decorator (@threecommas_mcp/utils/decorators.py:11)
   - Include `response_filter: str = "display"` parameter
   - Call `api_request()` from api/client.py
   - Apply `filter_response()` before returning (@threecommas_mcp/utils/response_filter.py:13)
3. Register tool in server.py with `mcp.tool()(function_name)`
4. Run quality tests
5. **Create/Update Documentation System**:
   - Add/update function reference in `docs/tools/{domain}.md` (parameters, returns, examples, error handling)
   - Add/update model documentation in `docs/models/{domain}.md` (request models, validation patterns, safety considerations)
   - Add/update conversation examples in `docs/conversations/{domain}-conversation.md` (realistic usage scenarios)
   - Update `docs/PATTERNS.md` if pattern is changed or new pattern is introduced
   - Update tracking files:
     - `@TASKS.md` (progress markers)
     - `@docs/API_REFERENCES.md` (⏸️ → ✅)
     - `@docs/MVP_GET_APIS.md` (priority tables)
   - Update `README.md`
6. [Memory Maintenance](#memory-maintenance) - Update relevant CLAUDE.md files when patterns change or new patterns are added

## Component Discovery
Each subtree has specialized CLAUDE.md with implementation-specific guidance:
- @tools/CLAUDE.md - MCP function patterns, MVP tracking
- @models/CLAUDE.md - Pydantic validation patterns, APIRequest inheritance
- @utils/CLAUDE.md - Authentication, error handling, rate limiting utilities  
- @api/CLAUDE.md - HTTP client implementation, HMAC-SHA256, rate limits
- @docs/CLAUDE.md - 4-layer documentation workflow

## Task Progress Maintenance
- Update progress markers in @TASKS.md (Phase tracking)
- Mark completed items in @docs/MVP_GET_APIS.md (Priority tables)
- Update status indicators in @docs/API_REFERENCES.md (⏸️ → ✅)

## Document Maintenance
- **Update relevant documentation** - When code changes affect documented workflows or APIs
- **Maintain accuracy** - Keep documentation synchronized with actual implementation

## Memory Maintenance
- **Update CLAUDE.md files** - When implementation patterns change or new components added
- **Reflect actual code** - Memory files must match current implementation, not theoretical patterns  
- **Component-specific guidance** - Each subtree provides focused context for its domain