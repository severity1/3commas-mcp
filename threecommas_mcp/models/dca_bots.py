"""DCA bot models for 3Commas MCP.

This module defines Pydantic models for DCA bot-related API requests.
These models provide validation for DCA bot management operations.

Reference: https://developers.3commas.io/dca-bot
"""

from pydantic import Field
from .base import APIRequest, StrategyType


class GetDCABotDetailsRequest(APIRequest):
    """Request parameters for DCA bot details retrieval."""

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
    """Request parameters for DCA bot list with filtering and sorting options."""

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
    """Request parameters for available DCA bot strategies."""

    pass


class GetDCABotProfitDataRequest(APIRequest):
    """Request parameters for DCA bot profit data retrieval."""

    bot_id: str = Field(
        ...,
        min_length=1,
        pattern=r"^\d+$",
        description="DCA bot unique identifier (numeric string)",
        examples=["12345", "67890", "123456789"],
    )
    days: int = Field(
        default=30,
        ge=1,
        le=365,
        description="Number of days for profit data (1-365 days, default: 30)",
        examples=[7, 30, 90, 180],
    )
