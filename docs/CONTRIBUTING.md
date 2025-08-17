# Contributing Guide

Thank you for your interest in contributing to the 3Commas MCP server project! This guide will help you understand our development process and standards.

## Getting Started

### Prerequisites
- Python 3.12 or higher
- 3Commas account with API access
- Basic understanding of cryptocurrency trading concepts
- Familiarity with MCP (Model Context Protocol) concepts

### Development Setup
1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/3commas-mcp.git
   cd 3commas-mcp
   ```

2. **Set up development environment**
   ```bash
   # Install dependencies
   uv pip install -e .[dev]
   
   # Set up environment variables
   cp env.example .env
   # Edit .env with your 3Commas API credentials (for testing)
   ```

3. **Verify setup**
   ```bash
   # Run quality checks
   ruff format . && ruff check . && mypy . && pytest
   ```

## Development Standards

### Code Quality Requirements
All contributions must meet these quality standards:
- **Formatting**: Code must be formatted with `ruff format .`
- **Linting**: Code must pass `ruff check .` without errors
- **Type Checking**: Code must pass `mypy .` without errors
- **Testing**: All new code must include comprehensive tests
- **Documentation**: All public APIs must be documented

### Trading Safety Standards
All contributions must prioritize trading safety:
- Validate all trading parameters thoroughly
- Verify account permissions and capabilities  
- Require explicit confirmation for destructive operations
- Provide clear error messages with trading context
- Never log or expose API credentials

## Contribution Process

### 1. Issue Discussion
Before starting work on a significant feature:
1. Check existing issues to avoid duplication
2. Create a new issue describing your proposed changes
3. Discuss the approach with maintainers
4. Wait for approval before beginning implementation

### 2. Development Workflow
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Follow component guidance**
   - Use CLAUDE.md files in each directory for component-specific guidance
   - Follow established patterns for tools, models, and utilities
   - Maintain consistency with existing code style

3. **Implement with safety first**
   - Include comprehensive input validation
   - Add appropriate error handling
   - Follow 3Commas API authentication requirements
   - Test with both valid and invalid inputs

4. **Update documentation**
   - Update relevant CLAUDE.md files if adding new patterns
   - Add or update docs/ files following the 4-layer structure
   - Update TASKS.md and API_REFERENCES.md implementation status
   - Include code docstrings with trading context

### 3. Testing Requirements
All contributions must include testing:
- Authentication, API connectivity, and error handling tests
- Trading safety and parameter validation tests
- Follow Arrange-Act-Assert pattern with descriptive test names

### 4. Pull Request Process
1. **Pre-submission checklist**
   - [ ] Code formatted with `ruff format .`
   - [ ] Linting passed with `ruff check .`
   - [ ] Type checking passed with `mypy .`
   - [ ] All tests pass with `pytest`
   - [ ] Documentation updated
   - [ ] Trading safety validated
   - [ ] **Pattern compliance verified** (see `docs/PATTERNS.md` checklist)

2. **Submit pull request**
   - Use descriptive title summarizing the change
   - Include detailed description of changes
   - Reference related issues
   - Include screenshots for UI changes (if applicable)

3. **Review process**
   - Maintainers will review code quality and trading safety
   - Address feedback promptly and thoroughly
   - Update tests and documentation as requested
   - Maintain focus on trading safety throughout review

## Component-Specific Guidelines

### API Client (`3commas_mcp/api/`)
- **Authentication**: Implement proper HMAC-SHA256 signature generation
- **Rate Limiting**: Include exponential backoff for rate limit compliance
- **Error Handling**: Handle 3Commas-specific error formats
- **Security**: Never log API credentials or sensitive data

### Tools (`3commas_mcp/tools/`)
- **Function Signatures**: Follow (routing_params, trading_params, optional_params) pattern
- **Validation**: Use Pydantic models for comprehensive input validation
- **Safety Checks**: Include trading safety validation before operations
- **Registration**: Register tools with appropriate destructiveness classification

### Models (`3commas_mcp/models/`)
- **Validation**: Include comprehensive trading parameter validation
- **API Mapping**: Document field mappings to 3Commas API structure
- **Type Safety**: Use complete type hints for all fields
- **Documentation**: Include trading context in model documentation

### Utilities (`3commas_mcp/utils/`)
- **Security**: Prioritize secure credential and data handling
- **Reusability**: Design for use across all components
- **Error Context**: Include trading context in error handling
- **Testing**: Comprehensive test coverage for utility functions

## Documentation Standards

### Required Documentation
- Include docstrings with trading context and type hints
- Update TASKS.md and docs/API_REFERENCES.md for new features
- Follow templates in docs/models/, docs/tools/, docs/conversations/
- Include trading safety warnings where applicable

## Trading Safety Guidelines

### Trading Safety Requirements
- Validate bot configuration and account permissions
- Include safety checks for trading operations
- Assess risk levels: Low (read-only), Medium (bot config), High (deletion/cancellation)  
- Provide clear error messages with trading context
- Never log API credentials or sensitive trading data

Thank you for contributing to the 3Commas MCP server project!