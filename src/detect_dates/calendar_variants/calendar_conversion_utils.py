# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    def setup_src_path():
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 3]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                break
    print("This module is not intended to be run directly. Import it in your code.")
    setup_src_path()

from detect_dates.data import CalendarDataLoader
from typing import Optional, Dict, List, Union
import pandas as pd


class DateMapping:
    """
    Utility class for mapping and converting dates between Gregorian, Hijri, and Solar Hijri calendars.

    Attributes
    ----------
    df : pandas.DataFrame
        DataFrame containing calendar mapping data.
    """

    def __init__(self):
        """
        Initialize the DateMapping instance by loading the mapping DataFrame.
        """
        loader = CalendarDataLoader()
        print(f"   Supported calendars: {loader.get_supported_calendars()}")
        
        self.df = loader.load_data()
        print(f"   Loaded {len(self.df):,} records (first call)")
        print(f"   Retrieved {len(self.df):,} records (cached)")

    def get_weekday_by_date(self, era: str, day: int, month: int, year: int) -> Optional[str]:
        """
        Get the weekday name for a specific date in the given calendar era.

        Parameters
        ----------
        era : str
            Calendar system: 'gregorian', 'hijri', or 'solar_hijri'.
        day : int
            Day of the date.
        month : int
            Month of the date.
        year : int
            Year of the date.

        Returns
        -------
        str or None
            Weekday name (e.g., 'Monday') if found, otherwise None.

        Examples
        --------
        >>> dm = DateMapping()
        >>> dm.get_weekday_by_date('gregorian', 2, 5, 1900)
        'Wednesday'
        """
        # Map era to corresponding DataFrame columns
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year'],
            # Keep 'julian' for backward compatibility
            'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            raise ValueError(f"Invalid era '{era}'. Must be one of: {list(era_columns.keys())}")

        day_col, month_col, year_col = era_columns[era]

        # Filter DataFrame for matching date
        mask = (self.df[day_col] == day) & (self.df[month_col] == month) & (self.df[year_col] == year)
        matching_rows = self.df[mask]

        if matching_rows.empty:
            return None

        return matching_rows.iloc[0]['Week Day']

    def get_date_alternative_calendar(self, era: str, day: int, month: int, year: int) -> Optional[Dict[str, Union[Dict[str, int], str]]]:
        """
        Get equivalent dates in all calendar systems for a specific date.

        Parameters
        ----------
        era : str
            Calendar system: 'gregorian', 'hijri', or 'solar_hijri'.
        day : int
            Day of the date.
        month : int
            Month of the date.
        year : int
            Year of the date.

        Returns
        -------
        dict or None
            Dictionary with dates in all calendar systems and weekday, or None if not found.
            Format: {
                'gregorian': {'day': int, 'month': int, 'year': int},
                'hijri': {'day': int, 'month': int, 'year': int},
                'solar_hijri': {'day': int, 'month': int, 'year': int},
                'weekday': str
            }

        Examples
        --------
        >>> dm = DateMapping()
        >>> dm.get_date_alternative_calendar('hijri', 3, 1, 1318)
        {'gregorian': {...}, 'hijri': {...}, 'solar_hijri': {...}, 'weekday': 'Wednesday'}
        """
        # Map era to corresponding DataFrame columns
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year'],
            # Keep 'julian' for backward compatibility
            'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            raise ValueError(f"Invalid era '{era}'. Must be one of: {list(era_columns.keys())}")

        day_col, month_col, year_col = era_columns[era]

        # Filter DataFrame for matching date
        mask = (self.df[day_col] == day) & (self.df[month_col] == month) & (self.df[year_col] == year)
        matching_rows = self.df[mask]

        if matching_rows.empty:
            return None

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
            'solar_hijri': {
                'day': int(row['Solar Hijri Day']),
                'month': int(row['Solar Hijri Month']),
                'year': int(row['Solar Hijri Year'])
            },
            'weekday': str(row['Week Day'])
        }

        return result

    def get_dates_by_month_year(self, era: str, month: int, year: int) -> List[Dict[str, Union[Dict[str, int], str]]]:
        """
        Get all dates in the specified month and year for the given calendar era.

        Parameters
        ----------
        era : str
            Calendar system: 'gregorian', 'hijri', or 'solar_hijri'.
        month : int
            Month to search for.
        year : int
            Year to search for.

        Returns
        -------
        list of dict
            List of dictionaries with date information for all matching dates.
            Returns empty list if no matches.

        Examples
        --------
        >>> dm = DateMapping()
        >>> dm.get_dates_by_month_year('gregorian', 5, 1900)
        [{'gregorian': {...}, 'hijri': {...}, 'solar_hijri': {...}, 'weekday': 'Wednesday'}, ...]
        """
        # Map era to corresponding DataFrame columns
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year'],
            # Keep 'julian' for backward compatibility
            'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            raise ValueError(f"Invalid era '{era}'. Must be one of: {list(era_columns.keys())}")

        day_col, month_col, year_col = era_columns[era]

        # Filter DataFrame for matching month and year
        mask = (self.df[month_col] == month) & (self.df[year_col] == year)
        matching_rows = self.df[mask]

        if matching_rows.empty:
            return []

        results = []
        for _, row in matching_rows.iterrows():
            # Build result dictionary for each matching row
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
                'solar_hijri': {
                    'day': int(row['Solar Hijri Day']),
                    'month': int(row['Solar Hijri Month']),
                    'year': int(row['Solar Hijri Year'])
                },
                'weekday': str(row['Week Day'])
            }
            results.append(result)

        # Sort by day for consistent ordering
        results.sort(key=lambda x: x[era]['day'])
        
        return results

    def get_date_range(self, era: str, start_date: Dict[str, int], end_date: Dict[str, int]) -> List[Dict[str, Union[Dict[str, int], str]]]:
        """
        Get all dates between start_date and end_date (inclusive) for the given calendar era.

        Parameters
        ----------
        era : str
            Calendar system: 'gregorian', 'hijri', or 'solar_hijri'.
        start_date : dict
            Start date with keys: 'day', 'month', 'year'.
        end_date : dict
            End date with keys: 'day', 'month', 'year'.

        Returns
        -------
        list of dict
            List of dictionaries with date information for all dates in range.
        """
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year'],
            'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            raise ValueError(f"Invalid era '{era}'. Must be one of: {list(era_columns.keys())}")

        day_col, month_col, year_col = era_columns[era]

        # Create date comparison values for filtering
        def date_to_comparable(day, month, year):
            return year * 10000 + month * 100 + day

        start_comp = date_to_comparable(start_date['day'], start_date['month'], start_date['year'])
        end_comp = date_to_comparable(end_date['day'], end_date['month'], end_date['year'])

        # Create comparable column
        self.df['_temp_date_comp'] = self.df.apply(
            lambda row: date_to_comparable(row[day_col], row[month_col], row[year_col]), 
            axis=1
        )

        # Filter for date range
        mask = (self.df['_temp_date_comp'] >= start_comp) & (self.df['_temp_date_comp'] <= end_comp)
        matching_rows = self.df[mask]

        # Clean up temporary column
        self.df.drop('_temp_date_comp', axis=1, inplace=True)

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
                'solar_hijri': {
                    'day': int(row['Solar Hijri Day']),
                    'month': int(row['Solar Hijri Month']),
                    'year': int(row['Solar Hijri Year'])
                },
                'weekday': str(row['Week Day'])
            }
            results.append(result)

        return results

    def validate_date(self, era: str, day: int, month: int, year: int) -> bool:
        """
        Validate if a date exists in the given calendar era.

        Parameters
        ----------
        era : str
            Calendar system: 'gregorian', 'hijri', or 'solar_hijri'.
        day : int
            Day of the date.
        month : int
            Month of the date.
        year : int
            Year of the date.

        Returns
        -------
        bool
            True if date exists in the mapping, False otherwise.
        """
        return self.get_weekday_by_date(era, day, month, year) is not None


