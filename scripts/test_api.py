#!/usr/bin/env python3
"""
Simple 3Commas API endpoint tester with accurate token counting.

Uses official Anthropic SDK for token counting as recommended at:
https://docs.anthropic.com/en/docs/build-with-claude/token-counting

Usage:
    python scripts/test_api.py <endpoint> [key=value ...]

Examples:
    python scripts/test_api.py ver1/bots/strategy_list
    python scripts/test_api.py ver1/bots account_id=31337503 limit=5
"""

import asyncio
import json
import sys
from pathlib import Path

# Load environment and add project to path
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from threecommas_mcp.api.client import api_request  # noqa: E402

# Use official Anthropic token counting
try:
    import anthropic
    from typing import Optional, TYPE_CHECKING

    if TYPE_CHECKING:
        _anthropic_client: Optional[anthropic.Anthropic] = None
    else:
        _anthropic_client = anthropic.Anthropic(
            api_key="dummy"  # We only use for token counting, not API calls
        )

    def count_tokens(text: str) -> int:
        """Count tokens using official Anthropic SDK."""
        try:
            if _anthropic_client is None:
                return len(text) // 4  # Simple fallback estimate
            response = _anthropic_client.messages.count_tokens(
                model="claude-3-sonnet-20240229",
                messages=[{"role": "user", "content": text}],
            )
            return int(response.input_tokens)
        except Exception:
            # Simple fallback if API fails
            return len(text) // 4

    has_anthropic = True
except ImportError:
    _anthropic_client = None
    has_anthropic = False

    def count_tokens(text: str) -> int:
        """Simple character-based token estimate."""
        return len(text) // 4


async def test_api(endpoint: str, params: dict | None = None):
    """Test API endpoint and show key metrics."""
    print(f"Testing: GET /{endpoint}")
    if params:
        print(f"Params: {params}")

    try:
        response = await api_request(endpoint, params=params, method="GET")

        if isinstance(response, dict) and "error" in response:
            print(f"❌ Error: {response['error']}")
            return

        response_str = json.dumps(response, separators=(",", ":"))  # Compact
        tokens = count_tokens(response_str)

        print("✅ Success")
        print(f"📏 {len(response_str):,} chars")
        print(
            f"🎯 {tokens:,} tokens (Anthropic SDK)"
            if has_anthropic and _anthropic_client is not None
            else f"🎯 {tokens:,} tokens (estimate)"
        )

        if tokens > 25000:
            print("⚠️  EXCEEDS MCP LIMIT (25,000)!")
        elif tokens > 20000:
            print("⚠️  Near MCP limit (25,000)")
        elif tokens > 15000:
            print("ℹ️  Approaching MCP limit")

        if isinstance(response, dict):
            keys = list(response.keys())[:5]
            print(f"🔑 Keys: {keys}{'...' if len(response.keys()) > 5 else ''}")

    except Exception as e:
        print(f"❌ Exception: {e}")


def parse_args():
    """Parse command line arguments."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    endpoint = sys.argv[1]
    params = {}

    for arg in sys.argv[2:]:
        if "=" in arg:
            key, value = arg.split("=", 1)
            params[key] = value

    return endpoint, params if params else None


if __name__ == "__main__":
    endpoint, params = parse_args()
    asyncio.run(test_api(endpoint, params))
