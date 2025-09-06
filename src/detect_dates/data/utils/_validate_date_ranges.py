"""
Date validation utilities for calendar data processing.

Usage
-----
Basic validation of a DataFrame with calendar data:

    import pandas as pd
    from your_module import _validate_date_ranges
    
    # Create sample data
    df = pd.DataFrame({
        'gregorian_day': [1, 15, 31],
        'gregorian_month': [1, 6, 12],
        'gregorian_year': [2020, 2021, 2022],
        'hijri_day': [1, 15, 29],
        'hijri_month': [1, 6, 12],
        'hijri_year': [1441, 1442, 1443]
    })
    
    # Validate the date ranges
    try:
        _validate_date_ranges(df)
        print("All dates are valid!")
    except ValueError as e:
        print(f"Validation failed: {e}")

Quick validation with error handling:

    import logging
    logging.basicConfig(level=logging.WARNING)
    
    # Your DataFrame here
    df = load_your_data()
    
    # Validate with automatic logging of warnings
    _validate_date_ranges(df)
"""
# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """Set up the source path to allow imports from the src directory."""
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                break
    
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()


from typing import Optional, Union
import pandas as pd
import logging
from detect_dates.keywords.constants import SUPPORTED_CALENDARS_COLUMNS

# Set up logger for this module
logger = logging.getLogger(__name__)


def _validate_date_ranges(df):
    """
    Validate that date values in DataFrame are within reasonable ranges.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing calendar data with date columns.

    Raises
    ------
    ValueError
        If any date values are outside reasonable ranges.

    Notes
    -----
    Checks day values (1-31), month values (1-12), and logs warnings
    for years outside typical ranges.
    
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'gregorian_day': [1, 15, 31],
    ...     'gregorian_month': [1, 6, 12], 
    ...     'gregorian_year': [2020, 2021, 2022]
    ... })
    >>> _validate_date_ranges(df)  # Passes without error
    """
    # Iterate through each supported calendar system
    for calendar_name, calendar_cols in SUPPORTED_CALENDARS_COLUMNS.items():
        day_col, month_col, year_col = calendar_cols
        
        # Validate day ranges (1-31)
        if not df[day_col].between(1, 31).all():
            invalid_days = df[~df[day_col].between(1, 31)][day_col].unique()
            raise ValueError(f"Invalid days in {calendar_name} calendar: {invalid_days}")
        
        # Validate month ranges (1-12)
        if not df[month_col].between(1, 12).all():
            invalid_months = df[~df[month_col].between(1, 12)][month_col].unique()
            raise ValueError(f"Invalid months in {calendar_name} calendar: {invalid_months}")
        
        # Check reasonable year ranges and log warnings for outliers
        if calendar_name == 'gregorian':
            if not df[year_col].between(1900, 2200).all():
                logger.warning(f"Some Gregorian years outside typical range (1900-2200)")
        elif calendar_name == 'hijri':
            if not df[year_col].between(1300, 1600).all():
                logger.warning(f"Some Hijri years outside typical range (1300-1600)")