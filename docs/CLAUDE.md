# CLAUDE.md for docs/

This file provides guidance about the documentation structure and standards for 3Commas trading contexts.

## Context Activation
This guidance activates when:
- Working in `docs/` directory
- Creating/editing documentation files (*.md)
- Implementing multi-layer documentation structure for trading operations
- Adding cross-references or updating documentation standards

**Companion directories**: All component directories (tools/, models/, utils/, api/)

## Documentation Architecture

### Core Files
- **DEVELOPMENT.md**: Development standards and comprehensive build/quality guidance for 3Commas
- **CONTRIBUTING.md**: Contributing guidelines and PR process with trading safety focus
- **README.md**: Documentation directory overview for trading contexts
- **API_REFERENCES.md**: 3Commas API reference links and implementation status

### Multi-Layer Structure
Documentation follows a consistent 4-layer pattern for each trading domain:

1. **conversations/**: Real-world trading usage examples and interaction patterns
2. **models/**: Pydantic model documentation with trading validation rules and API mappings
3. **tools/**: API tool reference with signatures, parameters, and trading safety scenarios
4. **Code docstrings**: Implementation-level documentation with cross-references

## Documentation Standards

### Core Principles
- **Consistency**: Each trading domain has documentation across all 4 layers
- **Trading-focused**: Reference actual trading scenarios rather than generic examples
- **Cross-referenced**: All layers link to related documentation with trading context
- **API-aligned**: Include 3Commas API documentation references and trading requirements

### Quality Requirements
- Document trading parameters, return types, and safety handling
- Organize examples from basic bot operations to advanced trading strategies
- Use consistent anchor names (#lowercase-with-hyphens)
- Maintain valid cross-references with relative paths
- Include trading safety warnings and risk management guidance

## New Tool Documentation Workflow

### Implementation Steps
1. **Model Documentation**: Create `docs/models/{domain}.md` with trading validation rules and API mappings
2. **Tool Documentation**: Create `docs/tools/{domain}.md` with function signatures and trading examples
3. **Conversation Examples**: Create `docs/conversations/{domain}-conversation.md` with trading scenarios
4. **Cross-References**: Link all layers bidirectionally with trading context
5. **Integration**: Update `docs/README.md` and relevant CLAUDE.md files

### Cross-Reference Requirements
Every new tool must maintain bidirectional links across all 4 layers:
- **Code docstrings** → docs/tools/ sections with trading context
- **docs/tools/** ↔ docs/models/ (bidirectional) with validation cross-references
- **docs/tools/** → docs/conversations/ trading examples
- **docs/models/** → tools that use the model for trading operations
- **docs/conversations/** → specific tool and model sections with trading scenarios

### Validation Checklist
- [ ] All markdown links use relative paths
- [ ] Cross-references use consistent anchor names (#lowercase-with-hyphens)
- [ ] Each layer references appropriate related layers with trading context
- [ ] All links are valid and accessible
- [ ] Trading safety warnings included where appropriate

## Development Standards

### Quality Checks
- **Format**: `ruff format .`
- **Lint**: `ruff check .`
- **Type Check**: `mypy .`
- **Test**: `pytest`

### Documentation Quality Standards
- Setup and quality check sequences for trading contexts
- Comprehensive validation process for all documentation layers
- KISS/DRY principles applied to documentation structure
- Error handling patterns documented consistently
- Trading safety patterns and risk management guidance

### AI Documentation Guidelines
- Maintain consistency with existing documentation patterns
- Reference actual trading implementation rather than duplicate examples
- Ensure examples include proper trading safety handling
- Keep examples concise but comprehensive for trading scenarios
- Follow cross-reference requirements for all layers
- Include trading context and safety warnings where appropriate

## Implementation Workflow

### New Documentation Creation Process
1. **Core Status Files**: Update TASKS.md and API_REFERENCES.md to reflect implementation progress
2. **Multi-Layer Documentation**: Create docs/models/, docs/tools/, and docs/conversations/ for new trading domains
3. **Cross-References**: Establish bidirectional links across all 4 layers with trading context
4. **Integration**: Update docs/README.md with new documentation sections
5. **Validation**: Test all links and anchor references

### Documentation Quality Checklist
For each new documentation implementation:
- [ ] All 4 documentation layers created (conversations, models, tools, code docstrings)
- [ ] Cross-references established bidirectionally between all layers with trading context
- [ ] TASKS.md and API_REFERENCES.md updated to reflect new capabilities
- [ ] All markdown links use relative paths and valid anchors
- [ ] Examples include proper trading safety handling and follow established patterns
- [ ] Documentation follows consistent template structure
- [ ] Trading safety warnings and risk management guidance included

## Documentation Templates

### Code Docstring Template
```python
"""Trading tool description with clear usage context and safety considerations.

API endpoint: METHOD /path/to/endpoint

Args:
    param_name: Description with format/constraints and trading context
    
Returns:
    Description of return structure and key trading fields
    
Safety:
    Trading safety considerations and risk warnings
    
See:
    docs/tools/domain.md#tool-name for usage examples
"""
```

### Tool Reference Template
```markdown
### tool_name
**Function:** `tool_name(param1: str, param2: int = 0) -> APIResponse`
**Description:** What it does and when to use it in trading context
**Parameters:**
- param1: Description with format requirements and trading constraints
- param2: Description with default value and trading implications
**Returns:** Return structure explanation with trading data
**Safety:** Trading safety considerations and risk warnings
**Models:** [TradingModel](../models/domain.md#tradingmodel)
**Examples:** [Trading Scenario](../conversations/domain-conversation.md#scenario-name)
```

### Model Documentation Template
```markdown
### ModelName
**Purpose:** What this model validates in trading context
**Used by:** [tool_name](../tools/domain.md#tool-name), [other_tool](../tools/domain.md#other-tool)
**Fields:** Field descriptions and trading validation rules
**API Mapping:** model_field -> "api-field-name"
**Safety:** Trading parameter constraints and risk considerations
```

### Conversation Example Template
```markdown
## Trading Scenario Name
**Tools used:** [tool_name](../tools/domain.md#tool-name)
**Models:** [ModelName](../models/domain.md#modelname)
**Description:** Realistic trading scenario with expected inputs/outputs
**Safety:** Trading safety considerations and risk management
**Risk Level:** Low/Medium/High trading risk assessment
```

### Trading-Specific Documentation Patterns
- **Bot Operations**: Include bot safety checks and account validation
- **Strategy Configuration**: Document strategy parameters and market requirements
- **Deal Management**: Include deal safety and profit/loss considerations
- **Account Operations**: Document exchange permissions and trading limits
- **Risk Management**: Include safety warnings and risk assessment for all operations