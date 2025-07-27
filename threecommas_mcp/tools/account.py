"""Account management tools for 3Commas MCP

This module implements account-related endpoints of the 3Commas API.
Reference: https://developers.3commas.io/account
"""

from ..api.client import api_request
from ..utils.decorators import handle_api_errors
from ..utils.response_filter import filter_response
from ..models.base import APIResponse


@handle_api_errors
async def get_connected_exchanges_and_wallets(
    response_filter: str = "display",
) -> APIResponse:
    """Get list of connected exchanges and wallets.

    Retrieves all connected exchange accounts and wallet information for the user.
    This provides core account information needed for trading operations, including
    exchange names, account types, trading permissions, and connection status.

    API endpoint: GET /ver1/accounts
    Security: SIGNED (requires API key + HMAC signature)
    Permission: ACCOUNTS_READ

    Args:
        response_filter: Filter type for response ("full" or "display", default: "display")

    Returns:
        List of connected exchanges and wallets including:
        - Exchange names and account IDs
        - Account types (spot, futures, etc.)
        - Trading permissions and status
        - Connection health and configuration
        - Available balance summaries

    Raises:
        ValueError: If response_filter is invalid
        APIError: If API request fails or access denied

    See:
        docs/tools/account.md#get-connected-exchanges-and-wallets for usage examples
    """
    # Make API request using existing authentication infrastructure
    response = await api_request("ver1/accounts", method="GET")

    # Apply response filtering for token efficiency
    if isinstance(response, dict) and "error" not in response:
        response = filter_response(response, response_filter)

    return response
