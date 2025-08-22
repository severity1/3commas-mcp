# Model Patterns

**Context**: Pydantic models for 3Commas API request validation with trading safety

## Component Focus
- **APIRequest inheritance** - Automatic response_filter field from base.py
- **Field validation** - Comprehensive constraints with Field() descriptors  
- **Enum integration** - StrategyType, ResponseFilter, LimitType from base.py

## Required Patterns
1. **Inherit from APIRequest** - Gets response_filter field automatically
2. **Use Field() with constraints** - Include ge, le, regex for validation
3. **Import enums from base** - Use StrategyType, ResponseFilter consistently
4. **Script-validated parameters** - Use exact names from test_api.py results

## Available Components
- **APIRequest**: Base with response_filter and to_query_params()
- **ResponseFilter**: DISPLAY/FULL enum for token optimization
- **StrategyType**: long/short enum for trading strategies
- **BaseModelConfig**: Standard Pydantic configuration

## Code Examples
```python
from .base import APIRequest, StrategyType, ResponseFilter
from pydantic import Field

class GetDCABotListRequest(APIRequest):
    """Request parameters for DCA bot list retrieval."""
    
    account_id: int = Field(default=0, ge=0, description="Account ID")
    strategy: StrategyType | None = Field(default=None, description="Trading strategy")
    limit: int = Field(default=50, ge=1, le=1000, description="Results limit")
```

## Integration Requirements
- All request models inherit from APIRequest
- Use Field() validation for all parameters with appropriate constraints
- Import and use enums from base.py for type safety
- Docstring format: "Request parameters for [domain] [action]"