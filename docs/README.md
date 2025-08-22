# Documentation

Documentation for the 3Commas MCP server project.

## Core Documentation
- **[PATTERNS.md](PATTERNS.md)**: Implementation patterns and compliance checklist
- **[DEVELOPMENT.md](DEVELOPMENT.md)**: Development standards and workflow
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contributing guidelines
- **[API_REFERENCES.md](API_REFERENCES.md)**: API reference links and implementation status
- **[MVP_GET_APIS.md](MVP_GET_APIS.md)**: MVP implementation plan and progress

## 4-Layer Documentation System

### Layer 1: Conversations (`conversations/`)
Example user prompts for trading scenarios:
- Account management and exchange validation
- DCA bot operations and performance tracking  
- Market data research and trading pair analysis

### Layer 2: Models (`models/`)
Pydantic model documentation with validation rules:
- DCA bot configuration and request models
- Account and exchange connection models
- Market data and trading pair models

### Layer 3: Tools (`tools/`)
API tool reference with function signatures:
- DCA bot management tools
- Account and exchange tools
- Market data and trading pair tools

### Layer 4: Code Docstrings
Implementation-level documentation in the codebase

## Cross-References
- **Code** → **Tools**: Docstrings reference tool documentation
- **Tools** ↔ **Models**: Bidirectional linking between tools and models
- **Tools** → **Conversations**: Tool docs reference usage examples
- **Conversations** → **Tools/Models**: Examples reference implementations

## Getting Started

### For Developers
1. Review [DEVELOPMENT.md](DEVELOPMENT.md) for setup and standards
2. Follow [PATTERNS.md](PATTERNS.md) for implementation patterns
3. Use component CLAUDE.md files for specific guidance

### For Users
1. Check `conversations/` for usage examples
2. Review `tools/` for API reference
3. Consult `models/` for parameter validation
4. Refer to API_REFERENCES.md for implementation status