# Example usage
if __name__ == "__main__":
    # Create DateMapping instance
    dm = DateMapping()
    
    print("Sample DataFrame shape:", dm.df.shape)
    print("Columns:", dm.df.columns.tolist())
    print()

    # Example 1: Get weekday for specific date
    try:
        weekday = dm.get_weekday_by_date('gregorian', 2, 5, 1900)
        print(f"Weekday for Gregorian 2/5/1900: {weekday}")
    except ValueError as e:
        print(f"Error: {e}")

    # Example 2: Get alternative calendar dates
    try:
        alternatives = dm.get_date_alternative_calendar('hijri', 3, 1, 1318)
        print(f"Alternative calendars for Hijri 3/1/1318:")
        if alternatives:
            print(f"  Gregorian: {alternatives['gregorian']['day']}/{alternatives['gregorian']['month']}/{alternatives['gregorian']['year']}")
            print(f"  Solar Hijri: {alternatives['solar_hijri']['day']}/{alternatives['solar_hijri']['month']}/{alternatives['solar_hijri']['year']}")
            print(f"  Weekday: {alternatives['weekday']}")
        else:
            print("  Date not found in mapping.")
    except ValueError as e:
        print(f"Error: {e}")

    # Example 3: Get all dates in a specific month/year
    try:
        dates_in_month = dm.get_dates_by_month_year('gregorian', 5, 1900)
        print(f"\nFirst 5 dates in Gregorian May 1900:")
        for i, date_info in enumerate(dates_in_month[:5]):
            print(f"  Gregorian: {date_info['gregorian']['day']}/5/1900 -> Hijri: {date_info['hijri']['day']}/{date_info['hijri']['month']}/{date_info['hijri']['year']} ({date_info['weekday']})")
    except ValueError as e:
        print(f"Error: {e}")

    # Example 4: Validate date
    try:
        is_valid = dm.validate_date('gregorian', 29, 2, 1900)  # Feb 29, 1900 (not a leap year)
        print(f"\nIs Gregorian 29/2/1900 valid? {is_valid}")
        
        is_valid = dm.validate_date('gregorian', 28, 2, 1900)  # Feb 28, 1900
        print(f"Is Gregorian 28/2/1900 valid? {is_valid}")
    except ValueError as e:
        print(f"Error: {e}")