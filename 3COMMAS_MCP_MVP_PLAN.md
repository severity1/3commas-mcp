# 3Commas MCP Server - MVP Implementation Plan

## Executive Summary

This document outlines the MVP (Minimum Viable Product) implementation plan for a Model Context Protocol (MCP) server that integrates Claude with the 3Commas cryptocurrency trading platform API. The MCP server will enable Claude to help users build, configure, and optimize DCA (Dollar Cost Averaging) bots and trading strategies through natural conversation.

## Project Overview

**Project Name:** 3commas-mcp  
**Target Framework:** FastMCP (Python 3.12+)  
**Reference Implementation:** terraform-cloud-mcp  
**API Base URL:** https://api.3commas.io  
**Authentication:** API Key + Signature-based  
**Current Status:** Foundation Complete - Ready for Implementation

## 🎯 **Bootstrap Progress Summary**

### ✅ **Phase 0: Foundation & Documentation (COMPLETED)**
**Completion Date:** Current  
**Key Achievements:**
- **Complete Memory System**: Full CLAUDE.md ecosystem with component-specific guidance
- **Documentation Architecture**: 4-layer system (conversations/models/tools/code) with templates
- **Reference Validation**: 100% structural alignment with terraform-cloud-mcp patterns  
- **API Planning**: Comprehensive API reference with MVP priorities and risk classifications
- **Development Standards**: Complete development, contributing, and quality guidelines
- **Cross-Reference System**: Bidirectional linking across all documentation layers

**Foundation Quality Score: 100%** - Ready for implementation with comprehensive guidance 

## MVP Scope & Priorities

### Phase 1: DCA Bot Building & Strategy Development (MVP)
Focus on APIs that enable building, configuring, and optimizing DCA bots:

#### 1. DCA Bot Creation & Configuration ⭐ (Core Value)
- **Create DCA Bot** - Build new bots with custom parameters
- **Update Bot Configuration** - Modify existing bot settings
- **Get Bot Details** - Retrieve bot configuration and status
- **Clone/Copy Bot** - Duplicate successful bot configurations
- **Delete Bot** - Remove bots (with safety checks)

#### 2. Strategy Management ⭐ (Intelligence Layer)
- **Get Available Strategies** - List all trading strategies
- **Get Strategy Details** - Configuration options for each strategy
- **QFL Strategy Config** - Quick Fingers Luc strategy settings
- **RSI Strategy Config** - RSI indicator-based strategies
- **Bollinger Bands Config** - BB strategy parameters
- **MACD Strategy Config** - MACD-based trading signals
- **Moving Average Config** - MA strategy settings
- **Custom Signal Integration** - External signal webhooks

#### 3. Market Data & Pair Management ⭐ (Foundation)
- **Get Market Pairs** - Available trading pairs per exchange
- **Get Currency Rates** - Current exchange rates
- **Manage Pairs Blacklist** - Control which pairs to avoid
- **Get Account Info** - Exchange account details and permissions

#### 4. Bot Testing & Validation ⭐ (Quality Assurance)
- **Enable/Disable Bot** - Control bot activation safely
- **Get Bot Performance Stats** - Historical performance data
- **Deal History Analysis** - Past deal outcomes and patterns
- **Safety Order Management** - Configure and test safety orders

### Phase 2: Advanced Features (Post-MVP)
- Smart Trade creation and management
- Grid Bot operations
- Advanced portfolio analytics
- Webhook management for external signals
- TradingView integration
- Risk management and position sizing

## Technical Architecture

### Project Structure
Following terraform-cloud-mcp patterns:

```
3commas_mcp/
├── __init__.py
├── server.py                 # Main MCP server entry point
├── api/
│   ├── __init__.py
│   └── client.py            # 3Commas API client with auth
├── models/
│   ├── __init__.py
│   ├── base.py              # Base models and config
│   ├── accounts.py          # Account and exchange models
│   ├── bots.py              # DCA bot creation/config models
│   ├── strategies.py        # Trading strategy models
│   ├── pairs.py             # Market pairs and blacklist models
│   └── deals.py             # Deal and safety order models
├── tools/
│   ├── __init__.py
│   ├── accounts.py          # Account and exchange tools
│   ├── bots.py              # DCA bot creation/management tools
│   ├── strategies.py        # Strategy configuration tools
│   ├── pairs.py             # Market data and pair management tools
│   └── deals.py             # Deal analysis and safety orders
└── utils/
    ├── __init__.py
    ├── auth.py              # 3Commas signature authentication
    ├── decorators.py        # Error handling decorators
    ├── env.py               # Environment configuration
    └── filters.py           # Response filtering utilities
```

### Dependencies
```toml
[project]
dependencies = [
    "fastmcp>=2.9.1",
    "httpx>=0.28.1", 
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
    "cryptography>=41.0.0"  # For signature generation
]
```

## Authentication & Security

### 3Commas API Authentication
3Commas uses API Key + Signature authentication:

