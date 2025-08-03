# 3Commas MCP Development

## Memory Management
**Reference**: https://docs.anthropic.com/en/docs/claude-code/memory for official memory guidelines

This root memory defines the master development workflow. Component-specific memories are automatically discovered in subdirectories when working in those areas.

**Component memories available:**
- `threecommas_mcp/tools/CLAUDE.md` - MCP function implementation patterns
- `threecommas_mcp/models/CLAUDE.md` - Pydantic validation patterns  
- `threecommas_mcp/utils/CLAUDE.md` - Authentication and error handling utilities
- `threecommas_mcp/api/CLAUDE.md` - HTTP client implementation
- `docs/CLAUDE.md` - Comprehensive documentation requirements

## Essential Commands
- **Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install**: `uv pip install -e .`
- **Quality**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

## Core Implementation Patterns
- **Trading safety first** - Always validate bot/deal operations before execution
- **Consistent tool structure** - All tools use `@handle_api_errors`, Pydantic models, and `filter_response()`
- **Security practices** - Never log credentials, always filter sensitive data in responses
- **Component-based architecture** - Each subtree has focused responsibilities

## Development Workflow
### Implementing New MCP Tools
1. **API Validation First** - Thoroughly test API endpoint parameters and response structure before implementation:
   ```bash
   python scripts/test_api.py <endpoint> [key=value ...]
   python scripts/validate_endpoint.py <endpoint_name>  # For common endpoints
   ```
   - Test with different parameter combinations to verify actual API behavior
   - Validate response structure matches documentation expectations
   - Confirm parameter names and types before creating Pydantic models
2. Create Pydantic request model in `models/{domain}.py` (inherit from APIRequest)
3. Implement tool function in `tools/{domain}.py`:
   - Use `@handle_api_errors` decorator
   - Include `response_filter: str = "display"` parameter
   - Call `api_request()` from api/client.py
   - Apply `filter_response()` before returning
4. Register tool in server.py with `mcp.tool()(function_name)`
5. **Run quality tests**: `uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`
6. **Documentation System** - Follow requirements in `docs/CLAUDE.md`
7. **Update Root README.md** - Update tool listings, phase completion, and usage examples
8. **Memory Maintenance** - Update CLAUDE.md files when patterns change

## Privacy & Security Requirements

**Critical Rule**: All documentation must use dummy/example data only
- **Never include**: Real account IDs, bot IDs, profit amounts, API keys, or trading data
- **Use instead**: Realistic but fictional examples (e.g., bot ID 12345678, $245.67 profit, account ID 98765)
- **Purpose**: Protect user privacy and prevent accidental exposure of sensitive trading information
- **Applies to**: All documentation layers - tools, models, conversations, README.md, tracking files

## Component Integration

**Memory Hierarchy**: Root memory (this file) defines workflow; component memories provide implementation details:
- **tools/** - MCP function patterns for step 3-4  
- **models/** - Pydantic validation patterns for step 2
- **utils/** - Error handling and authentication utilities
- **api/** - HTTP client implementation  
- **docs/** - Documentation requirements for steps 6-7

**Usage**: Consult component memories when implementing specific parts of the workflow.

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