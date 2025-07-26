"""Data models for 3Commas MCP"""

# Re-export the base models for easier access
from .base import (  # noqa: F401
    BaseModelConfig,
    APIRequest,
    APIResponse,
    ReqT,
    BotType,
    DealStatus,
    StrategyType,
)

# Define __all__ to control what's imported with wildcard imports
__all__ = [
    # Base models
    "BaseModelConfig",
    "APIRequest",
    "APIResponse",
    "ReqT",
    # Common enums
    "BotType",
    "DealStatus",
    "StrategyType",
]