```python
# Required headers for each request
headers = {
    "APIKEY": api_key,
    "APISIGN": generate_signature(query_string, secret_key)
}
```

### Environment Variables
```bash
3COMMAS_API_KEY=your_3commas_api_key
3COMMAS_SECRET_KEY=your_3commas_secret_key
3COMMAS_ENABLE_DESTRUCTIVE=false  # Enable bot disable/delete operations
```

### Security Considerations
- API credentials stored in environment variables only
- Signature-based request authentication
- Rate limiting compliance (300 req/min standard, 60 req/min trading)
- Destructive operations (disable/delete bots) behind feature flag
- Sensitive data masking in logs

## Core Implementation Details

### 1. API Client (`api/client.py`)
```python
async def api_request(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict] = None,
    data: Optional[Dict] = None
) -> Dict[str, Any]:
    """Make authenticated request to 3Commas API"""
    # Generate signature
    # Add required headers  
    # Handle rate limiting
    # Process response
```

### 2. Authentication Utils (`utils/auth.py`)
```python
def generate_signature(query_string: str, secret: str) -> str:
    """Generate HMAC-SHA256 signature for 3Commas API"""
    
def build_query_string(params: Dict) -> str:
    """Build properly formatted query string"""
```

### 3. Tool Implementation Pattern
```python
@handle_api_errors
async def create_dca_bot(
    account_id: int,
    pair: str,
    base_order_volume: float,
    safety_order_volume: float,
    strategy: str,
    params: Optional[BotParams] = None
) -> APIResponse:
    """Create new DCA bot with specified configuration
    
    Args:
        account_id: Exchange account ID
        pair: Trading pair (e.g., "BTCUSDT")
        base_order_volume: Initial order size
        safety_order_volume: Safety order size
        strategy: Trading strategy to use
        params: Additional bot parameters
    
    Returns:
        Created bot details with ID and configuration
    """
```

## MVP Endpoints Mapping

### DCA Bot Creation & Management
| Tool Function | 3Commas Endpoint | Method | Description |
|---------------|------------------|---------|-------------|
| `create_dca_bot` | `/ver1/bots/create_bot` | POST | Create new DCA bot with config |
| `update_bot_config` | `/ver1/bots/{id}/update` | PATCH | Update bot configuration |
| `get_bot_details` | `/ver1/bots/{id}/show` | GET | Get bot config and status |
| `list_bots` | `/ver1/bots` | GET | List all DCA bots |
| `clone_bot` | `/ver1/bots/{id}/copy` | POST | Duplicate bot configuration |
| `delete_bot` | `/ver1/bots/{id}/delete` | POST | Remove bot (destructive) |
| `enable_bot` | `/ver1/bots/{id}/enable` | POST | Activate bot trading |
| `disable_bot` | `/ver1/bots/{id}/disable` | POST | Pause bot trading |

### Strategy Configuration
| Tool Function | 3Commas Endpoint | Method | Description |
|---------------|------------------|---------|-------------|
| `get_strategy_list` | `/ver1/bots/strategy_list` | GET | Available trading strategies |
| `get_qfl_strategy` | `/ver1/bots/qfl_strategy` | GET | QFL strategy parameters |
| `get_rsi_strategy` | `/ver1/bots/rsi_strategy` | GET | RSI strategy configuration |
| `get_bb_strategy` | `/ver1/bots/bollinger_strategy` | GET | Bollinger Bands settings |
| `get_macd_strategy` | `/ver1/bots/macd_strategy` | GET | MACD strategy parameters |
| `get_ma_strategy` | `/ver1/bots/ma_strategy` | GET | Moving Average configuration |
| `create_custom_signal` | `/ver1/bots/custom_signal` | POST | Setup external signal webhook |

### Market Data & Pairs
| Tool Function | 3Commas Endpoint | Method | Description |
|---------------|------------------|---------|-------------|
| `get_market_pairs` | `/ver1/bots/pairs` | GET | Available trading pairs |
| `get_currency_rates` | `/ver1/bots/currency_rates` | GET | Current exchange rates |
| `get_pairs_blacklist` | `/ver1/bots/pairs_black_list` | GET | Blacklisted trading pairs |
| `update_pairs_blacklist` | `/ver1/bots/update_pairs_black_list` | POST | Modify pairs blacklist |
| `list_accounts` | `/ver1/accounts` | GET | Exchange accounts |
| `get_account_info` | `/ver1/accounts/{id}` | GET | Account details |

### Deal Analysis & Safety Orders
| Tool Function | 3Commas Endpoint | Method | Description |
|---------------|------------------|---------|-------------|
| `get_bot_stats` | `/ver1/bots/{id}/stats` | GET | Bot performance metrics |
| `get_bot_deals` | `/ver1/bots/{id}/deals` | GET | Bot deal history |
| `get_deal_details` | `/ver1/deals/{id}/show` | GET | Specific deal information |
| `add_safety_order` | `/ver1/deals/{id}/add_safety_order` | POST | Manual safety order |
| `get_deals_stats` | `/ver1/bots/deals_stats` | GET | Overall deal statistics |
| `cancel_deal` | `/ver1/deals/{id}/cancel` | POST | Cancel active deal |
| `update_deal` | `/ver1/deals/{id}/update` | PATCH | Modify deal parameters |

