# CLAUDE.md for models/

## Context Activation
**Triggers**: Creating Pydantic validation models for 3Commas API structures
**Usage**: Referenced during root CLAUDE.md step 2 (model creation)

## Required Model Structure
1. **Class Definition**
   ```python
   class ModelNameRequest(APIRequest):
       """Brief description of API endpoint and purpose.
       
       API Mapping:
           Endpoint: /api/ver1/endpoint_name
           Method: GET/POST
           Authentication: Required
       """
   ```

2. **Field Validation Pattern**
   ```python
   field_name: str = Field(
       description="Clear description of field purpose and constraints",
       example="example_value"
   )
   
   optional_field: Optional[int] = Field(
       default=None,
       description="Optional field description"
   )
   ```

3. **Required Inheritance**
   ```python
   from .base import APIRequest
   
   class YourModel(APIRequest):
       # APIRequest provides response_filter automatically
   ```

## Available Base Components
- **APIRequest**: Base class with response_filter support
- **ResponseFilter**: DISPLAY/FULL enum for token optimization  
- **Common Enums**: BotType, DealStatus, StrategyType, LimitType, MarketCode

## Reference Examples
- **Complete model**: dca_bots.py:13 (GetDCABotDetailsRequest)

## Documentation Requirements
After implementation, follow root CLAUDE.md step 6 for documentation workflow.