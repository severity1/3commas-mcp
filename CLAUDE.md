# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 3Commas MCP Development Guide

## Subtree Discovery System

This project uses Claude Code's automatic subtree discovery for context-aware guidance. Component-specific CLAUDE.md files are automatically loaded when working in their directories:

- **docs/** - Documentation standards and templates for 3Commas trading contexts
- **3commas_mcp/tools/** - MCP tools implementation patterns for DCA bots and trading strategies
- **3commas_mcp/models/** - Pydantic models for 3Commas API structures and validation
- **3commas_mcp/utils/** - Utility functions for authentication, error handling, and rate limiting
- **3commas_mcp/api/** - API client patterns for 3Commas authentication and request handling

## Working Directory Guidance

### When Working on Tool Implementation
- **Directory**: `3commas_mcp/tools/`
- **Context**: Automatic loading of tools-specific patterns for DCA bots, strategies, and deals
- **Focus**: MCP function signatures, trading safety checks, destructive operation controls

### When Working on Data Models
- **Directory**: `3commas_mcp/models/`
- **Context**: Automatic loading of model validation patterns for trading data
- **Focus**: Pydantic models for bots, strategies, deals, safety orders, and account structures

### When Working on Utilities
- **Directory**: `3commas_mcp/utils/`
- **Context**: Automatic loading of utility function patterns for trading operations
- **Focus**: HMAC-SHA256 authentication, rate limiting, trading-specific error handling

### When Working on API Client
- **Directory**: `3commas_mcp/api/`
- **Context**: Automatic loading of API client patterns for 3Commas integration
- **Focus**: HTTP client with signature auth, rate limiting, 3Commas-specific response handling

### When Working on Documentation
- **Directory**: `docs/`
- **Context**: Automatic loading of documentation standards for trading contexts
- **Focus**: Templates, formatting, structure requirements for bot/strategy/deal documentation

## Development Commands

### Package Management
- **Sync Dependencies**: `uv sync`
- **Install Package**: `uv pip install -e .`

### Quality Checks (Reference Tools)
- **Format**: Use external formatter (ruff not in pyproject.toml per reference pattern)
- **Lint**: Use external linter (configured via external tools)
- **Type Check**: `uv run -m mypy 3commas_mcp/` (configured in pyproject.toml)
- **Test**: `pytest` (when tests are implemented)

### Build Commands
- **Build Package**: `uv build`
- **Run Server**: `uv run 3commas-mcp` (when server.py is implemented)

## Core Principles

### Decision-Making Process
1. **Use component guidance**: Let subtree discovery load relevant context
2. **Apply documented patterns**: Follow loaded component standards
3. **Prioritize trading safety**: Always consider bot safety and destructive operation controls
4. **Validate against patterns**: Check implementation against guidance

### Task Complexity Assessment
- **Simple** (< 2 hours): Direct implementation, minimal planning
- **Medium** (2-8 hours): Use TodoWrite for 3-5 tasks
- **Complex** (> 8 hours): Use subagents (2-6) with comprehensive TodoWrite planning

## 3Commas-Specific Standards

### Authentication & Security
- **API Authentication**: HMAC-SHA256 signature authentication for all requests
- **Environment Variables**: Store API credentials securely, never log sensitive data
- **Rate Limiting**: Respect 3Commas rate limits (300/60/120 req/min by endpoint type)
- **Destructive Operations**: Bot enable/disable/delete operations behind feature flags

### Trading Safety Requirements
- **Bot Management**: Always validate bot configuration before creation
- **Deal Operations**: Include safety checks for deal cancellation and panic sells
- **Strategy Configuration**: Validate strategy parameters against 3Commas requirements
- **Account Validation**: Verify exchange account permissions before bot operations

### API Integration Standards
- **Base URL**: https://api.3commas.io
- **Required Headers**: APIKEY and APISIGN for all authenticated requests
- **Response Handling**: Handle 3Commas-specific error formats and success patterns
- **Rate Limiting**: Implement exponential backoff for rate limit compliance

## Documentation Standards

### Required Documentation Updates
For any new implementation, always update:
- **TASKS.md**: Move features from planned to completed status
- **docs/API_REFERENCES.md**: Mark corresponding API sections as implemented
- **docs/DEVELOPMENT.md**: Add new patterns if applicable
- **docs/CONTRIBUTING.md**: Update contribution guidelines if new patterns introduced

### Implementation Standards ✅ **UPDATED**
- **Use utility functions**: `sign_request()`, `@handle_api_errors`, `@rate_limit_retry`
- **Apply authentication**: HMAC-SHA256 signature generation for all requests (utils/auth.py)
- **Follow component patterns**: Apply standards from automatically loaded component CLAUDE.md files
- **Run quality checks**: Format, lint, type check before completion
- **Update relevant documentation**: Maintain consistency across project

### Response Filtering System ✅ **IMPLEMENTED**
This MCP server includes intelligent response filtering for token efficiency:
- **Security-first approach**: Always remove `url_secret`, `account_id` from all responses
- **Redundant field removal**: Remove bot-level fields duplicated in active deals (both filter types)
- **Filter types**: `"full"` (editing/analysis) vs `"display"` (general use, 85% token reduction)
- **Context preservation**: Display filter removes pairs array→count, events→3 recent, crypto widgets
- **Implementation**: `utils/response_filter.py` with layered filtering applied to all tools

### Simplified Implementation Approach
This MCP server uses a minimal, focused approach:
- **Token-efficient responses**: Implemented response filtering system for optimal AI context usage
- **Pydantic-first validation**: Use Pydantic models for parameter validation instead of separate utilities
- **Essential utilities only**: auth.py, env.py, decorators.py, response_filter.py - no over-engineering
- **Trading safety focus**: Destructive operation controls and comprehensive error handling

## Task Management

### TodoWrite Usage
Use TodoWrite for tasks with:
- Multiple distinct steps (> 2)
- Multiple file changes
- Cross-component coordination
- Medium to complex scope
- Trading safety validation requirements

### Progress Standards
- Mark todos `in_progress` before starting
- Mark `completed` immediately after finishing
- Update status in real-time
- Provide concise progress updates for major phases

## Memory System Maintenance

### Periodic Review Schedule
- **Monthly**: Review component CLAUDE.md files for outdated patterns
- **After major features**: Update decision matrices and workflow patterns
- **When adding new domains**: Verify subtree discovery optimization
- **Quality check failures**: Review and update development standards

### Maintenance Triggers
- **New implementation patterns**: Update relevant component guidance
- **API changes**: Review model and tool implementation standards
- **Development workflow changes**: Update quality check commands
- **Documentation structure changes**: Update docs/ guidance
- **3Commas API updates**: Review authentication and rate limiting patterns
- **Trading safety requirements**: Update destructive operation controls

### Memory Optimization Indicators
- **High context usage**: Review for redundant information across files
- **Frequent cross-referencing**: Consider consolidating related guidance
- **Outdated patterns**: Remove deprecated implementation approaches
- **Missing decision criteria**: Add decision matrices for common scenarios
- **Trading safety gaps**: Ensure all bot operations have proper safety documentation