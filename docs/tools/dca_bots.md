# DCA Bot Tools

This document provides reference documentation for DCA bot management tools in the 3Commas MCP server.

## Overview

DCA (Dollar Cost Averaging) bot tools provide functionality for managing and monitoring DCA bots through the 3Commas API. These tools enable Claude to help users retrieve bot information, analyze performance, and manage bot configurations.

## Functions

### get_dca_bot_details

**Function:** `get_dca_bot_details(bot_id: str, include_events: bool = False, response_filter: str = "display") -> APIResponse`

**Description:** Retrieves comprehensive information about a specific DCA bot including configuration, active deals, trading parameters, and performance data.

**API Endpoint:** `GET /ver1/bots/{bot_id}/show`  
**Security:** SIGNED (requires API key + HMAC signature)  
**Permission:** BOTS_READ

**Parameters:**
- `bot_id` (str, required): DCA bot unique identifier (3Commas bot ID)
- `include_events` (bool, optional): Include related events in response (default: False)
- `response_filter` (str, optional): Filter type for response ("full" or "display", default: "display")

**Returns:** Complete DCA bot details including:
- Bot configuration (trading pair, order volumes, strategy settings)
- Active deals information and status
- Trading parameters and safety order configuration
- Performance metrics and profit/loss data
- Bot status (enabled/disabled) and operational state

**Safety:** Read-only operation with no trading risks

**Examples:** [DCA Bot Management Conversation](../conversations/dca-bot-management-conversation.md#retrieving-bot-details)

## Usage Patterns

### Basic Bot Information Retrieval
```python
# Get basic bot details
bot_details = await get_dca_bot_details("12345678")

# Get bot details with events
detailed_bot = await get_dca_bot_details("12345678", include_events=True)
```

### Bot Status Monitoring
The function is commonly used for:
- Checking bot configuration before making changes
- Monitoring active deals and performance
- Analyzing bot strategy effectiveness
- Troubleshooting bot issues
- Preparing bot update parameters

## Error Handling

**Common Errors:**
- `ValueError`: Empty or invalid bot_id parameter
- `APIError`: Bot not found (invalid bot_id)
- `AuthenticationError`: Invalid API credentials
- `PermissionError`: Insufficient API key permissions (missing BOTS_READ)

**Error Prevention:**
- Ensure bot_id is valid and belongs to your account
- Verify API key has BOTS_READ permission
- Use proper bot ID format (numeric string)

## Integration

### Related Tools
- Future: `list_dca_bots()` - Get all DCA bots for filtering
- Future: `update_dca_bot()` - Modify bot configuration
- Future: `get_dca_bot_stats()` - Detailed performance statistics

### Cross-References
- **Models:** [Base Models](../models/base.md#apiresponse) (APIResponse return type)
- **Conversations:** [DCA Bot Management](../conversations/dca-bot-management-conversation.md)
- **API Reference:** [3Commas DCA Bot API](https://developers.3commas.io/dca-bot/get-dca-bot)

## Security Considerations

- **Read-only operation:** No trading or configuration risks
- **Authentication required:** Uses API key + HMAC signature
- **Rate limiting:** Respects 3Commas BOTS_READ rate limits
- **Data access:** Only returns data for bots owned by authenticated account