## Error Handling & Rate Limiting

### Rate Limits
- **Standard endpoints:** 300 requests/minute
- **Trading endpoints:** 60 requests/minute  
- **Statistics endpoints:** 120 requests/minute

### Error Handling Strategy
```python
@handle_api_errors
async def tool_function():
    """Decorator handles:
    - Rate limiting (429 errors)
    - Authentication errors (401)
    - API errors (4xx/5xx)
    - Network timeouts
    - Malformed responses
    """
```

## Testing Strategy

### Authentication Testing
- HMAC-SHA256 signature generation validation
- API credential handling and security
- Authentication flow verification

### API Testing
- Live API connectivity validation
- Rate limiting behavior verification
- Request/response handling validation

### Safety Validation
- Trading parameter validation and safety checks
- Bot configuration validation and security verification
- Error handling and recovery scenario testing

## Deployment & Configuration

### Package Configuration (`pyproject.toml`)
```toml
[project]
name = "3commas-mcp"
version = "0.1.0"
description = "A Model Context Protocol server for 3Commas cryptocurrency trading platform"
requires-python = ">=3.12"

[project.scripts]
3commas-mcp = "3commas_mcp.server:main"
```

### Environment Setup
```bash
# Create .env file
3COMMAS_API_KEY=your_api_key_here
3COMMAS_SECRET_KEY=your_secret_key_here
3COMMAS_ENABLE_DESTRUCTIVE=false
```

### MCP Client Configuration
```json
{
  "mcpServers": {
    "3commas": {
      "command": "3commas-mcp",
      "env": {
        "3COMMAS_API_KEY": "your_api_key",
        "3COMMAS_SECRET_KEY": "your_secret_key"
      }
    }
  }
}
```

## Development Milestones

### Milestone 1: Foundation ✅ **COMPLETED**
- [x] Project structure and dependencies framework
- [x] Complete CLAUDE.md ecosystem with subtree discovery
- [x] Component-specific memory files (api/, tools/, models/, utils/, docs/)
- [x] 4-layer documentation architecture (conversations/models/tools/code)
- [x] Core documentation infrastructure (DEVELOPMENT.md, CONTRIBUTING.md, README.md)
- [x] API reference with MVP priorities and risk classifications
- [x] Cross-reference system and documentation templates
- [x] Validation against terraform-cloud-mcp reference patterns
- ✅ Essential utilities implementation (auth, env, decorators) - **COMPLETED**
- [ ] API client with authentication (HMAC-SHA256) - **NEXT**
- [ ] Base models and error handling - **NEXT**
- [ ] FastMCP server setup with health check - **NEXT**

### Milestone 2: Core Bot Features ⏸️ **NEXT PHASE**
- [ ] DCA bot creation and management tools
- [ ] Strategy configuration tools  
- [ ] Bot performance and stats tools
- [ ] Deal analysis and safety orders

### Milestone 3: Advanced Features ⏸️ **FUTURE**
- [ ] Bot cloning and templates
- [ ] Custom signal integration
- [ ] Advanced market data tools
- [ ] Comprehensive validation suite

### Milestone 4: Polish & Release ⏸️ **FUTURE**
- [ ] Enhanced documentation and examples
- [ ] Error handling refinements
- [ ] Performance optimizations
- [ ] Package publishing and distribution

## Success Metrics

### Technical Metrics
- All DCA bot creation and strategy endpoints implemented
- <200ms average response time for bot operations
- 99%+ API call success rate for bot management
- Comprehensive test coverage (>90%)

### User Experience Metrics
- Claude can create and configure DCA bots through conversation
- Users can explore and apply different trading strategies
- Bot performance analysis provides optimization insights
- Market data helps inform bot configuration decisions

## Risk Mitigation

### Technical Risks
- **API Changes:** Monitor 3Commas API changelog, implement versioning
- **Rate Limiting:** Implement exponential backoff, request queuing
- **Authentication:** Secure credential handling, token rotation support

### Business Risks  
- **API Access:** Ensure compatibility with free tier limitations
- **User Adoption:** Focus on most valuable features first (bot creation, strategies)
- **Maintenance:** Plan for ongoing API updates and bug fixes

## Future Roadmap (Post-MVP)

### Phase 2: Smart Trading
- Smart trade creation and management
- Advanced order types and configurations
- Risk management and position sizing
- Portfolio rebalancing strategies

### Phase 3: Grid & Advanced Bots
- Grid bot operations and optimization
- Multi-pair bot strategies
- Advanced safety order algorithms
- Backtesting and simulation

### Phase 4: Integration & Automation
- TradingView signal integration
- Webhook automation and management
- Advanced analytics and reporting
- Community strategy sharing