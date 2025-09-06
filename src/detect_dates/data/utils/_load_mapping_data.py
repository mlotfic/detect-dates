"""
Calendar Data Loader Module

This module provides functionality for loading and validating calendar mapping data
from CSV files, supporting multiple calendar systems (Gregorian, Hijri, Solar Hijri).

Usage
=====

Quick Start::

    from calendar_data_loader import _load_mapping_data, DateDataLoader
    
    # Method 1: Direct function call
    df = _load_mapping_data()
    print(f"Loaded {len(df):,} calendar records")
    
    # Method 2: Using class-based loader (with caching)
    loader = DateDataLoader()
    data = loader.load_data()
    print(f"Available calendars: {loader.get_supported_calendars()}")
    
    # Access specific date conversion
    sample_record = df.iloc[0]
    print(f"Gregorian: {sample_record['Gregorian Day']}/{sample_record['Gregorian Month']}/{sample_record['Gregorian Year']}")
    print(f"Hijri: {sample_record['Hijri Day']}/{sample_record['Hijri Month']}/{sample_record['Hijri Year']}")

Custom CSV Path::

    # Load from custom location
    df = _load_mapping_data("/path/to/your/calendar_data.csv")
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

# Import constants and configuration
from detect_dates.keywords.constants import (
    Language,
    Calendar,
    OutputFormat,
    PRECISION_LEVELS,
    CALENDAR_ALIASES,
    SUPPORTED_LANGUAGES,
    SUPPORTED_CALENDARS,
    SUPPORTED_CALENDARS_COLUMNS,
    WEEKDAY_COLUMN,
    DEFAULT_LANGUAGE,
    DEFAULT_CALENDAR,
    RelationType,
    ComplexityLevel,
)

# Import validation functions
from _validate_date_ranges import _validate_date_ranges
import os
import pandas as pd

# Default CSV file path relative to this module
DEFAULT_CSV_PATH = "./mapping_date/Hijri-Gregorian-Solar_Hijri-V3.csv"


def _load_mapping_data(csv_path=DEFAULT_CSV_PATH):
    """
    Load and validate calendar mapping data from CSV file.

    This function handles the complete data loading pipeline including file validation,
    CSV parsing, data type conversions, range validation, and data cleaning.

    Parameters
    ----------
    csv_path : str, optional
        Path to the CSV file containing calendar mapping data.
        Defaults to DEFAULT_CSV_PATH ("./mapping_date/Hijri-Gregorian-Solar_Hijri-V3.csv").

    Returns
    -------
    pandas.DataFrame
        Validated and cleaned calendar mapping data with proper data types.
        Contains columns for multiple calendar systems (Gregorian, Hijri, Solar Hijri)
        and weekday information. Sorted by Gregorian date for consistent ordering.

    Raises
    ------
    FileNotFoundError
        If the calendar data file is not found or not accessible.
    PermissionError
        If the file cannot be read due to permission issues.
    ValueError
        If required columns are missing, data contains invalid values, or CSV is empty.
    RuntimeError
        If file loading or processing fails for any other reason.

    Examples
    --------
    >>> # Load default calendar data
    >>> df = _load_mapping_data()
    >>> print(f"Loaded {len(df)} calendar mapping records")
    Loaded 50000 calendar mapping records

    >>> # Access calendar systems
    >>> print(df.columns.tolist())
    ['Gregorian Day', 'Gregorian Month', 'Gregorian Year', 'Hijri Day', ...]

    >>> # Load from custom path
    >>> df = _load_mapping_data("/path/to/custom/calendar_data.csv")
    """
    # Construct absolute path to the CSV file
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), csv_path)
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
        print(f"Loading calendar data from: {file_path}")  # Using print since logger not imported
        df = pd.read_csv(file_path, encoding='utf-8')

        # Build set of all required columns from calendar definitions
        required_columns = set()
        for calendar_cols in SUPPORTED_CALENDARS_COLUMNS.values():
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
        rows_removed = initial_rows - len(df)
        if rows_removed > 0:
            print(f"Removed {rows_removed} rows with missing values")

        # Convert date columns to numeric, handling invalid values gracefully
        for calendar_name, calendar_cols in SUPPORTED_CALENDARS_COLUMNS.items():
            for col in calendar_cols:
                # Convert to numeric, replacing invalid values with NaN
                df[col] = pd.to_numeric(df[col], errors='coerce')

                # Log conversion failures for monitoring
                invalid_count = df[col].isna().sum()
                if invalid_count > 0:
                    print(f"Warning: Found {invalid_count} invalid values in {col}")

        # Remove any rows where numeric conversion failed
        numeric_columns = [col for cols in SUPPORTED_CALENDARS_COLUMNS.values() for col in cols]
        df = df.dropna(subset=numeric_columns)

        # Validate that date ranges are reasonable using external validator
        _validate_date_ranges(df)

        # Convert numeric columns to integers (safe after validation)
        for calendar_cols in SUPPORTED_CALENDARS_COLUMNS.values():
            for col in calendar_cols:
                df[col] = df[col].astype(int)

        # Validate weekday column contains expected values
        valid_weekdays = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}
        invalid_weekdays = set(df[WEEKDAY_COLUMN].unique()) - valid_weekdays
        if invalid_weekdays:
            print(f"Warning: Found unexpected weekday values: {invalid_weekdays}")

        # Sort by Gregorian date for consistent ordering and reset index
        df = df.sort_values(['Gregorian Year', 'Gregorian Month', 'Gregorian Day'])
        df = df.reset_index(drop=True)

        print(f"Successfully processed {len(df):,} valid calendar mapping records")
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
    
    This section provides examples of both the functional and class-based
    approaches to loading calendar data, along with data exploration examples.
    """
    print("=== Calendar Data Loader Example Usage ===\n")
    
    # Example 1: Basic usage with standalone function
    print("1. Loading data with standalone function:")
    try:
        df = _load_mapping_data()
        print(f"   ✓ Loaded {len(df):,} calendar records")
        print(f"   ✓ Date range: {df['Gregorian Year'].min()}-{df['Gregorian Year'].max()}")
        
        # Show sample record for verification
        sample = df.iloc[0]
        print(f"   ✓ Sample record:")
        print(f"     Gregorian: {sample['Gregorian Day']}/{sample['Gregorian Month']}/{sample['Gregorian Year']}")
        print(f"     Weekday: {sample['Week Day']}")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Data exploration
    print("2. Data exploration:")
    try:
        df = _load_mapping_data()
        
        # Show column structure
        print("   Available columns:")
        for i, col in enumerate(df.columns, 1):
            print(f"     {i:2d}. {col}")
        
        print(f"\n   Calendar systems mapping:")
        for name, cols in SUPPORTED_CALENDARS_COLUMNS.items():
            print(f"     {name:15s}: {cols}")
            
        print(f"\n   Sample conversions (first 3 records):")
        sample = df.head(3)[['Gregorian Day', 'Gregorian Month', 'Gregorian Year', 
                           'Hijri Day', 'Hijri Month', 'Hijri Year', 'Week Day']]
        print(sample.to_string(index=False))
        
        # Show data quality info
        print(f"\n   Data quality:")
        print(f"     Total records: {len(df):,}")
        print(f"     Date range: {df['Gregorian Year'].min()} - {df['Gregorian Year'].max()}")
        print(f"     Unique weekdays: {sorted(df['Week Day'].unique())}")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    print(f"\n{'='*50}")
    print("Example completed. Check output above for any errors or warnings.")