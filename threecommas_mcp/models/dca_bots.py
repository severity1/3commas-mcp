"""DCA bot models for 3Commas MCP.

This module defines Pydantic models for DCA bot-related API requests.
These models provide validation for DCA bot management operations.

Reference: https://developers.3commas.io/dca-bot
"""

from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseModelConfig, DealStatus, StrategyType


class GetDCABotDetailsRequest(BaseModelConfig):
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


class DCABotConfig(BaseModel):
    """Model representing DCA bot configuration (response documentation).

    This model represents the structure of a DCA bot configuration
    as returned by the 3Commas API. Used for documentation of
    bot data and trading parameters.

    Note:
        This is a documentation model for response structure.
        We do not validate API responses, only document them.

    API Mapping:
        id -> bot_id
        name -> bot_name
        account_id -> exchange_account_id
        pair -> trading_pair
        base_order_volume -> initial_order_size
        safety_order_volume -> safety_order_size
        safety_order_step_percentage -> price_deviation_percentage

    See:
        docs/models/dca_bots.md#dca-bot-config for reference
    """

    id: int = Field(..., description="Bot unique identifier")
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="User-defined bot name",
        examples=["BTC DCA Bot", "ETH Accumulator", "Conservative BTC"],
    )
    account_id: int = Field(
        ..., ge=1, description="Connected exchange account identifier"
    )
    pair: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[A-Z0-9]+_[A-Z0-9]+$",
        description="Trading pair in BASE_QUOTE format",
        examples=["BTC_USDT", "ETH_USDT", "USDT_BTC"],
    )
    base_order_volume: Decimal = Field(
        ..., gt=0, description="Initial order volume amount"
    )
    safety_order_volume: Decimal = Field(
        ..., gt=0, description="Safety order volume amount"
    )
    safety_order_step_percentage: Decimal = Field(
        ..., gt=0, le=100, description="Price deviation percentage for safety orders"
    )
    take_profit_percentage: Decimal = Field(
        ..., gt=0, le=100, description="Target profit percentage"
    )
    max_safety_orders: int = Field(
        ..., ge=0, le=100, description="Maximum number of safety orders"
    )
    max_active_deals: int = Field(
        ..., ge=1, le=100, description="Maximum concurrent deals"
    )
    strategy: StrategyType = Field(
        ..., description="Trading strategy type (long/short)"
    )
    is_enabled: bool = Field(
        default=False, description="Whether bot is currently active"
    )
    created_at: Optional[str] = Field(
        None, description="Bot creation timestamp (ISO format)"
    )
    updated_at: Optional[str] = Field(
        None, description="Last update timestamp (ISO format)"
    )


class DCABotDeal(BaseModel):
    """Model representing a DCA bot deal (response documentation).

    This model represents the structure of an active or completed deal
    as returned by the 3Commas API. Used for documentation of
    deal data and trading progress.

    Note:
        This is a documentation model for response structure.
        We do not validate API responses, only document them.

    API Mapping:
        id -> deal_id
        bot_id -> parent_bot_id
        pair -> trading_pair
        status -> current_status
        base_order_volume -> initial_order_amount
        safety_orders_count -> completed_safety_orders

    See:
        docs/models/dca_bots.md#dca-bot-deal for reference
    """

    id: int = Field(..., description="Deal unique identifier")
    bot_id: int = Field(..., description="Parent bot identifier")
    pair: str = Field(
        ..., pattern=r"^[A-Z0-9]+_[A-Z0-9]+$", description="Trading pair for this deal"
    )
    status: DealStatus = Field(..., description="Current deal status")
    base_order_volume: Decimal = Field(
        ..., gt=0, description="Base order volume amount"
    )
    safety_orders_count: int = Field(
        ..., ge=0, description="Number of completed safety orders"
    )
    bought_amount: Optional[Decimal] = Field(
        None, ge=0, description="Total amount purchased"
    )
    bought_volume: Optional[Decimal] = Field(
        None, ge=0, description="Total volume spent"
    )
    bought_average_price: Optional[Decimal] = Field(
        None, gt=0, description="Average purchase price"
    )
    current_price: Optional[Decimal] = Field(
        None, gt=0, description="Current market price"
    )
    profit_percentage: Optional[Decimal] = Field(
        None, description="Current profit/loss percentage"
    )
    profit_amount: Optional[Decimal] = Field(
        None, description="Current profit/loss amount"
    )
    created_at: Optional[str] = Field(
        None, description="Deal creation timestamp (ISO format)"
    )
    updated_at: Optional[str] = Field(
        None, description="Last update timestamp (ISO format)"
    )


class DCABotPerformance(BaseModel):
    """Model representing DCA bot performance metrics (response documentation).

    This model represents performance statistics for a DCA bot
    as returned by the 3Commas API. Used for documentation of
    bot profitability and trading history.

    Note:
        This is a documentation model for response structure.
        We do not validate API responses, only document them.

    API Mapping:
        total_profit -> cumulative_profit_amount
        total_profit_percentage -> cumulative_profit_percentage
        active_deals_count -> current_active_deals
        completed_deals_count -> total_completed_deals

    See:
        docs/models/dca_bots.md#dca-bot-performance for reference
    """

    total_profit: Optional[Decimal] = Field(
        None, description="Total cumulative profit/loss amount"
    )
    total_profit_percentage: Optional[Decimal] = Field(
        None, description="Total cumulative profit/loss percentage"
    )
    active_deals_count: int = Field(
        ..., ge=0, description="Number of currently active deals"
    )
    completed_deals_count: int = Field(
        ..., ge=0, description="Total number of completed deals"
    )
    successful_deals_count: int = Field(
        ..., ge=0, description="Number of profitable completed deals"
    )
    failed_deals_count: int = Field(
        ..., ge=0, description="Number of failed/cancelled deals"
    )
    average_deal_time: Optional[Decimal] = Field(
        None, ge=0, description="Average time to complete deals (hours)"
    )
    max_drawdown_percentage: Optional[Decimal] = Field(
        None, ge=0, le=100, description="Maximum drawdown percentage experienced"
    )
    sharpe_ratio: Optional[Decimal] = Field(
        None, description="Risk-adjusted return ratio"
    )
