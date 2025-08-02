"""DCA Bot management tools for 3Commas MCP

This module implements DCA bot-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/dca-bot
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse, ResponseFilter, StrategyType
from ..models.dca_bots import (
    GetDCABotDetailsRequest,
    GetDCABotListRequest,
    GetAvailableStrategyListRequest,
)


@handle_api_errors
async def get_dca_bot_details(
    bot_id: str, include_events: bool = False, response_filter: str = "display"
) -> APIResponse:
    """Get details for a specific DCA bot.

    Retrieves comprehensive information about a DCA bot including configuration,
    active deals, trading parameters, and performance data. This is useful for
    checking bot settings, monitoring performance, or preparing for bot updates.

    API endpoint: GET /ver1/bots/{bot_id}/show
    Security: SIGNED (requires API key + HMAC signature)
    Permission: BOTS_READ

    Args:
        bot_id: DCA bot unique identifier (3Commas bot ID)
        include_events: Include related events in response (default: False)
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        Complete DCA bot details including:
        - Bot configuration (pair, volumes, strategy)
        - Active deals information
        - Trading parameters and settings
        - Performance metrics and status

    Raises:
        ValueError: If bot_id is empty or invalid, or if response_filter is invalid
        APIError: If bot not found or access denied

    See:
        docs/tools/dca_bots.md#get-dca-bot-details for usage examples
    """
    # Validate inputs using Pydantic model
    request = GetDCABotDetailsRequest(
        bot_id=bot_id,
        include_events=include_events,
        response_filter=ResponseFilter(response_filter),
    )

    # Build query parameters using automatic Pydantic conversion
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request(
        f"ver1/bots/{request.bot_id}/show", params=params, method="GET"
    )

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_dca_bot_list(
    account_id: int = 0,
    strategy: StrategyType | None = None,
    order_direction: str = "DESC",
    limit: int = 50,
    offset: int = 0,
    from_date: str | None = None,
    scope: str | None = None,
    sort_by: str | None = None,
    quote: str | None = None,
    response_filter: str = "display",
) -> APIResponse:
    """Get list of DCA bots for the user's account.

    Retrieves the user's DCA bot portfolio with optional filtering and sorting.
    This provides an overview of all DCA bots including their status, configuration,
    and performance data. Essential for bot management and portfolio analysis.

    API endpoint: GET /ver1/bots
    Security: SIGNED (requires API key + HMAC signature)
    Permission: BOTS_READ

    Args:
        account_id: Filter bots by specific 3Commas exchange account ID (0 = all accounts, default: 0)
        strategy: Filter by trading strategy (StrategyType.LONG or StrategyType.SHORT)
        order_direction: Sort order ("ASC" or "DESC", default: "DESC")
        limit: Maximum number of bots to return (1-1000, default: 50)
        offset: Number of bots to skip for pagination (default: 0)
        from_date: Filter bots created from this date (ISO format)
        scope: Filter scope for bot selection
        sort_by: Field to sort by (created_at, updated_at, etc.)
        quote: Filter by quote currency (e.g., "USDT", "BTC")
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        List of DCA bots including:
        - Bot configuration (pairs, volumes, strategies)
        - Status and enabled state
        - Active deals information
        - Performance metrics
        - Trading parameters

    Raises:
        ValueError: If parameters are invalid or outside acceptable ranges
        APIError: If API request fails or access denied

    See:
        docs/tools/dca_bots.md#get-dca-bot-list for usage examples
    """
    # Validate inputs using Pydantic model
    request = GetDCABotListRequest(
        account_id=account_id,
        strategy=strategy,
        order_direction=order_direction,
        limit=limit,
        offset=offset,
        **{"from": from_date} if from_date is not None else {},
        scope=scope,
        sort_by=sort_by,
        quote=quote,
        response_filter=ResponseFilter(response_filter),
    )

    # Build query parameters using automatic Pydantic conversion
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request("ver1/bots", params=params, method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_available_strategy_list(
    account_id: int = 0, response_filter: str = "display"
) -> APIResponse:
    """Get list of available DCA bot strategies.

    Retrieves all available trading strategies for DCA bots. The API returns
    comprehensive strategy information including strategy names, types, options,
    and account compatibility without requiring type/direction filters.

    API endpoint: GET /ver1/bots/strategy_list
    Security: SIGNED (requires API key + HMAC signature)
    Permission: BOTS_READ

    Args:
        account_id: 3Commas exchange account ID to filter strategies by account compatibility (0 = all accounts, default: 0)
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        Complete strategy catalog including:
        - All available strategy types (QFL, RSI, Trading View, Manual, etc.)
        - Strategy configuration options and parameters
        - Account type compatibility information
        - Payment requirements and beta status
        - Strategy-specific settings and constraints

    Raises:
        ValueError: If account_id is invalid or response_filter is invalid
        APIError: If API request fails or access denied

    See:
        docs/tools/dca_bots.md#get-available-strategy-list for usage examples
    """
    # Validate inputs using Pydantic model
    request = GetAvailableStrategyListRequest(
        account_id=account_id,
        response_filter=ResponseFilter(response_filter),
    )

    # Build query parameters using automatic Pydantic conversion
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request("ver1/bots/strategy_list", params=params, method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response
