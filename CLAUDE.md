# 3Commas MCP Development

**Context**: 3Commas MCP server development with trading safety focus

## Essential Commands
- **Setup**: `uv sync && uv pip install -e .`
- **API Testing**: `python scripts/test_api.py <endpoint>` (mandatory before implementation)
- **Quality Checks**: `uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`
- **Planning**: Use `/plan <api-identifier>` for systematic implementation workflow

## Core Principles
- **Trading safety first** - Validate operations before execution
- **Script validation mandatory** - Always test APIs before implementation  
- **Pattern compliance** - Follow @docs/PATTERNS.md exactly
- **Privacy protection** - Use dummy data ONLY when documenting (bot ID 12345678, $245.67 profit)

## Component Focus
- **API layer** - HMAC-SHA256 auth, rate limiting (100/min global, 120/min deals, 40/10s smart_trades)
- **Model layer** - Pydantic validation with Field() constraints and enum integration
- **Tool layer** - @handle_api_errors decorator with filter_response() application
- **Utils layer** - Error handling, response filtering, authentication utilities

## Required Workflow
1. **Test endpoint**: `python scripts/test_api.py <endpoint>` (check token limits)
2. **Validate parameters**: Use script-validated parameter names only
3. **Follow patterns**: Implement using established patterns in @docs/PATTERNS.md
4. **Update documentation**: All 4 layers (status, tools, models, conversations)

## Integration Requirements
- All tools use @handle_api_errors decorator
- All responses use filter_response() before return
- All models inherit from APIRequest with response_filter field
- Authentication handled automatically via api_request()

## Available Infrastructure
- **FastMCP Server**: `server.py` with tool registration
- **Rate Limiting**: Automatic endpoint detection and limit application  
- **Token Optimization**: Response filtering (85% reduction on display mode)
- **Error Handling**: Consistent {"error": "message"} formatting