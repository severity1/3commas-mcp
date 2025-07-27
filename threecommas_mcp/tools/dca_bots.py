"""DCA Bot management tools for 3Commas MCP

This module implements DCA bot-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/dca-bot
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse
from ..models.dca_bots import GetDCABotDetailsRequest


@handle_api_errors
async def get_dca_bot_details(
    bot_id: str, include_events: bool = False, response_filter: str = "display"
) -> APIResponse:
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
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        Complete DCA bot details including:
        - Bot configuration (pair, volumes, strategy)
        - Active deals information
        - Trading parameters and settings
        - Performance metrics and status

    Raises:
        ValueError: If bot_id is empty or invalid, or if response_filter is invalid
        APIError: If bot not found or access denied

    See:
        docs/tools/dca_bots.md#get-dca-bot-details for usage examples
    """
    # Validate inputs using Pydantic model
    request = GetDCABotDetailsRequest(bot_id=bot_id, include_events=include_events)

    # Build query parameters
    params = {"include_events": str(request.include_events).lower()}

    # Make API request using existing authentication infrastructure
    response = await api_request(
        f"ver1/bots/{request.bot_id}/show", params=params, method="GET"
    )

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, response_filter)

    return response
