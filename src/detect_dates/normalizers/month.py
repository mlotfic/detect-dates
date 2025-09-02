#!/usr/bin/env python3
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides functions to normalize month names across different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing month names
    for Gregorian, Hijri (Islamic), and Persian (Jalali) calendars.
"""

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

# Import necessary modules
from detect_dates.keywords import (
    months_standard_keywords,  # Standard month names for different languages and calendars
    months_variations_list,  # All month keywords for normalization
    search_in_keywords
)

def normalize_key(input_key: str):
    """
    Detect calendar type and language from input key.

    Args:
        input_key (str): The input key indicating calendar type and language

    Returns:
        tuple: (calendar_type, language) or (None, None) if no match found
    """
    # Define supported calendar types with their language variants
    supported_calendar_types = [
        "gregorian_ar", "hijri_ar", "persian_ar",
        "gregorian_en", "hijri_en", "persian_en"
    ]

    # Check each calendar type to find a match
    for calendar_type in supported_calendar_types:
        if input_key.startswith(calendar_type):
            language = "ar" if calendar_type.endswith("ar") else "en"
            return calendar_type, language

    # Return None values if no match is found
    return None, None

from typing import Union, Tuple, Dict, Optional
import logging
from enum import Enum

# Set up logging
logger = logging.getLogger(__name__)

# ===================================================================================
# CONSTANTS AND ENUMS
# ===================================================================================

class Language(Enum):
    ARABIC = "ar"
    ENGLISH = "en"

class Calendar(Enum):
    HIJRI = "hijri"
    GREGORIAN = "gregorian"
    PERSIAN = "persian"
    JULIAN = "julian"

class OutputFormat(Enum):
    NUMBER = "num"
    FULL = "full"
    ABBREVIATED = "abbr"

SUPPORTED_LANGUAGES = {lang.value for lang in Language}
SUPPORTED_CALENDARS = {cal.value for cal in Calendar}
DEFAULT_LANGUAGE = Language.ARABIC.value
DEFAULT_CALENDAR = ""

# ===================================================================================
# HELPER FUNCTIONS
# ===================================================================================

def get_month_info(month: Union[str, int]) -> Tuple[Optional[str], Optional[str], Optional[int]]:
    """
    Extract calendar type, language, and month index from month name input.

    This function identifies the calendar system and language of a given month name,
    returning the detected calendar type, language, and month position.

    Args:
        month (Union[str, int]): Month name in any supported language (case-insensitive) or month number (1-12)

    Returns:
        Tuple[Optional[str], Optional[str], Optional[int]]:
            - detected_calendar: Calendar system ('gregorian', 'hijri', 'persian') or None
            - detected_language: Language code ('ar', 'en', 'fa') or None
            - month_index: Zero-based month position (0-11), or None if not found

    Examples:
        >>> get_month_info("January")
        ('gregorian', 'en', 0)

        >>> get_month_info("محرم")
        ('hijri', 'ar', 0)

        >>> get_month_info(1)
        (None, None, 0)  # Generic month number, no specific calendar/language

    Note:
        - Input is case-insensitive and whitespace is stripped for strings
        - Returns (None, None, None) if month not found in any calendar system
        - For integer input (1-12), returns (None, None, month_index) since no specific calendar is implied
        - Supports multiple calendar systems: Gregorian, Hijri (Islamic), Persian (Jalali)
    """
    # Handle integer input
    if isinstance(month, int):
        if 1 > month > 12:
            logger.warning(f"Invalid month number '{month}'. Must be between 1 and 12.")
            return None, None, None

    # Input validation for string
    if not isinstance(month, str) or not month.strip():
        logger.error(f"Invalid input type '{type(month)}'. Expected str or int.")
        return None, None, None

    # Normalize inputs
    search_month = str(month).lower().strip()

    # Search for month in keywords
    matching_key, detected_idx = search_in_keywords(search_month, months_variations_list)

    if matching_key is None:
        logger.warning(f"Month '{month}' not found in any keyword list")
        return None, None, None

    detected_key, detected_lang = normalize_key(matching_key)
    if detected_key is not None:
        detected_calendar = detected_key.replace(f"_{detected_lang}", "")
        return detected_calendar, detected_lang, detected_idx
    else:
        return None, None, None

# ===================================================================================
# MAIN FUNCTIONS
# ===================================================================================

def normalize_month(
    month: Union[int, str],
    to_lang: Optional[str] = None,
    to_calendar: Optional[str] = None,
    output_format: Optional[str] = None
) -> Optional[Union[str, int]]:
    """
    Normalize month names from various calendar systems to specified format.

    Args:
        month (Union[int, str]): Month name in any supported language/calendar system or month number (1-12)
        to_lang (Optional[str]): Target language ('ar', 'en', 'fa'). If None, uses detected language.
        to_calendar (Optional[str]): Target calendar ('hijri', 'gregorian', 'persian', 'julian').
                                   If None, uses detected calendar.
        output_format (Optional[str]): Output format ('num', 'full', 'abbr').
                                     If None, defaults to 'num' for number output.

    Returns:
        Optional[Union[str, int]]: Normalized month representation or None if conversion fails

    Examples:
        >>> normalize_month("January", output_format="num")
        1

        >>> normalize_month("January", to_lang="ar", to_calendar="hijri", output_format="full")
        "محرم"

        >>> normalize_month(1, to_lang="en", to_calendar="gregorian", output_format="abbr")
        "Jan"
    """

    def _to_num(idx: Optional[int]) -> Optional[int]:
        """Convert 0-based index to 1-based month number."""
        return idx + 1 if idx is not None and 0 <= idx <= 11 else None

    def _to_full(idx: Optional[int], calendar: Optional[str], lang: Optional[str]) -> Optional[str]:
        """Convert to full month name."""
        if idx is None or calendar is None or lang is None:
            return None
        if not (0 <= idx <= 11):
            return None

        try:
            key = f"{calendar}_{lang}"
            if key in months_standard_keywords:
                return months_standard_keywords[key][idx]
        except (KeyError, IndexError) as e:
            logger.error(f"Error accessing month data for {key}[{idx}]: {e}")
        return None

    def _to_abbr(idx: Optional[int], calendar: Optional[str], lang: Optional[str]) -> Optional[str]:
        """Convert to abbreviated month name."""
        if idx is None or calendar is None or lang is None:
            return None
        if not (0 <= idx <= 11):
            return None

        try:
            # Special case for Gregorian English abbreviations
            if calendar.lower() == "gregorian" and lang == "en":
                abbr_key = "gregorian_en_abbr"
                if abbr_key in months_standard_keywords:
                    return months_standard_keywords[abbr_key][idx]

            # Fall back to full name for other calendar/language combinations
            return _to_full(idx, calendar, lang)
        except Exception as e:
            logger.error(f"Error getting abbreviated month: {e}")
        return None

    # Get month information
    detected_calendar, detected_lang, detected_idx = get_month_info(month)

    if detected_idx is None:
        return None

    # Determine target language
    target_lang = detected_lang
    if to_lang and to_lang.lower() in SUPPORTED_LANGUAGES:
        target_lang = to_lang.lower()

    # Determine target calendar
    target_calendar = detected_calendar
    if to_calendar:
        calendar_lower = to_calendar.lower().strip()
        if calendar_lower in SUPPORTED_CALENDARS:
            target_calendar = calendar_lower
            # Special handling for Julian calendar
            if calendar_lower == "julian":
                target_calendar = "persian"  # Julian maps to Persian calendar

    # Determine output format
    format_type = output_format or OutputFormat.NUMBER.value

    # Convert based on requested format
    if format_type == OutputFormat.NUMBER.value:
        return _to_num(detected_idx)
    elif format_type == OutputFormat.FULL.value:
        return _to_full(detected_idx, target_calendar, target_lang)
    elif format_type == OutputFormat.ABBREVIATED.value:
        return _to_abbr(detected_idx, target_calendar, target_lang)
    else:
        logger.warning(f"Unknown output format '{format_type}'. Defaulting to number.")
        return _to_num(detected_idx)


# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================

def get_supported_languages() -> set:
    """Return set of supported languages."""
    return SUPPORTED_LANGUAGES.copy()

def get_supported_calendars() -> set:
    """Return set of supported calendars."""
    return SUPPORTED_CALENDARS.copy()

def is_valid_month_name(month: str) -> bool:
    """
    Check if a given string is a valid month name in any supported language/calendar.

    Args:
        month (str): Month name to validate

    Returns:
        bool: True if valid month name, False otherwise
    """
    if not isinstance(month, str) or not month.strip():
        return False

    search_month = month.lower().strip()
    matching_key, _ = search_in_keywords(search_month, months_variations_list)

    return matching_key is not None