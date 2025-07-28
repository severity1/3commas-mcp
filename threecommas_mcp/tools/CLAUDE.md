# CLAUDE.md for @tools/

## Context Activation
Activates when implementing MCP functions for 3Commas API trading operations.

## Implementation Pattern
Reference implementation: @threecommas_mcp/tools/dca_bots.py:14-64 (get_dca_bot_details function)

## Function Structure
- `@handle_api_errors` decorator (@threecommas_mcp/utils/decorators.py:11)
- Pydantic request validation (@threecommas_mcp/models/{domain}.py)
- `api_request()` call (@threecommas_mcp/api/client.py:48)
- `filter_response()` before return (@threecommas_mcp/utils/response_filter.py:13)

## Standard Imports Pattern
Reference: @threecommas_mcp/tools/dca_bots.py:7-11 for import structure

## Progress Tracking
Update: TASKS.md, docs/MVP_GET_APIS.md, docs/API_REFERENCES.md (⏸️ → ✅)