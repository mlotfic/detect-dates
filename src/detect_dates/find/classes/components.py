from typing import Optional, Union
from dataclasses import dataclass
@dataclass
class DateComponents:
    """
    Basic date components container for structured date representation.

    A lightweight container class that holds the fundamental components of a date,
    including day, month, year, century, era, and calendar system. Useful for
    passing date information between functions without normalization overhead.

    Parameters
    ----------
    weekday : str, optional
        Day of the week (e.g., 'Monday', 'Tuesday')
    day : int or str, optional
        Day of the month (1-31), accepts both numeric and string formats
    month : int or str, optional
        Month of the year (1-12 or month name like 'January')
    year : int or str, optional
        Year (positive for CE/AD, negative for BCE/BC)
    century : int or str, optional
        Century (e.g., 21 for 21st century)
    era : str, optional
        Era designation ('CE', 'BCE', 'AH')
    calendar : str, optional
        Calendar system ('gregorian', 'hijri', 'Jalali')

    Examples
    --------
    >>> components = DateComponents(day=15, month=3, year=2023, century=21, era="CE", calendar="gregorian")
    >>> simple_components = DateComponents(year=2023)
    >>> print(components.day)
    15
    """
    weekday: Optional[str] = None
    day: Optional[Union[int, str]] = None
    month: Optional[Union[int, str]] = None
    year: Optional[Union[int, str]] = None
    century: Optional[Union[int, str]] = None
    era: Optional[str] = None
    calendar: Optional[str] = None