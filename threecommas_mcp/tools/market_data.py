"""Market data tools for 3Commas MCP

This module implements market data-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/market-data
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse, LimitType, ResponseFilter
from ..models.market_data import (
    GetAllMarketPairsRequest,
    GetCurrencyRatesRequest,
    GetSupportedMarketsRequest,
)


@handle_api_errors
async def get_all_market_pairs(
    market_code: str | None = None, response_filter: str = "display"
) -> APIResponse:
    """Get all available trading pairs across markets.

    Args:
        market_code: Optional market filter (e.g., "binance", "okx")
        response_filter: Response detail level ("full" or "display")

    Returns:
        List of trading pairs with symbols, availability, and trading parameters.
    """
    # Validate inputs using Pydantic model
    request = GetAllMarketPairsRequest(
        market_code=market_code, response_filter=ResponseFilter(response_filter)
    )

    # Build query parameters using automatic Pydantic conversion
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request(
        "ver1/accounts/market_pairs", params=params, method="GET"
    )

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_currency_rates_and_limits(
    market_code: str,
    pair: str,
    limit_type: LimitType | None = None,
    response_filter: str = "display",
) -> APIResponse:
    """Get current exchange rates and trading limits for a currency pair.

    Args:
        market_code: Exchange market code
        pair: Trading pair (e.g., "BTC_USDT")
        limit_type: Optional limit type (bot or smart_trade)
        response_filter: Response detail level ("full" or "display")

    Returns:
        Exchange rates, trading limits, precision, and fee information.
    """
    # Validate inputs using Pydantic model
    request = GetCurrencyRatesRequest(
        market_code=market_code,
        pair=pair,
        limit_type=limit_type,
        response_filter=ResponseFilter(response_filter),
    )

    # Build query parameters using automatic Pydantic conversion
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request(
        "ver1/accounts/currency_rates", params=params, method="GET"
    )

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_supported_markets(response_filter: str = "display") -> APIResponse:
    """Get all supported trading markets and exchanges.

    Args:
        response_filter: Response detail level ("full" or "display")

    Returns:
        List of supported markets with names, features, and compatibility information.
    """
    # Validate inputs using Pydantic model
    request = GetSupportedMarketsRequest(
        response_filter=ResponseFilter(response_filter)
    )

    # Make API request using existing authentication infrastructure
    response = await api_request("ver1/accounts/market_list", method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response
