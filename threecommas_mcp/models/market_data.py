"""Market data models for 3Commas MCP.

This module defines Pydantic models for market data-related API requests.
These models provide validation for market information operations.

Reference: https://developers.3commas.io/market-data
"""

from pydantic import Field
from .base import APIRequest, LimitType


class GetAllMarketPairsRequest(APIRequest):
    """Request parameters for market pairs retrieval with optional filtering."""

    market_code: str | None = Field(
        None,
        min_length=1,
        max_length=50,
        description="Optional market code to filter pairs by exchange",
        examples=["binance", "okex", "bybit_spot"],
    )


class GetCurrencyRatesRequest(APIRequest):
    """Request parameters for currency rates and trading limits."""

    market_code: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Exchange market code from supported markets (e.g., 'binance', 'okex')",
        examples=["binance", "okex", "bybit_spot"],
    )
    pair: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[A-Z0-9]+_[A-Z0-9]+$",
        description="Trading pair in BASE_QUOTE format (e.g., 'BTC_USDT', 'ETH_USDT')",
        examples=["BTC_USDT", "ETH_USDT", "USDT_BTC"],
    )
    limit_type: LimitType | None = Field(
        None, description="Optional limit type for specific trading contexts"
    )


class GetSupportedMarketsRequest(APIRequest):
    """Request parameters for supported markets retrieval."""

    pass  # No parameters required for this endpoint
