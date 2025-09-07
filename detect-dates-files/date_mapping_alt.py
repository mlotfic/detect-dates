"""
Calendar Date Mapping Module
============================

A comprehensive module for converting dates between different calendar systems
including Gregorian, Hijri (Islamic), and Solar Hijri (Persian) calendars.

This module provides functionality to:
- Convert dates between calendar systems
- Get weekday information for specific dates
- Retrieve all dates within a specific month and year
- Access alternative calendar representations

The module relies on a CSV mapping file containing pre-calculated conversions
between the three calendar systems.

Classes:
    DateMapping: Main class for calendar date conversions and lookups

Example:
    >>> from calendar_mapping import DateMapping
    >>> mapper = DateMapping()
    >>> weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
    >>> print(f"Weekday: {weekday}")

Author: m.lotfi
Version: 2.0
"""

import os
import pandas as pd
from typing import Optional, Dict, List, Any, Union
from dataclasses import dataclass


# Module-level constants for supported calendar systems
# Based on actual CSV structure: Week Day,Hijri Day,Hijri Month,Hijri Year,Gregorian Day,Gregorian Month,Gregorian Year,Solar Hijri Day,Solar Hijri Month,Solar Hijri Year
SUPPORTED_CALENDARS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'Jalali': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
}

# Column name for weekday information
WEEKDAY_COLUMN = 'Week Day'


