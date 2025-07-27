# Account Management Conversation Examples

This document provides real-world conversation examples for account management operations using the 3Commas MCP server.

## Overview

Account management conversations demonstrate how to use account-related tools to gather essential trading information, validate account capabilities, and prepare for bot operations.

## Conversation Examples

### get-connected-exchanges

**Tools used:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Models:** [ConnectedExchange](../models/account.md#connected-exchange), [ExchangeBalance](../models/account.md#exchange-balance)

**Description:** Basic account information retrieval to understand available exchanges and trading capabilities.

**User:** "Show me all my connected exchanges and their status"

**Assistant:** "I'll retrieve your connected exchange accounts and their current status."

*Uses get_connected_exchanges_and_wallets()*

**Expected Response:**
```json
{
  "exchanges": [
    {
      "id": 12345,
      "name": "binance",
      "account_name": "Main Trading Account",
      "market_code": "binance",
      "is_locked": false,
      "created_at": "2024-01-15T10:30:00Z",
      "balances": [
        {
          "currency_code": "USDT",
          "total_balance": "5000.00",
          "available_balance": "4500.00",
          "reserved_balance": "500.00",
          "usd_value": "5000.00"
        },
        {
          "currency_code": "BTC",
          "total_balance": "0.15",
          "available_balance": "0.12",
          "reserved_balance": "0.03",
          "usd_value": "6750.00"
        }
      ]
    },
    {
      "id": 67890,
      "name": "okx",
      "account_name": "Secondary Account",
      "market_code": "okx",
      "is_locked": false,
      "created_at": "2024-02-01T14:20:00Z"
    }
  ]
}
```

**Safety:** Read-only operation with no trading risks. Sensitive account information automatically filtered.

**Risk Level:** Low - Information retrieval only

### Exchange Validation for Bot Setup

**Tools used:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Description:** Validating exchange accounts before configuring a DCA bot.

**User:** "I want to create a DCA bot for BTC/USDT. Which exchanges can I use?"

**Assistant:** "Let me check your connected exchanges and their capabilities for DCA bot trading."

*Uses get_connected_exchanges_and_wallets()*

**Assistant Analysis:**
- "You have 2 connected exchanges: Binance and OKX"
- "Both exchanges support DCA bots and BTC/USDT trading"
- "Binance account: Available USDT: $4,500, Available BTC: 0.12"
- "OKX account: Balance information needs to be loaded"
- "Recommendation: Use Binance for sufficient USDT balance"

**Safety Considerations:**
- Verified account is not locked before recommending for bot use
- Checked available balances to ensure sufficient funds
- Confirmed exchange supports desired trading pair

**Risk Level:** Low - Preparation and validation only

### Account Status Check

**Tools used:** [get_connected_exchanges_and_wallets](../tools/account.md#get-connected-exchanges-and-wallets)

**Description:** Checking account health and troubleshooting connection issues.

**User:** "Why can't I create bots? Are my exchange connections working?"

**Assistant:** "I'll check your exchange account connections and their status to identify any issues."

*Uses get_connected_exchanges_and_wallets()*

**Potential Issues Identified:**
- Account is locked: `"is_locked": true`
- No exchanges connected: Empty response
- Exchange connection error: API error returned
- Insufficient permissions: Missing trading permissions

**Assistant Response Examples:**
- **Healthy Account:** "All 2 exchanges are connected and active. No issues detected."
- **Locked Account:** "Your Binance account appears to be locked. Please check your exchange API settings."
- **No Connections:** "No exchange accounts are currently connected. You'll need to add an exchange account first."

**Safety:** Identifies potential issues that could affect trading safety and bot operations.

**Risk Level:** Low - Diagnostic information only

## Usage Patterns

### Pre-Bot Configuration Workflow
```
1. User: "I want to set up automated trading"
2. Assistant: Check connected exchanges
3. Assistant: Validate account permissions and balances
4. Assistant: Recommend suitable exchanges for bot type
5. Assistant: Guide to next steps (market data, bot configuration)
```

### Account Health Monitoring
```
1. User: "Check my account status"
2. Assistant: Retrieve all exchange connections
3. Assistant: Analyze account health and capabilities
4. Assistant: Report any issues or limitations
5. Assistant: Suggest fixes for identified problems
```

### Exchange Selection Guidance
```
1. User: "Which exchange should I use for [specific strategy]?"
2. Assistant: Get connected exchanges and capabilities
3. Assistant: Analyze balances and supported features
4. Assistant: Recommend optimal exchange for strategy
5. Assistant: Explain reasoning and next steps
```

## Trading Safety Scenarios

### Locked Account Detection
```
User: "Set up a DCA bot on Binance"
Assistant: *Checks account status*
Response: "Cannot proceed - your Binance account is currently locked. Please check your API settings and trading permissions before creating bots."
```

### Insufficient Balance Warning
```
User: "Create a $10,000 DCA bot"
Assistant: *Checks available balances*
Response: "Warning: Your available USDT balance ($4,500) is insufficient for a $10,000 DCA bot. Consider reducing the bot size or adding funds."
```

### No Exchange Connection
```
User: "List my bots"
Assistant: *Checks connected exchanges*
Response: "No exchange accounts are connected to your 3Commas account. You'll need to connect an exchange before creating or managing bots."
```

## Related Documentation

- **Tools:** [Account Management Tools](../tools/account.md) - Function reference and parameters
- **Models:** [Account Models](../models/account.md) - Data structures and validation
- **Bot Setup:** [DCA Bot Examples](dca-bot-management-conversation.md) - Using account data for bot configuration
- **Market Data:** [Market Data Examples](market-data-conversation.md) - Combining account and market information