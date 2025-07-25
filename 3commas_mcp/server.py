#!/usr/bin/env python3
"""
3Commas MCP Server
"""

import logging
from fastmcp import FastMCP

# Import environment configuration
from .utils.env import should_enable_destructive_ops

# Import API client health check
from .api.client import health_check

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create server instance
mcp: FastMCP = FastMCP("3Commas MCP Server")

# Check if destructive operations should be enabled
enable_destructive_ops = should_enable_destructive_ops()

# Register health check tool
mcp.tool()(health_check)


def main() -> None:
    """Run the 3Commas MCP server."""

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
