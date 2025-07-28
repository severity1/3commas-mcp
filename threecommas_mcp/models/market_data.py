"""Market data models for 3Commas MCP.

This module defines Pydantic models for market data-related API requests.
These models provide validation for market information operations.

Reference: https://developers.3commas.io/market-data
"""

from typing import Optional
from pydantic import Field
from .base import APIRequest, LimitType


class GetAllMarketPairsRequest(APIRequest):
    """Request model for getting all market pairs.

    Request parameters for retrieving all available trading pairs,
    optionally filtered by market code.

    API Mapping:
        market_code -> market_code (optional query parameter)

    API Endpoint: GET /ver1/accounts/market_pairs
    Reference: https://developers.3commas.io/market-data/all-market-pairs

    See:
        docs/models/market_data.md#get-all-market-pairs-request for reference
    """

    market_code: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Optional market code to filter pairs by exchange",
        examples=["binance", "okex", "bybit_spot"],
    )


class GetCurrencyRatesRequest(APIRequest):
    """Request model for getting currency rates and limits.

    Request parameters for retrieving currency exchange rates and
    trading limits for a specific market and trading pair.

    API Mapping:
        market_code -> market_code (query parameter)
        pair -> pair (query parameter)
        limit_type -> limit_type (optional query parameter)

    API Endpoint: GET /ver1/accounts/currency_rates
    Reference: https://developers.3commas.io/market-data/currency-rates-and-limits

    See:
        docs/models/market_data.md#get-currency-rates-request for reference
    """

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
    limit_type: Optional[LimitType] = Field(
        None, description="Optional limit type for specific trading contexts"
    )


class GetSupportedMarketsRequest(APIRequest):
    """Request model for getting supported markets.

    This is a simple request model for the get_supported_markets
    endpoint. No parameters are required for this endpoint.

    See:
        docs/models/market_data.md#get-supported-markets-request for reference
    """

    pass  # No parameters required for this endpoint
