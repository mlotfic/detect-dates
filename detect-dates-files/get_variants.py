
"""
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional
import os

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("INFO: Run Main File : adding file parent src to path ...")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

# Import normalization functions - handle import errors gracefully
from detect_dates.normalizers import normalize_month
from detect_dates.normalizers import normalize_era
from detect_dates.normalizers import normalize_weekday

from data._load_data import load_mapping_date
    
# ===================================================================================
# Function to get calendar variants by language
# ===================================================================================


def get_calendar_variants_by_lang(
    match_component: Dict[str, any],
    lang: str = "en"
) -> Dict[str, any]:
    """
    Normalize date components and extract calendar information based on language.
    
    Args:
        match_component: Dictionary with date components like year, month, day, weekday, era, etc.
        lang: Language code for normalization (default is "en")
        
    Returns:
        Dictionary with normalized date components and calendar information.
        
    Raises:
        ValueError: If required fields are missing or invalid.
    """
    
    """
    Example usage:
    match_component = {
        "year": "2023",
        "month": "December",
        "day": "25",
        "era": "AD"
    }
    lang = "en"
    result = get_calendar_variants_by_lang(match_component, lang)
    """
    # Initialize normalized components - start fresh
    n_match_component = {}
    calendar = ""

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
    # Extract calendar if specified - could be empty string, None, or actual
    # calendar name
    calendar = match_component.get("calendar", "") or ""
    # Process era and extract calendar information
    # Era processing might give us calendar info (e.g., "AD" implies Gregorian,
    # "هـ" implies Islamic)
    if match_component.get("era"):
        try:
            n_era, n_calendar = normalize_era(
                era=match_component.get("era", ""),
                lang=lang
            )
            n_match_component["era"] = n_era
            if n_calendar:
                calendar = n_calendar
        except NameError as e:
            raise ValueError(f"Invalid era: {e}")
    # Normalize month if present
    if "month" in n_match_component:
        try:
            n_month = normalize_month(
                month=n_match_component["month"], 
                lang=lang, 
                calendar=calendar
            )
            n_match_component["month"] = n_month
        except ValueError as e:
            raise ValueError(f"Invalid month: {e}")
    # Normalize weekday if present
    if "weekday" in n_match_component:
        try:
            n_weekday = normalize_weekday(
                weekday=n_match_component["weekday"],
                lang=lang
            )
            n_match_component["weekday"] = n_weekday
        except ValueError as e:
            raise ValueError(f"Invalid weekday: {e}")

    # Add calendar information to the result
    n_match_component["calendar"] = calendar
    # Return the normalized components with calendar info
    return n_match_component


# ===================================================================================
# Function to get calendar variants
# ===================================================================================
def get_calendar_variants(input_date: Dict[str, any]) -> List[Dict[str, any]]:
    """
    Convert a date from one calendar system to equivalent dates in all
    supported calendars.
    
    Args:
        input_date: Dictionary with keys 'calendar' and 'year' (required),
                   'day' and 'month' (optional)
                   calendar should be one of: 'gregorian', 'hijri', 'Jalali'
                   If 'day' or 'month' is missing, returns all matching dates
    
    Returns:
        List of dictionaries, each containing date info for one calendar system
        Empty list if no matching date found
    
    Raises:
        ValueError: If calendar type is not supported or required fields missing
        KeyError: If required columns are missing from DataFrame
    """
    date_df = load_mapping_date()
    
    
    # Check if input_date has required keys
    if 'calendar' not in input_date or 'year' not in input_date:
        raise ValueError("Input date must contain 'calendar' and 'year' keys")
    
    # Normalize calendar input
    if not isinstance(input_date['calendar'], str):
        raise ValueError("'calendar' must be a string")
    
    cal = input_date['calendar'].lower()
    
    # Validate required fields
    if 'year' not in input_date:
        raise ValueError("'year' is required in input_date")
    
    year = input_date['year']
    day = input_date.get('day')  # None if not provided
    month = input_date.get('month')  # None if not provided
    
    # Column maps for each calendar type
    calendar_columns = {
        'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
        'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
        'Jalali': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
    }
    
    if cal not in calendar_columns:
        supported_cals = list(calendar_columns.keys())
        raise ValueError(
            f"Unsupported calendar: {cal}. Supported calendars: {supported_cals}"
        )
    
    # Validate DataFrame has required columns
    required_columns = set()
    for cols in calendar_columns.values():
        required_columns.update(cols)
    required_columns.add('Week Day')
    
    missing_columns = required_columns - set(date_df.columns)
    if missing_columns:
        raise KeyError(f"DataFrame missing required columns: {missing_columns}")
    
    day_col, month_col, year_col = calendar_columns[cal]
    
    # Convert to numpy arrays for fast indexing
    try:
        d = date_df[day_col].to_numpy()
        m = date_df[month_col].to_numpy()
        y = date_df[year_col].to_numpy()
    except Exception as e:
        raise ValueError(f"Error converting columns to numpy arrays: {e}")
    
    # Get matching index using numpy - build mask conditionally
    mask = (y == year)  # Always filter by year
    
    if month is not None:
        mask = mask & (m == month)
    
    if day is not None:
        mask = mask & (d == day)
    
    idx = np.where(mask)[0]
    
    if len(idx) == 0:
        return []  # No match found
    
    # Get data for all matching rows (not just first one)
    results = []
    for i in idx:
        row = date_df.iloc[i]
        
        # Create result set for this matching date
        date_variants = [
            {
                "weekday": row['Week Day'],
                "day": int(row['Gregorian Day']),
                "month": int(row['Gregorian Month']),
                "year": int(row['Gregorian Year']),
                "calendar": "gregorian"
            },
            {
                "weekday": row['Week Day'],
                "day": int(row['Hijri Day']),
                "month": int(row['Hijri Month']),
                "year": int(row['Hijri Year']),
                "calendar": "hijri"
            },
            {
                "weekday": row['Week Day'],
                "day": int(row['Solar Hijri Day']),
                "month": int(row['Solar Hijri Month']),
                "year": int(row['Solar Hijri Year']),
                "calendar": "Jalali"
            }
        ]
        results.extend(date_variants)
    
    return results

# ===================================================================================
# Standalone testing and utilities
# ===================================================================================    


if __name__ == "__main__":
    def print_results(results, description):
        """Helper function to print results nicely"""
        print(f"Query: {description}")
        if not results:
            print("No matching dates found")
            return
    
        # Group results by original date for cleaner output
        grouped = {}
        for i in range(0, len(results), 3):  # Each date has 3 calendar variants
            if i + 2 < len(results):
                key = f"{results[i]['weekday']}"
                grouped[key] = results[i:i+3]
        
        for weekday, date_group in grouped.items():
            print(f"  {weekday}:")
            for date_info in date_group:
                print(f"    {date_info['calendar'].title()}: {date_info['day']}/{date_info['month']}/{date_info['year']}")
        print(f"Total matching dates: {len(grouped)}")
    
    
    """Test function with sample data for various scenarios"""
    # # Create sample DataFrame with more data
    # sample_data = {
    #     'Week Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    #     'Gregorian Day': [1, 2, 3, 15, 15, 31],
    #     'Gregorian Month': [1, 1, 1, 3, 6, 12],
    #     'Gregorian Year': [2024, 2024, 2024, 2024, 2024, 2024],
    #     'Hijri Day': [19, 20, 21, 4, 6, 18],
    #     'Hijri Month': [6, 6, 6, 9, 12, 6],
    #     'Hijri Year': [1445, 1445, 1445, 1445, 1445, 1446],
    #     'Solar Hijri Day': [11, 12, 13, 25, 26, 10],
    #     'Solar Hijri Month': [10, 10, 10, 12, 3, 10],
    #     'Solar Hijri Year': [1402, 1402, 1402, 1402, 1403, 1403]
    # }
    
    # df = pd.DataFrame(sample_data)
    
    
    print("=== Test 1: Specific date ===")
    input_date = {
        'calendar': 'gregorian',
        'day': 1,
        'month': 1,
        'year': 2024
    }
    result = get_calendar_variants(input_date)
    print_results(result, "January 1, 2024")
    
    print("\n=== Test 2: All dates in a month ===")
    input_date = {
        'calendar': 'gregorian',
        'month': 1,
        'year': 2024
    }
    result = get_calendar_variants(input_date)
    print_results(result, "All dates in January 2024")
    
    print("\n=== Test 3: All 15th days in a year ===")
    input_date = {
        'calendar': 'gregorian',
        'day': 15,
        'year': 2024
    }
    result = get_calendar_variants(input_date)
    print_results(result, "All 15th days in 2024")
    
    print("\n=== Test 4: All dates in a year ===")
    input_date = {
        'calendar': 'gregorian',
        'year': 2024
    }
    result = get_calendar_variants(input_date)
    print_results(result, "All dates in 2024")
