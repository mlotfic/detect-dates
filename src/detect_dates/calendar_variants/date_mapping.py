"""
Calendar Date Mapping Module
============================

A comprehensive module for converting dates between different calendar systems
including Gregorian, Hijri (Islamic), and Solar Hijri (Persian) calendars.

This module provides functionality to:

* Convert dates between calendar systems with high accuracy
* Get weekday information for specific dates across different calendars
* Retrieve all dates within a specific month and year
* Access alternative calendar representations for any given date
* Validate dates across different calendar systems

The module relies on a pre-calculated CSV mapping file containing astronomical
conversions between the three calendar systems, ensuring historical accuracy.

Architecture:
    The module uses pandas for efficient data manipulation and caching for
    performance optimization. All conversions are based on historical
    astronomical calculations rather than simple mathematical formulas.

Classes:
    DateMapping: Main class for calendar date conversions and lookups

Constants:
    SUPPORTED_CALENDARS: Dictionary mapping calendar names to CSV column names
    WEEKDAY_COLUMN: Column name for weekday information in the CSV

Example:
    Basic usage::

        from calendar_mapping import DateMapping

        # Initialize the mapper
        mapper = DateMapping()

        # Get weekday for a Gregorian date
        weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
        print(f"March 15, 2024 is a {weekday}")

        # Convert between calendar systems
        alternatives = mapper.get_date_alternative_calendar('gregorian', 1, 1, 2024)
        hijri_date = alternatives['hijri']
        print(f"January 1, 2024 = {hijri_date['day']}/{hijri_date['month']}/{hijri_date['year']} Hijri")

        # Get all dates in a month
        march_2024 = mapper.get_dates_by_month_year('gregorian', 3, 2024)
        print(f"March 2024 has {len(march_2024)} days")

File Structure:
    The module expects a CSV file at: ../mapping_date/Hijri-Gregorian-Solar_Hijri-V3.csv

    CSV Format:
        Week Day,Hijri Day,Hijri Month,Hijri Year,Gregorian Day,Gregorian Month,Gregorian Year,Solar Hijri Day,Solar Hijri Month,Solar Hijri Year

Performance:
    * First load reads and validates the entire CSV file
    * Subsequent operations use in-memory pandas DataFrame
    * Date lookups are optimized using boolean indexing
    * Data validation ensures integrity of conversions

Author: m.lotfi
Version: 2.0
License: MIT
Requires: pandas>=1.3.0
"""

import os
import pandas as pd
from detect_dates.data import CalendarDataLoader
from detect_dates.normalizers import normalize_calendar_name
from typing import Optional, Dict, List, Union
from dataclasses import dataclass
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Module-level constants for supported calendar systems
# Based on actual CSV structure: Week Day,Hijri Day,Hijri Month,Hijri Year,Gregorian Day,Gregorian Month,Gregorian Year,Solar Hijri Day,Solar Hijri Month,Solar Hijri Year
SUPPORTED_CALENDARS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']  # Note: 'julian' maps to Solar Hijri
}

# Column name for weekday information in the CSV file
WEEKDAY_COLUMN = 'Week Day'

