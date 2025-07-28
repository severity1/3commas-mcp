# 3Commas MCP Server

A Model Context Protocol (MCP) server that integrates AI assistants with the 3Commas cryptocurrency trading platform API, allowing you to manage your DCA bots and trading strategies through natural conversation. Built with Pydantic models and structured around domain-specific modules, this server is compatible with any MCP-supporting platform including Claude, Claude Code CLI, Claude Desktop, Cursor, Copilot Studio, and others.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![Type Checking](https://img.shields.io/badge/type_checking-mypy-brightgreen)
![Code Quality](https://img.shields.io/badge/code_quality-100%25-success)

---

## Features

- **DCA Bot Management**: Get bot details, configuration, and status information for Dollar Cost Averaging bots.
- *Coming Soon*: Create, update, enable/disable DCA bots with validated configurations.
- *Coming Soon*: Strategy Management for QFL, RSI, Bollinger Bands, MACD, and custom signal strategies.
- *Coming Soon*: Deal Management with safety order tracking and performance analytics.
- *Coming Soon*: Grid Bot Management for range-bound trading strategies.
- *Coming Soon*: Account Management and trading pair analytics.

### Performance Features

- **HMAC-SHA256 Authentication**: Secure signature-based authentication for all API requests.
- **Rate Limiting Compliance**: Respects 3Commas API limits (300/60/120 req/min by endpoint type).
- **Endpoint Type Detection**: Optimizes rate limiting based on trading operation types.

### Safety Features

- **Destructive Operation Controls**: Delete and panic sell operations are disabled by default and require explicit enablement via environment variable.
- **Trading Safety Validation**: Comprehensive parameter validation for all bot configurations.
- **Read-Only by Default**: All current operations are read-only with no trading risks.

---

## Quick Start

### Prerequisites

- Python 3.12+
- MCP (includes FastMCP and development tools)
- `uv` package manager (recommended) or `pip`
- 3Commas account with API access

---

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/3commas-mcp.git
cd 3commas-mcp

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install package
uv pip install .
```

### Adding to Claude Environments

#### Adding to Claude Code CLI

```bash
# Add to Claude Code with your 3Commas API credentials
claude mcp add -e 3COMMAS_API_KEY=YOUR_API_KEY -e 3COMMAS_SECRET_KEY=YOUR_SECRET_KEY -e 3COMMAS_ENABLE_DESTRUCTIVE=false -s user threecommas-mcp -- "threecommas-mcp"

# To enable destructive operations (use with extreme caution):
# claude mcp add -e 3COMMAS_API_KEY=YOUR_API_KEY -e 3COMMAS_SECRET_KEY=YOUR_SECRET_KEY -e 3COMMAS_ENABLE_DESTRUCTIVE=true -s user threecommas-mcp -- "threecommas-mcp"
```

#### Adding to Claude Desktop

Create a `claude_desktop_config.json` configuration file:
- mac: ~/Library/Application Support/Claude/claude_desktop_config.json
- win: %APPDATA%\Claude\claude_desktop_config.json

```json
{
  "mcpServers": {
    "threecommas-mcp": {
      "command": "/path/to/uv", # Get this by running: `which uv`
      "args": [
        "--directory",
        "/path/to/your/3commas-mcp", # Full path to this project
        "run",
        "threecommas-mcp"
      ],
      "env": {
        "3COMMAS_API_KEY": "your_api_key...", # replace with actual API key
        "3COMMAS_SECRET_KEY": "your_secret_key...", # replace with actual secret key
        "3COMMAS_ENABLE_DESTRUCTIVE": "false" # set to "true" to enable destructive operations
      }
    }
  }
}
```

Replace the API credentials with your actual 3Commas API key and secret.

#### Other MCP-Compatible Platforms

For other platforms (like Cursor, Copilot Studio, or Glama), follow their platform-specific instructions for adding an MCP server. Most platforms require:
1. The server path or command to start the server.
2. Environment variables for the 3Commas API credentials (`3COMMAS_API_KEY` and `3COMMAS_SECRET_KEY`).
3. Optional environment variable to enable destructive operations (`3COMMAS_ENABLE_DESTRUCTIVE=true` for high-risk operations).
4. Configuration to auto-start the server when needed.

---

## Available Tools

### DCA Bot Management Tools

#### Information & Status
- `get_dca_bot_details(bot_id, include_events)`: Get comprehensive information about a specific DCA bot including configuration, active deals, trading parameters, and performance data.

*Coming Soon*:
- `list_dca_bots(limit, offset)`: List all DCA bots with filtering and pagination.
- `get_dca_bot_stats(bot_id)`: Get detailed performance statistics and metrics.

#### Create & Update (Coming Soon)
- `create_dca_bot(name, pair, account_id, params)`: Create a new DCA bot with validated configuration.
- `update_dca_bot(bot_id, params)`: Update an existing bot's configuration with safety checks.
- `clone_dca_bot(bot_id, new_name)`: Clone a successful bot configuration.

#### Control Operations (Coming Soon)
- `enable_dca_bot(bot_id)`: Activate bot trading with safety validation.
- `disable_dca_bot(bot_id)`: Pause bot trading operations.

#### Delete (Requires 3COMMAS_ENABLE_DESTRUCTIVE=true, Coming Soon)
- `delete_dca_bot(bot_id)`: Permanently delete a bot (destructive operation with confirmation).

**Note**: Delete operations are disabled by default for safety. Set `3COMMAS_ENABLE_DESTRUCTIVE=true` to enable these destructive operations.

### Strategy Management Tools (Coming Soon)

- `get_available_strategies()`: List all available trading strategies.
- `get_strategy_details(strategy_name)`: Get configuration options for a specific strategy.
- `configure_qfl_strategy(params)`: Configure Quick Fingers Luc strategy parameters.
- `configure_rsi_strategy(params)`: Configure RSI indicator-based strategies.

---

## Usage Examples

### Getting Bot Information

```
"Can you show me the details of my DCA bot with ID 12345678?"

"What's the current configuration and performance of my Bitcoin DCA bot?"

"Help me analyze the strategy effectiveness of bot 87654321, including recent deals"
```

### Bot Management (Coming Soon)

```
"Create a new DCA bot for ETH/USDT with conservative settings"

"Update my bot to use RSI strategy with 14-period and 30/70 levels"

"Clone my successful BTC bot configuration for ADA trading"
```

---

## Development

### Project Structure

```
3commas-mcp/
├── threecommas_mcp/           # Main package
│   ├── api/                   # 3Commas API client with HMAC authentication
│   ├── models/                # Pydantic data models for trading structures
│   ├── tools/                 # MCP tool implementations
│   │   └── dca_bots.py        # DCA bot management tools
│   ├── utils/                 # Utilities (auth, env, decorators, rate limiting)
│   └── server.py              # MCP server entry point
├── docs/                      # Comprehensive documentation
│   ├── tools/                 # Tool reference documentation
│   ├── conversations/         # Usage examples and scenarios
│   ├── models/                # Model documentation
│   └── API_REFERENCES.md      # Complete 3Commas API mapping
└── README.md                  # This file
```

### Running Quality Checks

```bash
uv run mypy .          # Type checking
uv run ruff check .    # Linting  
uv run black .         # Code formatting
```

### Testing the Server

```bash
uv run threecommas-mcp  # Start the MCP server directly
```

---

## Security & Compliance

- **HMAC-SHA256 Authentication**: All API requests use cryptographic signatures for security.
- **Environment Variable Security**: API credentials are passed securely via environment variables.
- **Rate Limiting**: Respects 3Commas API limits to prevent account suspension.
- **Audit Trail**: All operations log API interactions for compliance and debugging.
- **Read-Only Default**: Current implementation focuses on information retrieval with no trading risks.

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the terraform-cloud-mcp reference patterns
4. Run quality checks: `uv run mypy . && uv run ruff check . && uv run black .`
5. Submit a pull request

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## Documentation

- **[Implementation Patterns](docs/PATTERNS.md)** - Definitive patterns reference for new API development
- **[API References](docs/API_REFERENCES.md)** - Complete 3Commas API endpoint mapping with implementation status
- **[Development Guide](docs/DEVELOPMENT.md)** - Contributing and development setup instructions
- **[Tool Documentation](docs/tools/)** - Detailed tool references and usage patterns
- **[Conversation Examples](docs/conversations/)** - Real-world usage scenarios and examples

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Disclaimer

This software is for educational and informational purposes. Trading cryptocurrencies involves substantial risk of loss. Always review bot configurations carefully and never trade with more than you can afford to lose. The authors are not responsible for any trading losses.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-username/3commas-mcp/issues)
- **Documentation**: [docs/](docs/)
- **3Commas API**: [Official Documentation](https://developers.3commas.io/)

---

**Built using [FastMCP](https://gofastmcp.com) and following the [terraform-cloud-mcp](https://github.com/severity1/terraform-cloud-mcp) reference implementation patterns.**