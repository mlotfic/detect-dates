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
    get_calendar
)

from detect_dates.calendar_variants import (
    get_century_from_year,
    get_century_range,
    format_century_with_era,
)


@dataclass
class ParsedDate:
    """
    Flexible date representation supporting partial dates and multiple calendar systems.

    This class handles real-world date parsing scenarios where information may be
    incomplete, ambiguous, or expressed in different calendar systems. It automatically
    normalizes raw date components during initialization.

    Parameters
    ----------
    raw_weekday : str, optional
        Raw weekday text before normalization (e.g., "Monday", "Mon", "الاثنين")
    raw_day : str, optional  
        Raw day text before parsing (e.g., "15", "fifteenth")
    raw_month : str, optional
        Raw month text before normalization (e.g., "March", "Mar", "3", "رمضان")
    raw_year : str or int, optional
        Raw year before parsing (e.g., "2023", 2023, "-44" for BCE years)
    raw_century : str, optional
        Raw century text (e.g., "21st", "first", "الحادي والعشرين")
    raw_era : str, optional
        Raw era designation (e.g., "BCE", "CE", "AD", "BC", "هـ")
    raw_calendar : str, optional
        Raw calendar system name (e.g., "gregorian", "hijri", "julian")
    text : str, optional
        Original text that was parsed to create this date
    calendar : str, optional
        Calendar system override ('gregorian', 'hijri', 'julian')
    lang : str, optional
        Language of the original text (ISO 639-1 code like 'en', 'ar')
    precision : str, optional
        Precision level indicator ('day', 'month', 'year', 'century')
    confidence : float, optional
        Parsing confidence score between 0.0 and 1.0
    metadata : dict, optional
        Additional parsing information and context

    Attributes
    ----------
    weekday : str or int, optional
        Normalized weekday (0-6 for int, full name for str)
    day : int, optional
        Parsed day of the month (1-31)
    month : int or str, optional
        Normalized month (1-12 for int, full name for str)
    year : int, optional
        Parsed year (positive for CE/AD, negative for BCE/BC)
    century : int or str, optional
        Calculated or parsed century information
    era : str, optional
        Normalized era designation ('CE', 'BCE', 'AH')
    calendar : str, optional
        Determined calendar system

    Raises
    ------
    ValueError
        If confidence is not between 0.0 and 1.0, day is not 1-31, or month is not 1-12

    Examples
    --------
    Create a complete date:

    >>> date = ParsedDate(
    ...     raw_day="15", raw_month="March", raw_year="2023",
    ...     raw_era="CE", confidence=1.0
    ... )
    >>> print(date)
    15 March 2023 CE

    Create a partial date with only month and year:

    >>> partial = ParsedDate(
    ...     raw_month="March", raw_year="2023",
    ...     precision='month', confidence=0.8
    ... )
    >>> print(partial.is_complete())
    False

    Handle BCE dates:

    >>> ancient = ParsedDate(
    ...     raw_day="15", raw_month="March", raw_year="-44",
    ...     raw_era="BCE"
    ... )
    >>> print(ancient.year)
    -44
    """
    
    # Raw extracted components before parsing/normalization
    raw_weekday: Optional[str] = None
    raw_day: Optional[str] = None
    raw_month: Optional[str] = None
    raw_year: Optional[Union[str, int]] = None
    raw_century: Optional[str] = None
    raw_era: Optional[str] = None
    raw_calendar: Optional[str] = None
    
    # Additional metadata
    text: Optional[str] = None
    calendar: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)
    
    def __post_init__(self):
        """
        Post-initialization processing to normalize and validate components.
        
        This method runs automatically after dataclass initialization to:
        - Normalize raw components using helper functions
        - Parse strings to appropriate data types
        - Infer missing information (like calendar from era)
        - Validate ranges and constraints
        
        Raises
        ------
        ValueError
            If validation fails for confidence, day, or month ranges
        """
        # Normalize and parse raw components into structured data
        self.weekday: Optional[Union[str, int]] = (
            normalize_weekday(self.raw_weekday) if self.raw_weekday else None
        )
        
        # Parse day as integer if it's a numeric string
        self.day: Optional[int] = (
            int(self.raw_day) if self.raw_day and self.raw_day.isdigit() else None
        )
        
        # Normalize month names/abbreviations to standard format
        self.month: Optional[Union[int, str]] = (
            normalize_month(self.raw_month) if self.raw_month else None
        )
        
        # Parse year, handling negative years for BCE dates
        self.year: Optional[int] = None
        if self.raw_year and isinstance(self.raw_year, (str, int)):
            year_str = str(self.raw_year).lstrip('-')
            if year_str.isdigit():
                self.year = int(self.raw_year)
        
        # Calculate century from year if available
        self.century, _ = (
            get_century_from_year(self.year) if self.year is not None else (None, None)
        )
        
        # Normalize era designation (BCE/CE/AD/BC etc.)
        self.era: Optional[str] = normalize_era(self.raw_era) if self.raw_era else None
        
        # Determine calendar system from raw input or infer from era
        self.calendar: Optional[str] = normalize_calendar_name(self.raw_calendar)
        if self.calendar:
            self.calendar = normalize_calendar_name(self.calendar)
        elif self.era:
            # Infer calendar from era (e.g., AH -> hijri, BCE/CE -> gregorian)
            self.calendar = get_calendar(self.era)
            
        # Validate confidence score range
        if self.confidence is not None:
            if not (0.0 <= self.confidence <= 1.0):
                raise ValueError("Confidence must be between 0.0 and 1.0")
        
        # Validate day range (basic check, doesn't account for month-specific limits)
        if self.day is not None:
            if not (1 <= self.day <= 31):
                raise ValueError("Day must be between 1 and 31")
                
        # Validate month range for numeric months
        if isinstance(self.month, int):
            if not (1 <= self.month <= 12):
                raise ValueError("Month must be between 1 and 12")
    
    def is_complete(self) -> bool:
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
        >>> complete = ParsedDate(raw_day="15", raw_month="3", raw_year="2023", raw_era="CE")
        >>> complete.is_complete()
        True

        >>> partial = ParsedDate(raw_month="March", raw_year="2023")
        >>> partial.is_complete()
        False
        """
        return (
            self.day is not None and 
            self.month is not None and 
            self.year is not None and 
            self.era is not None
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the ParsedDate instance to a dictionary representation.

        This is useful for serialization, JSON export, or interfacing with
        systems that expect dictionary-based date representations.

        Returns
        -------
        dict
            Dictionary containing all date components and metadata

        Examples
        --------
        >>> date = ParsedDate(raw_day="15", raw_month="March", raw_year="2023")
        >>> result = date.to_dict()
        >>> result['day']
        15
        >>> result['month']
        'March'
        """
        return {
            "weekday": self.weekday,
            "day": self.day,
            "month": self.month,
            "year": self.year,
            "century": self.century,
            "era": self.era,
            "calendar": self.calendar,
            "text": self.text,
            "lang": self.lang,
            "precision": self.precision,
            "confidence": self.confidence,
            "metadata": self.metadata,
        }
        
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
        >>> date = ParsedDate(raw_weekday="Monday", raw_day="15", raw_month="March", 
        ...                   raw_year="2023", raw_era="CE")
        >>> str(date)
        'Monday, 15 March 2023 CE'

        >>> partial = ParsedDate(raw_month="March", raw_year="2023")
        >>> str(partial)
        'March 2023'

        >>> empty = ParsedDate()
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