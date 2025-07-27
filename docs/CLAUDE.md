# CLAUDE.md for docs/

## Context Activation
Activates when working in `docs/` directory creating documentation for 3Commas trading contexts.

**Companions**: All component directories (tools/, models/, utils/, api/)

## Documentation Architecture

### Core Files
- **DEVELOPMENT.md**: Development standards and build/quality guidance
- **CONTRIBUTING.md**: Contributing guidelines with trading safety focus
- **README.md**: Documentation overview for trading contexts
- **API_REFERENCES.md**: 3Commas API reference and implementation status

### Multi-Layer Structure
Each trading domain follows consistent 4-layer documentation:
1. **conversations/**: Real-world trading examples and interaction patterns
2. **models/**: Pydantic model docs with validation rules and API mappings
3. **tools/**: API tool reference with signatures and trading safety scenarios
4. **Code docstrings**: Implementation-level docs with cross-references

## Documentation Standards

### Core Principles
- **Consistency**: Each trading domain documented across all 4 layers
- **Trading-focused**: Reference actual trading scenarios, not generic examples
- **Cross-referenced**: All layers link to related docs with trading context
- **API-aligned**: Include 3Commas API docs and trading requirements

### Quality Requirements
- Document trading parameters, return types, and safety handling
- Organize examples from basic bot operations to advanced strategies
- Use consistent anchor names (#lowercase-with-hyphens)
- Maintain valid cross-references with relative paths
- Include trading safety warnings and risk management guidance

## New Documentation Workflow

### Implementation Steps
1. **Model Documentation**: Create `docs/models/{domain}.md` with validation rules
2. **Tool Documentation**: Create `docs/tools/{domain}.md` with function signatures
3. **Conversation Examples**: Create `docs/conversations/{domain}-conversation.md`
4. **Cross-References**: Link all layers bidirectionally with trading context
5. **Integration**: Update `docs/README.md` and relevant CLAUDE.md files

### Cross-Reference Requirements
Every new tool maintains bidirectional links across all 4 layers:
- **Code docstrings** → docs/tools/ sections with trading context
- **docs/tools/** ↔ docs/models/ (bidirectional) with validation cross-references
- **docs/tools/** → docs/conversations/ trading examples
- **docs/models/** → tools that use the model for trading operations
- **docs/conversations/** → specific tool/model sections with trading scenarios

### Quality Checklist
- [ ] All 4 documentation layers created (conversations, models, tools, docstrings)
- [ ] Cross-references established bidirectionally between all layers
- [ ] All markdown links use relative paths and valid anchors
- [ ] Examples include proper trading safety handling
- [ ] Trading safety warnings and risk management guidance included

## Documentation Templates

### Tool Reference Template
```markdown
### tool_name
**Function:** `tool_name(param1: str, param2: int = 0) -> APIResponse`
**Description:** What it does and when to use it in trading context
**Parameters:**
- param1: Description with trading constraints
- param2: Description with trading implications
**Returns:** Return structure with trading data
**Safety:** Trading safety considerations and risk warnings
**Models:** [TradingModel](../models/domain.md#tradingmodel)
**Examples:** [Trading Scenario](../conversations/domain-conversation.md#scenario-name)
```

### Model Documentation Template
```markdown
### ModelName
**Purpose:** What this model validates in trading context
**Used by:** [tool_name](../tools/domain.md#tool-name)
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