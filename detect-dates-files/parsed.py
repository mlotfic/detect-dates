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
    normalize_numeric_word, 
    get_calendar
)

from detect_dates.calendar_variants import (
    get_century_from_year,
    get_century_range,
    format_century_with_era,
)

@dataclass
class DateComponents:
    """
    Basic date components structure.

    This class encapsulates the fundamental components of a date,
    including day, month, year, century, era, and calendar system.
    It serves as a simple container for these attributes.

    Parameters
    ----------
    day : int, optional
        Day of the month (1-31)
    month : int or str, optional
        Month of the year (1-12 or month name)
    year : int, optional
        Year (positive for CE/AD, negative for BCE/BC)
    century : int or str, optional
        Century (e.g., 21 for 21st century)
    era : str, optional
        Era designation ('CE', 'BCE', 'AH')
    calendar : str, optional
        Calendar system ('gregorian', 'hijri', 'julian')

    Attributes
    ----------
    day : int or None
        Day of the month
    month : int or str or None
        Month of the year
    year : int or None
        Year
    century : int or str or None
        Century
    era : str or None
        Era designation
    calendar : str or None
        Calendar system

    Examples
    --------
    Create a DateComponents instance with full details:

    >>> components = DateComponents(day=15, month=3, year=2023, century=21, era="CE", calendar="gregorian")
    
    Create a DateComponents instance with minimal details:

    >>> simple_components = DateComponents(year=2023)
    
    Access individual attributes:

    >>> print(components.day)
    15
    >>> print(simple_components.year)
    2023
    """
    weekday: Optional[str] = None
    day: Optional[int] = None
    month: Optional[Union[int, str]] = None
    year: Optional[int] = None
    century: Optional[Union[int, str]] = None
    era: Optional[str] = None
    calendar: Optional[str] = None
    
@dataclass
class DateComponentsDefault:
    """
    Basic date components structure.

    This class encapsulates the fundamental components of a date,
    including day, month, year, century, era, and calendar system.
    It serves as a simple container for these attributes.

    Parameters
    ----------
    day : int, optional
        Day of the month (1-31)
    month : int or str, optional
        Month of the year (1-12 or month name)
    year : int, optional
        Year (positive for CE/AD, negative for BCE/BC)
    century : int or str, optional
        Century (e.g., 21 for 21st century)
    era : str, optional
        Era designation ('CE', 'BCE', 'AH')
    calendar : str, optional
        Calendar system ('gregorian', 'hijri', 'julian')

    Attributes
    ----------
    day : int or None
        Day of the month
    month : int or str or None
        Month of the year
    year : int or None
        Year
    century : int or str or None
        Century
    era : str or None
        Era designation
    calendar : str or None
        Calendar system

    Examples
    --------
    Create a DateComponents instance with full details:

    >>> components = DateComponents(day=15, month=3, year=2023, century=21, era="CE", calendar="gregorian")
    
    Create a DateComponents instance with minimal details:

    >>> simple_components = DateComponents(year=2023)
    
    Access individual attributes:

    >>> print(components.day)
    15
    >>> print(simple_components.year)
    2023
    """
    weekday: Optional[str] = None
    day: Optional[int] = None strict from 1 to 31
    month: Optional[int] = None strict from 1 to 12 
    year: Optional[int] = None strict 1 to 3000
    century: Optional[int] = strict 1 to 30
    era: Optional[str] = None
    calendar: Optional[str] = strict ('gregorian', 'hijri', 'julian', None)

