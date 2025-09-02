#!/usr/bin/env python3
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize date components for different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing components like year, month, day, era, and weekday.
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
from detect_dates.normalizers.normalize_era import normalize_era
from detect_dates.normalizers.normalize_month import normalize_month
from detect_dates.normalizers.normalize_weekday import normalize_weekday
from detect_dates.calendar_variants.get_century_from_year import get_century_from_year

# Import type hints for better code clarity
from typing import Optional, Dict


# Function to normalize date output
# ===================================================================================
# This function takes a dictionary of date components and normalizes them for different languages and calendar systems.
# It handles both flat and nested structures, extracting and normalizing components like year, month,
# day, era, and weekday. It also auto-calculates the century based on the year.
def normalize_date_output(match_component: Dict[str, Optional[str]], lang="ar") -> Dict[str, Optional[str]]:
    """
    Normalize date components for different languages and calendar systems.

    Args:
        match_component (dict): Dictionary containing date components
        lang (str): Language code (default: "ar")

    Returns:
        dict: Normalized date components

    Examples:
        # Simple Gregorian date
        {"year": "2023", "month": "December", "day": "25"}
        → {"year": "2023", "month": "December", "day": "25", "century": 21, "calendar": ""}

        # Arabic Islamic date with era
        {"era": "هـ", "year": "1445", "month": "رمضان", "day": "15"}
        → {"era": "AH", "year": "1445", "month": "Ramadan", "day": "15", "century": 15, "calendar": "islamic"}

        # Nested structure from complex parser
        {"date": {"year": "1400", "month": {"name": "محرم", "number": "1"}}, "calendar": "hijri"}
        → {"date": {"year": "1400", "month": {"name": "Muharram", "number": "1"}}, "century": 14, "calendar": "hijri"}

        # Mixed components with weekday
        {"year": "2024", "month": "March", "weekday": "الجمعة", "day": "15"}
        → {"year": "2024", "month": "March", "weekday": "Friday", "day": "15", "century": 21, "calendar": ""}
    """
    # Initialize normalized components - start fresh
    n_match_component = {}
    calendar = ""
    force_calendar = False

    # Helper function to safely strip strings - handles None and non-strings gracefully
    def safe_strip(value):
        return value.strip() if isinstance(value, str) and value is not None else value

    # Process each component - handle both flat and nested structures
    # Some date parsers return nested dicts, others return flat structures
    for key, value in match_component.items():
        if isinstance(value, dict):
            # Nested structure - recursively process sub-components
            n_match_component[key] = {}
            for sub_key, sub_value in value.items():
                n_match_component[key][sub_key] = safe_strip(sub_value)
        else:
            # Flat structure - initialize as needed for normalization functions
            n_match_component[key] = safe_strip(value)

    # Extract calendar if specified - could be empty string, None, or actual calendar name
    calendar = match_component.get("calendar", "") or ""

    # Process era and extract calendar information
    # Era processing might give us calendar info (e.g., "AD" implies Gregorian, "هـ" implies Islamic)
    # Examples: "AD"/"CE" → Gregorian, "AH"/"هـ" → Islamic, "BE" → Buddhist
    if match_component.get("era"):
        try:
            n_era, n_calendar = normalize_era(
                era=match_component.get("era", ""),
                lang=lang
            )
            n_match_component["era"] = n_era
            # Update calendar if not already set and normalization provides one
            if not calendar and n_calendar:
                calendar = n_calendar
        except (NameError, TypeError):
            # Handle case where normalize_era function is not defined
            # Graceful degradation - just use the raw era value
            n_match_component["era"] = safe_strip(match_component.get("era"))

    # Process month - this might also give us calendar information
    # Different calendars have different month names/numbers
    # Examples: "January" → Gregorian, "رمضان" → Islamic, "Tishrei" → Hebrew
    if match_component.get("month"):
        try:
            n_month, meta = normalize_month(
                month=match_component.get("month", ""),
                lang=lang,
                calendar=calendar,
                force_calendar=force_calendar
            )
            n_match_component["month"] = n_month
            # Update calendar from metadata if available
            # Month names can help identify calendar system
            if meta.get("n_calendar") and not calendar:
                calendar = meta.get("n_calendar", "")
        except (NameError, TypeError):
            # Fallback to raw month value if normalization fails
            n_match_component["month"] = safe_strip(match_component.get("month"))

    # Process weekday - similar to month processing
    # Examples: "الجمعة" → "Friday", "Sunday" → "Sunday", "יום ראשון" → "Sunday"
    if match_component.get("weekday"):
        try:
            n_weekday, meta = normalize_weekday(
                weekday=match_component.get("weekday", ""),
                lang=lang
            )
            n_match_component["weekday"] = n_weekday
            # Update calendar from metadata if available
            if meta.get("n_calendar") and not calendar:
                calendar = meta.get("n_calendar", "")
        except (NameError, TypeError):
            # Fallback to raw weekday value
            n_match_component["weekday"] = safe_strip(match_component.get("weekday"))
    else:
        n_match_component["weekday"] = None

    # Process simple components (day, year) - these don't need special normalization
    # Just clean them up and pass them through
    for component in ["day", "year"]:
        value = match_component.get(component)
        n_match_component[component] = safe_strip(value) if value is not None else None

    # Auto-calculate century if we have a year but no explicit century
    # Century calculation is universal across calendar systems
    if (not match_component.get("century")) and match_component.get("year"):
        n_match_component["century"] = get_century_from_year(match_component.get("year"))[0]

    if (calendar or (calendar == "")) and int(str(match_component.get("year")).strip()):
        if int(str(match_component.get("year")).strip()) > 1446 :
            calendar = 'gregorian'

    # Set final calendar - this gets passed along for downstream processing
    n_match_component["calendar"] = calendar

    return n_match_component

# Example usage and test cases
# ===================================================================================
if __name__ == "__main__":
    # Example usage and test cases
    example_date = {
        "year": "2023",
        "month": "December",
        "day": "25",
        "era": "AD",
        "weekday": "Monday"
    }

    normalized_date = normalize_date_output(example_date, lang="en")
    print(normalized_date)

    # Example with Islamic date
    islamic_date = {
        "year": "1445",
        "month": "رمضان",
        "day": "15",
        "era": "هـ"
    }

    normalized_islamic_date = normalize_date_output(islamic_date, lang="ar")
    print(normalized_islamic_date)
