# 3Commas MCP Development

## Memory Architecture
**Reference**: https://docs.anthropic.com/en/docs/claude-code/memory for official memory guidelines

This root memory defines the complete development workflow. Component memories provide implementation-specific patterns without duplication.

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Script Discovery**: `ls scripts/` (always check before API work)
- **API Testing**: `python scripts/test_api.py <endpoint>`
- **Quality Checks**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

## Core Implementation Patterns
- **Trading safety first** - Always validate bot/deal operations before execution
- **Consistent tool structure** - All tools use `@handle_api_errors`, Pydantic models, and `filter_response()`
- **Security practices** - Never log credentials, always filter sensitive data in responses
- **Component-based architecture** - Each subtree has focused responsibilities

## Development Workflow

### Phase 1: Validation & Discovery
**MANDATORY FIRST STEPS:**
1. **Script Discovery**: `ls scripts/` (confirm testing scripts exist)
2. **API Testing**: `python scripts/test_api.py <endpoint>`
3. **Response Analysis**: Document structure, parameter names, token count
4. **Validation**: Confirm token count < 25,000 for MCP efficiency
5. **Parameter Verification**: Use exact API response names (not documentation)

### Phase 2: Implementation
**Core Implementation Steps:**
1. **Pydantic Model** (`models/{domain}.py`) - Script-validated parameters
2. **Tool Function** (`tools/{domain}.py`) - MCP function with error handling
3. **Tool Registration** (`server.py`) - `mcp.tool()(domain.function_name)`
4. **Quality Assurance** - `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

### Phase 3: Documentation
- Update TASKS.md, docs/API_REFERENCES.md, and docs/MV_GET_APIS.md (⏸️ → ✅)
- Create/Update Tool/model documentation (docs/tools/, docs/models/)
- Create/Update Conversation examples (docs/conversations)
- Update Pattern documentation (docs/PATTERNS.md)
- Update README.md

## Pattern Violation Recovery
If you find yourself implementing without running scripts:
1. **STOP** current work immediately
2. **Run required scripts**: `python scripts/test_api.py <endpoint>`
3. **Compare** script output to your current assumptions
4. **Adjust** implementation based on actual API behavior
5. **Continue** with corrected understanding

## Privacy & Security Requirements

**Critical Rule**: All documentation must use dummy/example data only
- **Never include**: Real account IDs, bot IDs, profit amounts, API keys, or trading data
- **Use instead**: Realistic but fictional examples (e.g., bot ID 12345678, $245.67 profit, account ID 98765)
- **Purpose**: Protect user privacy and prevent accidental exposure of sensitive trading information
- **Applies to**: All documentation layers - tools, models, conversations, README.md, tracking files

## Component Integration

**Component Focus Areas:**
- **tools/**: MCP function signatures, decorators, response handling
- **models/**: Pydantic class structure, field validation, inheritance
- **utils/**: Decorator usage, response filtering, authentication integration
- **api/**: Endpoint formatting, HTTP client usage, error handling
- **docs/**: Documentation templates, structure requirements, tracking updates

## Ongoing Maintenance
- **Update relevant documentation** - When code changes affect documented workflows or APIs
- **Maintain accuracy** - Keep documentation synchronized with actual implementation

## Memory Maintenance

**Update Triggers:**
- New components added or implementation patterns change
- API changes affecting workflow steps
- Documentation requirements evolve

**Maintenance Workflow:**
1. **Verify accuracy** - Ensure memory files reflect current implementation
2. **Update component memories** - When domain-specific patterns change  
3. **Consolidate duplicates** - Remove redundant information between memory files
4. **Validate references** - Check file paths and line numbers remain accurate
5. **Test workflow** - Verify development workflow still functions as documented

**Memory Validation Checklist:**
- [ ] Root memory defines clear workflow without implementation details
- [ ] Component memories contain domain-specific patterns only
- [ ] No circular dependencies between memory files
- [ ] All file references use consistent notation
- [ ] Official Claude Code memory guidelines followed