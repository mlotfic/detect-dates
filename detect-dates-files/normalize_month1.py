# --*- coding: utf-8 -*-
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize month names across different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing month names
    for Gregorian, Hijri (Islamic), and Persian (Jalali) calendars.
"""

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("INFO: Run Main File : adding file parent src to path ...")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

# Import necessary modules
from modules.keywords import (    
    months_standard_keywords,  # Standard month names for different languages and calendars
    months_variations_list,  # All month keywords for normalization
)

from typing import Union

# ===================================================================================
# FUNCTION: Normalize month names across languages and calendar systems
# ===================================================================================

def normalize_month(month, lang="ar", calendar="gregorian", force_calendar=False):
    """
    Normalize month names to canonical forms across different languages
    and calendar systems.
    
    This function handles month name normalization for Arabic, English, and Persian
    languages across Gregorian, Hijri (Islamic), and Persian (Jalali) calendar systems.
    
    Args:
        month (str): Month name in Arabic, English, or Farsi (case-insensitive)
        lang (str): Target language - "ar" for Arabic, "en" for English, "fa" for Farsi
        calendar (str): Target calendar system - "gregorian", "hijri", "persian",
            "levantine"
        force_calendar (bool): If True, forces conversion to specified calendar system
    
    Returns:
        tuple: (normalized_month_name, metadata_dict)
            - normalized_month_name (str): Normalized month name, or "" if not found
            - metadata_dict (dict): Contains original month, target lang, month number, 
                                   detected calendar, and detected language
    
    Example:
        >>> normalize_month("يناير", "en", "gregorian")
        ('January', {'month': 'يناير', 'lang': 'en', 'n_month_num': 0, 'n_calendar': 'gregorian', 'n_lang': 'ar'})
    
    Note:
        - Input is case-insensitive and whitespace is stripped
        - Returns empty string if month not found in any calendar system
        - Supports multiple spelling variations for each calendar system
    """
    
    # Input validation and normalization
    if not isinstance(month, str) or not month.strip():
        return "", {"month": month, "lang": lang, "n_month_num": -1, "n_calendar": "", "n_lang": ""}
    
    # Normalize inputs - convert to lowercase and strip whitespace
    search_month = month.lower().strip()
    
    # Validate and normalize input parameters
    if lang.lower() not in ["ar", "en", "fa"]:  # Added "fa" for Farsi support
        lang = "ar"  # Default to Arabic
    
    if calendar.lower() not in ["hijri", "gregorian", "julian", ""]:
        calendar = ""  # Default to empty (more common than hijri)
    
    # Initialize return variables
    n_month = ""
    n_calendar = ""
    n_lang = ""
    idx = -1  # Initialize idx to handle case where month is not found
    
    # Normalize calendar parameter
    n_calendar = calendar.lower().strip()
    
    # Search through all month name variations
    for key, value in months_variations_list.items():
        # Convert all month names to lowercase for case-insensitive comparison
        search_list = [mon.lower().strip() for mon in value]
        
        # Check if the input month matches any variation in current keyword list
        if search_month in search_list:
            idx = search_list.index(search_month)
            
            # Handle named months - detect calendar system and language from input
            if key.startswith("gregorian_en"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["gregorian_en"][idx]  # Fallback
                n_calendar = "gregorian"
                n_lang = "en"
                break
                
            elif key.startswith("hijri_en"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["hijri_en"][idx]  # Fallback
                n_calendar = "hijri"
                n_lang = "en"
                break
                
            elif key.startswith("persian_en"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["persian_en"][idx]  # Fallback
                n_calendar = "persian"
                n_lang = "en"
                break
                
            elif key.startswith("gregorian_ar"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["gregorian_ar"][idx]  # Fallback
                n_calendar = "gregorian"
                n_lang = "ar"
                break
                
            elif key.startswith("hijri_ar"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["hijri_ar"][idx]  # Fallback
                n_calendar = "hijri"
                n_lang = "ar"
                break
                
            elif key.startswith("persian_ar"):
                target_key = f"{calendar}_{lang}"
                if target_key in months_variations_list:
                    n_month = months_standard_keywords[target_key][idx]
                else:
                    n_month = months_standard_keywords["persian_ar"][idx]  # Fallback
                n_calendar = "persian"
                n_lang = "ar"
                break
            
            # Handle numeric input (1-12 or 01-12)
            elif key.startswith("num") or (calendar == ""):
                if force_calendar:
                    # Convert to specified calendar system
                    target_key = f"{calendar}_{lang}"
                    if target_key in months_variations_list:
                        n_month = months_standard_keywords[target_key][idx]
                        n_calendar = calendar
                        n_lang = lang
                    else:
                        # Fallback to default if target combination doesn't exist
                        n_month = months_standard_keywords["num"][idx]
                        n_calendar = ""
                        n_lang = ""
                else:
                    # Return as zero-padded number
                    n_month = months_standard_keywords["num"][idx]
                    n_calendar = ""
                    n_lang = ""
                break
    
    # Return normalized month name and metadata
    return n_month, {
        "month": month,           # Original input month
        "lang": lang,             # Target language parameter
        "n_month_num": idx,       # Month number (0-11, -1 if not found)
        "n_calendar": n_calendar, # Detected/target calendar system
        "n_lang": n_lang         # Detected source language
    }
    
# ===================================================================================
# FUNCTION: Normalize month names to numeric format (01-12)
# ===================================================================================
def normalize_month_to_num(month: Union[int, str]) -> int:
    """
    Normalize month names from various calendar systems to numeric format (01-12).
    
    Args:
        month (str): Month name in any supported language/calendar system
        
    Returns:
        str: Numeric month representation (01-12) or empty string if not found
    """
    if isinstance(month, int) and (month <= 12) and (month >= 1):
        return month

    # Input validation and normalization
    if not isinstance(month, str) or not month.strip():
        return None
    
    # Normalize inputs - convert to lowercase and strip whitespace
    search_month = month.lower().strip()
    
    # Initialize return variable
    n_month = None
    
    # Search through all month name variations
    for value in months_variations_list.values():
        # Convert all month names to lowercase for case-insensitive comparison
        search_list = [mon.lower().strip() for mon in value]
        
        # Check if the input month matches any variation in current keyword list
        if search_month in search_list:
            idx = search_list.index(search_month)
            # Use the numeric representation from months_standard_keywords
            # n_month = months_standard_keywords["num2"][idx]
            n_month = idx
            break  # Exit loop once found

    return n_month

# ===================================================================================
# FUNCTION: Normalize month names 
# ===================================================================================
def normalize_month_to_abbr(month: Union[int, str]) -> int:
    """
    Normalize month names from various calendar systems to numeric format (01-12).
    
    Args:
        month (str): Month name in any supported language/calendar system
        
    Returns:
        str: Numeric month representation (01-12) or empty string if not found
    """
    # Input validation and normalization
    if not isinstance(month, str) or not month.strip():
        return None
    
    # Normalize inputs - convert to lowercase and strip whitespace
    search_month = month.lower().strip()
    
    # Initialize return variables
    n_month = ""
  
    # Search through all month name variations
    for key, value in months_variations_list.items():
        # Convert all month names to lowercase for case-insensitive comparison
        search_list = [mon.lower().strip() for mon in value]
        
        # Check if the input month matches any variation in current keyword list
        if search_month in search_list:
            idx = search_list.index(search_month)
            
            # Handle named months - detect calendar system and language from input
            if key.startswith("gregorian_en"):
                n_month = months_standard_keywords["gregorian_en_abbr"][idx]
                break
            elif key.startswith("hijri_en"):
                n_month = months_standard_keywords["hijri_en"][idx]
                break
            elif key.startswith("persian_en"):
                n_month = months_standard_keywords["persian_en"][idx]
                break
            elif key.startswith("gregorian_ar"):
                n_month = months_standard_keywords["gregorian_ar"][idx]
                break
            elif key.startswith("hijri_ar"):
                n_month = months_standard_keywords["hijri_ar"][idx]
                break 
            elif key.startswith("persian_ar"):
                n_month = months_standard_keywords["persian_ar"][idx]
                break
            # Handle numeric input (1-12 or 01-12)
            elif key.startswith("num"):
                n_month = idx
                break
    
    # Return normalized month name
    return n_month


# ===================================================================================
# FUNCTION: Normalize month names t
# ===================================================================================
def normalize_month_to_full(month: Union[int, str]) -> int:
    """
    Normalize month names from various calendar systems to numeric format (01-12).
    
    Args:
        month (str): Month name in any supported language/calendar system
        
    Returns:
        str: Numeric month representation (01-12) or empty string if not found
    """
    # Input validation and normalization
    if not isinstance(month, str) or not month.strip():
        return None
    
    # Normalize inputs - convert to lowercase and strip whitespace
    search_month = month.lower().strip()
    
    # Initialize return variables
    n_month = ""
  
    # Search through all month name variations
    for key, value in months_variations_list.items():
        # Convert all month names to lowercase for case-insensitive comparison
        search_list = [mon.lower().strip() for mon in value]
        
        # Check if the input month matches any variation in current keyword list
        if search_month in search_list:
            idx = search_list.index(search_month)
            
            # Handle named months - detect calendar system and language from input
            if key.startswith("gregorian_en"):
                n_month = months_standard_keywords["gregorian_en_abbr"][idx]
                break
            elif key.startswith("hijri_en"):
                n_month = months_standard_keywords["hijri_en"][idx]
                break
            elif key.startswith("persian_en"):
                n_month = months_standard_keywords["persian_en"][idx]
                break
            elif key.startswith("gregorian_ar"):
                n_month = months_standard_keywords["gregorian_ar"][idx]
                break
            elif key.startswith("hijri_ar"):
                n_month = months_standard_keywords["hijri_ar"][idx]
                break 
            elif key.startswith("persian_ar"):
                n_month = months_standard_keywords["persian_ar"][idx]
                break
            # Handle numeric input (1-12 or 01-12)
            elif key.startswith("num"):
                n_month = idx
                break
    
    # Return normalized month name
    return n_month


# ===================================================================================
# FUNCTION: Get comprehensive information about a month
# ===================================================================================
def get_month_info(month):
    """
    Get comprehensive information about a month including calendar system and index.
    
    Args:
        month (str): Month name in any supported language/calendar system
        
    Returns:
        dict: Dictionary containing normalized month, calendar system, and index
    """
    if not isinstance(month, str) or not month.strip():
        return {"numeric_month": "", "calendar_system": "", "month_index": -1, "found": False}
    
    search_month = month.lower().strip()
    
    # Search through all month name variations
    for key, value in months_variations_list.items():
        search_list = [mon.lower().strip() for mon in value]
        
        if search_month in search_list:
            idx = search_list.index(search_month)
            
            # Determine calendar system from key
            calendar_system = ""
            if "gregorian" in key:
                calendar_system = "Gregorian"
            elif "hijri" in key:
                calendar_system = "Hijri/Islamic"
            elif "persian" in key:
                calendar_system = "Persian/Jalali"
            elif "num" in key:
                calendar_system = "Numeric"
            
            return {
                "numeric_month": months_standard_keywords["num2"][idx],
                "calendar_system": calendar_system,
                "month_index": idx + 1,  # 1-based index
                "found": True,
                "variation_key": key
            }
    
    return {"numeric_month": "", "calendar_system": "", "month_index": -1, "found": False}


# Test the function
# ===================================================================================
# This section is for testing the module functionality with various month inputs.
if __name__ == "__main__":
    # Test cases for different calendar systems and languages
    test_months = [
        "January", "يناير", "محرم", "فروردین",  # Different calendars
        "jan", "feb", "مارس", "april",          # Abbreviations and mixed case
        "رمضان", "Ramadan", "شعبان",            # Islamic months
        "Mehr", "مهر", "آذر",                   # Persian months
        "05", "5", "12",                       # Numeric
        "invalid_month", "", "   "             # Invalid inputs
    ]
    
    print("=== Month Normalization Tests ===")
    for month in test_months:
        result = normalize_month_to_num(month)
        info = get_month_info(month)
        print(f"Input: '{month}' -> Numeric: '{result}' | System: {info['calendar_system']}")
    
    print("\n=== Detailed Month Information ===")
    for month in ["January", "محرم", "فروردین", "رمضان"]:
        info = get_month_info(month)
        if info['found']:
            print(f"Month: {month}")
            print(f"  Numeric: {info['numeric_month']}")
            print(f"  Calendar: {info['calendar_system']}")
            print(f"  Index: {info['month_index']}")
            print(f"  Variation: {info['variation_key']}")
        else:
            print(f"Month: {month} - Not found")
        print()

    # Test cases
    test_cases = [
        # Gregorian calendar
        ("january", "en", "gregorian"),
        ("jan", "en", "gregorian"),
        ("1", "en", "gregorian"),
        ("يناير", "ar", "gregorian"),
        ("ژانویه", "fa", "gregorian"),
        
        # Hijri calendar
        ("محرم", "ar", "hijri"),
        ("muharram", "en", "hijri"),
        ("رمضان", "ar", "hijri"),
        
        # Persian calendar
        ("فروردین", "fa", "persian"),
        ("farvardin", "en", "persian"),
        ("مهر", "ar", "persian"),
        
        # Levantine calendar
        ("كانون الثاني", "ar", "levantine"),
        ("shubat", "en", "levantine"),
        
        # Invalid test
        ("invalid", "en", "gregorian"),
    ]
    
    for mon, lang, cal in test_cases:
        result = normalize_month(mon, lang, cal)
        print(f"Input: '{mon}' ({lang}, {cal}) -> Output: '{result}'")
    # Test cases
    test_cases = [
        ("january", "en"),
        ("jan", "en"),
        ("1", "en"),
        ("01", "en"),
        ("يناير", "ar"),
        ("كانون الثاني", "ar"),
        ("محرم", "ar"),
        ("ژانویه", "fa"),
        ("فروردین", "fa"),
        ("مارس", "fa"),
        ("invalid", "en"),
    ]
    
    for mon, lang in test_cases:
        result = normalize_month(mon, lang)
        print(f"Input: '{mon}' ({lang}) -> Output: '{result}'")