# ...existing code...
import os
import pandas as pd
from typing import Optional, Union

if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other data in the package structure
    from path_helper import add_data_to_sys_path
    # Ensure the data directory is in sys.path for imports
    add_data_to_sys_path()

class DateMapping:

    def __post_init__(self):
        self.df = self.load_mapping_date(self)



    def load_mapping_date(self) -> pd.DataFrame:
        # Corrected path to the CSV file
        file = os.path.join(
            os.path.dirname(__file__),
            "..", "mapping_date", "Hijri-Gregorian-Solar_Hijri-V3.csv"
        )
        file = os.path.abspath(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f"Calendar data file not found: {file}")

        df = pd.read_csv(file, encoding='utf-8')
        return df


    def get_weekday_by_date(era: str, day: int, month: int, year: int) -> Optional[str]:
        """
        Get weekday for a specific date in the given era.

        Parameters:
        -----------
        df : pandas.DataFrame
            DataFrame with calendar columns
        era : str
            'gregorian', 'hijri', or 'solar_hijri'
        day : int
            Day of the date
        month : int
            Month of the date
        year : int
            Year of the date

        Returns:
        --------
        str or None
            Weekday name (e.g., 'Monday') or None if not found
        """

        df = load_mapping_date()

        # Define column mappings
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            return None

        day_col, month_col, year_col = era_columns[era]

        # Find matching row
        mask = (df[day_col] == day) & (df[month_col] == month) & (df[year_col] == year)
        matching_rows = df[mask]

        if matching_rows.empty:
            return None

        return matching_rows.iloc[0]['Week Day']


    def get_date_alternative_calendar(self, era, day, month, year):
        """
        Get equivalent dates in other calendar systems for a specific date.

        Parameters:
        -----------
        df : pandas.DataFrame
            DataFrame with calendar columns
        era : str
            'gregorian', 'hijri', or 'solar_hijri'
        day : int
            Day of the date
        month : int
            Month of the date
        year : int
            Year of the date

        Returns:
        --------
        dict or None
            Dictionary with dates in all calendar systems, or None if not found
        """

        # Define column mappings
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            return None

        day_col, month_col, year_col = era_columns[era]

        # Find matching row
        mask = (df[day_col] == day) & (df[month_col] == month) & (df[year_col] == year)
        matching_rows = df[mask]

        if matching_rows.empty:
            return None

        row = matching_rows.iloc[0]

        result = {
            'gregorian': {
                'day': row['Gregorian Day'],
                'month': row['Gregorian Month'],
                'year': row['Gregorian Year']
            },
            'hijri': {
                'day': row['Hijri Day'],
                'month': row['Hijri Month'],
                'year': row['Hijri Year']
            },
            'solar_hijri': {
                'day': row['Solar Hijri Day'],
                'month': row['Solar Hijri Month'],
                'year': row['Solar Hijri Year']
            },
            'weekday': row['Week Day']
        }

        return result


    def get_dates_by_month_year(self, era, month, year):
        """
        Get all dates in the specified month and year for the given era.

        Parameters:
        -----------
        df : pandas.DataFrame
            DataFrame with calendar columns
        era : str
            'gregorian', 'hijri', or 'solar_hijri'
        month : int
            Month to search for
        year : int
            Year to search for

        Returns:
        --------
        list of dict or None
            List of dictionaries with date information for all matching dates
        """

        # Define column mappings
        era_columns = {
            'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
            'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
            'solar_hijri': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
        }

        if era not in era_columns:
            return None

        day_col, month_col, year_col = era_columns[era]

        # Find matching rows
        mask = (df[month_col] == month) & (df[year_col] == year)
        matching_rows = df[mask]

        if matching_rows.empty:
            return []

        results = []
        for _, row in matching_rows.iterrows():
            result = {
                'gregorian': {
                    'day': row['Gregorian Day'],
                    'month': row['Gregorian Month'],
                    'year': row['Gregorian Year']
                },
                'hijri': {
                    'day': row['Hijri Day'],
                    'month': row['Hijri Month'],
                    'year': row['Hijri Year']
                },
                'solar_hijri': {
                    'day': row['Solar Hijri Day'],
                    'month': row['Solar Hijri Month'],
                    'year': row['Solar Hijri Year']
                },
                'weekday': row['Week Day']
            }
            results.append(result)

        return results

# Example usage
if __name__ == "__main__":
    # Create sample data
    data = load_mapping_date()

    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)
    print()

    # Example 1: Get weekday for specific date
    weekday = get_weekday_by_date(df, 'gregorian', 2, 5, 1900)
    print(f"Weekday for Gregorian 2/5/1900: {weekday}")

    # Example 2: Get alternative calendar dates
    alternatives = get_date_alternative_calendar(df, 'hijri', 3, 1, 1318)
    print(f"Alternative calendars for Hijri 3/1/1318:")
    if alternatives:
        print(f"  Gregorian: {alternatives['gregorian']['day']}/{alternatives['gregorian']['month']}/{alternatives['gregorian']['year']}")
        print(f"  Solar Hijri: {alternatives['solar_hijri']['day']}/{alternatives['solar_hijri']['month']}/{alternatives['solar_hijri']['year']}")
        print(f"  Weekday: {alternatives['weekday']}")

    # Example 3: Get all dates in a specific month/year
    dates_in_month = get_dates_by_month_year(df, 'gregorian', 5, 1900)
    print(f"\nAll dates in Gregorian May 1900:")
    for date_info in dates_in_month:
        print(f"  Gregorian: {date_info['gregorian']['day']}/5/1900 -> Hijri: {date_info['hijri']['day']}/{date_info['hijri']['month']}/{date_info['hijri']['year']} ({date_info['weekday']})")
