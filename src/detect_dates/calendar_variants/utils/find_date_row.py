# ===================================================================================
# Date Row Finder and Calendar Data Lookup
# ===================================================================================
"""
Date lookup utilities for finding specific dates in calendar mapping data.

This module provides functionality to search for specific dates across multiple
calendar systems using pre-calculated mapping data. It supports flexible date
queries with optional components and returns matching DataFrame rows for further
processing (e.g., weekday extraction, date conversion).

Usage
-----
Basic date lookup with complete date components::

    import pandas as pd
    from date_row_finder import find_date_row
    
    # Load your calendar mapping data
    df = pd.read_csv('calendar_data.csv')
    
    # Find specific date in Gregorian calendar
    result = find_date_row(df, era="AD", day=15, month=3, year=2024)
    if not result.empty:
        weekday = result.iloc[0]['Weekday']  # Assuming 'Weekday' column exists
        print(f"March 15, 2024 is a {weekday}")

Flexible date queries with partial information::

    # Find all dates in a specific month and year
    march_2024 = find_date_row(df, era="gregorian", day=None, month=3, year=2024)
    print(f"Found {len(march_2024)} days in March 2024")
    
    # Find all dates in a specific year
    year_2024 = find_date_row(df, era="AD", day=None, month=None, year=2024)
    print(f"Found {len(year_2024)} days in year 2024")

Multi-calendar system support::

    # Gregorian calendar lookup
    greg_date = find_date_row(df, "AD", 25, 12, 2024)        # Christmas 2024
    
    # Hijri calendar lookup  
    hijri_date = find_date_row(df, "AH", 1, 1, 1446)        # New Hijri Year
    
    # Julian calendar lookup
    julian_date = find_date_row(df, "julian", 15, 6, 1400)  # Julian date

Error handling::

    try:
        result = find_date_row(df, "unknown_calendar", 1, 1, 2024)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Handle empty results
    result = find_date_row(df, "AD", 31, 2, 2024)  # Invalid date
    if result.empty:
        print("No matching dates found")

Integration with weekday lookup::

    def get_weekday_for_date(df, era, day, month, year):
        '''Helper function to extract weekday from date lookup'''
        result = find_date_row(df, era, day, month, year)
        if not result.empty:
            return result.iloc[0].get('Weekday', 'Unknown')
        return None
    
    weekday = get_weekday_for_date(df, "AD", 1, 1, 2025)
    print(f"New Year 2025 is a {weekday}")
"""

from typing import Optional, Dict, List, Union, Any, Tuple
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

# Import necessary modules
from detect_dates.keywords.constants import SUPPORTED_CALENDARS_COLUMNS
from detect_dates.normalizers import normalize_input_date


