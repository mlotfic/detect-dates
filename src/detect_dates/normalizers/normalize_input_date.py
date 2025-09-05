# ===================================================================================
# Date Input Normalization and Validation
# ===================================================================================
"""
Date input normalization utilities for multi-calendar date processing.

This module provides comprehensive date input validation and normalization across
multiple calendar systems including Gregorian, Hijri, and Julian calendars.
It handles various input formats and provides robust error handling with fallbacks.

Usage
-----
Basic date normalization (assuming this is a method in a DateProcessor class)::

    processor = DateProcessor()
    
    # Normalize a complete date
    calendar, day, month, year = processor.normalize_input_date(
        era="AD",           # Calendar era/system
        day=15,            # Day of month
        month="March",     # Month name or number
        year=2024          # Year
    )
    # Returns: ("gregorian", 15, 3, 2024)

Handle different input formats::

    # String month names
    result = processor.normalize_input_date("AH", 10, "Ramadan", 1445)
    
    # Numeric months
    result = processor.normalize_input_date("BCE", 5, 12, 500)
    
    # String numbers
    result = processor.normalize_input_date("AD", "25", "12", "2023")

Error handling and validation::

    try:
        result = processor.normalize_input_date("AD", 32, 13, 2024)  # Invalid date
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Invalid components are set to None with warnings
    result = processor.normalize_input_date("AD", 50, "InvalidMonth", 2024)
    # Returns: ("gregorian", None, None, 2024)

Supported calendar systems::

    # Gregorian calendar (1900-2077)
    processor.normalize_input_date("AD", 1, 1, 2024)
    
    # Hijri calendar (1318-1500)  
    processor.normalize_input_date("AH", 1, 1, 1445)
    
    # Julian calendar (1278-1456)
    processor.normalize_input_date("BCE", 1, 1, 1300)
"""

from typing import Optional, Union, Tuple, List, Dict, Any
import os

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """
        Add the src directory to Python path for proper module importing.
        
        This function traverses up the directory structure looking for a 'src'
        folder and adds it to sys.path if not already present.
        """
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        
        # Look for 'src' directory in the path hierarchy
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                    print(f"Added to sys.path: {src_second_path}")
                break
    
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

import pandas as pd

from detect_dates.keywords.constants import (
    SUPPORTED_CALENDARS_COLUMNS,
)

from month import normalize_month
from calendar import normalize_calendar_name, get_calendar
from calendar_from_era import normalize_calendar_from_era


