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
    """Get comprehensive details for a specific DCA bot.

    Args:
        bot_id: DCA bot unique identifier
        include_events: Include related events (default: False)
        response_filter: Response detail level ("full" or "display")

    Returns:
        Bot configuration, active deals, trading parameters, and performance metrics.
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
    """Get list of DCA bots with optional filtering and sorting.

    Args:
        account_id: Exchange account ID (0 = all accounts)
        strategy: Trading strategy filter (long/short)
        order_direction: Sort order ("ASC" or "DESC")
        limit: Maximum bots to return (1-1000)
        offset: Pagination offset
        from_date: Filter bots created from date (ISO format)
        scope: Filter scope for bot selection
        sort_by: Field to sort by
        quote: Filter by quote currency
        response_filter: Response detail level ("full" or "display")

    Returns:
        List of DCA bots with configuration, status, deals, and performance data.
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
async def get_available_strategy_list(response_filter: str = "display") -> APIResponse:
    """Get all available DCA bot trading strategies.

    Args:
        response_filter: Response detail level ("full" or "display")

    Returns:
        Complete catalog of available strategies with configuration options and compatibility.
    """
    # Validate inputs using Pydantic model
    request = GetAvailableStrategyListRequest(
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
