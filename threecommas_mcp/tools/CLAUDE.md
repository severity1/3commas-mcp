# CLAUDE.md for tools/

## Context Activation
Activates when working in `tools/` directory implementing MCP functions for 3Commas API.

**Companions**: models/ (validation), utils/ (auth/errors), api/ (HTTP client)

## Decision Matrices

### File Organization
| Scenario | Action |
|----------|--------|
| Tool fits domain + file <12 functions | Add to existing |
| New domain OR file ≥12 functions | Create new file |
| File exceeds 15 functions | Split by sub-domains |

### Tool Registration
| Operation Type | Examples | Registration |
|----------------|----------|-------------|
| Non-destructive | get_*, list_*, create_*, update_* | Basic |
| Destructive | delete_*, disable_*, force_* | Conditional |
| Potentially destructive | cancel_*, panic_sell* | Case-by-case |

### Function Signatures
| Parameter Count | Pattern | Example |
|-----------------|---------|---------|
| 1-2 required | Direct | `get_bot_details(bot_id)` |
| 3+ required | Routing + trading + params | `create_dca_bot(account_id, pair, params)` |
| 5+ optional | Use params object | `update_bot_config(bot_id, params)` |

## Implementation Requirements

### Essential Patterns
1. Use `@handle_api_errors` decorator
2. Include `response_filter` parameter ("full"|"display", default: "display")
3. Create Pydantic models for validation
4. **Pass response_filter string directly to model** (no enum conversion)
5. Follow signature: (routing_params, trading_params, optional_params)
6. Apply trading safety validation before destructive operations

**Pattern Reference**: See `docs/PATTERNS.md` for complete implementation templates

### Trading Safety
- **Bot operations**: Validate config and account permissions
- **Deal operations**: Check deal state before modifications
- **Destructive operations**: Require explicit confirmation flags

## Development Workflow

### Implementation Steps
1. Define signature with response_filter parameter
2. Create Pydantic models with trading validation
3. Implement with `@handle_api_errors` and safety checks
4. **Pass response_filter string directly to model** (simplified validation)
5. Apply `filter_response()` before returning
6. Register based on destructiveness classification
7. Test: success, errors, trading safety scenarios

**Quick Start**: Copy template from `docs/PATTERNS.md` for new API implementation

### Quality Checklist
- [ ] Uses `@handle_api_errors` decorator
- [ ] Includes `response_filter` parameter (default: "display")
- [ ] Pydantic models with trading safety validation
- [ ] Registered with appropriate destructiveness level
- [ ] Tests cover safety scenarios and filter types

## Progress Tracking Requirements

### Always Update After Implementation
When implementing any tool function, **MUST** update these tracking files:

1. **TASKS.md**: Update API status from ⏸️ to ✅ in MVP phase tables
2. **docs/MVP_GET_APIS.md**: Mark completed in implementation priority tables
3. **docs/API_REFERENCES.md**: Update status marker for implemented API

### MVP GET APIs Priority
Follow the implementation order defined in `docs/MVP_GET_APIS.md`:
- **Phase 1**: Foundation APIs (4 APIs) - Highest priority
- **Phase 2**: Bot Management APIs (8 APIs) - Core user value
- **Phase 3**: Account & Trading Data (12 APIs) - Management features
- **Phase 4**: Advanced Analytics (11 APIs) - Detailed insights

### Implementation Pattern Reference
All GET APIs should follow the `get_dca_bot_details` pattern established in this module.