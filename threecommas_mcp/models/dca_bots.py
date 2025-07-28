"""DCA bot models for 3Commas MCP.

This module defines Pydantic models for DCA bot-related API requests.
These models provide validation for DCA bot management operations.

Reference: https://developers.3commas.io/dca-bot
"""

from pydantic import Field
from .base import APIRequest


class GetDCABotDetailsRequest(APIRequest):
    """Request model for getting DCA bot details.

    Request parameters for retrieving comprehensive information about
    a specific DCA bot including configuration, deals, and performance.

    API Mapping:
        bot_id -> {bot_id} (path parameter)
        include_events -> include_events (query parameter)

    API Endpoint: GET /ver1/bots/{bot_id}/show
    Reference: https://developers.3commas.io/dca-bot/get-dca-bot

    See:
        docs/models/dca_bots.md#get-dca-bot-details-request for reference
    """

    bot_id: str = Field(
        ...,
        min_length=1,
        pattern=r"^\d+$",
        description="DCA bot unique identifier (numeric string)",
        examples=["12345", "67890", "123456789"],
    )
    include_events: bool = Field(
        default=False, description="Include related events in response for debugging"
    )
