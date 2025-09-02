"""
Calendar date conversion module for Gregorian, Hijri, and Solar Hijri calendars.

This module provides utilities to load and process calendar mapping data from CSV files,
supporting conversions between different calendar systems used worldwide.
"""

import os
import pandas as pd
from typing import Optional, Dict, List, Union
from dataclasses import dataclass
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Module-level constants for supported calendar systems
# Maps calendar names to their corresponding CSV column names
SUPPORTED_CALENDARS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']  # Note: 'julian' maps to Solar Hijri
}

# Column name for weekday information in the CSV file
WEEKDAY_COLUMN = 'Week Day'

# Default CSV file path relative to this module
DEFAULT_CSV_PATH = "../mapping_date/Hijri-Gregorian-Solar_Hijri-V3.csv"

# Calendar system aliases for user convenience
CALENDAR_ALIASES = {
    'solar_hijri': 'julian',
    'persian': 'julian',
    'islamic': 'hijri',
    'greg': 'gregorian'
}

class CalendarDataLoader:
    """
    Calendar data loader with caching and validation capabilities.

    This class provides a convenient interface for loading and caching calendar
    mapping data, supporting multiple calendar systems with validation and
    error handling.

    Parameters
    ----------
    csv_path : str, optional
        Path to the CSV file containing calendar mapping data.
        Defaults to DEFAULT_CSV_PATH.

    Attributes
    ----------
    csv_path : str
        Path to the calendar data CSV file.

    Examples
    --------
    >>> loader = CalendarDataLoader()
    >>> data = loader.load_data()
    >>> print(f"Loaded {len(data)} calendar records")

    >>> # Use custom CSV file
    >>> loader = CalendarDataLoader("/path/to/custom/data.csv")
    >>> data = loader.load_data()
    """

    def __init__(self, csv_path=DEFAULT_CSV_PATH):
        """
        Initialize the calendar data loader.

        Parameters
        ----------
        csv_path : str, optional
            Path to the CSV file containing calendar mapping data.
        """
        self.csv_path = csv_path
        self._data = None  # Cache for loaded data

    def load_data(self):
        """
        Load and return the calendar mapping data with caching.

        Returns
        -------
        pandas.DataFrame
            Validated and cleaned calendar mapping data. Subsequent calls
            return cached data without reloading from disk.

        Raises
        ------
        FileNotFoundError
            If the calendar data file is not found.
        ValueError
            If the data contains invalid values or missing columns.
        RuntimeError
            If loading fails for any other reason.

        Examples
        --------
        >>> loader = CalendarDataLoader()
        >>> data = loader.load_data()  # Loads from disk
        >>> data2 = loader.load_data()  # Returns cached data
        >>> assert data is data2  # Same object reference
        """
        if self._data is None:
            self._data = _load_mapping_data(self.csv_path)
        return self._data

    def reload_data(self):
        """
        Force reload of calendar data from disk, bypassing cache.

        Returns
        -------
        pandas.DataFrame
            Freshly loaded calendar mapping data.

        Examples
        --------
        >>> loader = CalendarDataLoader()
        >>> data1 = loader.load_data()
        >>> # ... CSV file is updated externally ...
        >>> data2 = loader.reload_data()  # Loads fresh data
        """
        self._data = None  # Clear cache
        return self.load_data()

    def get_supported_calendars(self):
        """
        Get list of supported calendar systems.

        Returns
        -------
        list
            List of supported calendar system names.

        Examples
        --------
        >>> loader = CalendarDataLoader()
        >>> calendars = loader.get_supported_calendars()
        >>> print(calendars)  # ['gregorian', 'hijri', 'julian']
        """
        return list(SUPPORTED_CALENDARS.keys())

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
    """
    for calendar_name, calendar_cols in SUPPORTED_CALENDARS.items():
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


def _load_mapping_data(csv_path=DEFAULT_CSV_PATH):
    """
    Load and validate calendar mapping data from CSV file.

    This function handles the complete data loading pipeline including file validation,
    CSV parsing, data type conversions, range validation, and data cleaning.

    Parameters
    ----------
    csv_path : str, optional
        Path to the CSV file containing calendar mapping data.
        Defaults to DEFAULT_CSV_PATH.

    Returns
    -------
    pandas.DataFrame
        Validated and cleaned calendar mapping data with proper data types.
        Sorted by Gregorian date for consistent ordering.

    Raises
    ------
    FileNotFoundError
        If the calendar data file is not found or not accessible.
    ValueError
        If required columns are missing or data contains invalid values.
    RuntimeError
        If file loading or processing fails for any other reason.

    Examples
    --------
    >>> df = _load_mapping_data()
    >>> print(f"Loaded {len(df)} calendar mapping records")
    >>> print(df.head())

    >>> # Load from custom path
    >>> df = _load_mapping_data("/path/to/custom/calendar_data.csv")
    """
    # Construct absolute path to the CSV file
    file_path = os.path.join(os.path.dirname(__file__), csv_path)
    file_path = os.path.abspath(file_path)

    # Verify file exists and is readable
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Calendar data file not found: {file_path}\n"
            f"Please ensure the CSV file exists in the expected location.\n"
            f"Expected structure: {DEFAULT_CSV_PATH}"
        )

    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Cannot read calendar data file: {file_path}")

    try:
        # Load CSV with UTF-8 encoding to handle international characters
        logger.info(f"Loading calendar data from: {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8')

        # Log initial data info for debugging
        logger.info(f"Loaded CSV with {len(df)} rows and {len(df.columns)} columns")

        # Build set of all required columns from calendar definitions
        required_columns = set()
        for calendar_cols in SUPPORTED_CALENDARS.values():
            required_columns.update(calendar_cols)
        required_columns.add(WEEKDAY_COLUMN)

        # Check that all required columns are present in the CSV
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"Missing required columns in CSV: {missing_columns}\n"
                f"Required columns: {sorted(required_columns)}\n"
                f"Found columns: {sorted(df.columns.tolist())}"
            )

        # Clean and validate data
        initial_rows = len(df)

        # Remove rows with any missing values in required columns
        df = df.dropna(subset=list(required_columns))
        logger.info(f"Removed {initial_rows - len(df)} rows with missing values")

        # Convert date columns to numeric, handling invalid values gracefully
        for calendar_name, calendar_cols in SUPPORTED_CALENDARS.items():
            for col in calendar_cols:
                # Convert to numeric, replacing invalid values with NaN
                df[col] = pd.to_numeric(df[col], errors='coerce')

                # Log conversion failures for monitoring
                invalid_count = df[col].isna().sum()
                if invalid_count > 0:
                    logger.warning(f"Found {invalid_count} invalid values in {col}")

        # Remove any rows where numeric conversion failed
        numeric_columns = [col for cols in SUPPORTED_CALENDARS.values() for col in cols]
        df = df.dropna(subset=numeric_columns)

        # Validate that date ranges are reasonable
        _validate_date_ranges(df)

        # Convert numeric columns to integers (safe after validation)
        for calendar_cols in SUPPORTED_CALENDARS.values():
            for col in calendar_cols:
                df[col] = df[col].astype(int)

        # Validate weekday column contains expected values
        valid_weekdays = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}
        invalid_weekdays = set(df[WEEKDAY_COLUMN].unique()) - valid_weekdays
        if invalid_weekdays:
            logger.warning(f"Found unexpected weekday values: {invalid_weekdays}")

        # Sort by Gregorian date for consistent ordering and reset index
        df = df.sort_values(['Gregorian Year', 'Gregorian Month', 'Gregorian Day'])
        df = df.reset_index(drop=True)

        logger.info(f"Successfully processed {len(df):,} valid calendar mapping records")
        return df

    except pd.errors.EmptyDataError:
        raise ValueError(f"Calendar data file is empty: {file_path}")
    except pd.errors.ParserError as e:
        raise ValueError(f"Error parsing CSV file: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Failed to load calendar data: {str(e)}")


if __name__ == "__main__":
    """
    Demonstrate typical usage patterns of the calendar data loader.
    """
    print("=== Calendar Data Loader Example Usage ===\n")
    
    # Example 1: Basic usage with standalone function
    print("1. Loading data with standalone function:")
    try:
        df = _load_mapping_data()
        print(f"   Loaded {len(df):,} calendar records")
        print(f"   Date range: {df['Gregorian Year'].min()}-{df['Gregorian Year'].max()}")
        print(f"   Sample record:\n{df.iloc[0][['Gregorian Day', 'Gregorian Month', 'Gregorian Year', 'Week Day']]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Using the class-based loader
    print("2. Using CalendarDataLoader class:")
    try:
        loader = CalendarDataLoader()
        print(f"   Supported calendars: {loader.get_supported_calendars()}")
        
        data = loader.load_data()
        print(f"   Loaded {len(data):,} records (first call)")
        
        data2 = loader.load_data()
        print(f"   Retrieved {len(data2):,} records (cached)")
        print(f"   Same object reference: {data is data2}")
        
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Data exploration
    print("3. Data exploration:")
    try:
        df = _load_mapping_data()
        
        # Show column structure
        print("   Available columns:")
        for i, col in enumerate(df.columns, 1):
            print(f"     {i}. {col}")
        
        print(f"\n   Calendar systems mapping:")
        for name, cols in SUPPORTED_CALENDARS.items():
            print(f"     {name}: {cols}")
            
        print(f"\n   Sample conversions:")
        sample = df.head(3)[['Gregorian Day', 'Gregorian Month', 'Gregorian Year', 
                           'Hijri Day', 'Hijri Month', 'Hijri Year', 'Week Day']]
        print(sample.to_string(index=False))
        
    except Exception as e:
        print(f"   Error: {e}")