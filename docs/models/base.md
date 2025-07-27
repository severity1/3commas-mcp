# Base Models Documentation

This document provides reference documentation for base models and core data structures used throughout the 3Commas MCP server.

## Overview

Base models provide the foundation for all Pydantic validation and API interaction patterns in the 3Commas MCP server. These models ensure consistent configuration, validation, and type safety across all trading operations.

## Base Model Classes

### BaseModelConfig

**Purpose:** Foundation configuration for all Pydantic models in the project  
**Used by:** All models that require consistent configuration  
**Location:** `threecommas_mcp.models.base.BaseModelConfig`

**Configuration:**
- `populate_by_name=True`: Allow field population by alias name or field name
- `use_enum_values=True`: Use string values from enums instead of enum objects  
- `extra="ignore"`: Ignore extra fields in input data to prevent validation errors

**Usage Example:**
```python
from threecommas_mcp.models.base import BaseModelConfig

class MyTradingModel(BaseModelConfig):
    pair: str
    volume: Decimal
```

**Safety:** Base configuration ensures robust validation while remaining flexible for API variations

### APIRequest

**Purpose:** Base class for all API request models  
**Used by:** All tools that make API requests to 3Commas  
**Location:** `threecommas_mcp.models.base.APIRequest`  
**Extends:** BaseModelConfig

**Features:**
- Inherits all BaseModelConfig settings
- Provides consistent foundation for request validation
- Ensures uniform API request patterns

**Usage Example:**
```python
from threecommas_mcp.models.base import APIRequest
from decimal import Decimal

class CreateBotRequest(APIRequest):
    account_id: int
    pair: str
    base_order_volume: Decimal
    
    @validator('base_order_volume')
    def validate_volume(cls, v):
        if v <= 0:
            raise ValueError('Volume must be positive')
        return v
```

**Safety:** Provides foundation for comprehensive trading parameter validation

### APIResponse

**Purpose:** Type alias for all API response data  
**Used by:** All tools that return 3Commas API data  
**Location:** `threecommas_mcp.models.base.APIResponse`  
**Type:** `Dict[str, Any]`

**Description:** 
- Unvalidated dictionary containing API response data
- No validation performed on response structure
- Allows flexible handling of varying 3Commas response formats
- Response filtering applied before returning to users

**Usage Example:**
```python
from threecommas_mcp.models.base import APIResponse

async def get_bot_details(bot_id: str) -> APIResponse:
    """Get bot details from 3Commas API."""
    response = await api_client.get(f"/bots/{bot_id}")
    return response  # Raw dictionary from API
```

**Safety:** 
- Response filtering removes sensitive data (`url_secret`, `account_id`)
- No validation ensures compatibility with API changes
- Tools handle data extraction and validation as needed

## Common Enums

### BotType

