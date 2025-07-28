# 3Commas MCP Development

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Quality**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

## Core Principles
- **Trading safety first** - Always validate bot/deal operations
- **Component guidance** - Let subtree discovery load context automatically
- **Pattern consistency** - Follow `docs/PATTERNS.md` for all implementations
- **Security focus** - Never log credentials, always filter responses

## Project Tracking Workflow
When implementing APIs, update status in:
- `TASKS.md` - Change ⏸️ to ✅ for completed APIs
- `docs/MVP_GET_APIS.md` - Mark completed in implementation tables
- `docs/API_REFERENCES.md` - Update status markers

## Memory Maintenance
- **Update CLAUDE.md files** - When implementation patterns change or new components added
- **Reflect actual code** - Memory files must match current implementation, not theoretical patterns
- **Component-specific guidance** - Each subtree provides focused context for its domain

## Component Discovery
Subtree memory loads specific guidance for:
- `tools/` - MCP functions, MVP tracking, trading safety patterns
- `models/` - Pydantic validation, APIRequest inheritance, field mapping
- `utils/` - Auth, error handling, response filtering, rate limiting
- `api/` - HTTP client, HMAC-SHA256, 3Commas integration
- `docs/` - Documentation workflow, 4-layer structure, templates