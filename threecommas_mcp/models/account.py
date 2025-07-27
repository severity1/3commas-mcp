"""Account models for 3Commas MCP.

This module defines Pydantic models for account-related API requests.
These models provide validation for account management operations.

Reference: https://developers.3commas.io/account
"""

from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseModelConfig


class ConnectedExchange(BaseModel):
    """Model representing a connected exchange account.

    This model represents the structure of a connected exchange account
    as returned by the 3Commas API. Used for validation and documentation
    of exchange account data.

    API Mapping:
        id -> account_id
        name -> exchange_name
        account_name -> user_defined_name
        market_code -> exchange_market_code

    See:
        docs/models/account.md#connected-exchange for reference
    """

    id: int = Field(
        ..., ge=1, description="Exchange account unique identifier (positive integer)"
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Exchange name (e.g., 'binance', 'okx', 'bybit')",
        examples=["binance", "okx", "bybit_spot"],
    )
    account_name: Optional[str] = Field(
        None, max_length=100, description="User-defined account name for identification"
    )
    market_code: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Exchange market code identifier",
        examples=["binance", "okex", "bybit_spot"],
    )
    is_locked: bool = Field(
        default=False, description="Whether account is locked for trading operations"
    )
    created_at: Optional[str] = Field(
        None, description="Account creation timestamp (ISO format)"
    )
    updated_at: Optional[str] = Field(
        None, description="Last update timestamp (ISO format)"
    )


class ExchangeBalance(BaseModel):
    """Model representing exchange account balance information.

    This model represents balance data for a connected exchange account.
    Used for tracking available funds and trading capacity.

    API Mapping:
        currency_code -> currency
        total_balance -> total
        available_balance -> available
        reserved_balance -> reserved

    See:
        docs/models/account.md#exchange-balance for reference
    """

    currency_code: str = Field(
        ...,
        min_length=1,
        max_length=10,
        pattern=r"^[A-Z0-9]+$",
        description="Currency symbol in uppercase (e.g., 'BTC', 'USDT', 'ETH')",
        examples=["BTC", "USDT", "ETH", "BNB"],
    )
    total_balance: Decimal = Field(
        default=Decimal("0"), ge=0, description="Total balance amount for this currency"
    )
    available_balance: Decimal = Field(
        default=Decimal("0"),
        ge=0,
        description="Available balance for trading operations",
    )
    reserved_balance: Decimal = Field(
        default=Decimal("0"), ge=0, description="Balance reserved in active orders"
    )
    usd_value: Optional[Decimal] = Field(
        None, ge=0, description="USD equivalent value of the balance"
    )


class GetConnectedExchangesRequest(BaseModelConfig):
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
