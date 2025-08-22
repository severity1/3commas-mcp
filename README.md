# 3Commas MCP Server

A Model Context Protocol (MCP) server that integrates AI assistants with the 3Commas cryptocurrency trading platform API. Manage your DCA bots and trading strategies through natural conversation with any MCP-supporting platform including Claude, Claude Code CLI, Claude Desktop, Cursor, and Copilot Studio.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![Implementation](https://img.shields.io/badge/10_of_29_apis-completed-success)
![Type Checking](https://img.shields.io/badge/type_checking-mypy-brightgreen)
![Code Quality](https://img.shields.io/badge/code_quality-100%25-success)

---

## Available Tools

### Account Management ✅
- `health_check()` - Test API connectivity and authentication status
- `get_account_info(account_id)` - Get account details, balance, profit metrics (summary or specific account)
- `get_connected_exchanges_and_wallets()` - View all connected exchanges with permissions and status
- `get_balance_history_data(date_from, account_id)` - Historical balance changes with profit tracking

### Market Data ✅  
- `get_supported_markets()` - List supported trading markets and exchanges
- `get_all_market_pairs(market_code)` - Get available trading pairs for any exchange
- `get_currency_rates_and_limits(market_code, pair)` - Current rates, limits, and precision for currency pairs

### DCA Bot Management ✅
- `get_dca_bot_list()` - Get all DCA bots with status, configuration, and performance overview
- `get_dca_bot_details(bot_id)` - Comprehensive bot configuration, deals, and performance data
- `get_available_strategy_list()` - Available DCA bot trading strategies with configuration options
- `get_dca_bot_profit_data(bot_id)` - Daily profit analytics with BTC/USD amounts and timestamps
- `get_blacklist_of_pairs()` - Get blacklisted trading pairs with restrictions and configurations

**Implementation Status**: 10 of 29 planned GET APIs completed (34.5%) - **Read-only operations only for trading safety**

All tools include `response_filter` parameter (`"display"` for essential data, `"full"` for complete response).

See [docs/tools/](docs/tools/) for detailed function documentation and [docs/API_REFERENCES.md](docs/API_REFERENCES.md) for complete API status.

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

## Usage Examples

```
"Show me all my connected exchanges and their status"
"List all my DCA bots and their current status"
"What trading pairs are available on Binance?"
```

See [docs/conversations/](docs/conversations/) for comprehensive usage examples and scenarios.

---

## Architecture & Security

**Read-only operations only** - Current implementation has zero trading risk with secure HMAC-SHA256 authentication and comprehensive error handling.

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for technical architecture and security details.

---

## Development

```bash
# Run quality checks
uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .
```

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution guidelines and [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for setup details.

---

## Documentation

- **[API References](docs/API_REFERENCES.md)** - Complete 3Commas API mapping with implementation status
- **[Tool Documentation](docs/tools/)** - Detailed function references and parameters
- **[Conversation Examples](docs/conversations/)** - Real-world usage scenarios  
- **[Development Guide](docs/DEVELOPMENT.md)** - Technical architecture and setup
- **[Contributing](docs/CONTRIBUTING.md)** - Contribution guidelines and standards
- **[Patterns](docs/PATTERNS.md)** - Implementation patterns and compliance

---

## License & Disclaimer

MIT License - see LICENSE file for details.

**Trading Disclaimer**: This software is for educational purposes. Cryptocurrency trading involves substantial risk. Always review configurations carefully and never trade more than you can afford to lose. Authors are not responsible for trading losses.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-username/3commas-mcp/issues)
- **3Commas API**: [Official Documentation](https://developers.3commas.io/)

Built with [FastMCP](https://gofastmcp.com) and comprehensive safety-first design patterns.