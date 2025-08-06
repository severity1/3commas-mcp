# Model Patterns

**Context**: Pydantic validation models for 3Commas API structures

## Component Focus
- **Pydantic class structure** - APIRequest inheritance and field definitions
- **Field validation** - Comprehensive constraints using Field()
- **Inheritance** - Base class integration for common functionality

## Required Patterns
1. **Inherit from APIRequest** - Automatic response_filter field
2. **Use Field() validation** - Comprehensive constraints and examples
3. **Script-validated parameters** - Use exact API parameter names
4. **Trading safety validation** - Appropriate constraints for trading operations

## Available Components
- **APIRequest**: Base class with response_filter
- **ResponseFilter**: DISPLAY/FULL enum 
- **Enums**: StrategyType, LimitType, MarketCode

## Pattern Example
```python
from .base import APIRequest

class GetDataRequest(APIRequest):
    """Request parameters for data retrieval."""
    
    param_name: str = Field(..., description="Parameter description")
```