@dataclass
class DateMapping:
    """
    A class for mapping and converting dates between different calendar systems.

    This class provides methods to convert dates between Gregorian, Hijri (Islamic),
    and Solar Hijri (Persian) calendar systems. It uses a pre-calculated CSV mapping
    file to ensure accuracy in conversions.

    Attributes:
        df (pd.DataFrame): DataFrame containing the calendar mapping data

    Note:
        The CSV file should be located at: ../mapping_date/Hijri-Gregorian-Solar_Hijri-V3.csv
        relative to this module's location.
    """

    df: Optional[pd.DataFrame] = None

    def __post_init__(self) -> None:
        """
        Initialize the DateMapping instance by loading the calendar data.

        This method is automatically called after object creation to load
        the mapping data from the CSV file.

        Raises:
            FileNotFoundError: If the calendar mapping CSV file cannot be found
        """
        self.df = self._load_mapping_data()

    def _load_mapping_data(self) -> pd.DataFrame:
        """
        Load the calendar mapping data from CSV file.

        Loads the pre-calculated calendar conversion data from a CSV file
        containing mappings between Gregorian, Hijri, and Solar Hijri dates.

        Returns:
            pd.DataFrame: DataFrame containing the calendar mapping data

        Raises:
            FileNotFoundError: If the calendar data file is not found

        Note:
            The expected CSV structure should include columns for each calendar
            system's day, month, year, and weekday information.
        """
        # Construct path to the CSV file relative to this module
        file_path = os.path.join(
            os.path.dirname(__file__),
            "..", "mapping_date", "Hijri-Gregorian-Solar_Hijri-V3.csv"
        )
        file_path = os.path.abspath(file_path)

        # Verify file exists before attempting to load
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Calendar data file not found: {file_path}. "
                f"Please ensure the CSV file exists in the expected location."
            )

        try:
            # Load CSV with UTF-8 encoding to handle international characters
            df = pd.read_csv(file_path, encoding='utf-8')

            # Validate that all required columns are present
            required_columns = set()
            for calendar_cols in SUPPORTED_CALENDARS.values():
                required_columns.update(calendar_cols)
            required_columns.add(WEEKDAY_COLUMN)

            missing_columns = required_columns - set(df.columns)
            if missing_columns:
                raise ValueError(f"Missing required columns in CSV: {missing_columns}")

            # Clean and validate data
            df = df.dropna()  # Remove rows with missing values

            # Convert numeric columns to proper types
            for calendar_cols in SUPPORTED_CALENDARS.values():
                for col in calendar_cols:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # Remove any rows where conversion failed
            df = df.dropna()

            return df

        except Exception as e:
            raise RuntimeError(f"Failed to load calendar data: {str(e)}")

    def get_weekday_by_date(self, era: str, day: int, month: int, year: int) -> Optional[str]:
        """
        Get the weekday name for a specific date in the given calendar system.

        Args:
            era (str): Calendar system ('gregorian', 'hijri', or 'Jalali')
            day (int): Day of the month (1-31 depending on calendar and month)
            month (int): Month of the year (1-12)
            year (int): Year in the specified calendar system

        Returns:
            Optional[str]: Weekday name (e.g., 'Monday', 'Tuesday') or None if date not found

        Raises:
            ValueError: If the era parameter is not supported

        Example:
            >>> mapper = DateMapping()
            >>> weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
            >>> print(weekday)  # Output: 'Friday'
        """
        # Validate input parameters
        if era not in SUPPORTED_CALENDARS:
            raise ValueError(
                f"Unsupported calendar era: '{era}'. "
                f"Supported eras: {list(SUPPORTED_CALENDARS.keys())}"
            )

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[era]

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
            return None

        return matching_rows.iloc[0][WEEKDAY_COLUMN]

    def get_date_alternative_calendar(self, era: str, day: int, month: int, year: int) -> Optional[Dict[str, Any]]:
        """
        Get equivalent dates in all calendar systems for a specific date.

        Given a date in one calendar system, this method returns the equivalent
        dates in all supported calendar systems along with weekday information.

        Args:
            era (str): Source calendar system ('gregorian', 'hijri', or 'Jalali')
            day (int): Day of the month in the source calendar
            month (int): Month of the year in the source calendar
            year (int): Year in the source calendar

        Returns:
            Optional[Dict[str, Any]]: Dictionary containing equivalent dates in all
                calendar systems and weekday, or None if date not found

        Raises:
            ValueError: If the era parameter is not supported

        Example:
            >>> mapper = DateMapping()
            >>> result = mapper.get_date_alternative_calendar('gregorian', 1, 1, 2024)
            >>> print(result['hijri'])  # Output: {'day': 19, 'month': 6, 'year': 1445}
        """
        # Validate input parameters
        if era not in SUPPORTED_CALENDARS:
            raise ValueError(
                f"Unsupported calendar era: '{era}'. "
                f"Supported eras: {list(SUPPORTED_CALENDARS.keys())}"
            )

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[era]

        # Create filter mask to find matching date
        mask = (
            (self.df[day_col] == day) &
            (self.df[month_col] == month) &
            (self.df[year_col] == year)
        )

        # Find matching rows
        matching_rows = self.df[mask]

        if matching_rows.empty:
            return None

        # Get the first matching row
        row = matching_rows.iloc[0]

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
            'Jalali': {
                'day': int(row['Solar Hijri Day']),
                'month': int(row['Solar Hijri Month']),
                'year': int(row['Solar Hijri Year'])
            },
            'weekday': row[WEEKDAY_COLUMN]
        }

        return result

    def get_dates_by_month_year(self, era: str, month: int, year: int) -> List[Dict[str, Any]]:
        """
        Get all dates within a specific month and year for the given calendar system.

        This method retrieves all dates that fall within the specified month and year
        in the given calendar system, returning equivalent dates in all calendar systems.

        Args:
            era (str): Calendar system ('gregorian', 'hijri', or 'Jalali')
            month (int): Month of the year (1-12)
            year (int): Year in the specified calendar system

        Returns:
            List[Dict[str, Any]]: List of dictionaries, each containing date information
                for all calendar systems and weekday. Empty list if no dates found.

        Raises:
            ValueError: If the era parameter is not supported

        Example:
            >>> mapper = DateMapping()
            >>> dates = mapper.get_dates_by_month_year('gregorian', 1, 2024)
            >>> print(f"Found {len(dates)} dates in January 2024")
        """
        # Validate input parameters
        if era not in SUPPORTED_CALENDARS:
            raise ValueError(
                f"Unsupported calendar era: '{era}'. "
                f"Supported eras: {list(SUPPORTED_CALENDARS.keys())}"
            )

        # Get column names for the specified calendar system
        day_col, month_col, year_col = SUPPORTED_CALENDARS[era]

        # Create filter mask to find matching month and year
        mask = (self.df[month_col] == month) & (self.df[year_col] == year)

        # Find matching rows
        matching_rows = self.df[mask]

        if matching_rows.empty:
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
                'Jalali': {
                    'day': int(row['Solar Hijri Day']),
                    'month': int(row['Solar Hijri Month']),
                    'year': int(row['Solar Hijri Year'])
                },
                'weekday': row[WEEKDAY_COLUMN]
            }
            results.append(result)

        # Sort results by day for consistent ordering
        results.sort(key=lambda x: x[era]['day'])
        return results

    def validate_date(self, era: str, day: int, month: int, year: int) -> bool:
        """
        Validate if a date exists in the specified calendar system.

        Args:
            era (str): Calendar system ('gregorian', 'hijri', or 'Jalali')
            day (int): Day of the month
            month (int): Month of the year
            year (int): Year

        Returns:
            bool: True if the date exists in the mapping data, False otherwise

        Example:
            >>> mapper = DateMapping()
            >>> is_valid = mapper.validate_date('gregorian', 29, 2, 2024)  # Leap year
            >>> print(is_valid)  # Output: True or False based on data availability
        """
        try:
            result = self.get_weekday_by_date(era, day, month, year)
            return result is not None
        except ValueError:
            return False

    def get_calendar_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the loaded calendar data.

        Returns:
            Dict[str, Any]: Dictionary containing data statistics and information

        Example:
            >>> mapper = DateMapping()
            >>> info = mapper.get_calendar_info()
            >>> print(f"Total records: {info['total_records']}")
        """
        if self.df is None or self.df.empty:
            return {"error": "No data loaded"}

        info = {
            'total_records': len(self.df),
            'supported_calendars': self.get_supported_calendars(),
            'date_ranges': self.get_data_range(),
            'weekdays': sorted(self.df[WEEKDAY_COLUMN].unique().tolist()),
            'csv_columns': list(self.df.columns),
            'sample_record': {}
        }

        # Add a sample record for reference
        if not self.df.empty:
            sample_row = self.df.iloc[0]
            info['sample_record'] = {
                'gregorian': f"{sample_row['Gregorian Day']}/{sample_row['Gregorian Month']}/{sample_row['Gregorian Year']}",
                'hijri': f"{sample_row['Hijri Day']}/{sample_row['Hijri Month']}/{sample_row['Hijri Year']}",
                'Jalali': f"{sample_row['Solar Hijri Day']}/{sample_row['Solar Hijri Month']}/{sample_row['Solar Hijri Year']}",
                'weekday': sample_row[WEEKDAY_COLUMN]
            }

        return info
        """
        Get list of supported calendar systems.

        Returns:
            List[str]: List of supported calendar system names

        Example:
            >>> mapper = DateMapping()
            >>> calendars = mapper.get_supported_calendars()
            >>> print(calendars)  # Output: ['gregorian', 'hijri', 'Jalali']
        """
        return list(SUPPORTED_CALENDARS.keys())

    def get_data_range(self) -> Dict[str, Dict[str, int]]:
        """
        Get the date range available in the mapping data for each calendar system.

        Returns:
            Dict[str, Dict[str, int]]: Dictionary containing min/max years for each calendar

        Example:
            >>> mapper = DateMapping()
            >>> ranges = mapper.get_data_range()
            >>> print(f"Gregorian range: {ranges['gregorian']['min_year']} - {ranges['gregorian']['max_year']}")
        """
        ranges = {}

        for era, columns in SUPPORTED_CALENDARS.items():
            year_col = columns[2]  # Year column is always third
            ranges[era] = {
                'min_year': int(self.df[year_col].min()),
                'max_year': int(self.df[year_col].max())
            }

        return ranges

    def get_supported_calendars(self) -> List[str]:
        """
        Get list of supported calendar systems.

        Returns:
            List[str]: List of supported calendar system names
        """
        return list(SUPPORTED_CALENDARS.keys())

def main():
    """
    Main function demonstrating usage of the DateMapping class.

    This function provides examples of how to use the DateMapping class
    for various calendar conversion operations.
    """
    try:
        # Initialize the DateMapping instance
        print("Initializing DateMapping...")
        mapper = DateMapping()
        print("✓ DateMapping initialized successfully")
        print()

        # Display calendar information
        print("Calendar Data Information:")
        info = mapper.get_calendar_info()
        print(f"  Total records: {info['total_records']:,}")
        print(f"  Available weekdays: {', '.join(info['weekdays'])}")
        print(f"  Sample record: {info['sample_record']['gregorian']} = {info['sample_record']['hijri']} (Hijri) = {info['sample_record']['Jalali']} (Solar Hijri) - {info['sample_record']['weekday']}")
        print()

        # Display supported calendars
        print("Supported calendar systems:")
        for calendar in mapper.get_supported_calendars():
            print(f"  - {calendar}")
        print()

        # Display data ranges
        print("Available date ranges:")
        ranges = mapper.get_data_range()
        for era, range_info in ranges.items():
            print(f"  {era}: {range_info['min_year']} - {range_info['max_year']}")
        print()

        # Example 1: Get weekday for specific date
        print("Example 1: Getting weekday for specific dates")
        test_dates = [
            ('gregorian', 1, 1, 2024),
            ('hijri', 1, 1, 1445),
            ('Jalali', 1, 1, 1403)
        ]

        for era, day, month, year in test_dates:
            weekday = mapper.get_weekday_by_date(era, day, month, year)
            print(f"  {era.title()} {day}/{month}/{year}: {weekday}")
        print()

        # Example 2: Get alternative calendar dates
        print("Example 2: Converting between calendar systems")
        alternatives = mapper.get_date_alternative_calendar('gregorian', 1, 1, 2024)
        if alternatives:
            print(f"  Gregorian 1/1/2024 equals:")
            print(f"    Hijri: {alternatives['hijri']['day']}/{alternatives['hijri']['month']}/{alternatives['hijri']['year']}")
            print(f"    Solar Hijri: {alternatives['Jalali']['day']}/{alternatives['Jalali']['month']}/{alternatives['Jalali']['year']}")
            print(f"    Weekday: {alternatives['weekday']}")
        print()

        # Example 3: Get dates in a specific month
        print("Example 3: Getting all dates in a specific month")
        dates_in_month = mapper.get_dates_by_month_year('gregorian', 1, 2024)
        print(f"  Found {len(dates_in_month)} dates in Gregorian January 2024")

        # Show first few dates as example
        for i, date_info in enumerate(dates_in_month[:5]):
            greg = date_info['gregorian']
            hijri = date_info['hijri']
            print(f"    {greg['day']}/1/2024 -> Hijri {hijri['day']}/{hijri['month']}/{hijri['year']} ({date_info['weekday']})")

        if len(dates_in_month) > 5:
            print(f"    ... and {len(dates_in_month) - 5} more dates")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure the calendar mapping CSV file exists in the correct location.")


if __name__ == "__main__":
    print("Calendar Date Mapping Module")
    print("=" * 40)
    print("This module provides calendar conversion functionality.")
    print("Import it in your code to use the DateMapping class.")
    print()

    # Run examples if executed directly
   main()