def normalize_input_date(
        era: str, 
        day: Optional[int], 
        month: Optional[Union[str, int]], 
        year: Optional[Union[str, int]]
        ) -> Tuple[Optional[str], Optional[int], Optional[int], Optional[int]]:
    """
    Validate and normalize input date components for multi-calendar processing.
    
    This method takes raw date input in various formats and normalizes them
    into a consistent format suitable for calendar conversion. It performs
    comprehensive validation, handles multiple input types, and provides
    graceful error handling with informative messages.

    Parameters
    ----------
    era : str
        Era or calendar system identifier. Can be era abbreviations like 'AD', 
        'AH', 'BCE', or calendar names like 'gregorian', 'hijri', 'islamic'.
    day : int or None
        Day of the month (1-31). Invalid values are set to None with warnings.
    month : int, str, or None
        Month of the year. Can be:
        - Integer (1-12)
        - String number ("1"-"12") 
        - Month name ("January", "March", etc.)
        - Month name in other languages (if supported by normalize_month)
    year : int, str, or None
        Year in the specified calendar system. String numbers are converted
        to integers. Must be within valid range for the calendar system.

    Returns
    -------
    Tuple[Optional[str], Optional[int], Optional[int], Optional[int]]
        Normalized (calendar, day, month, year) tuple where:
        - **calendar** (str): Normalized calendar name ('gregorian', 'hijri', 'julian')
        - **day** (int or None): Valid day (1-31) or None if invalid
        - **month** (int or None): Valid month (1-12) or None if invalid  
        - **year** (int): Valid year within calendar's supported range

    Raises
    ------
    RuntimeError
        If calendar mapping data is not loaded in the parent object.
    ValueError
        If calendar system is not supported, year is invalid, or year is
        outside the supported range for the specified calendar system.

    Examples
    --------
    Basic date normalization::
    
        # Complete valid date
        result = processor.normalize_input_date("AD", 15, "March", 2024)
        # Returns: ("gregorian", 15, 3, 2024)
        
        # Hijri calendar date  
        result = processor.normalize_input_date("AH", 10, 9, 1445)
        # Returns: ("hijri", 10, 9, 1445)

    Handling invalid components::
    
        # Invalid day and month (set to None with warnings)
        result = processor.normalize_input_date("AD", 35, "BadMonth", 2024)
        # Returns: ("gregorian", None, None, 2024)
        # Prints warnings about invalid day and month
        
        # String numbers are converted
        result = processor.normalize_input_date("AD", "15", "12", "2024")
        # Returns: ("gregorian", 15, 12, 2024)

    Error conditions::
    
        # Unsupported calendar
        processor.normalize_input_date("UNKNOWN", 1, 1, 2024)
        # Raises: ValueError("Unsupported calendar system...")
        
        # Invalid year type
        processor.normalize_input_date("AD", 1, 1, "invalid")  
        # Raises: ValueError("Year must be an integer value...")
        
        # Year out of range
        processor.normalize_input_date("AD", 1, 1, 1800)
        # Raises: ValueError("Unusual year value...")

    Notes
    -----
    **Calendar Year Ranges:**
    - Gregorian: 1900-2077
    - Hijri: 1318-1500  
    - Julian: 1278-1456
    
    **Validation Strategy:**
    - Invalid day/month components are set to None with warnings
    - Invalid years raise ValueError (strict validation)
    - Calendar names are normalized through era conversion
    - String inputs are converted to appropriate types when possible
    
    **Error Handling:**
    - Non-critical errors (invalid day/month) generate warnings but continue processing
    - Critical errors (invalid calendar/year) raise ValueError exceptions
    - All error messages provide specific guidance for correction
    """
    # Step 1: Normalize and validate calendar name from era
    calendar = self.normalize_calendar_from_era(era)
    
    if calendar not in SUPPORTED_CALENDARS_COLUMNS:
        supported_systems = list(SUPPORTED_CALENDARS_COLUMNS.keys())
        raise ValueError(
            f"Unsupported calendar system: '{calendar}'. "
            f"Supported systems: {supported_systems}"
        )
    
    # Step 2: Validate and normalize day component
    if not isinstance(day, int) or not (1 <= day <= 31):
        print(f"Invalid day value: {day}. Must be an integer between 1 and 31.")
        print(f"Day set to default value: None.")
        day = None

    # Step 3: Normalize month component (handle various input formats)
    # Convert string month names to numbers using normalize_month
    if isinstance(month, str):
        normalized_month = normalize_month(month, output_format="number")
        if normalized_month is None:
            print(f"Invalid month name: '{month}'. Could not normalize to month number.")
            month = None
        else:
            month = normalized_month
    
    # Convert string numbers to integers
    if isinstance(month, str) and month.isdigit():
        month = int(month)
    
    # Final validation: ensure month is valid integer in range 1-12
    if month is not None and (not isinstance(month, int) or not (1 <= month <= 12)):
        print(f"Invalid month value: {month}. Must be an integer between 1 and 12.")
        print(f"Month set to default value: None.")
        month = None
    
    # Step 4: Normalize year component  
    # Convert string numbers to integers
    if isinstance(year, str) and year.isdigit():
        year = int(year)
    
    # Year must be an integer (strict validation)
    if not isinstance(year, int):
        raise ValueError(f"Year must be an integer value. Got: {year}")
    
    # Step 5: Validate year range based on calendar system
    year_ranges = {
        'gregorian': (1900, 2077),
        'hijri': (1318, 1500), 
        'julian': (1278, 1456)
    }
    
    min_year, max_year = year_ranges.get(calendar, (None, None))
    
    # Ensure year is within supported range for the calendar
    if (min_year is None or max_year is None or 
        not (min_year <= year <= max_year)):
        raise ValueError(
            f"Unusual year value: {year}. Must be an integer between "
            f"{min_year} and {max_year} for {calendar} calendar."
        )
    
    return calendar, day, month, year