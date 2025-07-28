# CLAUDE.md for models/

## Context Activation
Activates when working in `models/` directory creating Pydantic validation for 3Commas API structures.

**Companions**: tools/ (usage), api/ (requests), utils/ (validation helpers)

## Decision Matrices

### File Organization
| Scenario | Action |
|----------|--------|
| Model fits domain + file <10 models | Add to existing |
| New domain OR file ≥10 models | Create new file |
| File exceeds 12 models | Split by sub-domains |

### Model Categories
| Domain | Focus | Examples |
|--------|-------|----------|
| Bot Models | Configuration, status | DCABotConfig, BotStatus |
| Strategy Models | Trading strategies | QFLStrategy, RSIStrategy |
| Deal Models | Deal management | DealConfig, SafetyOrderConfig |
| Account Models | Exchange accounts | AccountConfig, AccountBalance |
| Market Models | Trading pairs, rates | TradingPair, CurrencyRates |

## Implementation Requirements

### Essential Patterns
1. **Inherit from `APIRequest`** (not BaseModel) - Automatic response_filter field
2. Use Pydantic validators for trading parameters
3. Include API field mappings to 3Commas structure
4. Apply comprehensive trading safety validation
5. Use `Decimal` for all financial values

**Pattern Reference**: See `docs/PATTERNS.md` for complete model implementation templates

### Trading Validation
- **Bot configuration**: Validate volumes, safety orders, strategy params
- **Account validation**: Verify permissions and trading capabilities
- **Pair validation**: Check against account permissions and market availability
- **Deal validation**: Validate parameters and safety order configurations

### Field Mapping Pattern
```python
class DCABotConfig(BaseModel):
    account_id: int  # -> account_id
    pair: str        # -> pair
    base_order_volume: Decimal  # -> base_order_volume
    
    @validator('base_order_volume')
    def validate_volume(cls, v):
        if v <= 0:
            raise ValueError('Volume must be positive')
        return v
```

## Development Workflow

### Implementation Steps
1. Analyze 3Commas API documentation for field requirements
2. Create BaseModel with proper field definitions and types
3. Add trading-specific validation using Pydantic validators
4. Document field mappings to 3Commas API structure
5. Test with valid/invalid trading scenarios

### Quality Checklist
- [ ] Extends BaseModel with comprehensive type hints
- [ ] Trading parameter validation using Pydantic validators
- [ ] Field mappings to 3Commas API documented
- [ ] Comprehensive docstrings with trading context
- [ ] Tests cover validation scenarios: valid, invalid, edge cases