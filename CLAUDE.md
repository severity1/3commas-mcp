# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 3Commas MCP Development Guide

## Quick Start

### Context Loading
This project uses automatic subtree discovery. Component-specific guidance loads when working in:
- `tools/` - MCP function patterns, trading safety, destructive operations
- `models/` - Pydantic validation, API structures, trading parameters
- `utils/` - Authentication, error handling, rate limiting, response filtering
- `api/` - HTTP client, HMAC-SHA256 auth, 3Commas integration
- `docs/` - Documentation standards, templates, trading contexts

### Core Commands
- **Activate Environment**: `source .venv/bin/activate`
- **Dependencies**: `uv sync`
- **Install/Reinstall Server**: `uv pip install -e .`
- **Format**: `uv run -m black .` and `uv run -m ruff format .`
- **Lint**: `uv run -m ruff check .`
- **Type Check**: `uv run -m mypy .`

## Decision Matrices

### Component Decision Guide
| Need | Use Component | Focus |
|------|---------------|-------|
| Trading API functions | `tools/` | Safety checks, destructive controls |
| Data validation | `models/` | Pydantic models, trading parameters |
| Auth/errors/filtering | `utils/` | HMAC-SHA256, response optimization |
| HTTP requests | `api/` | 3Commas client integration |
| Documentation | `docs/` | Trading context templates |

## Core Principles
1. **Trading safety first** - Always validate bot/deal operations
2. **Component guidance** - Let subtree discovery load relevant context
3. **Response efficiency** - Use filtering system for 85% token reduction
4. **Security focus** - Never log credentials, validate all inputs
5. **Consistent workflow** - Always use subagents with TodoWrite for all tasks
6. **KISS/DRY** - Keep implementations simple, avoid code duplication

## Implementation Standards

### Essential Patterns
- **Authentication**: HMAC-SHA256 via `utils/auth.py`
- **Error handling**: `@handle_api_errors` decorator
- **Response filtering**: `filter_response()` for 85% token reduction
- **Validation**: Pydantic models with trading safety checks
- **Rate limiting**: 300/60/120 req/min compliance with exponential backoff

### API Integration
- **Base URL**: `https://api.3commas.io/public/api/`
- **Headers**: `APIKEY` and `APISIGN` for all authenticated requests
- **Security**: Never log `url_secret`, `account_id` - always filter responses
- **Trading safety**: Validate bot config, account permissions, deal states

### Quality Workflow
1. Activate environment: `source .venv/bin/activate`
2. Implement with utility decorators and response filtering
3. Format: `uv run -m black .` and `uv run -m ruff format .`
4. Lint check: `uv run -m ruff check .`
5. Type check: `uv run -m mypy .`
6. Update documentation status in relevant files
7. Reinstall MCP server: `uv pip install -e .`
8. Test trading safety scenarios

## Memory Maintenance

### When to Update CLAUDE.md Files
- **New implementation patterns** - Update component guidance
- **3Commas API changes** - Review auth/rate limiting patterns  
- **Trading safety gaps** - Add missing bot operation safety docs
- **High context usage** - Remove redundant information across files