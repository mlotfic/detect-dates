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
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                    print(f"Added to sys.path: {src_second_path}")
                break
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

import os
import pandas as pd

from detect_dates.keywords.constants import (
    SUPPORTED_CALENDARS_COLUMNS,
)

from month import normalize_month
from calendar import normalize_calendar_name, get_calendar
from calendar_from_era import normalize_calendar_from_era
from typing import Optional, Union, Tuple, List, Dict, Any


def normalize_input_date(
        self, 
        era: str, 
        day: Optional[int], 
        month: Optional[Union[str, int]], 
        year: Optional[Union[str, int]]
        ) -> Tuple[Optional[str], Optional[int], Optional[int], Optional[int]]:
        """
        Validate and normalize input date components for correctness.

        Parameters
        ----------
        era : str
            Era or calendar system identifier
        day : int
            Day of the month (1-31)
        month : int or str
            Month of the year (1-12 or month name)
        year : int
            Year in the specified calendar system

        Returns
        -------
        tuple
            Normalized (calendar, day, month, year) tuple

        Raises
        ------
        RuntimeError
            If calendar mapping data is not loaded
        ValueError
            If calendar system is not supported or date components are invalid
        """        
        
        # Normalize and validate calendar name
        calendar = self.normalize_calendar_from_era(era)  
        # print(calendar)
        if calendar not in SUPPORTED_CALENDARS_COLUMNS:
            raise ValueError(f"Unsupported calendar system: '{calendar}'. Supported systems: {list(SUPPORTED_CALENDARS_COLUMNS.keys())}")
        
        # Validate day - set to default if invalid
        if not isinstance(day, int) or not (1 <= day <= 31):
            day = None
            print(f"Invalid day value: {day}. Must be an integer between 1 and 31.")
            print(f"Day set to default value: None.")

        # Handle string month names by converting to numbers
        if isinstance(month, str):
            month = normalize_month(month, output_format="number")
            if month is None:
                print(f"Invalid month value after normalization: {month}. Must be between 1 and 12. or proper month name.")
        if isinstance(month, str) and month.isdigit():
            month = int(month)
        
        # If month is still a string (non-numeric), it's invalid
        if not isinstance(month, int) or not (1 <= month <= 12):
            print(f"Invalid month value: {month}. Must be an integer between 1 and 12.")
            month = None
            print(f"Month set to default value: None.")
        
        if isinstance(year, str) and year.isdigit():
            year = int(year)
        if not isinstance(year, int):
            raise ValueError(f"Year must be an integer value. Got: {year}")
        
        # Validate year range based on calendar system
        year_ranges = {
            'gregorian': (1900, 2077),
            'hijri': (1318, 1500),
            'julian': (1278, 1456)
        }
        min_year, max_year = year_ranges.get(calendar, (None, None))
        if (
            not isinstance(year, int)
            or min_year is None
            or max_year is None
            or year < min_year
            or year > max_year
        ):
            raise ValueError(
                f"Unusual year value: {year}. Must be an integer between {min_year} and {max_year} for {calendar} calendar."
            )
        
        return calendar, day, month, year