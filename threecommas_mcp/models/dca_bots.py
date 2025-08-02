"""DCA bot models for 3Commas MCP.

This module defines Pydantic models for DCA bot-related API requests.
These models provide validation for DCA bot management operations.

Reference: https://developers.3commas.io/dca-bot
"""

from pydantic import Field
from .base import APIRequest, StrategyType


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


class GetDCABotListRequest(APIRequest):
    """Request model for getting list of DCA bots.

    Request parameters for retrieving the user's DCA bot portfolio
    with optional filtering and sorting capabilities.

    API Mapping:
        account_id -> account_id (query parameter)
        strategy -> strategy (query parameter)
        order_direction -> order_direction (query parameter)
        limit -> limit (query parameter)
        offset -> offset (query parameter)
        from -> from (query parameter)
        scope -> scope (query parameter)
        sort_by -> sort_by (query parameter)
        quote -> quote (query parameter)

    API Endpoint: GET /ver1/bots
    Reference: https://developers.3commas.io/dca-bot/get-the-list-of-dca-bots

    See:
        docs/models/dca_bots.md#get-dca-bot-list-request for reference
    """

    account_id: int = Field(
        default=0,
        ge=0,
        description="Filter bots by specific 3Commas exchange account ID (0 = all accounts)",
        examples=[0, 12345, 67890, 123456789],
    )
    strategy: StrategyType | None = Field(
        default=None,
        description="Filter by trading strategy (long or short positions)",
        examples=["long", "short"],
    )
    order_direction: str = Field(
        default="DESC",
        pattern=r"^(ASC|DESC)$",
        description="Sort order for bot list (ASC for ascending, DESC for descending)",
        examples=["DESC", "ASC"],
    )
    limit: int = Field(
        default=50,
        ge=1,
        le=1000,
        description="Maximum number of bots to return (1-1000)",
        examples=[10, 50, 100],
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="Number of bots to skip for pagination",
        examples=[0, 10, 50],
    )
    from_date: str | None = Field(
        default=None,
        alias="from",
        description="Filter bots created from this date (ISO format)",
        examples=["2024-01-01T00:00:00Z", "2024-06-15T12:30:00Z"],
    )
    scope: str | None = Field(
        default=None,
        description="Filter scope for bot selection",
        examples=["enabled", "disabled", "all"],
    )
    sort_by: str | None = Field(
        default=None,
        description="Field to sort by (created_at, updated_at, etc.)",
        examples=["created_at", "updated_at", "name"],
    )
    quote: str | None = Field(
        default=None,
        description="Filter by quote currency (e.g., USDT, BTC)",
        examples=["USDT", "BTC", "ETH"],
    )


class GetAvailableStrategyListRequest(APIRequest):
    """Request model for getting available DCA bot strategies.

    Request parameters for retrieving all available trading strategies
    for DCA bots. The API returns comprehensive strategy information
    without requiring type/direction filters.

    API Mapping:
        account_id -> account_id (query parameter, optional)

    API Endpoint: GET /ver1/bots/strategy_list
    Reference: https://developers.3commas.io/dca-bot/available-strategy-list

    See:
        docs/models/dca_bots.md#get-available-strategy-list-request for reference
    """

    account_id: int = Field(
        default=0,
        ge=0,
        description="Optional 3Commas exchange account ID to filter strategies by account compatibility (0 = all accounts)",
        examples=[0, 12345, 67890, 123456789],
    )
