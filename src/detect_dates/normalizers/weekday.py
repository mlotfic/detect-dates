#!/usr/bin/env python3
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi
@description: This module provides weekday name extraction and normalization utilities.
'''

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

# Import necessary modules
from detect_dates.keywords import weekdays_keywords  # Import weekday keywords

# Import weekday variations and normalization data
from detect_dates.keywords import (
    weekdays_variations_list,  # Variations of weekday names
    weekdays_standard_keywords,  # Normalized weekday names
    search_in_keywords
)

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
    FARSI_ARABIC = "fa_ar"
    FARSI_ENGLISH = "fa_en"

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

# Weekday index mapping (0-based)
WEEKDAY_COUNT = 7

# ===================================================================================
# HELPER FUNCTIONS
# ===================================================================================
def normalize_key(input_key: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Detect calendar type and language from input key.

    Args:
        input_key (str): The input key indicating calendar type and language

    Returns:
        tuple: (calendar_type, language) or (None, None) if no match found
    """
    # Define supported calendar types with their language variants
    supported_calendar_types = [
        "weekdays_ar", "weekdays_en",
        "weekdays_fa_ar", "weekdays_fa_en", "num"
    ]

    # Check each calendar type to find a match
    for calendar_type in supported_calendar_types:
        if input_key.startswith(calendar_type):
            if calendar_type == "weekdays_en" or calendar_type == "weekdays_fa_en":
                language = "en"
            elif calendar_type == "weekdays_ar":
                language = "ar"
            elif calendar_type == "weekdays_fa_ar":
                language = "fa_ar"
            else:  # num
                language = "num"
            return calendar_type, language

    # Return None values if no match is found
    return None, None



def get_weekday_info(weekday: Union[str, int]) -> Tuple[Optional[str], Optional[int]]:
    """
    Extract language and weekday index from weekday name input.

    This function identifies the language of a given weekday name,
    returning the detected language and weekday position.

    Args:
        weekday (Union[str, int]): weekday name in any supported language (case-insensitive)
                                  or weekday number (1-7)

    Returns:
        Tuple[Optional[str], Optional[int]]:
            - detected_language: Language code ('ar', 'en', 'fa_ar', 'fa_en', 'num') or None
            - weekday_index: Zero-based weekday position (0-6), or None if not found

    Examples:
        >>> get_weekday_info("Sunday")
        ('en', 0)

        >>> get_weekday_info("الأحد")
        ('ar', 0)

        >>> get_weekday_info(1)
        ('num', 0)

        >>> get_weekday_info("invalid")
        (None, None)
    """
    # Handle integer input
    if isinstance(weekday, int):
        if 1 > weekday > 7:
            logger.warning(f"Invalid weekday number '{weekday}'. Must be between 1 and 7.")
            return None, None

    # Input validation for string
    if not isinstance(weekday, str) or not weekday.strip():
        logger.error(f"Invalid input type '{type(weekday)}'. Expected str or int.")
        return None, None

    # Normalize inputs
    search_weekday = str(weekday).lower().strip()

    # Search for weekday in keywords
    matching_key, detected_idx = search_in_keywords(search_weekday, weekdays_variations_list)

    if matching_key is None:
        logger.warning(f"weekday '{weekday}' not found in any keyword list")
        return None, None

    detected_key, detected_lang = normalize_key(matching_key)
    if detected_key is not None:
        return detected_lang, detected_idx
    else:
        return None, None

# ===================================================================================
# MAIN FUNCTIONS
# ===================================================================================

def normalize_weekday(
    weekday: Union[int, str],
    to_lang: Optional[str] = None,
    output_format: Optional[str] = "full"
) -> Optional[Union[str, int]]:
    """
    Normalize weekday names from various languages to specified format.

    Args:
        weekday (Union[int, str]): weekday name in any supported language or weekday number (1-7)
        to_lang (Optional[str]): Target language ('ar', 'en', 'fa_ar', 'fa_en').
                               If None, uses detected language.
        output_format (Optional[str]): Output format ('num', 'full', 'abbr').
                                     Defaults to 'full'.

    Returns:
        Optional[Union[str, int]]: Normalized weekday representation or None if conversion fails

    Examples:
        >>> normalize_weekday("Sunday", output_format="num")
        1

        >>> normalize_weekday("Sunday", to_lang="ar", output_format="full")
        "الأحد"

        >>> normalize_weekday(1, to_lang="en", output_format="abbr")
        "Sun"

        >>> normalize_weekday("الأحد", to_lang="en", output_format="full")
        "Sunday"
    """

    def _to_num(idx: Optional[int]) -> Optional[int]:
        """Convert 0-based index to 1-based weekday number."""
        return idx + 1 if idx is not None and 0 <= idx <= 6 else None

    def _to_full(idx: Optional[int], lang: Optional[str]) -> Optional[str]:
        """Convert to full weekday name."""
        if idx is None or lang is None:
            return None
        if not (0 <= idx <= 6):
            return None

        try:
            # Map language codes to weekday keys
            lang_to_key = {
                "ar": "weekdays_ar",
                "en": "weekdays_en",
                "fa_ar": "weekdays_fa_ar",
                "fa_en": "weekdays_fa_en"
            }

            key = lang_to_key.get(lang)
            if key and key in weekdays_standard_keywords:
                return weekdays_standard_keywords[key][idx]
            else:
                logger.warning(f"Unsupported language '{lang}' for full format")
                return None
        except (KeyError, IndexError) as e:
            logger.error(f"Error accessing weekday data for {lang}[{idx}]: {e}")
            return None

    def _to_abbr(idx: Optional[int], lang: Optional[str]) -> Optional[str]:
        """Convert to abbreviated weekday name."""
        if idx is None or lang is None:
            return None
        if not (0 <= idx <= 6):
            return None

        try:
            # Special case for English abbreviations
            if lang == "en":
                abbr_key = "weekdays_en_abbr"
                if abbr_key in weekdays_standard_keywords:
                    return weekdays_standard_keywords[abbr_key][idx]

            # Fall back to full name for other languages
            return _to_full(idx, lang)
        except Exception as e:
            logger.error(f"Error getting abbreviated weekday: {e}")
            return None


    # Get weekday information
    detected_lang, detected_idx = get_weekday_info(weekday)

    if detected_idx is None:
        logger.warning(f"Could not detect weekday information for '{weekday}'")
        return None

    # Determine target language
    target_lang = to_lang.lower() if to_lang else detected_lang

    # Validate target language
    if target_lang and target_lang not in SUPPORTED_LANGUAGES and target_lang != "num":
        logger.warning(f"Unsupported target language '{target_lang}'. Using detected language.")
        target_lang = detected_lang

    # Determine output format
    format_type = output_format.lower() if output_format else OutputFormat.FULL.value

    # Determine output format
    format_type = output_format or OutputFormat.NUMBER.value

    # Convert based on requested format
    if format_type == OutputFormat.NUMBER.value:
        return _to_num(detected_idx)
    elif format_type == OutputFormat.FULL.value:
        if target_lang == "num":
            return _to_num(detected_idx)
        return _to_full(detected_idx, target_lang)
    elif format_type == OutputFormat.ABBREVIATED.value:
        if target_lang == "num":
            return _to_num(detected_idx)
        return _to_abbr(detected_idx, target_lang)
    else:
        logger.warning(f"Unknown output format '{format_type}'. Defaulting to full.")
        return _to_full(detected_idx, target_lang) if target_lang != "num" else _to_num(detected_idx)


# ===================================================================================
# TEST FUNCTIONS
# ===================================================================================

def test_normalize_weekday():
    """Test the normalize_weekday function with various inputs."""
    test_cases = [
        # Arabic inputs
        ("الأحد", "ar", "full"),
        ("الجمعة", "en", "full"),
        ("الاثنين", "ar", "abbr"),

        # English inputs
        ("Sunday", "ar", "full"),
        ("FRIDAY", "en", "abbr"),
        ("monday", "fa_ar", "full"),

        # Numeric inputs
        (1, "en", "full"),
        (5, "ar", "full"),
        (7, "en", "abbr"),

        # Number format output
        ("Sunday", None, "num"),
        ("الأحد", None, "num"),
        (1, None, "num"),

        # Edge cases
        ("", "ar", "full"),
        ("invalid", "en", "full"),
        (0, "ar", "full"),  # Invalid number
        (8, "en", "full"),  # Invalid number
    ]

    print("Testing normalize_weekday function:")
    print("=" * 70)

    for weekday, lang, fmt in test_cases:
        try:
            result = normalize_weekday(weekday, lang, fmt)
            print(f"Input: '{weekday}' -> Lang: {lang}, Format: {fmt}")
            print(f"Output: '{result}'")
        except Exception as e:
            print(f"Input: '{weekday}' -> Error: {e}")
        print("-" * 50)


def test_get_weekday_metadata():
    """Test the get_weekday_metadata function."""
    test_cases = ["Sunday", "الأحد", "یکشنبه", 1, "invalid"]

    print("\nTesting get_weekday_metadata function:")
    print("=" * 70)

    for weekday in test_cases:
        metadata = get_weekday_metadata(weekday)
        print(f"Input: '{weekday}'")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
        print("-" * 50)


# Test the functions
# ===================================================================================
if __name__ == "__main__":
    test_normalize_weekday()
    test_get_weekday_metadata()