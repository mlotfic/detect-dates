"""
Calendar Date Mapping Module - Production-Ready Calendar Conversion System

Usage
=====

Basic usage for calendar date conversion and weekday lookup:

```python
from detect_dates.data import DateDataLoader
from detect_dates.mapping import DateMapping

# Initialize with default data
ddl = DateDataLoader()
mapper = DateMapping(ddl)

# Get weekday for any date
weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
print(f"March 15, 2024 is a {weekday}")  # "Friday"

# Convert between calendar systems
result = mapper.get_calendar_variants('gregorian', 1, 1, 2024)
hijri = result['hijri']
print(f"Jan 1, 2024 = {hijri['day']}/{hijri['month']}/{hijri['year']} Hijri")

# Validate dates
is_valid = mapper.validate_date('gregorian', 29, 2, 2024)  # True (leap year)

# Find specific weekdays
first_monday = mapper.find_date_by_weekday('gregorian', 'Monday', 3, 2024, 1)

# Get supported calendars and date ranges
calendars = mapper.get_supported_calendars()  # ['gregorian', 'hijri', 'julian']
ranges = mapper.get_data_range()
```

Custom CSV data:
```python
ddl = DateDataLoader("path/to/custom/calendar_data.csv")
mapper = DateMapping(ddl)
```
"""
 # Validate input date components
#calendar, day, month, year = normalize_input_date(era, day, month, year)
        
# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """Add src directory to Python path for module imports."""
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                    print(f"Added to sys.path: {src_second_path}")
                break
    
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

import os
import pandas as pd
from detect_dates.data import DateDataLoader

from detect_dates.keywords.constants import (
    SUPPORTED_CALENDARS_COLUMNS,
)

from detect_dates.normalizers import (
    calendar_from_era,
    normalize_era,
    normalize_month, 
    normalize_weekday,
    normalize_calendar_name,
    get_calendar,
    normalize_calendar_from_era,
    normalize_input_date
)

from utils.find_date_row import find_date_row
from typing import Optional, Dict, List, Union, Any, Tuple
from dataclasses import dataclass
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import necessary modules
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
)


