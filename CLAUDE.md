# 3Commas MCP Development

## Memory Architecture
**Reference**: https://docs.anthropic.com/en/docs/claude-code/memory for official memory guidelines

This root memory system provides development principles and guidance. For step-by-step implementation workflow, use the `/plan` slash command.

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Script Discovery**: `ls scripts/` (always check before API work)
- **API Testing**: `python scripts/test_api.py <endpoint>`
- **Quality Checks**: `uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`
- **Implementation Planning**: Use `/plan <api-identifier>` for compliant workflow generation

## Core Principles
- **Trading safety first** - Validate operations before execution
- **Follow established patterns** - Reference @docs/PATTERNS.md for consistency
- **Component-based architecture** - Each subtree has focused responsibilities
- **Script validation mandatory** - Always test APIs before implementation
- **3-phase workflow** - Use `/plan` command for systematic implementation

## Information Hierarchy
- **CLAUDE.md** (this file): Development principles and guidance
- **`/plan` command**: Step-by-step implementation workflow
- **@docs/PATTERNS.md**: Implementation details (HOW to implement)
- **Component memories**: Domain-specific patterns only

## Success Criteria

### Requirements (Non-Negotiable)
- **Trading Safety**: Validate operations before execution
- **Pattern Compliance**: Follow @docs/PATTERNS.md exactly for implementation details
- **Privacy**: Use dummy data only (bot ID 12345678, $245.67 profit)
- **Script Validation**: Always test APIs before implementation
- **Workflow Compliance**: Use `/plan` command for systematic implementation

### Common Violations to Avoid
- Skipping script testing and validation phase
- Using documentation parameters instead of script-validated ones
- Missing systematic workflow tracking
- Implementing without following established patterns
- Incomplete documentation (missing any required layers)

## Component Integration

### Available Infrastructure
- **FastMCP Server**: `server.py` with tool registration
- **Authentication**: HMAC-SHA256 with rate limiting in `api/client.py`
- **Validation**: Pydantic models with trading safety validation
- **Error Handling**: Comprehensive decorators in `utils/decorators.py`
- **Response Filtering**: Token optimization in `utils/response_filter.py`

### Documentation System
Four-layer documentation required for all implementations:
1. **Status Updates**: TASKS.md, docs/API_REFERENCES.md
2. **Tool Documentation**: docs/tools/{domain}.md
3. **Model Documentation**: docs/models/{domain}.md
4. **Conversation Examples**: docs/conversations/{domain}-conversation.md

---

## Memory Maintenance

**Update Triggers:**
- New components or architectural changes
- Core principle changes
- New infrastructure or tooling
- Component memory system changes

**Validation Checklist:**
- [ ] Root memory provides clear principles without implementation steps
- [ ] Component memories contain domain-specific guidance only
- [ ] `/plan` command handles all workflow implementation details
- [ ] All file references use consistent notation
- [ ] Official Claude Code memory guidelines followed

**Note**: Implementation workflow details have been moved to the `/plan` slash command to maintain clean separation between memory guidance and executable workflow.