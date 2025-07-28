"""Account models for 3Commas MCP.

This module defines Pydantic models for account-related API requests.
These models provide validation for account management operations.

Reference: https://developers.3commas.io/account
"""

from .base import APIRequest


class GetConnectedExchangesRequest(APIRequest):
    """Request model for getting connected exchanges and wallets.

    This is a simple request model for the get_connected_exchanges_and_wallets
    endpoint. No parameters are required for this endpoint.

    API Mapping:
        No parameters required for this endpoint

    API Endpoint: GET /ver1/accounts
    Reference: https://developers.3commas.io/account/list-of-connected-exchanges-and-wallets

    See:
        docs/models/account.md#get-connected-exchanges-request for reference
    """

    pass  # No parameters required for this endpoint
