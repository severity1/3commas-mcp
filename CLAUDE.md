# 3Commas MCP Development

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Quality**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

## Core Implementation Patterns
- **Trading safety first** - Always validate bot/deal operations before execution
- **Consistent tool structure** - All tools use `@handle_api_errors` (decorators.py:11), Pydantic models, and `filter_response()` (response_filter.py:13)
- **Security practices** - Never log credentials, always filter sensitive data in responses
- **Component-based architecture** - Each subtree (tools/, models/, utils/, api/) has focused responsibilities

## Development Workflow
### Implementing New MCP Tools
1. Create Pydantic request model in `models/{domain}.py` (inherit from APIRequest base.py:52)
2. Implement tool function in `tools/{domain}.py`:
   - Use `@handle_api_errors` decorator (decorators.py:11)
   - Include `response_filter: str = "display"` parameter
   - Call `api_request()` from api/client.py
   - Apply `filter_response()` before returning (response_filter.py:13)
3. Update tracking files: TASKS.md, docs/MVP_GET_APIS.md, docs/API_REFERENCES.md

## Component Discovery
Each subtree has specialized CLAUDE.md with implementation-specific guidance:
- `tools/CLAUDE.md` - MCP function patterns, MVP tracking
- `models/CLAUDE.md` - Pydantic validation patterns, APIRequest inheritance
- `utils/CLAUDE.md` - Authentication, error handling, rate limiting utilities  
- `api/CLAUDE.md` - HTTP client implementation, HMAC-SHA256, rate limits
- `docs/CLAUDE.md` - 4-layer documentation workflow

## Task Progress Maintenance
When implementing a task, update status in task tracking files:
- Update progress markers in TASKS.md (Phase tracking)
- Mark completed items in MVP_GET_APIS.md (Priority tables)
- Update status indicators in API_REFERENCES.md (⏸️ → ✅)

## Memory Maintenance
- **Update CLAUDE.md files** - When implementation patterns change or new components added
- **Reflect actual code** - Memory files must match current implementation, not theoretical patterns  
- **Component-specific guidance** - Each subtree provides focused context for its domain

## Document Maintenance
- **Update relevant documentation** - When code changes affect documented workflows or APIs
- **Maintain accuracy** - Keep documentation synchronized with actual implementation

Update triggers: New modules, architectural changes, function signatures modified, documentation becomes outdated