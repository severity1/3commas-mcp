"""DCA Bot management tools for 3Commas MCP

This module implements DCA bot-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/dca-bot
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..models.base import APIResponse


@handle_api_errors
async def get_dca_bot_details(bot_id: str, include_events: bool = False) -> APIResponse:
    """Get details for a specific DCA bot.

    Retrieves comprehensive information about a DCA bot including configuration,
    active deals, trading parameters, and performance data. This is useful for
    checking bot settings, monitoring performance, or preparing for bot updates.

    API endpoint: GET /ver1/bots/{bot_id}/show
    Security: SIGNED (requires API key + HMAC signature)
    Permission: BOTS_READ

    Args:
        bot_id: DCA bot unique identifier (3Commas bot ID)
        include_events: Include related events in response (default: False)

    Returns:
        Complete DCA bot details including:
        - Bot configuration (pair, volumes, strategy)
        - Active deals information
        - Trading parameters and settings
        - Performance metrics and status

    Raises:
        ValueError: If bot_id is empty or invalid
        APIError: If bot not found or access denied

    See:
        docs/tools/dca_bots.md#get-dca-bot-details for usage examples
    """
    if not bot_id or not bot_id.strip():
        raise ValueError("bot_id is required and cannot be empty")

    # Build query parameters
    params = {"include_events": str(include_events).lower()}

    # Make API request using existing authentication infrastructure
    return await api_request(f"ver1/bots/{bot_id}/show", params=params, method="GET")
