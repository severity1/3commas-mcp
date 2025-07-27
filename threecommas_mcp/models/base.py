"""Base models for 3Commas MCP.

This module defines base models for 3Commas API requests.
We validate requests using Pydantic models but do not validate responses.
Response structures are documented in comments for reference only.

Reference: https://github.com/3commas-io/3commas-official-api-docs
"""

from enum import Enum
from typing import Any, Dict, TypeVar
from pydantic import BaseModel, ConfigDict


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


class APIRequest(BaseModelConfig):
    """Base model for API requests.

    All API request models should inherit from this class to ensure
    consistent configuration and behavior. It inherits settings from
    BaseModelConfig.

    Note:
        This class provides the foundation for all API requests and inherits
        model configuration from BaseModelConfig.

    See:
        docs/models/base.md for reference
    """

    pass


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
