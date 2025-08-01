"""Base models for 3Commas MCP.

This module defines base models for 3Commas API requests.
We validate requests using Pydantic models but do not validate responses.
Response structures are documented in comments for reference only.

Reference: https://github.com/3commas-io/3commas-official-api-docs
"""

from enum import Enum
from typing import Any, Dict, TypeVar
from pydantic import BaseModel, ConfigDict, Field


class BaseModelConfig(BaseModel):
    """Base model configuration for all models in the project.

    Provides common configuration settings for Pydantic models including:
    - populate_by_name: Allow populating models by alias name or field name
    - use_enum_values: Use string values from enums instead of enum objects
    - extra: Ignore extra fields in input data

    See:
        docs/models/base.md for reference
    """

    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
        extra="ignore",
    )


class ResponseFilter(str, Enum):
    """Response filter options for API responses.

    Defines the type of response filtering to apply:
    - DISPLAY: Returns filtered response optimized for display (85% token reduction)
    - FULL: Returns complete API response with all fields

    This enum is used across all API requests to control response verbosity
    and optimize token usage in Claude interactions.

    See:
        docs/models/base.md#response-filter for reference
    """

    DISPLAY = "display"
    FULL = "full"


class APIRequest(BaseModelConfig):
    """Base model for API requests.

    All API request models should inherit from this class to ensure
    consistent configuration and behavior. It inherits settings from
    BaseModelConfig and includes the universal response_filter field.

    Note:
        This class provides the foundation for all API requests and inherits
        model configuration from BaseModelConfig. All requests include
        response filtering capabilities for token optimization.

    See:
        docs/models/base.md for reference
    """

    response_filter: ResponseFilter = Field(
        default=ResponseFilter.DISPLAY,
        description="Filter type for response ('full' or 'display', default: 'display')",
    )

    def to_query_params(self, exclude_defaults: bool = True) -> dict[str, str]:
        """Convert model to API query parameters dict.

        Automatically converts the Pydantic model to a dictionary suitable for
        API query parameters. Handles field aliases, excludes None values,
        converts all values to strings, and excludes internal fields.

        Special handling for optional-like integer parameters:
        - account_id=0 is excluded (means "all accounts")
        - Other 0 values are included as they may be valid API parameters

        Args:
            exclude_defaults: Exclude fields with default values (default: True)

        Returns:
            Dict suitable for API request query parameters with all values as strings

        Example:
            >>> request = GetDCABotListRequest(account_id=12345, strategy="long")
            >>> params = request.to_query_params()
            >>> # {'account_id': '12345', 'strategy': 'long'}
        """
        # Get model data using by_alias to handle field aliases properly
        data = self.model_dump(
            by_alias=True,
            exclude_none=True,
            exclude_defaults=exclude_defaults,
            exclude={"response_filter"},  # Exclude internal field
        )

        # Handle special cases for optional-like behavior
        if data.get("account_id") == 0:
            data.pop("account_id", None)  # Don't filter by account

        # Convert all values to strings as required by query parameters
        return {key: str(value) for key, value in data.items()}


# Common enums used across multiple modules
class BotType(str, Enum):
    """Bot type options for DCA and Grid bots.

    Defines the type of trading bot:
    - DCA: Dollar Cost Averaging bot for accumulating positions
    - GRID: Grid trading bot for range-bound markets

    Reference: https://github.com/3commas-io/3commas-official-api-docs/blob/master/bots_api.md

    See:
        docs/models/bots.md for reference
    """

    DCA = "Bot::DcaBot"
    GRID = "Bot::GridBot"


class DealStatus(str, Enum):
    """Deal status options for bot deals.

    Defines the current status of a trading deal:
    - CREATED: Deal has been created but not started
    - BASE_ORDER_PLACED: Base order has been placed
    - BOUGHT: Base order filled, waiting for profit target
    - CANCELLED: Deal was cancelled before completion
    - COMPLETED: Deal completed successfully with profit
    - FAILED: Deal failed due to error
    - PANIC_SELL_PENDING: Panic sell order placed, waiting for fill
    - PANIC_SELL_ORDER_PLACED: Panic sell order active on exchange

    Reference: https://github.com/3commas-io/3commas-official-api-docs/blob/master/deals_api.md

    See:
        docs/models/deals.md for reference
    """

    CREATED = "created"
    BASE_ORDER_PLACED = "base_order_placed"
    BOUGHT = "bought"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    PANIC_SELL_PENDING = "panic_sell_pending"
    PANIC_SELL_ORDER_PLACED = "panic_sell_order_placed"


class StrategyType(str, Enum):
    """Strategy type options for bot strategies.

    Defines the type of trading strategy:
    - LONG: Long positions (buy low, sell high)
    - SHORT: Short positions (sell high, buy low)

    Reference: https://github.com/3commas-io/3commas-official-api-docs/blob/master/bots_api.md

    See:
        docs/models/strategies.md for reference
    """

    LONG = "long"
    SHORT = "short"


class LimitType(str, Enum):
    """Limit type options for currency rates and trading limits.

    Defines the type of trading limits to retrieve:
    - BOT: Trading limits for DCA, Signal, and Grid bots
    - SMART_TRADE: Trading limits for SmartTrade operations

    Reference: https://developers.3commas.io/market-data/currency-rates-and-limits

    See:
        docs/models/market_data.md for reference
    """

    BOT = "bot"
    SMART_TRADE = "smart_trade"


class MarketCode(str, Enum):
    """Market code options for supported exchanges.

    Defines the supported exchange market codes:
    - BINANCE: Binance spot trading
    - BINANCE_FUTURES: Binance USDT-M futures
    - BINANCE_MARGIN: Binance margin trading
    - OKX: OKX spot trading
    - BYBIT: Bybit spot trading
    - GATE_IO: Gate.io spot trading

    Reference: https://developers.3commas.io/market-data/supported_markets_list

    See:
        docs/models/market_data.md for reference
    """

    BINANCE = "binance"
    BINANCE_FUTURES = "binance_futures"
    BINANCE_MARGIN = "binance_margin"
    OKX = "okex"
    BYBIT = "bybit_spot"
    GATE_IO = "gate_io"


# Response type for all API calls - just a dictionary with no validation
APIResponse = Dict[str, Any]


# Type variable for API requests to use with generics
ReqT = TypeVar("ReqT", bound=APIRequest)
