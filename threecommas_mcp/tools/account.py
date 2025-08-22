"""Account management tools for 3Commas MCP

This module implements account-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/account
"""

from typing import Optional, Union
from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse, ResponseFilter
from ..models.account import (
    GetConnectedExchangesRequest,
    GetAccountInfoRequest,
    GetBalanceHistoryRequest,
)


@handle_api_errors
async def get_connected_exchanges_and_wallets(
    response_filter: str = "display",
) -> APIResponse:
    """Get all connected exchange accounts and wallets.

    Args:
        response_filter: Response detail level ("full" or "display")

    Returns:
        List of connected exchanges with account details, permissions, and status.
    """
    # Validate inputs using Pydantic model
    request = GetConnectedExchangesRequest(
        response_filter=ResponseFilter(response_filter)
    )

    # Make API request using existing authentication infrastructure
    response = await api_request("ver1/accounts", method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_account_info(
    account_id: Union[str, int] = "summary",
    response_filter: str = "display",
) -> APIResponse:
    """Get account information for a specific account or aggregated summary.

    Args:
        account_id: Account ID (integer) or 'summary' for aggregated data
        response_filter: Response detail level ("full" or "display")

    Returns:
        Account information including settings, balance, profit metrics, and trading permissions.
    """
    # Validate inputs using Pydantic model
    request = GetAccountInfoRequest(
        account_id=account_id, response_filter=ResponseFilter(response_filter)
    )

    # Build endpoint with account ID
    endpoint = f"ver1/accounts/{request.account_id}"

    # Make API request using existing authentication infrastructure
    response = await api_request(endpoint, method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response


@handle_api_errors
async def get_balance_history_data(
    date_from: str,
    account_id: Union[str, int] = "summary",
    date_to: Optional[str] = None,
    response_filter: str = "display",
) -> APIResponse:
    """Get account balance history over time.

    Args:
        date_from: Start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.sssZ)
        account_id: Account ID (integer) or 'summary' for aggregated data
        date_to: End date in ISO 8601 format (optional)
        response_filter: Response detail level ("full" or "display")

    Returns:
        Balance history data with timestamps, USD/BTC values, and deposit amounts.
    """
    # Validate inputs using Pydantic model
    request = GetBalanceHistoryRequest(
        account_id=account_id,
        date_from=date_from,
        date_to=date_to,
        response_filter=ResponseFilter(response_filter),
    )

    # Build endpoint with account ID
    endpoint = f"ver1/accounts/{request.account_id}/balance_chart_data"

    # Build query parameters
    params = request.to_query_params()

    # Make API request using existing authentication infrastructure
    response = await api_request(endpoint, method="GET", params=params)

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, request.response_filter)

    return response
