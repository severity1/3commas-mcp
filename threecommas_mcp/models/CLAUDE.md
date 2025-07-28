# CLAUDE.md for @models/

## Context Activation
Activates when creating Pydantic validation models for 3Commas API structures.

## Implementation Pattern
Reference implementation: @threecommas_mcp/models/dca_bots.py:13-39 (GetDCABotDetailsRequest class)

## Model Structure
- Inherit from APIRequest (@threecommas_mcp/models/base.py:52)
- Field validation with Field() constraints (@threecommas_mcp/models/dca_bots.py:30-38)
- API mapping in docstring (@threecommas_mcp/models/dca_bots.py:19-21)
- Trading context descriptions (@threecommas_mcp/models/dca_bots.py:34-35)

## Base Architecture
- **APIRequest base class** (@threecommas_mcp/models/base.py:52) - All models inherit, includes response_filter
- **ResponseFilter enum** (@threecommas_mcp/models/base.py:34) - DISPLAY/FULL for token optimization
- **Common enums** - BotType, DealStatus, StrategyType, LimitType, MarketCode (base.py:75-178)