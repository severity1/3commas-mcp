"""Response filtering utilities for token efficiency

This module provides filtering functions to reduce API response size
while maintaining necessary context for different use cases.
"""

from typing import Dict, Any, Union
import logging

logger = logging.getLogger(__name__)


def filter_response(data: Dict[str, Any], filter_type: str) -> Dict[str, Any]:
    """Filter API response based on use case requirements.

    Args:
        data: Raw API response data
        filter_type: Type of filtering to apply ("full" or "display")

    Returns:
        Filtered response data

    Raises:
        ValueError: If filter_type is not supported
    """
    if filter_type not in ["full", "display"]:
        raise ValueError(
            f"Invalid filter_type: {filter_type}. Must be 'full' or 'display'"
        )

    # Always apply security filtering
    filtered_data = _apply_security_filter(data.copy())

    # Always apply redundant field removal for token efficiency
    filtered_data = _remove_redundant_fields(filtered_data)

    # Apply additional filtering for display mode
    if filter_type == "display":
        filtered_data = _apply_display_filter(filtered_data)

    return filtered_data


def _apply_security_filter(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove security-sensitive fields from response.

    This filter is always applied regardless of filter type.
    """
    security_fields = ["url_secret", "account_id"]

    for field in security_fields:
        if field in data:
            del data[field]
            logger.debug(f"Removed security field: {field}")

    return data


def _apply_display_filter(data: Dict[str, Any]) -> Dict[str, Any]:
    """Apply display-optimized filtering for token efficiency."""

    # Replace pairs array with count
    if "pairs" in data and isinstance(data["pairs"], list):
        pairs_count = len(data["pairs"])
        del data["pairs"]
        data["pairs_count"] = pairs_count
        logger.debug(f"Replaced pairs array with count: {pairs_count}")

    # Keep only recent 3 bot events
    if "bot_events" in data and isinstance(data["bot_events"], list):
        original_count = len(data["bot_events"])
        data["bot_events"] = data["bot_events"][:3]
        logger.debug(
            f"Reduced bot_events from {original_count} to {len(data['bot_events'])}"
        )

    # Remove crypto_widget objects from active deals
    if "active_deals" in data and isinstance(data["active_deals"], list):
        for deal in data["active_deals"]:
            if isinstance(deal, dict) and "crypto_widget" in deal:
                del deal["crypto_widget"]
        logger.debug("Removed crypto_widget objects from active deals")

    # Remove null/empty fields
    data = _remove_null_empty_fields(data)

    return data


def _remove_null_empty_fields(
    data: Union[Dict[str, Any], Any],
) -> Union[Dict[str, Any], Any]:
    """Recursively remove null, empty string, and empty array fields."""
    if not isinstance(data, dict):
        return data

    cleaned_data = {}
    removed_count = 0

    for key, value in data.items():
        if value is None or value == [] or value == {}:
            removed_count += 1
            continue
        elif isinstance(value, dict):
            cleaned_value = _remove_null_empty_fields(value)
            if cleaned_value:  # Only keep non-empty dicts
                cleaned_data[key] = cleaned_value
            else:
                removed_count += 1
        elif isinstance(value, list):
            # Clean each item in the list if it's a dict
            cleaned_list = []
            for item in value:
                if isinstance(item, dict):
                    cleaned_item = _remove_null_empty_fields(item)
                    if cleaned_item:  # Only keep non-empty dicts
                        cleaned_list.append(cleaned_item)
                else:
                    cleaned_list.append(item)
            if cleaned_list:  # Only keep non-empty lists
                cleaned_data[key] = cleaned_list
            else:
                removed_count += 1
        else:
            cleaned_data[key] = value

    if removed_count > 0:
        logger.debug(f"Removed {removed_count} null/empty fields")

    return cleaned_data


def _remove_redundant_fields(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove fields from active deals that duplicate bot-level data.

    This reduces token usage by eliminating redundant information that's
    available at the parent bot level.
    """
    # Fields that duplicate bot-level configuration data
    redundant_fields = [
        "bot_name",  # Available as bot.name
        "account_name",  # Available as bot.account_name
        "leverage_type",  # Available as bot.leverage_type
        "strategy",  # Available as bot.strategy
        "bot_id",  # Available as bot.id (and redundant since deals are nested)
        "base_order_volume",  # Available as bot.base_order_volume
        "safety_order_volume",  # Available as bot.safety_order_volume
        "take_profit",  # Available as bot.take_profit
        "safety_order_step_percentage",  # Available as bot.safety_order_step_percentage
        "safety_order_calculation_mode",  # Available as bot.safety_order_calculation_mode
        "take_profit_type",  # Available as bot.take_profit_type
        "martingale_volume_coefficient",  # Available as bot.martingale_volume_coefficient
        "martingale_step_coefficient",  # Available as bot.martingale_step_coefficient
        "stop_loss_percentage",  # Available as bot.stop_loss_percentage
        "profit_currency",  # Available as bot.profit_currency
        "stop_loss_type",  # Available as bot.stop_loss_type
        "safety_order_volume_type",  # Available as bot.safety_order_volume_type
        "base_order_volume_type",  # Available as bot.base_order_volume_type
        "trailing_deviation",  # Available as bot.trailing_deviation
        "min_profit_percentage",  # Available as bot.min_profit_percentage
    ]

    # Remove redundant fields from active deals
    if "active_deals" in data and isinstance(data["active_deals"], list):
        removed_fields_count = 0
        for deal in data["active_deals"]:
            if isinstance(deal, dict):
                for field in redundant_fields:
                    if field in deal:
                        del deal[field]
                        removed_fields_count += 1

        if removed_fields_count > 0:
            logger.debug(
                f"Removed {removed_fields_count} redundant fields from active deals"
            )

    return data
