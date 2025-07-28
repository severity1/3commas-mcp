# CLAUDE.md for tools/

## Context Activation
Activates when implementing MCP functions for 3Commas API trading operations.

## Implementation Pattern
Reference implementation: `dca_bots.py:14-64` (get_dca_bot_details function)

## Function Structure
- `@handle_api_errors` decorator (decorators.py:11)
- Pydantic request validation (models/{domain}.py)
- `api_request()` call (api/client.py:48)
- `filter_response()` before return (response_filter.py:13)

## Standard Imports Pattern
Reference: `dca_bots.py:7-11` for import structure

## Progress Tracking
Update: TASKS.md, docs/MVP_GET_APIS.md, docs/API_REFERENCES.md (⏸️ → ✅)