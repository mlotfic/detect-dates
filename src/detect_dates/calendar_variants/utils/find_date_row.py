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

# Import necessary modules
from detect_dates.keywords.constants import SUPPORTED_CALENDARS_COLUMNS
from detect_dates.normalizers import normalize_input_date
from typing import Optional, Dict, List, Union, Any, Tuple


def find_date_row(
        df: pd.DataFrame,
        era: Optional[str], 
        day: Optional[int], 
        month: Optional[Union[str, int]], 
        year: Optional[Union[str, int]]
        ) -> Optional[pd.DataFrame]:
        """
        Get the weekday name for a specific date in the given calendar system.

        This method looks up the weekday for a specific date using the pre-calculated
        mapping data. The lookup is fast and accurate, based on astronomical calculations.

        Parameters
        ----------
        era : str, default "AD"
            Calendar system ('gregorian', 'hijri', 'julian', or aliases) or era ('AD', 'AH', etc.)
        day : int, default 1
            Day of the month (1-31 depending on calendar and month)
        month : int or str, default 1
            Month of the year (1-12) or month name
        year : int, default 2009
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

        >>> mapper = DateMapping()
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
        # Validate input date components
        calendar, day, month, year = normalize_input_date(era, day, month, year)
        
        # Ensure at least year and calendar are provided        
        if calendar:
            # Get column names for the specified calendar system
            day_col, month_col, year_col = SUPPORTED_CALENDARS_COLUMNS[calendar]
        else:
            raise ValueError("Calendar system could not be determined from input.")

        # Create filter mask to find matching date
        if day is not None and month is not None and year is not None:
            mask = (
                (df[day_col] == day) &
                (df[month_col] == month if month else True) &
                (df[year_col] == year)
            )
        elif month is not None and year is not None:
            mask = (
                (df[month_col] == month if month else True) &
                (df[year_col] == year)
            )
        elif year is not None:
            mask = (df[year_col] == year)
        
        else:
            raise ValueError("At least year and calendar system must be specified.")

        # Find matching rows
        return df[mask]