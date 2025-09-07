from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class DateComponentsDefault:
    """
    Strict date components with validation constraints.

    Similar to DateComponents but with strict validation rules enforced.
    This class is intended for scenarios where you need guaranteed valid
    date component ranges and type safety.

    Parameters
    ----------
    weekday : str, optional
        Day of the week
    day : int, optional
        Day of the month, must be between 1-31 if provided
    month : int, optional
        Month of the year, must be between 1-12 if provided
    year : int, optional
        Year, must be between 1-3000 if provided
    century : int, optional
        Century, must be between 1-30 if provided
    era : str, optional
        Era designation
    calendar : str, optional
        Calendar system, must be one of ('gregorian', 'hijri', 'Jalali') if provided

    Raises
    ------
    ValueError
        If any component is outside its valid range during initialization

    Notes
    -----
    The validation constraints are enforced automatically during initialization.
    This provides immediate feedback on invalid date components.

    Examples
    --------
    >>> valid_date = DateComponentsDefault(day=15, month=3, year=2023)
    >>> # This will raise ValueError:
    >>> invalid_date = DateComponentsDefault(day=35, month=3, year=2023)
    """
    weekday: Optional[str] = None
    day: Optional[int] = None  # strict from 1 to 31
    month: Optional[int] = None  # strict from 1 to 12 
    year: Optional[int] = None  # strict 1 to 3000
    century: Optional[int] = None  # strict 1 to 30
    era: Optional[str] = None
    calendar: Optional[str] = None  # strict ('gregorian', 'hijri', 'Jalali', None)
    
    def __post_init__(self):
        """
        Post-initialization validation of date components.

        This method checks that the provided components adhere to the
        specified constraints. Raises ValueError if any component is out of range.

        Raises
        ------
        ValueError
            If any component is outside its valid range
        """
        if self.day is not None and not (1 <= self.day <= 31):
            raise ValueError("Day must be between 1 and 31")
        if self.month is not None and not (1 <= self.month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if self.year is not None and not (1 <= self.year <= 3000):
            raise ValueError("Year must be between 1 and 3000")
        if self.century is not None and not (1 <= self.century <= 30):
            raise ValueError("Century must be between 1 and 30")
        if self.calendar is not None and self.calendar not in ('gregorian', 'hijri', 'Jalali'):
            raise ValueError("Calendar must be one of ('gregorian', 'hijri', 'Jalali') or None")

