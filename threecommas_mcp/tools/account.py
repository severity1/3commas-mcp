"""Account management tools for 3Commas MCP

This module implements account-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/account
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse, ResponseFilter
from ..models.account import GetConnectedExchangesRequest


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
