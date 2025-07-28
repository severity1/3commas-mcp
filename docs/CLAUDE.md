# CLAUDE.md for docs/

## Context Activation
Activates when creating documentation for 3Commas trading contexts.

## Current Documentation Status
**20 markdown files, 3,194 total lines:**
- **Core documentation** (6 files): PATTERNS.md, DEVELOPMENT.md, CONTRIBUTING.md, API_REFERENCES.md, MVP_GET_APIS.md, README.md
- **4-layer structure implemented**: conversations/, models/, tools/ directories with README files
- **Domain coverage**: 3 domains documented (account, market_data, dca_bots)

## Documentation Architecture (verified structure)

### 4-Layer Structure (implemented)
1. **conversations/** (4 files) - Real-world trading examples and interaction patterns
2. **models/** (5 files) - Pydantic model docs with validation rules and API mappings  
3. **tools/** (4 files) - API tool reference with signatures and trading safety scenarios
4. **Code docstrings** - Implementation-level docs with cross-references

### Core Files (actual files)
- **PATTERNS.md** (119 lines) - Implementation patterns and compliance checklist
- **DEVELOPMENT.md** (251 lines) - Development standards and workflow  
- **CONTRIBUTING.md** (237 lines) - Contributing guidelines with trading safety focus
- **API_REFERENCES.md** - 3Commas API reference and implementation status
- **MVP_GET_APIS.md** - Implementation roadmap and progress tracking
- **README.md** (132 lines) - Documentation overview and navigation

## Documentation Workflow (established patterns)

### For New Domains
1. Create `docs/models/{domain}.md` with validation rules
2. Create `docs/tools/{domain}.md` with function signatures  
3. Create `docs/conversations/{domain}-conversation.md` with examples
4. Update `docs/README.md` with new domain references
5. Establish cross-references between all layers

### Current Domains Documented
- **account** - Exchange account management and validation
- **market_data** - Trading pairs, rates, and market information
- **dca_bots** - DCA bot configuration and management

## Quality Standards (established in current docs)
- **Trading-focused**: All examples use realistic trading scenarios
- **Cross-referenced**: Bidirectional links between documentation layers
- **Comprehensive**: Average 160 lines per document
- **Template consistency**: All follow established documentation templates
- **Safety emphasis**: Trading safety warnings and risk assessments included

## Quality Checklist (based on current structure)
- [ ] Domain documented across all 4 layers (conversations, models, tools, docstrings)
- [ ] Cross-references established bidirectionally
- [ ] Trading safety warnings and risk levels included
- [ ] Follows established templates and formatting standards