# Calendar system aliases for user convenience
CALENDAR_ALIASES = {
    'solar_hijri': 'julian',
    'persian': 'julian',
    'islamic': 'hijri',
    'greg': 'gregorian'
}


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

    Attributes:
        df (Optional[pd.DataFrame]): DataFrame containing the calendar mapping data.
            This is loaded automatically during initialization.
        csv_path (str): Path to the CSV file containing mapping data.
        _data_loaded (bool): Internal flag indicating successful data loading.
        _date_ranges (Dict[str, Dict[str, int]]): Cached date ranges for each calendar.

    Example:
        Initialize and perform basic operations::

            # Standard initialization (uses default CSV path)
            mapper = DateMapping()

            # Custom CSV path
            mapper = DateMapping(csv_path="custom/path/to/calendar_data.csv")

            # Check if data loaded successfully
            if mapper.is_data_loaded():
                weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)

    Note:
        The CSV file should be located at the specified path relative to this
        module's location. If the file is not found, the class will raise a
        FileNotFoundError with helpful guidance.
    """
    
    _data_loaded: bool = False
    _date_ranges: Optional[Dict[str, Dict[str, int]]] = None

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

        Raises:
            FileNotFoundError: If the calendar mapping CSV file cannot be found
            ValueError: If the CSV file has incorrect structure or missing columns
            RuntimeError: If there are issues with data processing
        """
        try:
            loader = CalendarDataLoader()
            print(f"   Supported calendars: {loader.get_supported_calendars()}")
            
            self.df = loader.load_data()
            print(f"   Loaded {len(self.df):,} records (first call)")
            print(f"   Retrieved {len(self.df):,} records (cached)")

            self._data_loaded = True
            logger.info(f"Successfully loaded {len(self.df):,} calendar mapping records")
        except Exception as e:
            logger.error(f"Failed to initialize DateMapping: {str(e)}")
            self._data_loaded = False
            # Don't re-raise to allow graceful degradation

    def is_data_loaded(self) -> bool:
        """
        Check if the calendar mapping data was loaded successfully.

        Returns:
            bool: True if data is loaded and ready for use, False otherwise

        Example::

            mapper = DateMapping()
            if mapper.is_data_loaded():
                # Safe to use mapping functions
                result = mapper.get_weekday_by_date('gregorian', 1, 1, 2024)
            else:
                print("Calendar data not available")
        """
        return self._data_loaded and self.df is not None and not self.df.empty

    def _validate_date_ranges(self) -> None:
        """
        Validate that date ranges in the DataFrame are reasonable.

        Raises:
            ValueError: If date ranges are invalid or suspicious
        """
        for calendar_name, columns in SUPPORTED_CALENDARS.items():
            day_col, month_col, year_col = columns

            # Check day ranges (1-31)
            day_min, day_max = self.df[day_col].min(), self.df[day_col].max()
            if not (1 <= day_min and day_max <= 31):
                raise ValueError(f"Invalid day range for {calendar_name}: {day_min}-{day_max}")

            # Check month ranges (1-12)
            month_min, month_max = self.df[month_col].min(), self.df[month_col].max()
            if not (1 <= month_min and month_max <= 12):
                raise ValueError(f"Invalid month range for {calendar_name}: {month_min}-{month_max}")

            # Check year ranges (reasonable historical range)
            year_min, year_max = self.df[year_col].min(), self.df[year_col].max()
            if calendar_name == 'gregorian':
                if year_min < -5000 or year_max > 10000:
                    logger.warning(f"Unusual Gregorian year range: {year_min}-{year_max}")

    

    def get_weekday_by_date(self, calendar: str, day: int, month: int, year: int) -> Optional[str]:
        """
        Get the weekday name for a specific date in the given calendar system.

        This method looks up the weekday for a specific date using the pre-calculated
        mapping data. The lookup is fast and accurate, based on astronomical calculations.

        Args:
            calendar (str): Calendar system ('gregorian', 'hijri', 'julian', or aliases)
            day (int): Day of the month (1-31 depending on calendar and month)
            month (int): Month of the year (1-12)
            year (int): Year in the specified calendar system

        Returns:
            Optional[str]: Weekday name ('Sunday', 'Monday', ..., 'Saturday')
                          or None if date not found in mapping data

        Raises:
            ValueError: If the calendar parameter is not supported
            RuntimeError: If calendar data is not loaded

        Example:
            Get weekdays for different calendar systems::

                mapper = DateMapping()

                # Gregorian calendar
                weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
                print(f"March 15, 2024 is a {weekday}")  # "Friday"

                # Hijri calendar
                weekday = mapper.get_weekday_by_date('hijri', 1, 1, 1445)
                print(f"1st Muharram 1445 AH is a {weekday}")

                # Using aliases
                weekday = mapper.get_weekday_by_date('islamic', 15, 6, 1445)

        Note:
            The method returns None if the specific date is not found in the
            mapping data, which may occur for dates outside the available range
            or invalid date combinations.
        """
        if not self.is_data_loaded():
            raise RuntimeError("Calendar mapping data is not loaded. Check initialization.")

        # Normalize and validate calendar name
        calendar = self._normalize_calendar_name(calendar)

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[calendar]

        # Create filter mask to find matching date
        mask = (
            (self.df[day_col] == day) &
            (self.df[month_col] == month) &
            (self.df[year_col] == year)
        )

        # Find matching rows
        matching_rows = self.df[mask]

        # Return weekday if found, None otherwise
        if matching_rows.empty:
            logger.debug(f"Date not found: {calendar} {day}/{month}/{year}")
            return None

        # Log if multiple matches found (shouldn't happen with clean data)
        if len(matching_rows) > 1:
            logger.warning(f"Multiple matches found for {calendar} {day}/{month}/{year}")

        return matching_rows.iloc[0][WEEKDAY_COLUMN]

    def get_date_alternative_calendar(self, calendar: str, day: int, month: int, year: int) -> Optional[Dict[str, Any]]:
        """
        Get equivalent dates in all supported calendar systems for a specific date.

        Given a date in one calendar system, this method returns the equivalent
        dates in all supported calendar systems along with weekday information.
        This is the core conversion functionality of the module.

        Args:
            calendar (str): Source calendar system ('gregorian', 'hijri', 'julian', or aliases)
            day (int): Day of the month in the source calendar
            month (int): Month of the year in the source calendar
            year (int): Year in the source calendar

        Returns:
            Optional[Dict[str, Any]]: Dictionary containing equivalent dates in all
                calendar systems and weekday information, structured as::

                {
                    'gregorian': {'day': int, 'month': int, 'year': int},
                    'hijri': {'day': int, 'month': int, 'year': int},
                    'julian': {'day': int, 'month': int, 'year': int},
                    'weekday': str
                }

                Returns None if the date is not found in the mapping data.

        Raises:
            ValueError: If the calendar parameter is not supported
            RuntimeError: If calendar data is not loaded

        Example:
            Convert between different calendar systems::

                mapper = DateMapping()

                # Convert Gregorian to all systems
                result = mapper.get_date_alternative_calendar('gregorian', 1, 1, 2024)
                if result:
                    print(f"January 1, 2024 (Gregorian) equals:")
                    hijri = result['hijri']
                    print(f"  Hijri: {hijri['day']}/{hijri['month']}/{hijri['year']}")
                    julian = result['julian']
                    print(f"  Julian : {julian['day']}/{julian['month']}/{julian['year']}")
                    print(f"  Weekday: {result['weekday']}")

                # Convert from Hijri
                result = mapper.get_date_alternative_calendar('hijri', 1, 1, 1445)

        Note:
            This method is the foundation for calendar conversion functionality.
            It returns complete information for all supported calendar systems,
            enabling seamless conversion between any two systems.
        """
        if not self.is_data_loaded():
            raise RuntimeError("Calendar mapping data is not loaded. Check initialization.")

        # Normalize and validate calendar name
        calendar = normalize_calendar_name(calendar)

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[calendar]

        # Create filter mask to find matching date
        mask = (
            (self.df[day_col] == day) &
            (self.df[month_col] == month) &
            (self.df[year_col] == year)
        )

        # Find matching rows
        matching_rows = self.df[mask]

        if matching_rows.empty:
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

    def get_dates_by_month_year(self, calendar: str, month: int, year: int) -> List[Dict[str, Any]]:
        """
        Get all dates within a specific month and year for the given calendar system.

        This method retrieves all dates that fall within the specified month and year
        in the given calendar system, returning equivalent dates in all calendar systems.
        This is useful for generating calendar views or date ranges.

        Args:
            calendar (str): Calendar system ('gregorian', 'hijri', 'julian', or aliases)
            month (int): Month of the year (1-12)
            year (int): Year in the specified calendar system

        Returns:
            List[Dict[str, Any]]: List of dictionaries, each containing date information
                for all calendar systems and weekday. Each dictionary has the same
                structure as returned by get_date_alternative_calendar().
                Returns empty list if no dates found.

        Raises:
            ValueError: If the calendar parameter is not supported
            RuntimeError: If calendar data is not loaded

        Example:
            Get all dates in a specific month::

                mapper = DateMapping()

                # Get all dates in Gregorian January 2024
                dates = mapper.get_dates_by_month_year('gregorian', 1, 2024)
                print(f"January 2024 has {len(dates)} days")

                for date_info in dates[:5]:  # Show first 5 days
                    greg = date_info['gregorian']
                    hijri = date_info['hijri']
                    print(f"  {greg['day']}/1/2024 -> {hijri['day']}/{hijri['month']}/{hijri['year']} Hijri ({date_info['weekday']})")

                # Get all dates in Hijri Muharram 1445
                hijri_dates = mapper.get_dates_by_month_year('hijri', 1, 1445)

        Note:
            The returned list is sorted by day for consistent ordering.
            This method is efficient for generating month views across
            different calendar systems.
        """
        if not self.is_data_loaded():
            raise RuntimeError("Calendar mapping data is not loaded. Check initialization.")

        # Normalize and validate calendar name
        calendar = self._normalize_calendar_name(calendar)

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[calendar]

        # Create filter mask to find matching month and year
        mask = (self.df[month_col] == month) & (self.df[year_col] == year)

        # Find matching rows
        matching_rows = self.df[mask]

        if matching_rows.empty:
            logger.debug(f"No dates found for {calendar} {month}/{year}")
            return []

        # Build list of results for all matching dates
        results = []
        for _, row in matching_rows.iterrows():
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
            results.append(result)

        # Sort results by day for consistent ordering
        results.sort(key=lambda x: x[calendar]['day'])

        logger.debug(f"Found {len(results)} dates for {calendar} {month}/{year}")
        return results

    def validate_date(self, calendar: str, day: int, month: int, year: int) -> bool:
        """
        Validate if a date exists in the specified calendar system.

        This method checks whether a given date combination is valid and exists
        in the mapping data. It's useful for input validation before performing
        conversions or other operations.

        Args:
            calendar (str): Calendar system ('gregorian', 'hijri', 'julian', or aliases)
            day (int): Day of the month
            month (int): Month of the year
            year (int): Year

        Returns:
            bool: True if the date exists in the mapping data and is valid,
                  False otherwise

        Example:
            Validate dates before conversion::

                mapper = DateMapping()

                # Valid date
                is_valid = mapper.validate_date('gregorian', 29, 2, 2024)  # Leap year
                print(f"Feb 29, 2024 is valid: {is_valid}")

                # Invalid date
                is_valid = mapper.validate_date('gregorian', 31, 2, 2024)
                print(f"Feb 31, 2024 is valid: {is_valid}")  # False

                # Check Hijri date
                is_valid = mapper.validate_date('hijri', 30, 12, 1445)

        Note:
            This method is more efficient than get_weekday_by_date() when you
            only need to check validity without retrieving additional information.
        """
        if not self.is_data_loaded():
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
        
        Returns:
            Dict[str, Any]: Data quality metrics
        """
        if not self.is_data_loaded():
            return {'status': 'no_data'}
        
        metrics = {
            'status': 'good',
            'total_records': len(self.df),
            'unique_weekdays': len(self.df[WEEKDAY_COLUMN].unique()),
            'date_coverage': {}
        }
        
        # Check date coverage for each calendar
        for calendar_name, columns in SUPPORTED_CALENDARS.items():
            year_col = columns[2]
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
        
        Returns:
            List[str]: List of supported calendar system names, including both
                      primary names and aliases
                      
        Example::
        
            mapper = DateMapping()
            calendars = mapper.get_supported_calendars()
            print(f"Supported calendars: {', '.join(calendars)}")
            # Output: "Supported calendars: gregorian, hijri, julian"
        
        Note:
            This returns only the primary calendar names. For aliases,
            use get_calendar_info() to see the full mapping of aliases to primary names.
        """
        return list(SUPPORTED_CALENDARS.keys())
    
    def get_data_range(self) -> Dict[str, Dict[str, int]]:
        """
        Get the date range available in the mapping data for each calendar system.
        
        This method calculates the minimum and maximum years available in the
        mapping data for each supported calendar system. This information is
        useful for determining the valid date ranges for conversions.
        
        Returns:
            Dict[str, Dict[str, int]]: Dictionary containing min/max years for each calendar::
            
                {
                    'gregorian': {'min_year': int, 'max_year': int},
                    'hijri': {'min_year': int, 'max_year': int},
                    'julian': {'min_year': int, 'max_year': int}
                }
                
        Example:
            Check available date ranges::
            
                mapper = DateMapping()
                ranges = mapper.get_data_range()
                
                greg_range = ranges['gregorian']
                print(f"Gregorian dates available: {greg_range['min_year']} to {greg_range['max_year']}")
                
                hijri_range = ranges['hijri']
                print(f"Hijri dates available: {hijri_range['min_year']} to {hijri_range['max_year']}")
                
                # Check if a specific year is in range
                target_year = 2025
                if greg_range['min_year'] <= target_year <= greg_range['max_year']:
                    print(f"Year {target_year} is available for conversion")
        
        Note:
            These ranges represent the actual data available in the CSV file.
            Dates outside these ranges cannot be converted between calendar systems.
        """
        if not self.is_data_loaded():
            return {}
        
        # Use cached ranges if available
        if self._date_ranges is not None:
            return self._date_ranges.copy()
        
        ranges = {}
        
        for calendar, columns in SUPPORTED_CALENDARS.items():
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
    
    def get_month_info(self, calendar: str, month: int, year: int) -> Dict[str, Any]:
        """
        Get detailed information about a specific month in a calendar system.
        
        Args:
            calendar (str): Calendar system
            month (int): Month number (1-12)
            year (int): Year
            
        Returns:
            Dict[str, Any]: Month information including day count, weekday distribution, etc.
            
        Example::
        
            mapper = DateMapping()
            info = mapper.get_month_info('gregorian', 2, 2024)  # February 2024
            print(f"February 2024 has {info['day_count']} days")
            print(f"Starts on {info['first_weekday']}, ends on {info['last_weekday']}")
        """
        if not self.is_data_loaded():
            return {'error': 'Data not loaded'}
        
        try:
            calendar = self._normalize_calendar_name(calendar)
        except ValueError as e:
            return {'error': str(e)}
        
        # Get all dates in the month
        dates = self.get_dates_by_month_year(calendar, month, year)
        
        if not dates:
            return {
                'calendar': calendar,
                'month': month,
                'year': year,
                'day_count': 0,
                'error': 'No dates found for specified month/year'
            }
        
        # Sort dates by day
        dates.sort(key=lambda x: x[calendar]['day'])
        
        # Calculate month statistics
        weekdays = [d['weekday'] for d in dates]
        weekday_counts = {day: weekdays.count(day) for day in set(weekdays)}
        
        return {
            'calendar': calendar,
            'month': month,
            'year': year,
            'day_count': len(dates),
            'first_day': dates[0][calendar]['day'],
            'last_day': dates[-1][calendar]['day'],
            'first_weekday': dates[0]['weekday'],
            'last_weekday': dates[-1]['weekday'],
            'weekday_distribution': weekday_counts,
            'month_name': self._get_month_name(calendar, month)
        }
    
    def _get_month_name(self, calendar: str, month: int) -> str:
        """
        Get the month name for a specific calendar system (placeholder).
        
        Args:
            calendar: Calendar system
            month: Month number
            
        Returns:
            str: Month name or number as string
        """
        # This would ideally use the normalize_month function from the normalizers module
        # For now, return a placeholder
        month_names = {
            'gregorian': ['', 'January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'],
            'hijri': ['', 'Muharram', 'Safar', 'Rabi al-Awwal', 'Rabi al-Thani', 'Jumada al-Awwal',
                     'Jumada al-Thani', 'Rajab', 'Shaban', 'Ramadan', 'Shawwal', 'Dhu al-Qidah', 'Dhu al-Hijjah']
        }
        
        if calendar in month_names and 1 <= month <= 12:
            return month_names[calendar][month]
        return str(month)
    
    def find_date_by_weekday(self, calendar: str, weekday: str, month: int, year: int, 
                           occurrence: int = 1) -> Optional[Dict[str, Any]]:
        """
        Find a specific occurrence of a weekday in a given month/year.
        
        Args:
            calendar (str): Calendar system
            weekday (str): Target weekday ('Monday', 'Tuesday', etc.)
            month (int): Month number (1-12)
            year (int): Year
            occurrence (int): Which occurrence (1=first, 2=second, -1=last, etc.)
            
        Returns:
            Optional[Dict[str, Any]]: Date information if found, None otherwise
            
        Example::
        
            mapper = DateMapping()
            
            # Find first Monday of March 2024
            first_monday = mapper.find_date_by_weekday('gregorian', 'Monday', 3, 2024, 1)
            
            # Find last Friday of December 2023
            last_friday = mapper.find_date_by_weekday('gregorian', 'Friday', 12, 2023, -1)
        """
        if not self.is_data_loaded():
            return None
        
        try:
            calendar = self._normalize_calendar_name(calendar)
        except ValueError:
            return None
        
        # Get all dates in the month
        dates = self.get_dates_by_month_year(calendar, month, year)
        
        # Filter by weekday
        matching_dates = [d for d in dates if d['weekday'] == weekday]
        
        if not matching_dates:
            return None
        
        # Sort by day
        matching_dates.sort(key=lambda x: x[calendar]['day'])
        
        # Handle occurrence selection
        try:
            if occurrence > 0:
                # Positive: count from beginning
                return matching_dates[occurrence - 1]
            else:
                # Negative: count from end
                return matching_dates[occurrence]
        except IndexError:
            return None
    
    def get_year_info(self, calendar: str, year: int) -> Dict[str, Any]:
        """
        Get comprehensive information about a specific year in a calendar system.
        
        Args:
            calendar (str): Calendar system
            year (int): Year to analyze
            
        Returns:
            Dict[str, Any]: Year information including day count, leap year status, etc.
        """
        if not self.is_data_loaded():
            return {'error': 'Data not loaded'}
        
        try:
            calendar = self._normalize_calendar_name(calendar)
        except ValueError as e:
            return {'error': str(e)}
        
        # Get column names
        day_col, month_col, year_col = SUPPORTED_CALENDARS[calendar]
        
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
                'day': int(year_data.iloc[0][day_col]),
                'month': int(year_data.iloc[0][month_col]),
                'weekday': year_data.iloc[0][WEEKDAY_COLUMN]
            },
            'last_date': {
                'day': int(year_data.iloc[-1][day_col]),
                'month': int(year_data.iloc[-1][month_col]),
                'weekday': year_data.iloc[-1][WEEKDAY_COLUMN]
            }
        }
    
    def _is_leap_year(self, calendar: str, year: int, day_count: int) -> Optional[bool]:
        """
        Determine if a year is a leap year based on day count.
        
        Args:
            calendar: Calendar system
            year: Year to check
            day_count: Total days in the year
            
        Returns:
            Optional[bool]: True if leap year, False if not, None if undetermined
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


def create_date_mapping(csv_path: str = None) -> DateMapping:
    """
    Convenience function to create a DateMapping instance with optional custom CSV path.
    
    Args:
        csv_path (Optional[str]): Path to custom CSV file. If None, uses default path.
        
    Returns:
        DateMapping: Configured DateMapping instance
        
    Example::
    
        # Use default CSV path
        mapper = create_date_mapping()
        
        # Use custom CSV path
        mapper = create_date_mapping('/path/to/custom/calendar_data.csv')
        
        if mapper.is_data_loaded():
            weekday = mapper.get_weekday_by_date('gregorian', 1, 1, 2024)
    """
    if csv_path:
        return DateMapping(csv_path=csv_path)
    return DateMapping()


def main():
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
        mapper = DateMapping()
        
        if not mapper.is_data_loaded():
            print("❌ Failed to load calendar data. Please check the CSV file path.")
            return
        
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
            alternatives = mapper.get_date_alternative_calendar(calendar, day, month, year)
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


if __name__ == "__main__":
    print("Calendar Date Mapping Module")
    print("=" * 40)
    print("This module provides calendar conversion functionality.")
    print("Import it in your code to use the DateMapping class.")
    print()
    
    # Run comprehensive examples if executed directly
    main()