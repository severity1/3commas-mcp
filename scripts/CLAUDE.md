# Testing Patterns

**Context**: API testing and validation before MCP implementation with token limit validation

## Component Focus
- **Endpoint testing** - test_api.py with accurate token counting via Anthropic SDK
- **Parameter validation** - validate_endpoint.py with predefined test cases
- **Token limit checks** - 25,000 character threshold for MCP compatibility

## Required Patterns
1. **Test before implement** - Always test raw API before MCP tool creation
2. **Validate token limits** - Check for ⚠️ EXCEEDS MCP LIMIT! warnings
3. **Use script-validated parameters** - Use exact parameter names from test results
4. **Check response structure** - Validate response format and size

## Available Scripts
- **test_api.py**: Test any endpoint with parameters and token counting
- **validate_endpoint.py**: Run predefined test cases for common endpoints

## Code Examples
```bash
# Test basic endpoint
python scripts/test_api.py ver1/bots/strategy_list

# Test with parameters
python scripts/test_api.py ver1/bots account_id=31337503 limit=5

# Test specific bot
python scripts/test_api.py ver1/bots/123456/show include_events=true

# Validate common endpoints
python scripts/validate_endpoint.py dca_bots
python scripts/validate_endpoint.py accounts
```

## Integration Requirements
- Test all endpoints before MCP implementation
- If response >25,000 tokens, plan response filtering or parameter reduction
- Use exact parameter names discovered through testing in Pydantic models
- Validate API connectivity and authentication before tool development

## Workflow Integration
1. **Script test** - `python scripts/test_api.py <endpoint>`
2. **Check token warning** - Look for MCP limit warnings
3. **Validate parameters** - Use discovered parameter names in models
4. **Implement tool** - Follow patterns from component CLAUDE.md files