# Testing Scripts

Simple, streamlined scripts for testing 3Commas API endpoints before MCP implementation.

## Scripts

### `test_api.py` - Test Any Endpoint
```bash
# Basic test
python scripts/test_api.py ver1/bots/strategy_list

# With parameters  
python scripts/test_api.py ver1/bots account_id=31337503 limit=5

# Specific bot
python scripts/test_api.py ver1/bots/123456/show include_events=true
```

**Shows:**
- Success/error status
- Response size (chars/tokens)
- MCP token limit warnings
- Response structure overview

### `validate_endpoint.py` - Quick Validation Suite
```bash
python scripts/validate_endpoint.py strategy_list
python scripts/validate_endpoint.py dca_bots
python scripts/validate_endpoint.py accounts
python scripts/validate_endpoint.py market_pairs
```

Runs predefined test cases for common endpoints to validate parameters and response sizes.

## Development Workflow

**Before implementing any MCP tool:**

1. **Test the raw API:**
   ```bash
   python scripts/test_api.py <endpoint> [params...]
   ```

2. **Check token limits:**
   - Look for `⚠️ EXCEEDS MCP LIMIT!` warnings
   - If >25,000 tokens, plan response filtering or remove parameters

3. **Validate parameter combinations:**
   ```bash
   python scripts/validate_endpoint.py <endpoint_name>
   ```

## Benefits

- **Prevents debugging time waste** - Catch token limit issues before implementation
- **Validates API documentation** - Test which parameters actually work
- **Accurate token counting** - Uses official Anthropic SDK for precise estimates
- **Simple interface** - No complex configuration or verbose output

## Requirements

- `.env` file with `3COMMAS_API_KEY` and `3COMMAS_SECRET_KEY`
- Anthropic SDK (included in project dependencies) for accurate token counting