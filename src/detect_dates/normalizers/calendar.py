# ===================================================================================
# Calendar Utilities and Data Management
# ===================================================================================
"""
Calendar utilities for date detection and calendar system management.

This module provides functions and methods for normalizing calendar names,
managing calendar data mappings, and retrieving comprehensive calendar information.
It supports multiple calendar systems including Gregorian, Hijri, and Julian calendars.

Usage
-----
Basic calendar normalization::

    from calendar_utilities import normalize_calendar_name
    
    # Normalize calendar names
    cal = normalize_calendar_name("islamic")     # Returns: "hijri"
    cal = normalize_calendar_name("gregorian")   # Returns: "gregorian"
    cal = normalize_calendar_name("christian")   # Returns: "gregorian"

Calendar information retrieval::

    # Assuming this is a method in a DateMapping class
    mapper = DateMapping()
    info = mapper.get_calendar_info()
    
    print(f"Data loaded: {info['data_loaded']}")
    print(f"Total records: {info['total_records']:,}")
    print(f"Supported calendars: {info['supported_calendars']}")
    
    # Check date ranges
    for calendar, range_info in info['date_ranges'].items():
        print(f"{calendar}: {range_info['min_year']}-{range_info['max_year']}")

Error handling::

    try:
        cal = normalize_calendar_name("unknown_calendar")
    except ValueError as e:
        print(f"Error: {e}")
        # Shows supported calendar names
"""

from typing import Dict, Any, List, Optional
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
    WEEKDAY_COLUMN,
    CALENDAR_ALIASES,
)


def normalize_calendar_name(calendar: Optional[str]) -> Optional[str]:
    """
    Normalize calendar name using aliases and supported calendar mappings.
    
    This function takes a calendar name or alias and returns the standardized
    calendar name. It handles case-insensitive matching and provides helpful
    error messages for unsupported calendar systems.

    Parameters
    ----------
    calendar : str or None
        Calendar name to normalize (e.g., 'islamic', 'gregorian', 'christian').
        Can be None.

    Returns
    -------
    str or None
        Normalized calendar name if input is valid, None if input is None.

    Raises
    ------
    ValueError
        If calendar name is not recognized. The error message includes
        a list of all supported calendar names and aliases.

    Examples
    --------
    >>> normalize_calendar_name("islamic")
    'hijri'
    
    >>> normalize_calendar_name("GREGORIAN")
    'gregorian'
    
    >>> normalize_calendar_name("christian")
    'gregorian'
    
    >>> normalize_calendar_name(None)
    None
    
    >>> normalize_calendar_name("unknown")
    ValueError: Unsupported calendar system: 'unknown'. Supported systems: [...]
    
    Notes
    -----
    The function performs the following checks in order:
    1. Returns None for None input
    2. Converts input to lowercase and strips whitespace
    3. Checks calendar aliases first
    4. Checks direct matches in supported calendars
    5. Raises ValueError with helpful message if no match found
    """
    if calendar is None:
        return None
    
    # Normalize input: lowercase and strip whitespace
    calendar = calendar.lower().strip()

    # Check aliases first (e.g., 'islamic' -> 'hijri')
    if calendar in CALENDAR_ALIASES:
        return CALENDAR_ALIASES[calendar]

    # Check direct matches in supported calendars
    if calendar in SUPPORTED_CALENDARS_COLUMNS:
        return calendar

    # Generate helpful error message with all supported options
    all_names = list(SUPPORTED_CALENDARS_COLUMNS.keys()) + list(CALENDAR_ALIASES.keys())
    raise ValueError(
        f"Unsupported calendar system: '{calendar}'. "
        f"Supported systems: {sorted(all_names)}"
    )


