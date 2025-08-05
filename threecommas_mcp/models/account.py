"""Account models for 3Commas MCP.

This module defines Pydantic models for account-related API requests.
These models provide validation for account management operations.

Reference: https://developers.3commas.io/account
"""

from typing import Optional, Union
from pydantic import Field
from .base import APIRequest


class GetConnectedExchangesRequest(APIRequest):
    """Request parameters for connected exchanges and wallets retrieval."""

    pass  # No parameters required for this endpoint


class GetAccountInfoRequest(APIRequest):
    """Request parameters for account information retrieval."""

    account_id: Optional[Union[str, int]] = Field(
        default="summary",
        description="Account ID or 'summary' for aggregated data from all accounts",
    )