@dataclass
class DateMeta:
    """
    Metadata about the date parsing process.

    This class captures additional context and information about how
    a date was parsed, including the original text, language, calendar
    system, precision level, confidence score, and any extra metadata.

    Parameters
    ----------
    text : str, optional
        Original text that was parsed to create this date
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
    text : str or None
        Original text that was parsed
    calendar : str or None
        Calendar system used for parsing
    lang : str or None
        Language of the original text
    precision : str or None
        Precision level of the parsed date
    confidence : float or None
        Confidence score of the parsing (0.0 to 1.0)
    metadata : dict
        Additional metadata about the parsing process

    Raises
    ------
    ValueError
        If confidence is not between 0.0 and 1.0

    Examples
    --------
    Create a DateMeta instance with full details:

    >>> meta = DateMeta(
    ...     text="15 March 2023",
    ...     calendar="gregorian",
    ...     lang="en",
    ...     precision="day",
    ...     confidence=0.95,
    ...     metadata={"source": "user_input"}
    ... )
    
    Create a DateMeta instance with minimal details:

    >>> simple_meta = DateMeta(
    ...     text="March 2023",
    ...     precision="month"
    ... )
    
    Attempting to set an invalid confidence score raises an error:

    >>> invalid_meta = DateMeta(confidence=1.5)
    Traceback (most recent call last):
        ...
    ValueError: Confidence must be between 0.0 and 1.0
    """
    
    text: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    created_at: Optional[str] = None
    is_calendar_date: bool = False
    is_complete_date: bool = False
    valid_date: bool = False
    role_in_text: Optional[str] = None
    related_to: Optional[str] = None
    

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
        self.calendar: Optional[str] = None
        if self.raw_calendar is not None:
            self.calendar = normalize_calendar_name(self.raw_calendar)
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
            
        
        # 
        self.month_num: Optional[int] = None
        if self.month is not None:
            normalized_month = normalize_month(self.month, output_format="num")
            if normalized_month is not None:
                self.month_num = int(normalized_month)
            else:
                self.month_num = None
        
        self.is_calendar_date: bool = self._is_calendar()
        self.is_complete_date: bool = self._is_complete()
        self.valid_date: bool = self.is_complete_date and self.is_calendar_date
        self.lang = self._detect_language()
        self.precision = self.precision or (
            'day' if self.is_complete_date else
            'month' if self.month and self.year else
            'year' if self.year else
            'century' if self.century else
            'partial'
        )
        
    def analysis_date(self):
        """
        Provide a human-readable analysis of the date components.

        This method generates a summary string that describes the parsed
        date components, their values, and any inferred information. It's
        useful for debugging and understanding how the date was interpreted.

        Returns
        -------
        str
            Summary of the date components and their interpretations

        Examples
        --------
        >>> date = ParsedDate(raw_weekday="Sunday", raw_day="15", raw_month="March", raw_year="2023", raw_era="CE")
        >>> print(date.analysis_date())
        Input  : [Weekday: None, Day: 15, Month: March), Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Standard Output : [Weekday: None, Day: 15, Month: 3 (March), Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Numeric Output : [Weekday: None, Day: 15, Month: 3, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Date Time : python datetime 
        Date Info : Is Valid Date: , Is Complete: True, Is Calendar: True, Precision: day, Language: en, Confidence: 1.0
        """
        
        
    def _detect_language(self) -> Optional[str]:
        """
        Detect the language of the original text if not explicitly provided.

        This is a placeholder for actual language detection logic. In a real
        implementation, this could use a library like `langdetect` or similar.

        Returns
        -------
        str or None
            Detected language code (ISO 639-1) or None if undetectable

        Examples
        --------
        >>> date = ParsedDate(text="15 March 2023")
        >>> date._detect_language()
        'en'
        >>> date_ar = ParsedDate(text="15 مارس 2023")
        >>> date_ar._detect_language()
        'ar'
        """
        if self.lang:
            return self.lang
        
        if self.text:
            # Simple heuristic: check for Arabic characters
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
    
    def _is_calendar(self) -> bool:
        """
        Check if the date has calendar-level information (year and era).

        This method determines if the date has sufficient information to
        represent a specific year in a given calendar system.

        Returns
        -------
        bool
            True if both year and era components are present

        Examples
        --------
        >>> date = ParsedDate(raw_year="2023", raw_era="CE")
        >>> date.is_calendar()
        True

        >>> incomplete = ParsedDate(raw_year="2023")
        >>> incomplete.is_calendar()
        False
        """
        return self.year is not None and self.era is not None and self.calendar is not None
    
    def to_dict(self, format = "standard") -> Dict[str, Any]:
        
        """
        format = "standard", "default", "raw", "meta", "standard+meta", "default+meta", "raw+meta"
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
        base_dict = {
            'raw_weekday': self.raw_weekday,
            'raw_day': self.raw_day,
            'raw_month': self.raw_month,
            'raw_year': self.raw_year,
            'raw_century': self.raw_century,
            'raw_era': self.raw_era,
            'raw_calendar': self.raw_calendar,
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
                'raw_weekday': self.raw_weekday,
                'raw_day': self.raw_day,
                'raw_month': self.raw_month,
                'raw_year': self.raw_year,
                'raw_century': self.raw_century,
                'raw_era': self.raw_era,
                'raw_calendar': self.raw_calendar
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