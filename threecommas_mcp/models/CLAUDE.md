# Pydantic Model Creation Patterns

**Context**: Pydantic validation models for 3Commas API structures  
**When to Use**: During Root CLAUDE.md Phase 2 implementation, after script validation

## Model Creation Based on Script Output
1. **Class Definition** (using exact API mapping from scripts):
   ```python
   class ModelNameRequest(APIRequest):
       """Brief description based on script testing results.
       
       Script Validation:
           Tested: python scripts/test_api.py ver1/endpoint/<param>
           Response: <key_fields_from_script_output>
           Tokens: <count_from_script> (must be <25,000)
       
       API Mapping:
           Endpoint: /ver1/endpoint/<param>  # Exact format from scripts
           Method: GET
           Authentication: SIGNED
       """
   ```

2. **Field Definition** (using parameter names from script testing):
   ```python
   # Use EXACT parameter names from script output, not documentation
   account_id: str = Field(
       description="Account ID confirmed working in script test",
       example="31337503"  # Real working value from testing
   )
   
   # Only include optional fields that script testing confirmed work
   optional_param: Optional[bool] = Field(
       default=None,
       description="Optional parameter validated in script testing"
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

## Integration Notes
- Use exact parameter names from Root CLAUDE.md Phase 1 script testing
- All models inherit from APIRequest base class
- Return to Root CLAUDE.md for Phase 3 (documentation) after implementation