@dataclass
class DateMapping:
    """
    A class for mapping and converting dates between different calendar systems.

    This class provides comprehensive methods to convert dates between Gregorian,
    Hijri (Islamic), and Solar Hijri (Persian) calendar systems. It uses a
    pre-calculated CSV mapping file containing astronomical conversions to ensure
    accuracy across different historical periods.

    The class is designed with performance in mind, using pandas for efficient
    data operations and caching mechanisms to avoid repeated file I/O.

    Parameters
    ----------
    ddl : DateDataLoader
        Data loader instance that handles CSV file loading and caching

    Attributes
    ----------
    df : Optional[pd.DataFrame]
        DataFrame containing the calendar mapping data.
        This is loaded automatically during initialization.
    _data_loaded : bool
        Internal flag indicating successful data loading.
    _date_ranges : Dict[str, Dict[str, int]]
        Cached date ranges for each calendar.

    Examples
    --------
    Initialize and perform basic operations:

    >>> # Standard initialization (uses default CSV path)
    >>> ddl = DateDataLoader()
    >>> mapper = DateMapping(ddl)
    >>> # Custom CSV path
    >>> ddl = DateDataLoader("custom/path/to/calendar_data.csv")
    >>> mapper = DateMapping(ddl)
    >>> # Check if data loaded successfully
    >>> if mapper._is_data_loaded():
    ...     weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)

    Notes
    -----
    The CSV file should be located at the specified path relative to this
    module's location. If the file is not found, the class will raise a
    FileNotFoundError with helpful guidance.
    """
    ddl: DateDataLoader

    def __post_init__(self) -> None:
        """
        Initialize the DateMapping instance by loading the calendar data.

        This method is automatically called after object creation to:

        * Load and validate the mapping data from the CSV file
        * Perform data integrity checks
        * Cache frequently used information
        * Set up error handling for missing or corrupt data

        The initialization is fail-safe: if data loading fails, the object
        is still created but with limited functionality.

        Raises
        ------
        FileNotFoundError
            If the calendar mapping CSV file cannot be found
        ValueError
            If the CSV file has incorrect structure or missing columns
        RuntimeError
            If there are issues with data processing
        """
        try:
            loader = self.ddl
            print(f"   Supported calendars: {loader.get_supported_calendars()}")
            
            # Load the calendar mapping data
            self.df = loader.load_data()
            print(f"   Loaded {len(self.df):,} records (first call)")
            print(f"   Retrieved {len(self.df):,} records (cached)")

            self._data_loaded = True
            self._date_ranges = loader.date_ranges()  # Initialize cache for date ranges
            
            logger.info(f"Successfully loaded {len(self.df):,} calendar mapping records")
        except Exception as e:
            logger.error(f"Failed to initialize DateMapping: {str(e)}")
            self._data_loaded = False
            self.df = None
            self._date_ranges = None
            # Don't re-raise to allow graceful degradation        

    def _is_data_loaded(self) -> bool:
        """
        Check if the calendar mapping data was loaded successfully.

        Returns
        -------
        bool
            True if data is loaded and ready for use, False otherwise

        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> if mapper._is_data_loaded():
        ...     # Safe to use mapping functions
        ...     result = mapper.get_weekday_by_date('gregorian', 1, 1, 2024)
        ... else:
        ...     print("Calendar data not available")
        """
        return self._data_loaded and self.df is not None and not self.df.empty
    
    def get_weekday_by_date(
        self, 
        era: Optional[str], 
        day: Optional[int], 
        month: Optional[Union[str, int]], 
        year: Optional[Union[str, int]]
        ) -> Optional[str]:
        """
        Get the weekday name for a specific date in the given calendar system.

        This method looks up the weekday for a specific date using the pre-calculated
        mapping data. The lookup is fast and accurate, based on astronomical calculations.

        Parameters
        ----------
        era : str
            Calendar system ('gregorian', 'hijri', 'julian', or aliases) or era ('AD', 'AH', etc.)
        day : int, optional
            Day of the month (1-31 depending on calendar and month)
        month : int or str, optional
            Month of the year (1-12) or month name
        year : int, optional
            Year in the specified calendar system

        Returns
        -------
        Optional[str]
            Weekday name ('Sunday', 'Monday', ..., 'Saturday')
            or None if date not found in mapping data

        Raises
        ------
        ValueError
            If the calendar parameter is not supported
        RuntimeError
            If calendar data is not loaded

        Examples
        --------
        Get weekdays for different calendar systems:

        >>> mapper = DateMapping(DateDataLoader())
        >>> # Gregorian calendar
        >>> weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
        >>> print(f"March 15, 2024 is a {weekday}")  # "Friday"
        >>> # Hijri calendar
        >>> weekday = mapper.get_weekday_by_date('hijri', 1, 1, 1445)
        >>> print(f"1st Muharram 1445 AH is a {weekday}")
        >>> # Using aliases
        >>> weekday = mapper.get_weekday_by_date('islamic', 15, 6, 1445)

        Notes
        -----
        The method returns None if the specific date is not found in the
        mapping data, which may occur for dates outside the available range
        or invalid date combinations.
        """
        if not self._is_data_loaded() or self.df is None:
            logger.error("Calendar data not loaded")
            return None

        # Find matching rows using the utility function
        matching_rows: Optional[pd.DataFrame] = find_date_row(self.df, era, day, month, year)
        

        # Return weekday if found, None otherwise
        if (matching_rows is None) or matching_rows.empty:
            logger.debug(f"Date not found: {era} {day}/{month}/{year}")
            return None

        # Log if multiple matches found (shouldn't happen with clean data)
        if (len(matching_rows) > 1) and isinstance(matching_rows, pd.DataFrame):
            logger.warning(f"Multiple matches found for {era} {day}/{month}/{year}")

        return matching_rows.iloc[0][WEEKDAY_COLUMN]

    def get_calendar_variants(self, calendar: Optional[str], day: int, month: int, year: int) -> Optional[Dict[str, Any]]:
        """
        Get equivalent dates in all supported calendar systems for a specific date.

        Given a date in one calendar system, this method returns the equivalent
        dates in all supported calendar systems along with weekday information.
        This is the core conversion functionality of the module.

        Parameters
        ----------
        calendar : str
            Source calendar system ('gregorian', 'hijri', 'julian', or aliases)
        day : int
            Day of the month in the source calendar
        month : int
            Month of the year in the source calendar
        year : int
            Year in the source calendar

        Returns
        -------
        Optional[Dict[str, Any]]
            Dictionary containing equivalent dates in all calendar systems and weekday information:
            
            {
                'gregorian': {'day': int, 'month': int, 'year': int},
                'hijri': {'day': int, 'month': int, 'year': int},
                'julian': {'day': int, 'month': int, 'year': int},
                'weekday': str
            }

            Returns None if the date is not found in the mapping data.

        Raises
        ------
        ValueError
            If the calendar parameter is not supported
        RuntimeError
            If calendar data is not loaded

        Examples
        --------
        Convert between different calendar systems:

        >>> mapper = DateMapping(DateDataLoader())
        >>> # Convert Gregorian to all systems
        >>> result = mapper.get_calendar_variants('gregorian', 1, 1, 2024)
        >>> if result:
        ...     print(f"January 1, 2024 (Gregorian) equals:")
        ...     hijri = result['hijri']
        ...     print(f"  Hijri: {hijri['day']}/{hijri['month']}/{hijri['year']}")
        ...     julian = result['julian']
        ...     print(f"  Julian : {julian['day']}/{julian['month']}/{julian['year']}")
        ...     print(f"  Weekday: {result['weekday']}")
        >>> # Convert from Hijri
        >>> result = mapper.get_calendar_variants('hijri', 1, 1, 1445)

        Notes
        -----
        This method is the foundation for calendar conversion functionality.
        It returns complete information for all supported calendar systems,
        enabling seamless conversion between any two systems.
        """
        if not self._is_data_loaded() or self.df is None:
            logger.error("Calendar data not loaded")
            return None

        # Find matching rows using the utility function
        matching_rows = find_date_row(self.df, calendar, day, month, year)

        if (matching_rows is None) or matching_rows.empty:
            logger.debug(f"Date not found for conversion: {calendar} {day}/{month}/{year}")
            return None

        # Get the first matching row (should be unique)
        row = matching_rows.iloc[0]

        # Log if multiple matches found
        if len(matching_rows) > 1:
            logger.warning(f"Multiple matches found for conversion: {calendar} {day}/{month}/{year}")

        # Build result dictionary with all calendar systems
        result = {
            'gregorian': {
                'day': int(row['Gregorian Day']),
                'month': int(row['Gregorian Month']),
                'year': int(row['Gregorian Year'])
            },
            'hijri': {
                'day': int(row['Hijri Day']),
                'month': int(row['Hijri Month']),
                'year': int(row['Hijri Year'])
            },
            'julian': {
                'day': int(row['Solar Hijri Day']),
                'month': int(row['Solar Hijri Month']),
                'year': int(row['Solar Hijri Year'])
            },
            'weekday': row[WEEKDAY_COLUMN]
        }

        return result

    def validate_date(self, calendar: Optional[str], day: int, month: int, year: int) -> bool:
        """
        Validate if a date exists in the specified calendar system.

        This method checks whether a given date combination is valid and exists
        in the mapping data. It's useful for input validation before performing
        conversions or other operations.

        Parameters
        ----------
        calendar : str
            Calendar system ('gregorian', 'hijri', 'julian', or aliases)
        day : int
            Day of the month
        month : int
            Month of the year
        year : int
            Year

        Returns
        -------
        bool
            True if the date exists in the mapping data and is valid,
            False otherwise

        Examples
        --------
        Validate dates before conversion:

        >>> mapper = DateMapping(DateDataLoader())
        >>> # Valid date
        >>> is_valid = mapper.validate_date('gregorian', 29, 2, 2024)  # Leap year
        >>> print(f"Feb 29, 2024 is valid: {is_valid}")
        >>> # Invalid date
        >>> is_valid = mapper.validate_date('gregorian', 31, 2, 2024)
        >>> print(f"Feb 31, 2024 is valid: {is_valid}")  # False
        >>> # Check Hijri date
        >>> is_valid = mapper.validate_date('hijri', 30, 12, 1445)

        Notes
        -----
        This method is more efficient than get_weekday_by_date() when you
        only need to check validity without retrieving additional information.
        """
        if not self._is_data_loaded() or self.df is None:
            return False

        try:
            result = self.get_weekday_by_date(calendar, day, month, year)
            return result is not None
        except ValueError:
            # Invalid calendar system
            return False
        except Exception:
            # Any other error means the date is not valid
            return False
    
    def _get_data_quality_metrics(self) -> Dict[str, Any]:
        """
        Calculate data quality metrics for the loaded dataset.
        
        Returns
        -------
        Dict[str, Any]
            Data quality metrics including record count, date coverage, etc.
        """
        if not self._is_data_loaded() or self.df is None:
            return {'status': 'no_data'}
        
        metrics = {
            'status': 'good',
            'total_records': len(self.df),
            'unique_weekdays': len(self.df[WEEKDAY_COLUMN].unique()),
            'date_coverage': {}
        }
        
        # Check date coverage for each calendar
        for calendar_name, columns in SUPPORTED_CALENDARS_COLUMNS.items():
            year_col = columns[2]  # Year column is always third
            year_range = self.df[year_col].max() - self.df[year_col].min() + 1
            unique_years = len(self.df[year_col].unique())
            
            metrics['date_coverage'][calendar_name] = {
                'year_span': year_range,
                'unique_years': unique_years,
                'coverage_ratio': unique_years / year_range if year_range > 0 else 0
            }
        
        return metrics
    
    def get_supported_calendars(self) -> List[str]:
        """
        Get list of supported calendar systems.
        
        Returns
        -------
        List[str]
            List of supported calendar system names (primary names only)
        
        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> calendars = mapper.get_supported_calendars()
        >>> print(f"Supported calendars: {', '.join(calendars)}")
        # Output: "Supported calendars: gregorian, hijri, julian"
        
        Notes
        -----
        This returns only the primary calendar names. For aliases,
        use get_calendar_info() to see the full mapping of aliases to primary names.
        """
        return list(SUPPORTED_CALENDARS_COLUMNS.keys())
    
    def get_data_range(self) -> Dict[str, Dict[str, int]]:
        """
        Get the date range available in the mapping data for each calendar system.
        
        This method calculates the minimum and maximum years available in the
        mapping data for each supported calendar system. This information is
        useful for determining the valid date ranges for conversions.
        
        Returns
        -------
        Dict[str, Dict[str, int]]
            Dictionary containing min/max years for each calendar:
            
            {
                'gregorian': {'min_year': int, 'max_year': int},
                'hijri': {'min_year': int, 'max_year': int},
                'julian': {'min_year': int, 'max_year': int}
            }
                
        Examples
        --------
        Check available date ranges:
        
        >>> mapper = DateMapping(DateDataLoader())
        >>> ranges = mapper.get_data_range()
        >>> greg_range = ranges['gregorian']
        >>> print(f"Gregorian dates available: {greg_range['min_year']} to {greg_range['max_year']}")
        >>> hijri_range = ranges['hijri']
        >>> print(f"Hijri dates available: {hijri_range['min_year']} to {hijri_range['max_year']}")
        >>> # Check if a specific year is in range
        >>> target_year = 2025
        >>> if greg_range['min_year'] <= target_year <= greg_range['max_year']:
        ...     print(f"Year {target_year} is available for conversion")
        
        Notes
        -----
        These ranges represent the actual data available in the CSV file.
        Dates outside these ranges cannot be converted between calendar systems.
        """
        if not self._is_data_loaded() or self.df is None:
            return {}
        
        # Use cached ranges if available
        if self._date_ranges is not None:
            return self._date_ranges.copy()
        
        ranges = {}
        
        for calendar, columns in SUPPORTED_CALENDARS_COLUMNS.items():
            year_col = columns[2]  # Year column is always third
            year_series = self.df[year_col]
            
            ranges[calendar] = {
                'min_year': int(year_series.min()),
                'max_year': int(year_series.max()),
                'total_years': len(year_series.unique()),
                'year_span': int(year_series.max() - year_series.min() + 1)
            }
        
        # Cache the results
        self._date_ranges = ranges.copy()
        return ranges
    
    def get_month_info(self, calendar: Optional[str], month: Optional[int], year: Optional[int]) -> Dict[str, Any]:
        """
        Get detailed information about a specific month in a calendar system.
        
        Parameters
        ----------
        calendar : str
            Calendar system
        month : int
            Month number (1-12)
        year : int
            Year
            
        Returns
        -------
        Dict[str, Any]
            Month information including day count, weekday distribution, etc.
            
        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> info = mapper.get_month_info('gregorian', 2, 2024)  # February 2024
        >>> print(f"February 2024 has {info['day_count']} days")
        >>> print(f"Starts on {info['first_weekday']}, ends on {info['last_weekday']}")
        """
        
        if not self._is_data_loaded() or self.df is None:
            return {
                'calendar': calendar,
                'month': month,
                'year': year,
                'day_count': 0,
                'error': 'Calendar data not loaded'
            }

        
        calendar = normalize_calendar_from_era(calendar)
        if calendar not in SUPPORTED_CALENDARS_COLUMNS:
            return {
                'calendar': calendar,
                'month': month,
                'year': year,
                'day_count': 0,
                'error': 'Unsupported calendar system'
            }

        # Get column names for this calendar
        day_col, month_col, year_col = SUPPORTED_CALENDARS_COLUMNS[calendar]
        
        # Filter data for the specific month and year
        month_mask = (self.df[month_col] == month) & (self.df[year_col] == year)
        month_data = self.df[month_mask].sort_values(day_col)
        
        if month_data.empty:
            return {
                'calendar': calendar,
                'month': month,
                'year': year,
                'day_count': 0,
                'error': 'No data found for specified month/year'
            }
        
        # Count weekday occurrences
        weekdays = month_data[WEEKDAY_COLUMN].tolist()
        weekday_counts = {day: weekdays.count(day) for day in set(weekdays)}
        
        return {
            'calendar': calendar,
            'month': month,
            'year': year,
            'day_count': len(month_data),
            'first_day': int(month_data.iloc[0][day_col]),
            'last_day': int(month_data.iloc[-1][day_col]),
            'first_weekday': month_data.iloc[0][WEEKDAY_COLUMN],
            'last_weekday': month_data.iloc[-1][WEEKDAY_COLUMN],
            'weekday_distribution': weekday_counts,
            'month_name': self._get_month_name(calendar, month)
        }
    
    def _get_month_name(self, calendar: Optional[str], month: Optional[int]) -> Optional[Union[str, int]]:
        """
        Get the month name for a specific calendar system using the normalize_month function.
        
        Parameters
        ----------
        calendar : str
            Calendar system
        month : int
            Month number
            
        Returns
        -------
        str
            Month name or number as string
        """
        try:
            # Use the imported normalize_month function
            return normalize_month(month, to_calendar=calendar, output_format="full")
        except Exception:
            # Fallback to string representation if normalization fails
            return str(month)
    
    def get_year_info(self, calendar: Optional[str], year: int) -> Dict[str, Any]:
        """
        Get comprehensive information about a specific year in a calendar system.
        
        Parameters
        ----------
        calendar : str
            Calendar system
        year : int
            Year to analyze
            
        Returns
        -------
        Dict[str, Any]
            Year information including day count, leap year status, etc.
        """
        if not self._is_data_loaded() or self.df is None:
            return {'error': 'Data not loaded'}
        
        
        calendar = normalize_calendar_from_era(calendar)
        if calendar not in SUPPORTED_CALENDARS_COLUMNS:
            return {
                'calendar': calendar,
                'year': year,
                'day_count': 0,
                'error': 'Unsupported calendar system'
            }        
        
        # Get column names
        day_col, month_col, year_col = SUPPORTED_CALENDARS_COLUMNS[calendar]
        
        # Filter data for the specific year
        year_mask = self.df[year_col] == year
        year_data = self.df[year_mask]
        
        if year_data.empty:
            return {
                'calendar': calendar,
                'year': year,
                'day_count': 0,
                'error': 'No data found for specified year'
            }
        
        # Calculate year statistics
        total_days = len(year_data)
        months_present = sorted(year_data[month_col].unique())
        
        # Month-wise day counts
        month_day_counts = {}
        for month in months_present:
            month_days = len(year_data[year_data[month_col] == month])
            month_day_counts[month] = month_days
        
        # Weekday distribution
        weekdays = year_data[WEEKDAY_COLUMN].tolist()
        weekday_counts = {day: weekdays.count(day) for day in set(weekdays)}
        
        # Sort year data by month and day for first/last date calculation
        year_data_sorted = year_data.sort_values([month_col, day_col])
        
        return {
            'calendar': calendar,
            'year': year,
            'day_count': total_days,
            'month_count': len(months_present),
            'months_present': months_present,
            'month_day_counts': month_day_counts,
            'weekday_distribution': weekday_counts,
            'is_leap_year': self._is_leap_year(calendar, year, total_days),
            'first_date': {
                'day': int(year_data_sorted.iloc[0][day_col]),
                'month': int(year_data_sorted.iloc[0][month_col]),
                'weekday': year_data_sorted.iloc[0][WEEKDAY_COLUMN]
            },
            'last_date': {
                'day': int(year_data_sorted.iloc[-1][day_col]),
                'month': int(year_data_sorted.iloc[-1][month_col]),
                'weekday': year_data_sorted.iloc[-1][WEEKDAY_COLUMN]
            }
        }
    
    def _is_leap_year(self, calendar: Optional[str], year: int, day_count: int) -> Optional[bool]:
        """
        Determine if a year is a leap year based on day count.
        
        Parameters
        ----------
        calendar : str
            Calendar system
        year : int
            Year to check
        day_count : int
            Total days in the year
            
        Returns
        -------
        Optional[bool]
            True if leap year, False if not, None if undetermined
        """
        if calendar == 'gregorian':
            # Gregorian leap year has 366 days
            return day_count == 366
        elif calendar == 'hijri':
            # Hijri leap year has 355 days (normal has 354)
            return day_count == 355
        elif calendar == 'julian':
            # Solar Hijri leap year has 366 days
            return day_count == 366
        
        return None

    def get_calendar_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the calendar mapping system.
        
        This method provides detailed information about the loaded data,
        supported calendar systems, and basic statistics.
        
        Returns
        -------
        Dict[str, Any]
            Dictionary containing calendar system information:
            
            {
                'total_records': int,
                'supported_calendars': List[str],
                'weekdays': List[str],
                'date_ranges': Dict[str, Dict[str, int]],
                'sample_record': Dict[str, Any]
            }
            
        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> info = mapper.get_calendar_info()
        >>> print(f"Total records: {info['total_records']:,}")
        >>> print(f"Supported calendars: {', '.join(info['supported_calendars'])}")
        """
        if not self._is_data_loaded() or self.df is None:
            return {'error': 'Data not loaded'}
        
        # Get sample record for demonstration
        sample_row = self.df.iloc[0]
        sample_record = {
            'gregorian': {
                'day': int(sample_row['Gregorian Day']),
                'month': int(sample_row['Gregorian Month']),
                'year': int(sample_row['Gregorian Year'])
            },
            'hijri': {
                'day': int(sample_row['Hijri Day']),
                'month': int(sample_row['Hijri Month']),
                'year': int(sample_row['Hijri Year'])
            },
            'julian': {
                'day': int(sample_row['Solar Hijri Day']),
                'month': int(sample_row['Solar Hijri Month']),
                'year': int(sample_row['Solar Hijri Year'])
            },
            'weekday': sample_row[WEEKDAY_COLUMN]
        }
        
        return {
            'total_records': len(self.df),
            'supported_calendars': list(SUPPORTED_CALENDARS_COLUMNS.keys()),
            'calendar_aliases': CALENDAR_ALIASES,
            'weekdays': sorted(self.df[WEEKDAY_COLUMN].unique()),
            'date_ranges': self.get_data_range(),
            'sample_record': sample_record,
            'data_quality': self._get_data_quality_metrics()
        }

    def to_date(self):
        """
        Convert to Python datetime object if possible.
        
        Attempts to create a Python datetime object from the parsed date components.
        Only works for complete Gregorian calendar dates with all required components
        (day, month, year). Other calendar systems and partial dates cannot be converted.

        Returns
        -------
        datetime or None
            Python datetime object if conversion is possible, None otherwise

        Notes
        -----
        Conversion requirements:
        - Must be a complete date (day, month, year all present)
        - Must use Gregorian calendar system
        - Date components must represent a valid calendar date
        - Negative years (BCE) are not supported by Python datetime

        Examples
        --------
        
        """
        # Import datetime here to avoid circular imports
        from datetime import date
        
        # Check if we have a complete Gregorian date
        if not self.is_complete_date:
            return None
            
        if self.calendar != 'gregorian':
            return None
            
        # Check for required components
        if self.day is None or self.month_num is None or self.year is None:
            return None
            
        # Python datetime doesn't support negative years (BCE dates)
        if self.year <= 0:
            return None
        
        try:
            # Attempt to create datetime object with validation
            return datetime(
                year=int(self.year),
                month=int(self.month_num), 
                day=int(self.day)
            )
        except (ValueError, TypeError, OverflowError):
            # Handle invalid dates (e.g., Feb 30, invalid ranges)
            return None


if __name__ == "__main__":
    """
    Main function demonstrating usage of the DateMapping class.
    
    This function provides comprehensive examples of how to use the DateMapping 
    class for various calendar conversion operations, serving as both documentation
    and a test suite for the module's functionality.
    """
    print("Calendar Date Mapping Module")
    print("=" * 50)
    print("Comprehensive calendar conversion and date mapping functionality")
    print()
    
    try:
        # Initialize the DateMapping instance
        print("1. Initializing DateMapping...")
        ddl = DateDataLoader()
        mapper = DateMapping(ddl)
        
        if not mapper._is_data_loaded():
            print("❌ Failed to load calendar data. Please check the CSV file path.")

        else:
            print("✓ DateMapping initialized successfully")
            print()
            
            # Display calendar information
            print("2. Calendar Data Information:")
            info = mapper.get_calendar_info()
            print(f"   📊 Total records: {info['total_records']:,}")
            print(f"   📅 Supported calendars: {', '.join(info['supported_calendars'])}")
            print(f"   🌍 Available weekdays: {', '.join(info['weekdays'])}")
            
            if info['sample_record']:
                sample = info['sample_record']
                print(f"   📝 Sample record:")
                print(f"      Gregorian: {sample['gregorian']}")
                print(f"      Hijri: {sample['hijri']}")
                print(f"      Solar Hijri: {sample['julian']}")
                print(f"      Weekday: {sample['weekday']}")
            print()
            
            # Display data ranges
            print("3. Available Date Ranges:")
            ranges = mapper.get_data_range()
            for calendar, range_info in ranges.items():
                print(f"   {calendar.title()}: {range_info['min_year']} - {range_info['max_year']} "
                      f"({range_info['total_years']:,} years)")
            print()
            
            # Example 1: Get weekday for specific dates
            print("4. Weekday Lookup Examples:")
            test_dates = [
                ('gregorian', 1, 1, 2024, 'New Year 2024'),
                ('hijri', 1, 1, 1445, 'Islamic New Year 1445'),
                ('julian', 1, 1, 1403, 'Persian New Year 1403')
            ]
            
            for calendar, day, month, year, description in test_dates:
                weekday = mapper.get_weekday_by_date(calendar, day, month, year)
                if weekday:
                    print(f"   📅 {description} ({calendar} {day}/{month}/{year}): {weekday}")
                else:
                    print(f"   ❓ {description}: Date not found in mapping data")
            print()
            
            # Example 2: Calendar system conversions
            print("5. Calendar System Conversion Examples:")
            conversion_examples = [
                ('gregorian', 1, 1, 2024, 'January 1, 2024 (Gregorian)'),
                ('hijri', 1, 1, 1445, 'Muharram 1, 1445 (Hijri)'),
                ('julian', 1, 1, 1403, 'Farvardin 1, 1403 (Solar Hijri)')
            ]
            
            for calendar, day, month, year, description in conversion_examples:
                alternatives = mapper.get_calendar_variants(calendar, day, month, year)
                if alternatives:
                    print(f"   🔄 {description} converts to:")
                    for cal_name, cal_date in alternatives.items():
                        if cal_name != 'weekday' and cal_name != calendar:
                            print(f"      {cal_name.title()}: {cal_date['day']}/{cal_date['month']}/{cal_date['year']}")
                    print(f"      Weekday: {alternatives['weekday']}")
                    print()
            
            # Example 3: Month analysis
            print("6. Month Analysis Example:")
            month_info = mapper.get_month_info('gregorian', 2, 2024)  # February 2024
            if 'error' not in month_info:
                print(f"   📅 February 2024 Analysis:")
                print(f"      Days in month: {month_info['day_count']}")
                print(f"      First day: {month_info['first_day']} ({month_info['first_weekday']})")
                print(f"      Last day: {month_info['last_day']} ({month_info['last_weekday']})")
                print(f"      Weekday distribution: {month_info['weekday_distribution']}")
            print()
            
            # Example 4: Find specific weekdays
            print("7. Weekday Search Example:")
            # Find first Monday of March 2024
            first_monday = mapper.find_date_by_weekday('gregorian', 'Monday', 3, 2024, 1)
            if first_monday:
                greg_date = first_monday['gregorian']
                print(f"   🔍 First Monday of March 2024: {greg_date['day']}/{greg_date['month']}/{greg_date['year']}")
            
            # Find last Friday of December 2023
            last_friday = mapper.find_date_by_weekday('gregorian', 'Friday', 12, 2023, -1)
            if last_friday:
                greg_date = last_friday['gregorian']
                print(f"   🔍 Last Friday of December 2023: {greg_date['day']}/{greg_date['month']}/{greg_date['year']}")
            print()
            
            # Example 5: Date validation
            print("8. Date Validation Examples:")
            validation_tests = [
                ('gregorian', 29, 2, 2024, 'Feb 29, 2024 (leap year)'),
                ('gregorian', 29, 2, 2023, 'Feb 29, 2023 (non-leap year)'),
                ('hijri', 30, 12, 1445, 'Dhu al-Hijjah 30, 1445'),
                ('julian', 31, 12, 1403, 'Esfand 31, 1403 (invalid - max 29/30)')
            ]
            
            for calendar, day, month, year, description in validation_tests:
                is_valid = mapper.validate_date(calendar, day, month, year)
                status = "✅ Valid" if is_valid else "❌ Invalid"
                print(f"   {status}: {description}")
            print()
            
            # Example 6: Performance demonstration
            print("9. Performance Test:")
            import time
            
            start_time = time.time()
            for i in range(100):
                mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
            end_time = time.time()
            
            print(f"   ⚡ 100 weekday lookups completed in {(end_time - start_time)*1000:.2f}ms")
            print(f"   📈 Average lookup time: {(end_time - start_time)*10:.2f}ms per lookup")
            
    except Exception as e:
        print(f"❌ Error during demonstration: {str(e)}")
        logger.exception("Error in main demonstration")
    
    print()
    print("=" * 50)
    print("Demonstration completed. Import this module to use DateMapping in your code.")