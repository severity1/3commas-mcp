# Base Models

## Available Models

### BaseModelConfig

**Purpose:** Foundation configuration for all Pydantic models in the project.

**Used by:** All domain-specific models (account, dca_bots, market_data)

**Key Features:**
- `populate_by_name=True` - Allow field population by alias or field name
- `use_enum_values=True` - Use string values from enums
- `extra="ignore"` - Ignore extra fields to prevent validation errors

### APIRequest

**Purpose:** Base class for all API request models with response filtering.

**Used by:** All tool request models

**Key Fields:**
- `response_filter: ResponseFilter` - Response detail level (default: "display")

**Features:** Inherits BaseModelConfig settings, provides consistent request validation foundation.

### APIResponse

**Purpose:** Type alias for all API response data (`Dict[str, Any]`).

**Used by:** All tools that return 3Commas API data

**Key Features:**
- Unvalidated dictionary containing API response data
- Flexible handling of varying 3Commas response formats
- Response filtering applied before returning to users

### ResponseFilter

**Purpose:** Enum defining response filtering options for token optimization.

**Used by:** All API request models via APIRequest base class

**Values:**
- `DISPLAY = "display"` - Filtered response optimized for display (85% token reduction)
- `FULL = "full"` - Complete API response with all fields

## Common Enums

### BotType

**Purpose:** Defines available bot types for trading operations.

**Values:**
- `DCA = "Bot::DcaBot"` - Dollar Cost Averaging bot
- `GRID = "Bot::GridBot"` - Grid trading bot

### StrategyType

**Purpose:** Defines trading strategy directions.

**Values:**
- `LONG = "long"` - Long positions (buy low, sell high)
- `SHORT = "short"` - Short positions (sell high, buy low)

### DealStatus

**Purpose:** Defines deal lifecycle states for trading operations.

**Values:**
- `CREATED`, `BASE_ORDER_PLACED`, `BOUGHT`, `CANCELLED`, `COMPLETED`, `FAILED`, `PANIC_SELL_PENDING`, `PANIC_SELL_ORDER_PLACED`