def get_calendar_info(self) -> Dict[str, Any]:
    """
    Get comprehensive information about the loaded calendar data.
    
    This method provides detailed statistics and metadata about the calendar
    mapping data, including data ranges, record counts, sample entries, and
    data quality metrics. It's useful for debugging, data analysis, system
    monitoring, and understanding the scope of available calendar data.
    
    Returns
    -------
    Dict[str, Any]
        Dictionary containing comprehensive data information with the following keys:
        
        - **data_loaded** (bool): Whether calendar data is successfully loaded
        - **total_records** (int): Number of records in the dataset
        - **supported_calendars** (List[str]): List of supported calendar systems
        - **calendar_aliases** (Dict[str, str]): Mapping of aliases to calendar names
        - **date_ranges** (Dict[str, Dict[str, int]]): Min/max years for each calendar
        - **weekdays** (List[str]): Available weekday names in the dataset
        - **csv_columns** (List[str]): Column names in the CSV data
        - **sample_record** (Dict[str, Any]): Sample date record for reference
        - **file_path** (str): Absolute path to the CSV data file
        - **data_quality** (Dict[str, Any]): Data quality metrics and status
        
        If data loading failed, returns minimal info with 'data_loaded': False.

    Examples
    --------
    Basic usage::
    
        mapper = DateMapping()
        info = mapper.get_calendar_info()
        
        # Check if data is loaded
        if info['data_loaded']:
            print(f"Dataset contains {info['total_records']:,} records")
        else:
            print(f"Error: {info.get('error', 'Unknown error')}")
    
    Analyzing date ranges::
    
        info = mapper.get_calendar_info()
        for calendar, range_info in info['date_ranges'].items():
            print(f"{calendar.title()}: {range_info['min_year']}-{range_info['max_year']}")
    
    Examining sample data::
    
        sample = info['sample_record']
        if sample:
            print(f"Sample dates:")
            print(f"  Gregorian: {sample['gregorian']}")
            print(f"  Hijri: {sample['hijri']}")
            print(f"  Julian: {sample['julian']}")
            print(f"  Weekday: {sample['weekday']}")
    
    Data quality assessment::
    
        quality = info['data_quality']
        print(f"Data quality status: {quality['status']}")
        if 'completeness' in quality:
            print(f"Data completeness: {quality['completeness']:.1%}")
            
    Notes
    -----
    This method is designed to be safe and always returns a dictionary,
    even if the underlying data loading failed. Always check the 'data_loaded'
    key before accessing data-dependent fields.
    
    The sample record is selected from the middle of the dataset to provide
    a representative example that's likely to contain valid data across
    all calendar systems.
    """
    # Build base information that's always available
    base_info = {
        'data_loaded': self.is_data_loaded(),
        'supported_calendars': self.get_supported_calendars(),
        'calendar_aliases': CALENDAR_ALIASES.copy(),
        'file_path': os.path.abspath(os.path.join(os.path.dirname(__file__), self.csv_path))
    }
    
    # If data is not loaded, return minimal info with error details
    if not self.is_data_loaded():
        base_info.update({
            'error': 'Calendar data not loaded',
            'total_records': 0,
            'date_ranges': {},
            'weekdays': [],
            'csv_columns': [],
            'sample_record': {},
            'data_quality': {'status': 'data_not_loaded'}
        })
        return base_info
    
    # Build comprehensive information when data is loaded
    info = {
        **base_info,
        'total_records': len(self.df),
        'date_ranges': self.get_data_range(),
        'weekdays': sorted(self.df[WEEKDAY_COLUMN].unique().tolist()),
        'csv_columns': list(self.df.columns),
        'sample_record': {}
    }
    
    # Add a representative sample record for reference
    if not self.df.empty:
        # Use middle record for variety (avoids edge cases at start/end)
        sample_row = self.df.iloc[len(self.df) // 2]
        info['sample_record'] = {
            'gregorian': f"{sample_row['Gregorian Day']}/{sample_row['Gregorian Month']}/{sample_row['Gregorian Year']}",
            'hijri': f"{sample_row['Hijri Day']}/{sample_row['Hijri Month']}/{sample_row['Hijri Year']}",
            'julian': f"{sample_row['Solar Hijri Day']}/{sample_row['Solar Hijri Month']}/{sample_row['Solar Hijri Year']}",
            'weekday': sample_row[WEEKDAY_COLUMN]
        }
    
    # Add data quality metrics for monitoring and validation
    info['data_quality'] = self._get_data_quality_metrics()
    
    return info