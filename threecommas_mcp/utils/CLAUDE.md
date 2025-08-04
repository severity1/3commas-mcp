# Utility Usage Patterns

**Context**: Authentication, error handling, and validation utilities  
**When to Use**: Throughout Root CLAUDE.md Phase 2 implementation as needed

## Required Usage Patterns
1. **Error Handling Decorator**
   ```python
   from ..utils.decorators import handle_api_errors
   
   @handle_api_errors
   async def your_function():
       # Automatically handles API errors with consistent formatting
       # Returns: {"error": "message"} on failure
   ```

2. **Response Filtering**
   ```python
   from ..utils.response_filter import filter_response
   
   # Always filter responses before returning
   filtered_data = filter_response(api_response, response_filter)
   # - Security: Removes url_secret, account_id
   # - Display: Removes crypto_widget, reduces arrays (85% token reduction)
   ```

3. **Authentication Integration**
   ```python
   # Authentication handled automatically via api_request()
   # Never manually implement HMAC-SHA256 signing
   response = await api_request("endpoint", params)
   ```

## Available Utilities
- **Error Handling**: Consistent `{"error": "message"}` formatting, security-safe
- **Response Filtering**: Security + display filtering with token optimization
- **Rate Limiting**: Global (100/min), Deals (120/min), SmartTrades (40/10s)
- **Authentication**: HMAC-SHA256 via api_request() integration

## Reference Examples
- **Complete decorator usage**: decorators.py:11 (handle_api_errors)
- **Response filtering**: response_filter.py:13 (filter_response)

## Integration Notes
- All tools must use @handle_api_errors decorator
- Always apply filter_response() before returning data
- Authentication handled automatically via api_request()