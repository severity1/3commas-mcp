# CLAUDE.md for tools/

This file provides guidance for MCP tool implementations that expose 3Commas API functionality to AI assistants.

## Context Activation
This guidance activates when:
- Working in `3commas_mcp/tools/` directory
- Reading/editing tool implementation files (*.py)
- Implementing MCP functions for 3Commas API (DCA bots, strategies, deals)
- Adding new tool domains or expanding existing trading tools

**Companion directories**: models/ (for validation), utils/ (for utilities), api/ (for client)

## Tool Architecture

### Directory Structure
- **__init__.py**: Tool registration and imports
- **Domain modules**: Bots (DCA/Grid), strategies, deals, accounts, pairs, safety orders, portfolio

### Implementation Standards
- **Consistent patterns**: All tools follow standardized implementation patterns for trading operations
- **Error handling**: Use @handle_api_errors decorator for consistent error management
- **Async patterns**: All API functions are async using httpx
- **Parameter validation**: Use Pydantic models for input validation with trading safety checks

## Tool Organization

### Operation Categories
- **CRUD**: create_*, get_*, update_*, delete_* operations for bots, strategies, deals
- **List**: list_* operations with filtering and pagination for trading data
- **Actions**: enable_*, disable_*, cancel_*, clone_* state changes for bots/deals
- **Specialized**: Trading-specific operations (panic_sell, add_safety_order, strategy_config)

### File Organization Rules
- **Add to existing**: Tool fits domain and file has < 12 functions (trading complexity)
- **Create new file**: New domain OR existing file ≥ 12 functions
- **Split file**: When file exceeds 15 functions, split by logical sub-domains
- **Domain boundaries**: Create new domain for ≥ 4 conceptually distinct tools
- **Naming**: Use singular form matching 3Commas API domain (e.g., bot.py, deal.py)

### Registration Classification
- **Non-destructive**: get_*, list_*, create_*, update_* (basic registration)
- **Destructive**: delete_*, force_*, disable_* affecting active trading (conditional)
- **Potentially destructive**: cancel_*, panic_sell*, clone_* operations (case-by-case)

## Decision Matrices

### When to Create New File vs Add to Existing
| Scenario | New File | Add to Existing |
|----------|----------|-----------------|
| New API domain (≥4 conceptually distinct tools) | ✅ | ❌ |
| Existing file has ≥12 functions | ✅ | ❌ |
| Tool fits existing domain + file <12 functions | ❌ | ✅ |
| Existing file will exceed 15 functions | ✅ Split by sub-domains | ❌ |

### Tool Registration Decision Matrix
| Operation Type | Examples | Registration | Reason |
|----------------|----------|-------------|---------|
| Non-destructive | get_*, list_*, create_*, update_* | Basic | Safe operations |
| Destructive | delete_*, disable_*, force_* | Conditional | Affects active trading |
| Potentially destructive | cancel_*, panic_sell*, clone_* | Case-by-case | Context-dependent trading impact |

### Function Signature Pattern Decision
| Parameter Count | Structure | Example |
|-----------------|-----------|---------|
| 1-2 required | Direct parameters | `get_bot_details(bot_id)` |
| 3+ required | Routing + individual + params | `create_dca_bot(account_id, pair, params)` |
| 5+ optional | Use params object | `update_bot_config(bot_id, params)` |
| <5 optional | Direct parameters | `list_bots(account_id, search, page)` |

## Implementation Requirements

### Essential Patterns
1. Use @handle_api_errors decorator for consistent error handling
2. Create corresponding Pydantic models for validation with trading safety checks
3. Follow function signature pattern: (required_routing_params, required_trading_params, optional_params_object)
4. Use utility functions for payload creation and parameter handling:
   - `create_api_payload()` for 3Commas API compliant payload creation
   - `query_params()` for transforming Pydantic models to API parameters
   - `validate_trading_params()` for bot/strategy parameter validation
5. Document thoroughly with 3Commas API endpoint references
6. Register appropriately in server.py based on trading destructiveness

### Function Signature Patterns

Tool functions follow a consistent parameter structure adapted for trading operations.

**Parameter Order:**
1. **Required routing parameters** (bot_id, account_id, deal_id, etc.)
2. **Required trading parameters** (pair, strategy, base_order_volume, etc.)
3. **Optional params object** for additional configuration

### Trading Safety Requirements
- **Bot Creation**: Validate pair availability, account permissions, and strategy parameters
- **Bot Modification**: Ensure bot is in safe state for modifications
- **Deal Operations**: Include safety checks for active deals before cancellation
- **Strategy Changes**: Validate strategy parameters against 3Commas requirements
- **Destructive Operations**: Require explicit confirmation flags

### Query Parameter Pattern
For list operations with filtering/pagination, use `query_params()` utility. Adapt patterns for 3Commas filtering (account_id, pair, strategy, status).

### Documentation Integration
- Reference API_REFERENCES.md for official 3Commas API groupings
- Create usage examples in docs/tools/ with trading scenarios
- Link to model definitions and conversation examples
- Include safety warnings for destructive operations

## Development Standards

### Quality Checks
- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type Check**: `mypy .`
- **Test**: `pytest`

### Code Style Requirements
- Use @handle_api_errors decorator for all API functions
- Follow (required_routing_params, required_trading_params, optional_params_object) signature pattern
- Apply async patterns with httpx for all API calls
- Use Pydantic models for input validation with trading safety
- Apply comprehensive testing: Happy path → Edge cases → Error cases → Trading safety scenarios

### Model Integration
When working with models:
- Create corresponding Pydantic models for all tool parameters with trading validation
- Use model validation for input parameters with safety checks
- Follow field naming conventions (snake_case for Python, API naming for 3Commas)
- Apply proper type hints and validation rules for trading data

### Utility Function Usage
Essential utility functions for tool implementation:
- `create_api_payload()`: For 3Commas API compliant payload creation
- `query_params()`: For transforming Pydantic models to API parameters
- `@handle_api_errors`: Decorator for consistent error handling
- `validate_trading_safety()`: Trading-specific validation functions

## Implementation Workflow

### New Tool Development Process
1. **Define function signature**: Follow parameter order pattern for trading operations
2. **Create Pydantic models**: For validation and type safety with trading checks
3. **Implement core logic**: Using utility functions and decorators
4. **Add error handling**: Apply @handle_api_errors decorator with trading context
5. **Add safety checks**: Validate trading parameters and account permissions
6. **Register in server.py**: Based on trading destructiveness classification
7. **Test thoroughly**: Cover happy path, edge cases, error conditions, and trading safety
8. **Update documentation**: TASKS.md, API_REFERENCES.md status updates

### Quality Validation Checklist
For each tool implementation:
- [ ] Function follows Essential Patterns (decorator, models, utilities)
- [ ] Pydantic models created and validated with trading safety checks
- [ ] Trading safety requirements implemented (bot validation, account checks)
- [ ] Tool registered in server.py with appropriate destructiveness classification
- [ ] Quality checks passed: format, lint, type check
- [ ] Documentation updated: implementation status tracking
- [ ] Tests cover all scenarios: success, edge cases, errors, trading safety

### 3Commas-Specific Tool Patterns
- **Bot Management**: Always include account_id validation and bot status checks
- **Deal Operations**: Validate deal state before modifications
- **Strategy Configuration**: Include strategy parameter validation against 3Commas requirements
- **Account Operations**: Verify exchange account permissions and connectivity
- **Safety Orders**: Include deal volume and account balance validation