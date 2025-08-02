"""Account models for 3Commas MCP.

This module defines Pydantic models for account-related API requests.
These models provide validation for account management operations.

Reference: https://developers.3commas.io/account
"""

from .base import APIRequest


class GetConnectedExchangesRequest(APIRequest):
    """Request parameters for connected exchanges and wallets retrieval."""

    pass  # No parameters required for this endpoint