**Purpose:** Defines available bot types for trading operations  
**Used by:** [DCA Bot Tools](../tools/dca_bots.md#get-dca-bot-details), Future Grid Bot Tools  
**Location:** `threecommas_mcp.models.base.BotType`

**Values:**
- `DCA = "Bot::DcaBot"`: Dollar Cost Averaging bot
- `GRID = "Bot::GridBot"`: Grid trading bot

**API Mapping:** Direct mapping to 3Commas bot type field
**Safety:** Prevents invalid bot type configurations

### DealStatus

**Purpose:** Defines deal lifecycle states for trading operations  
**Used by:** Future Deal Management Tools  
**Location:** `threecommas_mcp.models.base.DealStatus`

**Values:**
- `CREATED = "created"`: Deal created but not started
- `BASE_ORDER_PLACED = "base_order_placed"`: Base order placed on exchange
- `BOUGHT = "bought"`: Base order filled, waiting for profit target
- `CANCELLED = "cancelled"`: Deal cancelled before completion
- `COMPLETED = "completed"`: Deal completed successfully with profit
- `FAILED = "failed"`: Deal failed due to error
- `PANIC_SELL_PENDING = "panic_sell_pending"`: Panic sell order placed
- `PANIC_SELL_ORDER_PLACED = "panic_sell_order_placed"`: Panic sell active

**API Mapping:** Direct mapping to 3Commas deal status field
**Safety:** Enables proper deal state validation and risk assessment

### StrategyType

**Purpose:** Defines trading strategy directions  
**Used by:** Future Strategy Configuration Tools  
**Location:** `threecommas_mcp.models.base.StrategyType`

**Values:**
- `LONG = "long"`: Long positions (buy low, sell high)
- `SHORT = "short"`: Short positions (sell high, buy low)

**API Mapping:** Direct mapping to 3Commas strategy type field
**Safety:** Prevents invalid strategy direction configurations

## Type Variables

### ReqT

**Purpose:** Generic type variable for API request models  
**Used by:** Generic functions that work with multiple request types  
**Location:** `threecommas_mcp.models.base.ReqT`  
**Bound:** APIRequest

**Usage Example:**
```python
from typing import TypeVar
from threecommas_mcp.models.base import ReqT

async def validate_request(request: ReqT) -> ReqT:
    """Generic request validation."""
    # Validation logic applies to any APIRequest subclass
    return request
```

## Model Patterns

### Validation Patterns

**Trading Parameter Validation:**
```python
from decimal import Decimal
from pydantic import validator
from threecommas_mcp.models.base import APIRequest

class TradingRequest(APIRequest):
    volume: Decimal
    safety_orders: int
    
    @validator('volume')
    def validate_volume(cls, v):
        if v <= 0:
            raise ValueError('Volume must be positive')
        return v
    
    @validator('safety_orders')
    def validate_safety_orders(cls, v):
        if not 0 <= v <= 10:
            raise ValueError('Safety orders must be between 0 and 10')
        return v
```

**Enum Field Patterns:**
```python
from threecommas_mcp.models.base import APIRequest, BotType, StrategyType

class BotConfigRequest(APIRequest):
    bot_type: BotType = BotType.DCA
    strategy_type: StrategyType = StrategyType.LONG
```

### API Integration Patterns

**Request/Response Pattern:**
```python
from threecommas_mcp.models.base import APIRequest, APIResponse

class GetBotRequest(APIRequest):
    bot_id: str
    include_events: bool = False

async def get_bot_details(request: GetBotRequest) -> APIResponse:
    # API call implementation
    return response_data
```

## Cross-References

### Integration with Other Documentation Layers
- **Tools Documentation:** [DCA Bot Tools](../tools/dca_bots.md) - Uses APIResponse type
- **Conversation Examples:** [DCA Bot Management](../conversations/dca-bot-management-conversation.md) - Shows model usage
- **Code Implementation:** `threecommas_mcp/models/base.py` - Actual model definitions
- **API Reference:** [3Commas API Documentation](https://developers.3commas.io) - Source of truth for field mappings

### Model Relationships
- **BaseModelConfig** → All domain-specific models (bots, deals, strategies)
- **APIRequest** → All tool request models
- **APIResponse** → All tool return types
- **Common Enums** → Domain models and validation logic

## Development Guidelines

### Adding New Base Models
When extending base model functionality:
1. **Inherit from BaseModelConfig** for consistent configuration
2. **Include comprehensive validation** for trading safety
3. **Document API mappings** to 3Commas fields
4. **Add safety considerations** for trading operations
5. **Update this documentation** with new patterns

### Validation Best Practices
- **Trading Safety First:** Validate all trading parameters comprehensively
- **Clear Error Messages:** Provide actionable validation error messages
- **Range Validation:** Include min/max validation for numerical trading parameters
- **Required Fields:** Mark essential trading parameters as required
- **Default Values:** Provide safe defaults for optional parameters

## Trading Safety Considerations

### Parameter Validation
- **Volume Validation:** Ensure positive volumes and reasonable minimums
- **Safety Order Limits:** Validate safety order counts within reasonable ranges
- **Account Validation:** Verify account permissions before bot operations
- **Pair Validation:** Ensure trading pairs are valid and available

### Risk Assessment
- **Risk Level:** Low - Base models provide validation foundation only
- **Trading Impact:** None - Models only validate request parameters
- **Account Safety:** Comprehensive validation prevents invalid configurations
- **Data Privacy:** No sensitive data stored in model definitions

### Error Handling
- **Validation Errors:** Clear messages with trading context
- **Type Errors:** Descriptive errors for incorrect parameter types
- **Range Errors:** Specific guidance for out-of-range trading parameters
- **Required Field Errors:** Clear indication of missing required parameters

This base model documentation provides the foundation for understanding data validation and type safety throughout the 3Commas MCP server, ensuring safe and reliable trading operations.