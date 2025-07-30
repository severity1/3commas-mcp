# 3Commas MCP Server

A Model Context Protocol (MCP) server that integrates AI assistants with the 3Commas cryptocurrency trading platform API. Manage your DCA bots and trading strategies through natural conversation with any MCP-supporting platform including Claude, Claude Code CLI, Claude Desktop, Cursor, and Copilot Studio.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![Implementation](https://img.shields.io/badge/phase_1-complete-success)
![Type Checking](https://img.shields.io/badge/type_checking-mypy-brightgreen)
![Code Quality](https://img.shields.io/badge/code_quality-100%25-success)

---

## What's Available Now

**Phase 1 Foundation (Complete)** - Safe, read-only operations with no trading risks:

- **Account Management**: View connected exchanges, wallets, and trading permissions
- **Market Data**: Access trading pairs, exchange rates, limits, and supported markets  
- **DCA Bot Information**: Get detailed bot configuration, status, and performance data
- **System Health**: Test API connectivity and authentication

**Coming in Phase 2+**: Full bot management (create, update, enable/disable), grid bots, advanced analytics, and strategy configuration.

---

## Installation & Setup

### Prerequisites
- Python 3.12+
- `uv` package manager (recommended) or `pip`
- 3Commas account with API access

### Install
```bash
git clone https://github.com/your-username/3commas-mcp.git
cd 3commas-mcp

# Setup environment
uv venv && source .venv/bin/activate
uv sync && uv pip install -e .
```

### Configure for Claude Code CLI
```bash
claude mcp add -e 3COMMAS_API_KEY=your_api_key -e 3COMMAS_SECRET_KEY=your_secret_key -e 3COMMAS_ENABLE_DESTRUCTIVE=false -s user threecommas-mcp -- "threecommas-mcp"
```

### Configure for Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "threecommas-mcp": {
      "command": "/path/to/uv",
      "args": ["--directory", "/path/to/3commas-mcp", "run", "threecommas-mcp"],
      "env": {
        "3COMMAS_API_KEY": "your_api_key",
        "3COMMAS_SECRET_KEY": "your_secret_key", 
        "3COMMAS_ENABLE_DESTRUCTIVE": "false"
      }
    }
  }
}
```

**Config file locations:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

---

## Available Tools

### Account & Market Data
- `get_connected_exchanges_and_wallets()` - View all connected exchanges with permissions and status
- `get_supported_markets()` - List supported trading markets and exchanges
- `get_all_market_pairs()` - Get available trading pairs for any exchange
- `get_currency_rates_and_limits()` - Current rates, limits, and precision for currency pairs

### DCA Bot Information  
- `get_dca_bot_list()` - Get all DCA bots with status, configuration, and performance overview
- `get_dca_bot_details()` - Comprehensive bot configuration, deals, and performance data

### System
- `health_check()` - Test API connectivity and authentication

All tools include `response_filter` parameter (`"display"` for essential data, `"full"` for complete response).

---

## Usage Examples

**Account & Market Analysis:**
```
"Show me all my connected exchanges and their status"
"What trading pairs are available on Binance?"
"Get current BTC/USDT rates and limits on OKX"
```

**DCA Bot Analysis:**
```
"List all my DCA bots and their status"
"Show details for my DCA bot ID 12345678"
"What's the current performance of my Bitcoin bot?"
"Check if my bot is active and show safety order configuration"
```

**System Health:**
```
"Test my 3Commas API connection"
"Verify my API credentials are working"
```

---

## Architecture & Security

### Technical Design
- **HMAC-SHA256 Authentication** with secure credential handling
- **Rate Limiting Compliance** respecting 3Commas API limits (300/60/120 req/min)
- **Pydantic Models** for comprehensive data validation
- **Component-based Architecture** with domain-specific modules

### Safety Features
- **Read-Only Operations** - Current implementation has zero trading risk
- **Environment Variable Security** - Credentials never stored in code
- **Destructive Operation Controls** - High-risk operations disabled by default
- **Comprehensive Error Handling** with trading context

### Component Architecture
- **API Layer**: HMAC-SHA256 authenticated 3Commas client with rate limiting
- **Model Layer**: Pydantic validation for all trading parameters
- **Tool Layer**: MCP-compatible functions with comprehensive error handling
- **Utils Layer**: Authentication, environment, and safety decorators

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed project structure.

---

## Development

### Quality Checks
```bash
# Run all checks
uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .

# Test server
uv run threecommas-mcp
```

### Contributing
1. Fork repository and create feature branch
2. Follow established patterns in existing code
3. Run quality checks before submitting
4. Update documentation for any new features

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## Documentation

- **[API References](docs/API_REFERENCES.md)** - Complete 3Commas API mapping with implementation status
- **[Development Guide](docs/DEVELOPMENT.md)** - Contributing and development instructions  
- **[Tool Documentation](docs/tools/)** - Detailed function references
- **[Conversation Examples](docs/conversations/)** - Real-world usage scenarios

---

## License & Disclaimer

MIT License - see LICENSE file for details.

**Trading Disclaimer**: This software is for educational purposes. Cryptocurrency trading involves substantial risk. Always review configurations carefully and never trade more than you can afford to lose. Authors are not responsible for trading losses.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-username/3commas-mcp/issues)
- **3Commas API**: [Official Documentation](https://developers.3commas.io/)

Built with [FastMCP](https://gofastmcp.com) and comprehensive safety-first design patterns.