def find_date_row(
        df: pd.DataFrame,
        era: str, 
        day: Optional[int], 
        month: Optional[Union[str, int]], 
        year: Optional[Union[str, int]]
        ) -> Optional[pd.DataFrame]:
    """
    Find matching rows in calendar data for specified date components.
    
    This function searches through calendar mapping data to find rows that match
    the specified date criteria. It supports flexible queries where some date
    components can be omitted, allowing for broad searches (e.g., all dates in
    a year, all dates in a month). The function handles multiple calendar systems
    and normalizes input data for accurate matching.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing calendar mapping data with columns for different
        calendar systems (Gregorian, Hijri, Julian day/month/year columns).
    era : str
        Calendar system identifier. Can be era abbreviations ('AD', 'AH', 'BCE')
        or calendar names ('gregorian', 'hijri', 'julian', 'islamic', etc.).
    day : int or None
        Day of the month (1-31). If None, matches all days in the specified
        month/year combination.
    month : int, str, or None
        Month of the year. Can be:
        - Integer (1-12)  
        - String number ("1"-"12")
        - Month name ("January", "March", etc.)
        - None (matches all months in the specified year)
    year : int, str, or None
        Year in the specified calendar system. String numbers are converted
        to integers. Cannot be None - at least year must be specified.

    Returns
    -------
    pd.DataFrame or None
        DataFrame containing all rows that match the specified criteria.
        Returns empty DataFrame if no matches found. Each row contains
        date information across all calendar systems plus additional
        columns like weekday names.

    Raises
    ------
    ValueError
        - If calendar system cannot be determined from era parameter
        - If year is not specified (at least year is required)
        - If input date components are invalid after normalization
    RuntimeError
        If calendar mapping data is not properly loaded or formatted.

    Examples
    --------
    Find specific complete dates::
    
        # Find March 15, 2024 in Gregorian calendar
        result = find_date_row(df, era="AD", day=15, month=3, year=2024)
        if not result.empty:
            print(f"Found {len(result)} matching row(s)")
            weekday = result.iloc[0]['Weekday']  # Extract weekday
            print(f"March 15, 2024 is a {weekday}")
        
        # Find Hijri date
        result = find_date_row(df, era="AH", day=1, month=1, year=1446)

    Flexible queries with partial date information::
    
        # Find all dates in March 2024
        march_dates = find_date_row(df, era="gregorian", day=None, month=3, year=2024)
        print(f"March 2024 has {len(march_dates)} days")
        
        # Find all dates in year 2024 
        year_dates = find_date_row(df, era="AD", day=None, month=None, year=2024)
        print(f"Year 2024 has {len(year_dates)} total days")
        
        # Find specific month across all days
        ramadan_1445 = find_date_row(df, era="hijri", day=None, month=9, year=1445)

    Error handling and edge cases::
    
        # Handle invalid dates gracefully
        result = find_date_row(df, era="AD", day=31, month=2, year=2024)
        if result.empty:
            print("No matching dates found (invalid date combination)")
        
        # Handle unsupported calendar
        try:
            result = find_date_row(df, era="unknown", day=1, month=1, year=2024)
        except ValueError as e:
            print(f"Calendar error: {e}")

    Integration patterns::
    
        def get_weekday_for_date(df, era, day, month, year):
            '''Extract weekday from date lookup result'''
            result = find_date_row(df, era, day, month, year)
            return result.iloc[0]['Weekday'] if not result.empty else None
        
        def get_date_conversions(df, era, day, month, year):
            '''Get date in all calendar systems'''
            result = find_date_row(df, era, day, month, year)
            if not result.empty:
                row = result.iloc[0]
                return {
                    'gregorian': f"{row['Gregorian Day']}/{row['Gregorian Month']}/{row['Gregorian Year']}",
                    'hijri': f"{row['Hijri Day']}/{row['Hijri Month']}/{row['Hijri Year']}",
                    'julian': f"{row['Solar Hijri Day']}/{row['Solar Hijri Month']}/{row['Solar Hijri Year']}"
                }
            return None

    Notes
    -----
    **Query Flexibility:**
    - At minimum, year and calendar system must be specified
    - day=None: matches all days in the specified month/year
    - month=None: matches all months in the specified year  
    - Both day and month None: matches all dates in the specified year
    
    **Performance Considerations:**
    - Function uses pandas boolean indexing for efficient filtering
    - Large datasets benefit from pre-indexed DataFrames
    - Consider caching results for frequently accessed date ranges
    
    **Data Requirements:**
    - DataFrame must contain columns defined in SUPPORTED_CALENDARS_COLUMNS
    - Expected columns include day/month/year for each calendar system
    - Additional columns (like 'Weekday') are preserved in results
    """
    # Step 1: Validate and normalize input date components
    calendar, day, month, year = normalize_input_date(era, day, month, year)
    
    # Step 2: Ensure calendar system was successfully determined
    if not calendar:
        raise ValueError(
            "Calendar system could not be determined from input era. "
            f"Please provide a valid era/calendar identifier."
        )
    
    # Step 3: Ensure at least year is specified (minimum requirement)
    if year is None:
        raise ValueError(
            "At least year and calendar system must be specified. "
            "Year cannot be None."
        )
        
    # Step 4: Get column names for the specified calendar system
    if calendar not in SUPPORTED_CALENDARS_COLUMNS:
        supported = list(SUPPORTED_CALENDARS_COLUMNS.keys())
        raise ValueError(
            f"Unsupported calendar system: '{calendar}'. "
            f"Supported systems: {supported}"
        )
    
    day_col, month_col, year_col = SUPPORTED_CALENDARS_COLUMNS[calendar]

    # Step 5: Build filtering mask based on provided date components
    # Start with year filter (always required)
    mask = (df[year_col] == year)
    
    # Add month filter if month is provided
    if month is not None:
        mask = mask & (df[month_col] == month)
    
    # Add day filter if day is provided  
    if day is not None:
        mask = mask & (df[day_col] == day)

    # Step 6: Apply filter and return matching rows
    matching_rows = df[mask]
    
    return matching_rows