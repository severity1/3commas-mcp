#!/usr/bin/env python3
"""3Commas MCP Server."""

import logging
from fastmcp import FastMCP

# Import environment configuration
from .utils.env import should_enable_destructive_ops

# Import API client health check
from .api.client import health_check

# Import tools
from .tools import dca_bots, account, market_data

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create server instance
mcp: FastMCP = FastMCP("3Commas MCP Server")

# Check if destructive operations should be enabled
enable_destructive_ops = should_enable_destructive_ops()

# Register health check tool
mcp.tool()(health_check)

# Register DCA bot management tools
mcp.tool()(dca_bots.get_dca_bot_details)

# Register account management tools
mcp.tool()(account.get_connected_exchanges_and_wallets)

# Register market data tools
mcp.tool()(market_data.get_all_market_pairs)
mcp.tool()(market_data.get_currency_rates_and_limits)
mcp.tool()(market_data.get_supported_markets)


def main() -> None:
    """Run the 3Commas MCP server."""

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
