# Account Models

This document describes the Pydantic models used for account management operations in the 3Commas MCP server.

## Overview

Account models provide validation and structure for account-related API requests and responses. These models ensure data integrity and provide clear documentation of expected data formats for account operations.

## Models

### ConnectedExchange

**Purpose:** Model representing a connected exchange account as returned by the 3Commas API.

**Used by:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Fields:**
- `id: int` - Exchange account unique identifier
- `name: str` - Exchange name (binance, okx, etc.)
- `account_name: Optional[str]` - User-defined account name
- `market_code: str` - Market code for the exchange
- `is_locked: bool` - Whether account is locked (default: False)
- `created_at: Optional[str]` - Account creation timestamp
- `updated_at: Optional[str]` - Last update timestamp

**API Mapping:**
- `id` -> `account_id`
- `name` -> `exchange_name`
- `account_name` -> `user_defined_name`
- `market_code` -> `exchange_market_code`

**Validation Rules:**
- Exchange name cannot be empty and is normalized to lowercase
- Market code cannot be empty and is normalized to lowercase
- All string fields are stripped of whitespace

**Safety:** Model includes validation to ensure exchange account data integrity and prevent configuration errors.

**Example:**
```python
exchange = ConnectedExchange(
    id=12345,
    name="binance",
    account_name="Main Trading Account",
    market_code="binance",
    is_locked=False
)
```

### ExchangeBalance

**Purpose:** Model representing balance data for a connected exchange account.

**Used by:** Balance components within exchange account data

**Fields:**
- `currency_code: str` - Currency symbol (BTC, USDT, etc.)
- `total_balance: Decimal` - Total balance (default: 0)
- `available_balance: Decimal` - Available for trading (default: 0)
- `reserved_balance: Decimal` - Reserved in orders (default: 0)
- `usd_value: Optional[Decimal]` - USD equivalent value

**API Mapping:**
- `currency_code` -> `currency`
- `total_balance` -> `total`
- `available_balance` -> `available`
- `reserved_balance` -> `reserved`

**Validation Rules:**
- Currency code cannot be empty and is normalized to uppercase
- All balance values must be non-negative
- Uses Decimal type for precise financial calculations

**Safety:** Ensures accurate financial data representation and prevents negative balance errors.

**Example:**
```python
balance = ExchangeBalance(
    currency_code="BTC",
    total_balance=Decimal("1.5"),
    available_balance=Decimal("1.2"),
    reserved_balance=Decimal("0.3"),
    usd_value=Decimal("67500.00")
)
```

### GetConnectedExchangesRequest

**Purpose:** Request model for the get_connected_exchanges_and_wallets endpoint.

**Used by:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Fields:** No parameters required for this endpoint.

**Validation:** Inherits from BaseModelConfig for consistent configuration.

**Safety:** Simple model with no parameters, ensuring safe endpoint access.

## Validation Patterns

### Financial Data Validation
All balance-related fields use `Decimal` type for precise financial calculations:
```python
@validator('total_balance', 'available_balance', 'reserved_balance')
def validate_balance_positive(cls, v):
    if v < 0:
        raise ValueError("Balance values must be non-negative")
    return v
```

### String Field Normalization
Exchange and currency identifiers are normalized for consistency:
```python
@validator('currency_code')
def validate_currency_code(cls, v):
    if not v or not v.strip():
        raise ValueError("Currency code cannot be empty")
    return v.strip().upper()
```

## Trading Safety Considerations

- **Financial Precision:** All monetary values use Decimal type to prevent floating-point errors
- **Data Validation:** Strict validation prevents invalid account configurations
- **Credential Security:** Models do not store or validate API credentials directly
- **Exchange Compatibility:** Validation ensures exchange names match supported markets

## Integration Examples

### Account Validation
```python
# Validate exchange account data before using for bot configuration
try:
    exchange = ConnectedExchange(**api_response_data)
    if exchange.is_locked:
        raise ValueError("Cannot use locked exchange account")
except ValidationError as e:
    logger.error(f"Invalid exchange data: {e}")
```

### Balance Checking
```python
# Validate balance data for trading decisions
try:
    balance = ExchangeBalance(**balance_data)
    if balance.available_balance < minimum_required:
        raise ValueError("Insufficient available balance for trading")
except ValidationError as e:
    logger.error(f"Invalid balance data: {e}")
```

## Related Documentation

- **Tools:** [Account Management Tools](../tools/account.md) - Functions using these models
- **Base Models:** [Base Models](base.md) - Common model patterns and configuration
- **API Reference:** [3Commas Account API](https://developers.3commas.io/account)
- **Conversations:** [Account Management Examples](../conversations/account-management-conversation.md)