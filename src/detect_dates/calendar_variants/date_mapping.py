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
weekday = mapper.find_weekday('gregorian', 15, 3, 2024)
print(f"March 15, 2024 is a {weekday}")  # "Friday"

# Convert between calendar systems
result = mapper.find_calendars('gregorian', 1, 1, 2024)
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
    ...     weekday = mapper.find_weekday('gregorian', 15, 3, 2024)

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
        ...     result = mapper.find_weekday('gregorian', 1, 1, 2024)
        ... else:
        ...     print("Calendar data not available")
        """
        return self._data_loaded and self.df is not None and not self.df.empty
    
    def set_date(self, calendar: Optional[str], day: Optional[int], month: Optional[Union[int, str]], year: Optional[int]) -> None:
        """
        Set the current date context for instance methods.

        This method allows setting a specific date in a given calendar system.
        The date components are stored as instance attributes for use in other
        methods that operate on the current date context.

        Parameters
        ----------
        calendar : str
            Calendar system ('gregorian', 'hijri', 'julian', or aliases)
        day : int, optional
            Day of the month (1-31 depending on calendar and month)
        month : int or str, optional
            Month of the year (1-12) or month name
        year : int, optional
            Year in the specified calendar system

        Examples
        --------
        Set a date and then find its weekday:

        >>> mapper = DateMapping(DateDataLoader())
        >>> mapper.set_date('gregorian', 15, 3, 2024)
        >>> weekday = mapper.find_weekday()
        >>> print(f"March 15, 2024 is a {weekday}")  # "Friday"

        Notes
        -----
        This method does not validate the date. Use validate_date() to check
        if the date exists in the mapping data.
        """
        # Validate input date components
        self.calendar, self.day, self.month, self.year = normalize_input_date(calendar, day, month, year)
        
        # Ensure at least year and calendar are provided        
        if self.calendar:
            # Get column names for the specified calendar system
            self.day_col, self.month_col, self.year_col = SUPPORTED_CALENDARS_COLUMNS[self.calendar]
        else:
            raise ValueError("Calendar system could not be determined from input.")
                
        # Determine if we have a complete date (all components present)
        self.is_complete_date = (
            self.calendar in SUPPORTED_CALENDARS_COLUMNS and
            isinstance(self.day, int) and
            isinstance(self.month, int) and
            isinstance(self.year, int)
        )
    
    def find_weekday(self) -> Optional[str]:
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
        >>> weekday = mapper.find_weekday('gregorian', 15, 3, 2024)
        >>> print(f"March 15, 2024 is a {weekday}")  # "Friday"
        >>> # Hijri calendar
        >>> weekday = mapper.find_weekday('hijri', 1, 1, 1445)
        >>> print(f"1st Muharram 1445 AH is a {weekday}")
        >>> # Using aliases
        >>> weekday = mapper.find_weekday('islamic', 15, 6, 1445)

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

    def find_calendars(self) -> Optional[Dict[str, Any]]:
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
        >>> result = mapper.find_calendars('gregorian', 1, 1, 2024)
        >>> if result:
        ...     print(f"January 1, 2024 (Gregorian) equals:")
        ...     hijri = result['hijri']
        ...     print(f"  Hijri: {hijri['day']}/{hijri['month']}/{hijri['year']}")
        ...     julian = result['julian']
        ...     print(f"  Julian : {julian['day']}/{julian['month']}/{julian['year']}")
        ...     print(f"  Weekday: {result['weekday']}")
        >>> # Convert from Hijri
        >>> result = mapper.find_calendars('hijri', 1, 1, 1445)

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

    def validate_date(self) -> bool:
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
        This method is more efficient than find_weekday() when you
        only need to check validity without retrieving additional information.
        """
        if not self._is_data_loaded() or self.df is None:
            return False

        try:
            result = self.find_weekday()
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
    
    def month_info(self) -> Optional[Dict[str, Any]]:
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
        
        if not self._is_data_loaded() or self.df is None or self.month is None or self.year is None or self.calendar is None:
            return None 

        # Find matching rows using the utility function
        month_data = find_date_row(
            df = self.df, 
            era =self.calendar, 
            day= None, 
            month=self.month, 
            year=self.year
        )

        if (month_data is None) or month_data.empty:
            logger.debug(f"Date not found for conversion: {calendar} {month}/{year}")
            return None
        
        # Count weekday occurrences
        weekdays = month_data[WEEKDAY_COLUMN].tolist()
        weekday_counts = {day: weekdays.count(day) for day in set(weekdays)}
        
        return {
            'calendar': calendar,
            'month': month,
            'year': year,
            'day_count': len(month_data),
            'first_day': int(month_data.iloc[0][self.day_col]),
            'last_day': int(month_data.iloc[-1][self.day_col]),
            'first_weekday': month_data.iloc[0][WEEKDAY_COLUMN],
            'last_weekday': month_data.iloc[-1][WEEKDAY_COLUMN],
            'weekday_distribution': weekday_counts,
            'month_name': self._get_month_name(calendar, month)
        }
    def year_info(self) -> Optional[Dict[str, Any]]:
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
        if not self._is_data_loaded() or self.df is None or self.year is None or self.calendar is None:
            return None
        
        # Find matching rows using the utility function
        year_data = find_date_row(
            df = self.df, 
            era =self.calendar, 
            day= None, 
            month=None, 
            year=self.year
        )

        if (year_data is None) or year_data.empty:
            logger.debug(f"Date not found for conversion: {calendar} {year}")
            return None
        
        # Calculate year statistics
        total_days = len(year_data)
        months_present = sorted(year_data[self.month_col].unique())
        
        # Month-wise day counts
        month_day_counts = {}
        for month in months_present:
            month_days = len(year_data[year_data[self.month_col] == month])
            month_day_counts[month] = month_days
        
        # Weekday distribution
        weekdays = year_data[WEEKDAY_COLUMN].tolist()
        weekday_counts = {day: weekdays.count(day) for day in set(weekdays)}
        
        # Sort year data by month and day for first/last date calculation
        year_data_sorted = year_data.sort_values([self.month_col, self.day_col])
        
        return {
            'calendar': calendar,
            'year': year,
            'day_count': total_days,
            'month_count': len(months_present),
            'months_present': months_present,
            'month_day_counts': month_day_counts,
            'weekday_distribution': weekday_counts,
            'is_leap_year': self._is_leap_year(),
            'first_date': {
                'day': int(year_data_sorted.iloc[0][self.day_col]),
                'month': int(year_data_sorted.iloc[0][self.month_col]),
                'weekday': year_data_sorted.iloc[0][WEEKDAY_COLUMN]
            },
            'last_date': {
                'day': int(year_data_sorted.iloc[-1][self.day_col]),
                'month': int(year_data_sorted.iloc[-1][self.month_col]),
                'weekday': year_data_sorted.iloc[-1][WEEKDAY_COLUMN]
            }
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
    
    
    
    def _is_leap_year(self, day_count: int) -> Optional[bool]:
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
        if self.calendar == 'gregorian':
            # Gregorian leap year has 366 days
            return day_count == 366
        elif self.calendar == 'hijri':
            # Hijri leap year has 355 days (normal has 354)
            return day_count == 355
        elif self.calendar == 'julian':
            # Solar Hijri leap year has 366 days
            return day_count == 366
        
        return None

    
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
        
        result = self.find_calendars()
        if result is None:
            return None
        result = result['gregorian']      
        if result['year'] < 1:
            return None
        day = result['day']
        month = result['month']
        year = result['year']
        
        try:
            # Attempt to create datetime object with validation
            return date(
                year=int(year),
                month=int(month), 
                day=int(day)
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
            info = mapper.info()
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
                weekday = mapper.find_weekday()
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
                alternatives = mapper.find_calendars(calendar, day, month, year)
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
                mapper.find_weekday('gregorian', 15, 3, 2024)
            end_time = time.time()
            
            print(f"   ⚡ 100 weekday lookups completed in {(end_time - start_time)*1000:.2f}ms")
            print(f"   📈 Average lookup time: {(end_time - start_time)*10:.2f}ms per lookup")
            
    except Exception as e:
        print(f"❌ Error during demonstration: {str(e)}")
        logger.exception("Error in main demonstration")
    
    print()
    print("=" * 50)
    print("Demonstration completed. Import this module to use DateMapping in your code.")
    

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Union

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """Set up the source path for module imports when running as main script."""
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        # Look for 'src' directory in the path hierarchy
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                break
                
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

from detect_dates.normalizers import (
    normalize_era,  
    normalize_month,
    normalize_weekday,
    normalize_calendar_name,
    # normalize_numeric_word, 
    get_calendar
)

from detect_dates.calendar_variants import (
    get_century_from_year,
    get_century_range,
    format_century_with_era,
)

from components import DateComponents
from components_default import DateComponentsDefault
from meta import DateMeta


@dataclass 
class ParsedDate:
    """
    Comprehensive parsed date with raw, standardized, and numeric representations.

    This is the main class for representing a fully processed date with multiple
    representation formats and rich metadata. It automatically normalizes input
    components and provides convenient property access to all date information.

    Parameters
    ----------
    raw : DateComponents
        Original raw input components before normalization
    standard : DateComponents  
        Standardized/normalized components
    numeric : DateComponents
        Numeric representations where possible
    meta : DateMeta
        Metadata about parsing context and quality

    Examples
    --------
    >>> # Create from raw components
    >>> raw_components = DateComponents(day="15", month="March", year="2023", era="CE")
    >>> meta = DateMeta(text="15 March 2023", lang="en")
    >>> date = ParsedDate(raw=raw_components, standard=DateComponents(), 
    ...                   numeric=DateComponents(), meta=meta)
    
    >>> # Access normalized properties
    >>> print(date.day)  # 15
    >>> print(date.month)  # "March" 
    >>> print(date.month_num)  # 3
    >>> print(date.is_complete_date)  # True
    
    >>> # Get analysis
    >>> print(date.analysis_date())
    """
    raw: DateComponents
    standard: DateComponents
    numeric: DateComponents
    meta: DateMeta
    
    def __post_init__(
        self, date: Optional[dict] = None, weekday: Optional[str] = None,
        day: Optional[int] = None, month: Optional[Union[int, str]] = None,
        year: Optional[int] = None, century: Optional[Union[int, str]] = None,
        era: Optional[str] = None, calendar: Optional[str] = None, text: Optional[str] = None,
        lang: Optional[str] = None, precision: Optional[str] = None,
        confidence: Optional[float] = None, created_at: Optional[str] = None, 
        created_by: Optional[str] = None,
        role_in_text: Optional[str] = None, related_to: Optional[str] = None,
        is_calendar_date: bool = False, is_complete_date: bool = False,
        valid_date: bool = False
    ):
        """
        Post-initialization processing for automatic normalization and validation.
        
        This method runs automatically after dataclass initialization to:
        1. Process any legacy dictionary input format
        2. Normalize raw components into standard format
        3. Create numeric representations
        4. Calculate metadata flags and derived values
        5. Validate confidence scores and set precision levels

        Parameters
        ----------
        date : dict, optional
            Legacy dictionary format for backward compatibility
        weekday, day, month, year, century, era, calendar : various types, optional
            Individual date components (overrides date dict if provided)
        text, lang, precision, confidence, created_at, created_by : various types, optional
            Metadata components
        role_in_text, related_to : str, optional
            Contextual metadata
        is_calendar_date, is_complete_date, valid_date : bool
            Validation flags
        """
        
        # Process raw date components from individual parameters or date dict
        self.raw = DateComponents(
            weekday=weekday if weekday else (date.get('weekday', None) if date else None),
            day=day if day else (date.get('day', None) if date else None),
            month=month if month else (date.get('month', None) if date else None),
            year=year if year else (date.get('year', None) if date else None),
            century=century if century else (date.get('century', None) if date else None),
            era=era if era else (date.get('era', None) if date else None),
            calendar=calendar if calendar else (date.get('calendar', None) if date else None)
        )
        
        # Process metadata from individual parameters or date dict
        self.meta = DateMeta(
            text=text if text else (date.get('text', None) if date else None),
            lang=lang if lang else (date.get('lang', None) if date else None),
            precision=precision if precision else (date.get('precision', None) if date else None),
            confidence=confidence if confidence else (date.get('confidence', None) if date else None),
            created_at=created_at if created_at else (date.get('created_at', None) if date else None),
            created_by=created_by if created_by else (date.get('created_by', None) if date else None),
            is_calendar_date=is_calendar_date if is_calendar_date else (date.get('is_calendar_date', False) if date else False),
            is_complete_date=is_complete_date if is_complete_date else (date.get('is_complete_date', False) if date else False),
            valid_date=valid_date if valid_date else (date.get('valid_date', False) if date else False),
            role_in_text=role_in_text if role_in_text else (date.get('role_in_text', None) if date else None),
            related_to=related_to if related_to else (date.get('related_to', None) if date else None),
        )
        
        # Calculate century if not provided but year is available
        century = self.raw.century
        if not century and self.raw.year is not None:
            try:
                if str(self.raw.year).lstrip('-').isdigit():
                    century_result = get_century_from_year(int(self.raw.year))
                    # get_century_from_year returns tuple (century, era)
                    century = century_result[0] if isinstance(century_result, tuple) else century_result
            except (ValueError, TypeError):
                century = None
        
        # Create standardized components with normalization
        self.standard = DateComponents(
            weekday=str(normalize_weekday(self.raw.weekday)) if self.raw.weekday else None,
            day=int(self.raw.day) if self.raw.day and str(self.raw.day).isdigit() else None,
            month=normalize_month(self.raw.month) if self.raw.month else None,
            year=int(self.raw.year) if self.raw.year and str(self.raw.year).lstrip('-').isdigit() else None,
            century=century if century else None,
            era=normalize_era(self.raw.era) if self.raw.era else None,
            calendar=normalize_calendar_name(self.raw.calendar) if self.raw.calendar else (
                get_calendar(self.raw.era) if self.raw.era else None
            )
        )
        
        # Create numeric representation (primarily for month conversion)
        self.numeric = DateComponents(
            weekday=self.standard.weekday if isinstance(self.standard.weekday, str) else None,
            day=self.standard.day,
            month=normalize_month(self.standard.month, output_format="num") if self.standard.month else None,
            year=self.standard.year,
            century=self.standard.century,
            era=self.standard.era,
            calendar=self.standard.calendar
        )
        
        # Validate confidence score range
        if self.meta.confidence is not None:
            if not (0.0 <= self.meta.confidence <= 1.0):
                raise ValueError("Confidence must be between 0.0 and 1.0")
        
        # Calculate validation flags and metadata if not explicitly set
        if self.meta.is_calendar_date is False:
            self.meta.is_calendar_date = self._is_calendar()
        if self.meta.is_complete_date is False:
            self.meta.is_complete_date = self._is_complete()
        if self.meta.valid_date is False:
            self.meta.valid_date = self.meta.is_calendar_date and self.meta.is_complete_date
            
        # Auto-detect language if not provided
        if self.meta.lang is None:
            self.meta.lang = self._detect_language()
        
        # Set precision based on available components if not explicitly provided
        if self.meta.precision is None:
            self.meta.precision = (
                'day' if self.meta.is_complete_date else
                'month' if self.raw.month and self.raw.year else
                'year' if self.raw.year else
                'century' if self.raw.century else
                'partial'
            )

    # Property accessors for convenient access to components
    @property
    def text(self) -> Optional[str]:
        """Get the original text that was parsed."""
        return self.meta.text

    @property
    def lang(self) -> Optional[str]:
        """Get the detected or specified language."""
        return self.meta.lang

    @property
    def precision(self) -> Optional[str]:
        """Get the precision level of this date."""
        return self.meta.precision

    @property
    def confidence(self) -> Optional[float]:
        """Get the parsing confidence score."""
        return self.meta.confidence

    @property
    def metadata(self) -> Dict[str, Any]:
        """Get dictionary of metadata fields."""
        return {
            'created_at': self.meta.created_at,
            'created_by': self.meta.created_by,
            'is_calendar_date': self.meta.is_calendar_date,
            'is_complete_date': self.meta.is_complete_date,
            'valid_date': self.meta.valid_date,
            'role_in_text': self.meta.role_in_text,
            'related_to': self.meta.related_to
        }

    @property
    def weekday(self) -> Optional[Union[int, str]]:
        """Get the standardized weekday."""
        return self.standard.weekday

    @property
    def day(self) -> Optional[int]:
        """Get the standardized day of month."""
        return self.standard.day

    @property
    def month(self) -> Optional[Union[int, str]]:
        """Get the standardized month (name format)."""
        return self.standard.month

    @property
    def month_num(self) -> Optional[int]:
        """Get the month as a number (1-12)."""
        return self.numeric.month

    @property
    def year(self) -> Optional[int]:
        """Get the standardized year."""
        return self.standard.year

    @property
    def century(self) -> Optional[Union[int, str]]:
        """Get the calculated or provided century."""
        return self.standard.century

    @property
    def era(self) -> Optional[str]:
        """Get the standardized era."""
        return self.standard.era

    @property
    def calendar(self) -> Optional[str]:
        """Get the standardized calendar system."""
        return self.standard.calendar

    @property
    def valid_date(self) -> bool:
        """Check if this represents a valid, complete date."""
        return self.meta.valid_date

    @property
    def is_complete_date(self) -> bool:
        """Check if this has day-level precision."""
        return self.meta.is_complete_date

    @property
    def is_calendar_date(self) -> bool:
        """Check if this has calendar-level information (year + era)."""
        return self.meta.is_calendar_date

    def analysis_date(self):
        """
        Provide a human-readable analysis of the date components.

        This method generates a comprehensive summary string that describes the parsed
        date components, their values, and any inferred information. Useful for
        debugging and understanding how the date was interpreted.

        Returns
        -------
        str
            Multi-line summary of the date components and their interpretations

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(weekday="Sunday", day="15", month="March", 
        ...                                     year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> print(date.analysis_date())
        Input  : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: None, Era: CE, Calendar: gregorian]
        Standard Output : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Numeric Output : [Weekday: Sunday, Day: 15, Month: 3, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Date Info : Is Valid Date: True, Is Complete: True, Is Calendar: True, Precision: day, Language: en
        """
        # Format input components
        input_components = [
            f"Weekday: {self.raw.weekday}",
            f"Day: {self.raw.day}",
            f"Month: {self.raw.month}",
            f"Year: {self.raw.year}",
            f"Century: {self.raw.century}",
            f"Era: {self.raw.era}",
            f"Calendar: {self.raw.calendar}"
        ]
        
        # Format standard output components
        standard_components = [
            f"Weekday: {self.weekday}",
            f"Day: {self.day}",
            f"Month: {self.month}",
            f"Year: {self.year}",
            f"Century: {self.century}",
            f"Era: {self.era}",
            f"Calendar: {self.calendar}"
        ]
        
        # Format numeric output components  
        numeric_components = [
            f"Weekday: {self.weekday}",
            f"Day: {self.day}",
            f"Month: {self.month_num}",
            f"Year: {self.year}",
            f"Century: {self.century}",
            f"Era: {self.era}",
            f"Calendar: {self.calendar}"
        ]
        
        # Format date info
        date_info = [
            f"Is Valid Date: {self.valid_date}",
            f"Is Complete: {self.is_complete_date}",
            f"Is Calendar: {self.is_calendar_date}",
            f"Precision: {self.precision}",
            f"Language: {self.lang}",
            f"Confidence: {self.confidence}"
        ]
        
        return (
            f"Input  : [{', '.join(input_components)}]\n"
            f"Standard Output : [{', '.join(standard_components)}]\n"
            f"Numeric Output : [{', '.join(numeric_components)}]\n"
            f"Date Info : {', '.join(date_info)}"
        )

    def _detect_language(self) -> Optional[str]:
        """
        Detect the language of the original text if not explicitly provided.

        Uses simple heuristics to detect language based on character sets.
        Currently supports basic English/Arabic detection.

        Returns
        -------
        str or None
            Detected language code (ISO 639-1) or None if undetectable

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(), standard=DateComponents(), 
        ...                   numeric=DateComponents(), meta=DateMeta(text="15 March 2023"))
        >>> date._detect_language()
        'en'
        >>> date_ar = ParsedDate(raw=DateComponents(), standard=DateComponents(),
        ...                      numeric=DateComponents(), meta=DateMeta(text="15 مارس 2023"))
        >>> date_ar._detect_language()
        'ar'
        """
        # Return explicitly set language
        if self.lang:
            return self.lang
        
        if self.text:
            # Simple heuristic: check for Arabic characters (U+0600 to U+06FF range)
            if any('\u0600' <= char <= '\u06FF' for char in self.text):
                return 'ar'
            else:
                return 'en'
        
        return None

    def _is_complete(self) -> bool:
        """
        Check if the date has complete day-level precision information.

        A complete date must have day, month, year, and era components.
        This is useful for determining if the date can be converted to
        a specific calendar date.

        Returns
        -------
        bool
            True if all required components (day, month, year, era) are present

        Examples
        --------
        >>> complete = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", era="CE"),
        ...                       standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> complete._is_complete()
        True
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial._is_complete()
        False
        """
        return (
            self.day is not None and 
            self.month is not None and 
            self.year is not None and 
            (self.era is not None or self.calendar is not None)
        )

    def _is_calendar(self) -> bool:
        """
        Check if the date has calendar-level information (year and era).

        This method determines if the date has sufficient information to
        represent a specific year in a given calendar system.

        Returns
        -------
        bool
            True if year, era, and calendar components are all present

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(year="2023", era="CE", calendar="gregorian"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> date._is_calendar()
        True
        >>> incomplete = ParsedDate(raw=DateComponents(year="2023"),
        ...                         standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> incomplete._is_calendar()
        False
        """
        return (
            self.year is not None and 
            (self.era is not None or self.calendar is not None)
        )

    def to_dict(self, format="standard") -> Dict[str, Any]:
        """
        Convert the ParsedDate instance to a dictionary representation.

        This method provides different dictionary formats for various use cases
        like serialization, JSON export, or interfacing with other systems.

        Parameters
        ----------
        format : str, default "standard"
            Output format type. Options are:
            - "standard": normalized components with metadata
            - "numeric": numeric representations where possible
            - "raw": original raw input components
            - "all": complete information including raw and processed
            - "meta": metadata only

        Returns
        -------
        dict
            Dictionary containing date components based on specified format

        Raises
        ------
        ValueError
            If an unknown format string is provided

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(day="15", month="March", year="2023"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> standard = date.to_dict("standard")
        >>> standard['day']
        15
        >>> numeric = date.to_dict("numeric")
        >>> numeric['month']
        3
        """
        # Build complete dictionary with all available information
        base_dict = {
            'raw_weekday': self.raw.weekday,
            'raw_day': self.raw.day,
            'raw_month': self.raw.month,
            'raw_year': self.raw.year,
            'raw_century': self.raw.century,
            'raw_era': self.raw.era,
            'raw_calendar': self.raw.calendar,
            'text': self.text,
            'calendar': self.calendar,
            'lang': self.lang,
            'precision': self.precision,
            'confidence': self.confidence,
            'metadata': self.metadata,
            'weekday': self.weekday,
            'day': self.day,
            'month': self.month,
            'month_num': self.month_num,
            'year': self.year,
            'century': self.century,
            'era': self.era,
        }
        
        # Return appropriate subset based on format
        if format == "standard":
            return {
                'weekday': self.weekday,
                'day': self.day,
                'month': self.month,
                'year': self.year,
                'century': self.century,
                'era': self.era,
                'calendar': self.calendar,
                'lang': self.lang,
                'precision': self.precision,
                'confidence': self.confidence
            }
        elif format == "numeric":
            return {
                'weekday': self.weekday if isinstance(self.weekday, int) else None,
                'day': self.day,
                'month': self.month_num,
                'year': self.year,
                'century': self.century,
                'era': self.era,
                'calendar': self.calendar,
                'lang': self.lang,
                'precision': self.precision,
                'confidence': self.confidence
            }
        elif format == "raw":
            return {
                'raw_weekday': self.raw.weekday,
                'raw_day': self.raw.day,
                'raw_month': self.raw.month,
                'raw_year': self.raw.year,
                'raw_century': self.raw.century,
                'raw_era': self.raw.era,
                'raw_calendar': self.raw.calendar
            }
        elif format == "all":
            return base_dict
        elif format == "meta":
            return {
                'text': self.text,
                'calendar': self.calendar,
                'lang': self.lang,
                'precision': self.precision,
                'confidence': self.confidence,
                'metadata': self.metadata
            }
        else:
            # Default to standard format for unknown format strings
            return self.to_dict("standard")

    def __str__(self) -> str:
        """
        Create a human-readable string representation of the date.

        Builds a natural language representation using available components,
        following the pattern: [Weekday,] [Day] [Month] [Year Era] [Century Era] [(Calendar)]

        Returns
        -------
        str
            Human-readable string representation, or "No date information" if empty

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(weekday="Monday", day="15", month="March", 
        ...                                     year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> str(date)
        'Monday, 15 March 2023 CE'
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> str(partial)
        'March 2023'
        >>> empty = ParsedDate(raw=DateComponents(), standard=DateComponents(), 
        ...                    numeric=DateComponents(), meta=DateMeta())
        >>> str(empty)
        'No date information'
        """
        parts = []
        
        # Add weekday with comma separator
        if self.weekday:
            parts.append(f"{self.weekday},")
            
        # Add day
        if self.day:
            parts.append(f"{self.day}")
            
        # Add month
        if self.month:
            parts.append(f"{self.month}")
            
        # Add year with era, or century with era if no year
        if self.year:
            year_str = f"{self.year}"
            if self.era:
                year_str += f" {self.era}"
            parts.append(year_str)
        elif self.century:
            century_str = f"{self.century}"
            if self.era:
                century_str += f" {self.era}"
            parts.append(century_str)
            
        # Add calendar system in parentheses if specified
        if self.calendar:
            parts.append(f"({self.calendar})")
            
        return " ".join(parts) if parts else "No date information"

    def strftime(self, format_string: str) -> str:
        """
        Format the parsed date using strftime-like format codes with extensions.
        
        Supports standard strftime codes plus custom extensions for partial dates
        and calendar-specific information. Missing components are displayed with
        question marks to indicate incomplete data.

        Parameters
        ----------
        format_string : str
            Format string with % codes for date components

        Returns
        -------
        str
            Formatted date string with missing components shown as ? marks

        Notes
        -----
        Standard strftime codes supported:
        - %d: Day with zero padding (01-31) or ?? if None
        - %e: Day without padding (1-31) or ? if None  
        - %m: Month as number with padding (01-12) or ?? if None
        - %n: Month as number without padding (1-12) or ? if None
        - %b: Abbreviated month name (Jan, Feb, ...) or ??? if None
        - %B: Full month name (January, February, ...) or ??? if None
        - %y: Year without century (00-99) or ?? if None
        - %Y: Year with century (e.g. 2023, 1066) or ???? if None
        - %C: Century number or ?? if None
        - %A: Full weekday name (Monday, ...) or ??? if None
        - %a: Abbreviated weekday name (Mon, ...) or ??? if None

        Custom extensions:
        - %E: Era (BCE, CE, AD, BC) or empty if None
        - %S: Calendar system or empty if None  
        - %P: Precision level or empty if None
        - %%: Literal % character

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> date.strftime("%Y-%m-%d")
        '2023-03-15'
        >>> date.strftime("%B %e, %Y %E")
        'March 15, 2023 CE'
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial.strftime("%B %Y")
        'March 2023'
        >>> partial.strftime("%Y-%m-%d")
        '2023-03-??'
        """
        result = format_string
        
        # Day formatting
        if self.day is not None:
            result = result.replace('%d', f"{self.day:02d}")
            result = result.replace('%e', str(self.day))
        else:
            result = result.replace('%d', '??')
            result = result.replace('%e', '?')
        
        # Month formatting
        if self.month_num is not None:
            result = result.replace('%m', f"{self.month_num:02d}")
            result = result.replace('%n', str(self.month_num))
            
            # Use existing month name from standard components if available
            if self.month:
                # Full month name
                result = result.replace('%B', str(self.month))
                # Abbreviated month name (first 3 characters)
                abbr_month = str(self.month)[:3] if len(str(self.month)) >= 3 else str(self.month)
                result = result.replace('%b', abbr_month)
            else:
                result = result.replace('%B', '???')
                result = result.replace('%b', '???')
        else:
            result = result.replace('%m', '??')
            result = result.replace('%n', '?')
            result = result.replace('%B', '???')
            result = result.replace('%b', '???')
        
        # Year formatting
        if self.year is not None:
            result = result.replace('%Y', str(self.year))
            result = result.replace('%y', f"{abs(self.year) % 100:02d}")
            # Century calculation
            if self.century is not None:
                result = result.replace('%C', str(self.century))
            else:
                # Calculate century from year
                century_num = (abs(self.year) // 100) + 1
                result = result.replace('%C', str(century_num))
        else:
            result = result.replace('%Y', '????')
            result = result.replace('%y', '??')
            result = result.replace('%C', '??')
        
        # Weekday formatting
        if self.weekday is not None:
            weekday_str = str(self.weekday)
            result = result.replace('%A', weekday_str)
            # Abbreviated weekday (first 3 characters)
            abbr_weekday = weekday_str[:3] if len(weekday_str) >= 3 else weekday_str
            result = result.replace('%a', abbr_weekday)
        else:
            result = result.replace('%A', '???')
            result = result.replace('%a', '???')
        
        # Custom extension formatting
        result = result.replace('%E', self.era or '')
        result = result.replace('%S', self.calendar or '')
        result = result.replace('%P', self.precision or '')
        
        # Handle literal % character (must be done last)
        result = result.replace('%%', '%')
        
        return result


# Example usage and testing
if __name__ == "__main__":
    # Example 1: Basic date components
    print("=== Example 1: Basic Date Components ===")
    components = DateComponents(day=15, month=3, year=2023, era="CE", calendar="gregorian")
    print(f"Basic components: day={components.day}, month={components.month}, year={components.year}")
    
    # Example 2: Validated date components
    print("\n=== Example 2: Validated Date Components ===")
    try:
        valid_date = DateComponentsDefault(day=15, month=3, year=2023)
        print("Valid date created successfully")
        
        # This should raise an error
        # invalid_date = DateComponentsDefault(day=35, month=3, year=2023)
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Example 3: Date metadata
    print("\n=== Example 3: Date Metadata ===")
    meta = DateMeta(
        text="15 March 2023",
        lang="en", 
        precision="day",
        confidence=0.95,
        is_complete_date=True
    )
    print(f"Metadata: text='{meta.text}', confidence={meta.confidence}")
    
    # Example 4: Full parsed date
    print("\n=== Example 4: Full Parsed Date ===")
    raw_components = DateComponents(day="15", month="March", year="2023", era="CE")
    date_meta = DateMeta(text="15 March 2023", lang="en")
    
    parsed = ParsedDate(
        raw=raw_components,
        standard=DateComponents(),  # Will be auto-populated
        numeric=DateComponents(),   # Will be auto-populated  
        meta=date_meta
    )
    
    print(f"Parsed date string: {parsed}")
    print(f"Day: {parsed.day}, Month: {parsed.month}, Month number: {parsed.month_num}")
    print(f"Complete date: {parsed.is_complete_date}")
    print(f"Analysis:\n{parsed.analysis_date()}")
    
    # Example 5: Dictionary export
    print("\n=== Example 5: Dictionary Export ===")
    standard_dict = parsed.to_dict("standard")
    print(f"Standard format: {standard_dict}")
    
    numeric_dict = parsed.to_dict("numeric") 
    print(f"Numeric format: {numeric_dict}")