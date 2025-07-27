# Market Data Conversation Examples

This document provides real-world conversation examples for market data operations using the 3Commas MCP server.

## Overview

Market data conversations demonstrate how to use market-related tools to research trading opportunities, validate trading pairs, understand exchange capabilities, and gather essential information for bot configuration.

## Conversation Examples

### get-all-market-pairs

**Tools used:** [get_all_market_pairs](../tools/market_data.md#get-all-market-pairs)

**Models:** [TradingPair](../models/market_data.md#trading-pair)

**Description:** Research available trading pairs for bot configuration and market analysis.

**User:** "What BTC trading pairs are available on Binance?"

**Assistant:** "I'll check all available BTC trading pairs on Binance for you."

*Uses get_all_market_pairs(market_code="binance")*

**Expected Response:**
```json
{
  "pairs": [
    {
      "pair": "BTC_USDT",
      "base_currency": "BTC",
      "quote_currency": "USDT",
      "market_code": "binance",
      "min_volume": "0.00001",
      "max_volume": "9000.0",
      "volume_precision": 5,
      "price_precision": 2
    },
    {
      "pair": "BTC_BUSD",
      "base_currency": "BTC",
      "quote_currency": "BUSD",
      "market_code": "binance",
      "min_volume": "0.00001",
      "max_volume": "9000.0"
    },
    {
      "pair": "BTC_ETH",
      "base_currency": "BTC", 
      "quote_currency": "ETH",
      "market_code": "binance"
    }
  ]
}
```

**Assistant Analysis:**
- "Found 25+ BTC trading pairs on Binance"
- "Most liquid pairs: BTC_USDT, BTC_BUSD, BTC_ETH"
- "BTC_USDT has the tightest spreads and highest volume"
- "Minimum volume requirement: 0.00001 BTC"

**Safety:** Read-only market research with no trading risks.

**Risk Level:** Low - Information gathering only

### get-currency-rates

**Tools used:** [get_currency_rates_and_limits](../tools/market_data.md#get-currency-rates-and-limits)

**Models:** [CurrencyRate](../models/market_data.md#currency-rate)

**Description:** Getting current rates and trading limits for order calculations.

**User:** "What's the current BTC rate and what are the trading limits?"

**Assistant:** "I'll get the current BTC exchange rate and trading limits for you."

*Uses get_currency_rates_and_limits(pair="BTC_USDT")*

**Expected Response:**
```json
{
  "rates": [
    {
      "currency_code": "BTC",
      "rate_to_usd": "45125.50",
      "min_trading_amount": "0.00001",
      "max_trading_amount": "9000.0",
      "trading_fee": "0.1",
      "precision": 5
    }
  ]
}
```

**Assistant Analysis:**
- "Current BTC price: $45,125.50"
- "Minimum order: 0.00001 BTC ($0.45)"
- "Maximum order: 9,000 BTC"
- "Trading fee: 0.1%"
- "Price precision: 5 decimal places"

**Use Case:** Essential for calculating DCA bot order sizes and profit targets.

**Safety:** Current market data for accurate trading calculations.

**Risk Level:** Low - Rate information only

### get-supported-markets

**Tools used:** [get_supported_markets](../tools/market_data.md#get-supported-markets)

**Models:** [SupportedMarket](../models/market_data.md#supported-market)

**Description:** Understanding exchange compatibility and available features.

**User:** "Which exchanges support DCA bots and what features are available?"

**Assistant:** "I'll check all supported markets and their DCA bot capabilities."

*Uses get_supported_markets()*

**Expected Response:**
```json
{
  "markets": [
    {
      "market_name": "Binance",
      "market_code": "binance",
      "market_type": "spot",
      "is_active": true,
      "supported_features": [
        "dca_bots",
        "grid_bots", 
        "smart_trades",
        "copy_trading"
      ]
    },
    {
      "market_name": "OKX",
      "market_code": "okx",
      "market_type": "spot",
      "is_active": true,
      "supported_features": [
        "dca_bots",
        "grid_bots",
        "smart_trades"
      ]
    },
    {
      "market_name": "Binance Futures",
      "market_code": "binance_futures",
      "market_type": "futures",
      "is_active": true,
      "supported_features": [
        "dca_bots",
        "smart_trades"
      ]
    }
  ]
}
```

**Assistant Analysis:**
- "15 exchanges support DCA bots"
- "Binance: Full feature support including copy trading"
- "OKX: DCA, Grid, and Smart Trading support"
- "Futures markets: Limited to DCA and Smart Trading"
- "All major spot exchanges are currently active"

**Safety:** Validates exchange capabilities before bot configuration.

**Risk Level:** Low - Compatibility information only

## Complex Workflow Examples

### Complete Bot Configuration Research

**Description:** Comprehensive market research before setting up a DCA bot.

**User:** "I want to create a DCA bot for altcoins. Help me research the best setup."

**Assistant Workflow:**

1. **Check Supported Markets**
   *Uses get_supported_markets()*
   "Let me first check which exchanges support DCA bots..."

2. **Research Trading Pairs**
   *Uses get_all_market_pairs(market_code="binance")*
   "Now I'll look at available altcoin pairs on your preferred exchange..."

3. **Get Rate Information**
   *Uses get_currency_rates_and_limits()*
   "Let me check current rates and limits for the most promising pairs..."

**Assistant Recommendations:**
- "Binance offers the most altcoin pairs (450+) with DCA support"
- "High-volume altcoin pairs: ETH_USDT, ADA_USDT, DOT_USDT"
- "Minimum volumes range from $1-10 depending on the altcoin"
- "Consider ETH_USDT for stability or ADA_USDT for higher volatility"

**Safety Considerations:**
- Verified exchange supports DCA bots for chosen pairs
- Checked minimum volume requirements fit user's budget
- Confirmed pairs are actively traded with good liquidity

**Risk Level:** Low - Research and planning only

### Cross-Exchange Arbitrage Research

**Description:** Comparing opportunities across multiple exchanges.

**User:** "Are there arbitrage opportunities between Binance and OKX?"

**Assistant Workflow:**

1. **Check Both Exchanges**
   *Uses get_all_market_pairs(market_code="binance")*
   *Uses get_all_market_pairs(market_code="okx")*

2. **Compare Common Pairs**
   *Uses get_currency_rates_and_limits() for each exchange*

3. **Analyze Opportunities**

**Assistant Analysis:**
- "Found 125 common trading pairs between exchanges"
- "BTC_USDT price difference: Binance $45,125 vs OKX $45,140"
- "ETH_USDT spread: 0.05% difference"
- "Note: Consider trading fees and transfer costs"

**Safety:** Pure research with no trading execution or financial risk.

**Risk Level:** Low - Comparative analysis only

### Trading Limit Validation

**Description:** Ensuring proposed bot configuration fits within exchange limits.

**User:** "I want to create a $50,000 DCA bot with $1,000 base orders. Is this possible?"

**Assistant Workflow:**

1. **Check Currency Limits**
   *Uses get_currency_rates_and_limits(pair="BTC_USDT")*

2. **Validate Configuration**

**Assistant Analysis:**
- "BTC_USDT maximum order: $405M (well within your $1,000 requirement)"
- "Minimum order: $0.45 (your $1,000 base order is valid)"
- "Your $50,000 bot with $1,000 orders = 50 potential safety orders"
- "Configuration is within all exchange limits ✓"

**Safety:** Validates bot parameters against exchange limits before creation.

**Risk Level:** Low - Pre-flight validation only

## Trading Safety Scenarios

### Invalid Pair Warning

```
User: "Create a DCA bot for SCAM_USDT"
Assistant: *Checks get_all_market_pairs()*
Response: "SCAM_USDT is not available on any supported exchanges. Please choose from verified trading pairs only."
```

### Minimum Volume Alert

```
User: "Set up $0.10 BTC orders"
Assistant: *Checks get_currency_rates_and_limits()*
Response: "Warning: $0.10 is below the minimum BTC order size of $0.45. Minimum order would be 0.00001 BTC."
```

### Exchange Downtime Detection

```
User: "Why can't I trade on KuCoin?"
Assistant: *Checks get_supported_markets()*
Response: "KuCoin is currently marked as inactive. Please use an alternative exchange like Binance or OKX."
```

## Market Analysis Patterns

### Trend Analysis Setup
```
1. Get all major pairs for analysis
2. Check current rates and volumes
3. Compare across multiple exchanges
4. Identify high-volume, liquid pairs
5. Recommend optimal pairs for strategy
```

### New Listing Research
```
1. Check supported markets for new listings
2. Verify trading pair availability
3. Analyze minimum volumes and precision
4. Assess exchange support and liquidity
5. Provide launch readiness assessment
```

### Portfolio Diversification
```
1. Research available pairs across asset classes
2. Check correlation between different pairs
3. Validate minimum investment requirements
4. Recommend diversified pair selection
5. Plan risk-appropriate allocation
```

## Related Documentation

- **Tools:** [Market Data Tools](../tools/market_data.md) - Function reference and parameters
- **Models:** [Market Data Models](../models/market_data.md) - Data structures and validation
- **Account Data:** [Account Examples](account-management-conversation.md) - Combining market and account information
- **Bot Configuration:** [DCA Bot Examples](dca-bot-management-conversation.md) - Using market data for bot setup