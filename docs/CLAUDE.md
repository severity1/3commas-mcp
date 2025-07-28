# CLAUDE.md for @docs/

## Context Activation
Activates when creating documentation for 3Commas trading contexts.

## Documentation Structure
### Core Tracking Files
- **@docs/API_REFERENCES.md** - Status tracking (⏸️ → ✅)
- **@docs/MVP_GET_APIS.md** - Implementation roadmap with phases
- **@TASKS.md** - Phase-based implementation progress

### Documentation Layers
1. **@docs/conversations/** - Real-world usage examples
2. **@docs/models/** - Pydantic validation documentation  
3. **@docs/tools/** - API function reference

## Documentation Update Requirements (Per New API Implementation)

### 1. Function Reference Documentation (@docs/tools/{domain}.md)
**Required Content:**
- Function signature with all parameters and types
- API endpoint, security requirements, and permissions
- Parameter descriptions with trading constraints and validation
- Return value structure and key data fields
- Error handling patterns and common failure scenarios
- Usage examples with realistic trading contexts
- Integration notes and cross-references to related tools
- Safety considerations and risk assessment

**Template Pattern:** Follow existing `dca_bots.md` structure for consistency

### 2. Model Documentation (@docs/models/{domain}.md)
**Required Content:**
- Request model class descriptions with purpose and usage
- Field validation rules with Field() constraints and patterns
- API parameter mapping from model fields to endpoint parameters
- Validation examples with error handling demonstrations
- Trading safety considerations for parameter validation
- Integration examples showing request model usage in tools
- Development guidelines for extending model functionality

**Template Pattern:** Follow existing `dca_bots.md` model documentation structure

### 3. Conversation Examples (@docs/conversations/{domain}-conversation.md)
**Required Content:**
- Realistic user scenarios demonstrating natural language interactions
- Step-by-step Claude response processes showing API calls
- Expected Claude responses with properly formatted trading data
- Multiple conversation patterns (information retrieval, troubleshooting, analysis)
- Tool integration examples showing function calls and data processing
- Safety considerations and risk assessment for conversation scenarios
- Cross-references to related tools and API documentation

**Template Pattern:** Follow existing `dca-bot-management-conversation.md` structure

### 4. Tracking File Updates
**Required Updates:**
- **@docs/API_REFERENCES.md:** Change status from `[⏸️]` to `[✅]` for implemented API
- **@TASKS.md:** Update progress counters and phase completion status
- **@docs/MVP_GET_APIS.md:** Mark API as implemented in priority tables if applicable