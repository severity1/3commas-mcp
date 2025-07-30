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
    """Get all available market pairs.

    Retrieves all available trading pairs across markets or for a specific market.
    This is essential for bot configuration as it provides the complete list of
    tradeable pairs, their symbols, and market availability.

    API endpoint: GET /ver1/market_pairs
    Security: SIGNED (requires API key + HMAC signature)
    Permission: NONE (public data with authentication)

    Args:
        market_code: Optional market code to filter pairs (e.g., "binance", "okx")
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        List of all available trading pairs including:
        - Pair symbols (base/quote currencies)
        - Market availability and status
        - Trading parameters and restrictions
        - Volume and liquidity information

    Raises:
        ValueError: If response_filter is invalid
        APIError: If API request fails

    See:
        docs/tools/market_data.md#get-all-market-pairs for usage examples
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
    """Get currency rates and trading limits.

    Retrieves current exchange rates and trading limits for currencies.
    This is required for trading decisions as it provides essential pricing
    and limit information needed for order calculations and risk management.

    API endpoint: GET /ver1/accounts/currency_rates
    Security: NONE (no authentication required)
    Permission: NONE (public data)

    Args:
        market_code: Exchange market code (string from supported markets)
        pair: Trading pair to get specific rates (e.g., "BTC_USDT")
        limit_type: Optional limit type (LimitType.BOT or LimitType.SMART_TRADE)
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        Currency rates and limits including:
        - Current exchange rates between currencies
        - Minimum and maximum trading limits
        - Price precision and step sizes
        - Trading fees and commission rates

    Raises:
        ValueError: If market_code, pair, limit_type, or response_filter is invalid
        APIError: If API request fails

    See:
        docs/tools/market_data.md#get-currency-rates-and-limits for usage examples
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
    """Get list of supported trading markets.

    Retrieves the complete list of supported trading markets and exchanges.
    This provides exchange compatibility information needed to understand
    which markets are available for trading operations and bot deployment.

    API endpoint: GET /ver1/market_list
    Security: SIGNED (requires API key + HMAC signature)
    Permission: NONE (public data with authentication)

    Args:
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        List of supported markets including:
        - Market names and codes
        - Exchange compatibility status
        - Available trading features
        - Market-specific limitations
        - Connection requirements

    Raises:
        ValueError: If response_filter is invalid
        APIError: If API request fails

    See:
        docs/tools/market_data.md#get-supported-markets for usage examples
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
