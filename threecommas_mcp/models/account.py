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


class GetBalanceHistoryRequest(APIRequest):
    """Request parameters for balance history data retrieval."""

    account_id: Union[str, int] = Field(
        default="summary",
        description="Account ID or 'summary' for aggregated data from all accounts",
    )
    date_from: str = Field(
        description="Start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.sssZ)",
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$",
    )
    date_to: Optional[str] = Field(
        default=None,
        description="End date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.sssZ)",
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$",
    )
