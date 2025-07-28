# CLAUDE.md for api/

## Context Activation
Activates when implementing HTTP client for 3Commas API integration.

## Core Function: api_request() (client.py:48-173)
Used by all tool functions for authenticated API calls.

## Implementation Features
- HMAC-SHA256 authentication via `sign_request()` (client.py:103-111)
- Rate limiting with `_rate_limiter` (client.py:75-80)
- Endpoint type detection (client.py:24-44): global/deals/smart_trades/deals_show
- JSON/text response handling (client.py:144-153)
- Security: Never logs credentials (client.py:166)