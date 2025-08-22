# Documentation Patterns

**Context**: 4-layer documentation system for 3Commas MCP with streamlined structure

## Component Focus
- **Tools documentation** - Function references in docs/tools/{domain}.md
- **Model documentation** - Validation specs in docs/models/{domain}.md  
- **Conversation examples** - User prompts in docs/conversations/{domain}-conversation.md

## Required Documentation
1. **Update API status** - Mark ⏸️ → ✅ in docs/API_REFERENCES.md
2. **Tool documentation** - Add function to docs/tools/{domain}.md
3. **Model documentation** - Add model to docs/models/{domain}.md
4. **Usage examples** - Add prompts to docs/conversations/{domain}-conversation.md

## Documentation Standards
- **Privacy protection** - Use dummy data ONLY when documenting (bot ID 12345678, $245.67 profit)
- **Streamlined format** - Concise, scannable structure (90%+ reduction achieved)
- **Cross-references** - Link between tools, models, conversations layers
- **Trading safety** - Include risk assessment for trading operations

## Code Examples
```markdown
# Tool documentation format
## get_function_name
Brief description with parameters and return info.

# Model documentation format  
## RequestModelName
Purpose and key validation fields.

# Conversation examples format
## Category Name
- "Example user prompt for this functionality"
```

## Integration Requirements
- Update all 4 layers when implementing new tools
- Follow streamlined format established in existing documentation
- Use consistent dummy data across all examples
- Include trading safety context for financial operations