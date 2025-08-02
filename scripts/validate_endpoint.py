#!/usr/bin/env python3
"""
Quick validation for common 3Commas endpoints with accurate token counting.

Uses official Anthropic SDK for token counting as recommended at:
https://docs.anthropic.com/en/docs/build-with-claude/token-counting

Usage:
    python scripts/validate_endpoint.py <endpoint_name>

Available endpoints: strategy_list, dca_bots, accounts, market_pairs
"""

import asyncio
import sys
from pathlib import Path

# Add project to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.test_api import test_api  # noqa: E402

# Test cases for common endpoints
TESTS: dict[str, list[tuple[str, dict[str, str] | None]]] = {
    "strategy_list": [
        ("ver1/bots/strategy_list", None),
        ("ver1/bots/strategy_list", {"account_id": "31337503"}),
    ],
    "dca_bots": [
        ("ver1/bots", {"limit": "5"}),
        ("ver1/bots", {"account_id": "31337503", "limit": "2"}),
    ],
    "accounts": [
        ("ver1/accounts", None),
    ],
    "market_pairs": [
        ("ver1/market_pairs", None),
        ("ver1/market_pairs", {"market_code": "binance"}),
    ],
}


async def validate(endpoint_name: str):
    """Run validation tests for an endpoint."""
    if endpoint_name not in TESTS:
        print(f"Unknown endpoint: {endpoint_name}")
        print(f"Available: {', '.join(TESTS.keys())}")
        return False

    tests = TESTS[endpoint_name]
    print(f"Validating {endpoint_name} ({len(tests)} tests):")
    print("=" * 50)

    for i, (endpoint, params) in enumerate(tests, 1):
        print(f"\nTest {i}/{len(tests)}:")
        await test_api(endpoint, params)

    print("\n" + "=" * 50)
    print("Validation complete")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    asyncio.run(validate(sys.argv[1]))
