"""Market data models for 3Commas MCP.

This module defines Pydantic models for market data-related API requests.
These models provide validation for market information operations.

Reference: https://developers.3commas.io/market-data
"""

from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, Field
from .base import BaseModelConfig, LimitType


class TradingPair(BaseModel):
    """Model representing a trading pair.

    This model represents the structure of a trading pair as returned
    by the 3Commas API. Used for validation and documentation of
    trading pair data and market availability.

    API Mapping:
        pair -> trading_pair_symbol
        base_currency -> base
        quote_currency -> quote
        market_code -> exchange_market_code

    See:
        docs/models/market_data.md#trading-pair for reference
    """

    pair: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[A-Z0-9]+_[A-Z0-9]+$",
        description="Trading pair symbol in BASE_QUOTE format (e.g., 'BTC_USDT')",
        examples=["BTC_USDT", "ETH_USDT", "USDT_BTC"],
    )
    base_currency: str = Field(
        ...,
        min_length=1,
        max_length=10,
        pattern=r"^[A-Z0-9]+$",
        description="Base currency symbol (e.g., 'BTC', 'ETH')",
        examples=["BTC", "ETH", "ADA"],
    )
    quote_currency: str = Field(
        ...,
        min_length=1,
        max_length=10,
        pattern=r"^[A-Z0-9]+$",
        description="Quote currency symbol (e.g., 'USDT', 'BTC')",
        examples=["USDT", "BTC", "ETH"],
    )
    market_code: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Exchange market code identifier",
        examples=["binance", "okex", "bybit_spot"],
    )
    min_volume: Optional[Decimal] = Field(
        None, gt=0, description="Minimum trading volume allowed for this pair"
    )
    max_volume: Optional[Decimal] = Field(
        None, gt=0, description="Maximum trading volume allowed for this pair"
    )
    volume_precision: Optional[int] = Field(
        None, ge=0, le=18, description="Number of decimal places for volume precision"
    )
    price_precision: Optional[int] = Field(
        None, ge=0, le=18, description="Number of decimal places for price precision"
    )


class CurrencyRate(BaseModel):
    """Model representing currency exchange rate and limits.

    This model represents exchange rate and trading limit information
    for currencies. Used for trading calculations and risk management.

    API Mapping:
        currency_code -> currency
        rate_to_usd -> usd_rate
        min_trading_amount -> min_amount
        max_trading_amount -> max_amount

    See:
        docs/models/market_data.md#currency-rate for reference
    """

    currency_code: str = Field(
        ...,
        min_length=1,
        max_length=10,
        pattern=r"^[A-Z0-9]+$",
        description="Currency symbol in uppercase (e.g., 'BTC', 'ETH', 'USDT')",
        examples=["BTC", "ETH", "USDT", "BNB"],
    )
    rate_to_usd: Decimal = Field(
        ..., gt=0, description="Current exchange rate to USD (must be positive)"
    )
    min_trading_amount: Optional[Decimal] = Field(
        None, gt=0, description="Minimum trading amount allowed for this currency"
    )
    max_trading_amount: Optional[Decimal] = Field(
        None, gt=0, description="Maximum trading amount allowed for this currency"
    )
    trading_fee: Optional[Decimal] = Field(
        None, ge=0, le=1, description="Trading fee as decimal percentage (0.001 = 0.1%)"
    )
    precision: Optional[int] = Field(
        None, ge=0, le=18, description="Number of decimal places for amount precision"
    )


class SupportedMarket(BaseModel):
    """Model representing a supported trading market.

    This model represents information about supported exchanges and
    their capabilities. Used for understanding market compatibility.

    API Mapping:
        market_name -> name
        market_code -> code
        market_type -> type

    See:
        docs/models/market_data.md#supported-market for reference
    """

    market_name: str = Field(..., description="Human-readable market name")
    market_code: str = Field(..., description="Market code identifier")
    market_type: str = Field(..., description="Market type (spot, futures, etc.)")
    is_active: bool = Field(default=True, description="Whether market is active")
    supported_features: Optional[List[str]] = Field(
        default_factory=list, description="Available features"
    )


class GetAllMarketPairsRequest(BaseModelConfig):
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


class GetCurrencyRatesRequest(BaseModelConfig):
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


class GetSupportedMarketsRequest(BaseModelConfig):
    """Request model for getting supported markets.

    This is a simple request model for the get_supported_markets
    endpoint. No parameters are required for this endpoint.

    See:
        docs/models/market_data.md#get-supported-markets-request for reference
    """

    pass  # No parameters required for this endpoint
