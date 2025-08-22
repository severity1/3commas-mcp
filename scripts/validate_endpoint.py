#!/usr/bin/env python3
"""
Quick validation for common 3Commas endpoints with accurate token counting.

Uses official Anthropic SDK for token counting as recommended at:
https://docs.anthropic.com/en/docs/build-with-claude/token-counting

Usage:
    python scripts/validate_endpoint.py <endpoint_name>

Available endpoints: strategy_list, dca_bots, accounts, market_pairs, dca_bot_profit
"""

import asyncio
import sys
from pathlib import Path

# Add project to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.test_api import test_api  # noqa: E402
from threecommas_mcp.api.client import api_request  # noqa: E402

async def get_trading_account_id() -> str | None:
    """Fetch first trading-enabled account ID."""
    try:
        response = await api_request("ver1/accounts")
        # Handle response format (could be dict with 'data' key or direct list)
        if isinstance(response, dict) and "data" in response:
            accounts = response["data"]
        elif isinstance(response, list):
            accounts = response
        else:
            return None
            
        for account in accounts:
            if account.get("trading_supported", False):
                return str(account["id"])
        return None
    except Exception:
        return None


async def get_sample_bot_id() -> str | None:
    """Fetch first available DCA bot ID."""
    try:
        # Call the bots API directly with limit=1 
        response = await api_request("ver1/bots", params={"limit": "1"}, method="GET")
        
        # Handle response format - the MCP tools expect {"data": [...]} format
        if isinstance(response, dict) and "data" in response:
            bots = response["data"]
            if bots and len(bots) > 0:
                return str(bots[0]["id"])
        elif isinstance(response, list) and len(response) > 0:
            # Handle direct list response
            return str(response[0]["id"])
        return None
    except Exception:
        return None


async def build_test_cases() -> dict[str, list[tuple[str, dict[str, str] | None]]]:
    """Build test cases with dynamic IDs."""
    account_id = await get_trading_account_id()
    bot_id = await get_sample_bot_id()
    
    if account_id:
        print(f"📋 Using account ID: {account_id}")
    if bot_id:
        print(f"🤖 Using bot ID: {bot_id}")
    
    tests = {
        "strategy_list": [
            ("ver1/bots/strategy_list", None),
        ],
        "dca_bots": [
            ("ver1/bots", {"limit": "5"}),
        ],
        "accounts": [
            ("ver1/accounts", None),
        ],
        "market_pairs": [
            ("ver1/accounts/market_pairs", None),
            ("ver1/accounts/market_pairs", {"market_code": "binance"}),
        ],
    }
    
    # Add account-specific tests if account ID available
    if account_id:
        tests["strategy_list"].append(("ver1/bots/strategy_list", {"account_id": account_id}))
        tests["dca_bots"].append(("ver1/bots", {"account_id": account_id, "limit": "2"}))
    
    # Add bot-specific tests if bot ID available
    if bot_id:
        tests["dca_bot_profit"] = [
            (f"ver1/bots/{bot_id}/profit_by_day", None),
            (f"ver1/bots/{bot_id}/profit_by_day", {"days": "7"}),
            (f"ver1/bots/{bot_id}/profit_by_day", {"days": "30"}),
            (f"ver1/bots/{bot_id}/profit_by_day", {"days": "90"}),
        ]
    
    return tests


async def validate(endpoint_name: str):
    """Run validation tests for an endpoint."""
    print("🔍 Fetching dynamic account and bot IDs...")
    tests_dict = await build_test_cases()
    
    if endpoint_name not in tests_dict:
        print(f"Unknown endpoint: {endpoint_name}")
        print(f"Available: {', '.join(tests_dict.keys())}")
        return False

    tests = tests_dict[endpoint_name]
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
