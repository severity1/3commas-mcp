# CLAUDE.md for models/

## Context Activation
Activates when creating Pydantic validation models for 3Commas API structures.

## Implementation Pattern
Reference implementation: `dca_bots.py:13-39` (GetDCABotDetailsRequest class)

## Model Structure
- Inherit from APIRequest (base.py:52)
- Field validation with Field() constraints (dca_bots.py:30-38)
- API mapping in docstring (dca_bots.py:19-21)
- Trading context descriptions (dca_bots.py:34-35)

## Base Architecture
- **APIRequest base class** (base.py:52) - All models inherit, includes response_filter
- **ResponseFilter enum** (base.py:34) - DISPLAY/FULL for token optimization
- **Common enums** - BotType, DealStatus, StrategyType, LimitType, MarketCode (base.py:75-178)