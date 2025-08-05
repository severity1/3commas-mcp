# Documentation Creation Patterns

**Context**: Documentation for 3Commas trading operations  
**When to Use**: Root CLAUDE.md Phase 3 (documentation) after implementation complete

## Required Documentation Workflow
1. **Function Reference** - Create `docs/tools/{domain}.md`
2. **Model Documentation** - Create `docs/models/{domain}.md`  
3. **Conversation Examples** - Create `docs/conversations/{domain}-conversation.md`
4. **Root README Updates** - Update tool listings, phase status, and usage examples in main README.md
5. **Tracking Updates** - Update API_REFERENCES.md, TASKS.md, MVP_GET_APIS.md

## Documentation Structure Templates

### 1. Function Reference Template (docs/tools/{domain}.md)
```markdown
# {Domain} Tools API Reference

## function_name()
**Purpose**: Brief description of what the function does
**Endpoint**: /api/ver1/endpoint_name
**Authentication**: Required

### Parameters
- `param_name` (type): Description with constraints
- `optional_param` (type, optional): Description

### Returns
- Dictionary with key data fields
- Error object on failure: `{"error": "message"}`

### Example Usage
\`\`\`python
result = await function_name(param="example_value")
\`\`\`

### Safety Considerations
- Risk assessment and trading safety notes
```

### 2. Model Documentation Template (docs/models/{domain}.md)
```markdown
# {Domain} Models Reference

## ModelNameRequest
**Purpose**: Brief description of model purpose
**API Endpoint**: /api/ver1/endpoint_name

### Fields
- `field_name` (type): Description and validation rules
- `optional_field` (type, optional): Description

### Example
\`\`\`python
request = ModelNameRequest(
    field_name="example_value"
)
\`\`\`
```

### 3. Conversation Example Template (docs/conversations/{domain}-conversation.md)
```markdown
# {Domain} Conversation Examples

## Scenario: User Task Description
**User**: "Natural language request"
**Claude**: "Response with function call and formatted results"

## Integration Examples
- Show function calls with realistic dummy data
- Demonstrate error handling and troubleshooting
```

## Root README.md Update Checklist
- [ ] Update phase completion badge if applicable (e.g., phase_1 → phase_2)
- [ ] Add new tool to appropriate category section (Account, DCA Bot, Market Data, System)
- [ ] Update "What's Available Now" section for new capabilities
- [ ] Add usage examples for new functionality
- [ ] Update phase descriptions when phases complete

## Critical Requirements
- **Privacy**: Use dummy/example data only (bot ID 12345678, $245.67 profit)
- **Consistency**: Follow existing documentation structure patterns
- **Cross-References**: Link between tools, models, and conversation docs
- **Tracking**: Update API_REFERENCES.md (⏸️ → ✅), TASKS.md, MVP_GET_APIS.md

## Reference Examples
- **Complete documentation**: docs/tools/dca_bots.md, docs/models/dca_bots.md
- **Conversation pattern**: docs/conversations/dca-bot-management-conversation.md