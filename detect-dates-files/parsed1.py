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
    Basic date components container for structured date representation.

    A lightweight container class that holds the fundamental components of a date,
    including day, month, year, century, era, and calendar system. Useful for
    passing date information between functions without normalization overhead.

    Parameters
    ----------
    weekday : str, optional
        Day of the week (e.g., 'Monday', 'Tuesday')
    day : int, optional
        Day of the month (1-31)
    month : int or str, optional
        Month of the year (1-12 or month name like 'January')
    year : int, optional
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
    day:  Optional[Union[int, str]] = None
    month: Optional[Union[int, str]] = None
    year:  Optional[Union[int, str]] = None
    century: Optional[Union[int, str]] = None
    era: Optional[str] = None
    calendar: Optional[str] = None
    

@dataclass
class DateComponentsDefault:
    """
    Strict date components with validation constraints.

    Similar to DateComponents but with strict validation rules enforced.
    This class is intended for scenarios where you need guaranteed valid
    date component ranges.

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

    Notes
    -----
    The validation constraints are documented but not automatically enforced.
    This is a design choice to maintain flexibility while indicating intended usage.
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
            If any component is outside its valid range.
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


@dataclass
class DateMeta:
    """
    Metadata container for date parsing context and quality information.

    Stores additional information about how a date was parsed, including
    the original text, language detection, precision level, confidence scoring,
    and validation flags. Used for debugging, quality assessment, and
    post-processing decisions.

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
    created_at : str, optional
        Timestamp when the date was parsed
    is_calendar_date : bool, default False
        Whether the date has calendar-level information (year + era)
    is_complete_date : bool, default False
        Whether the date has complete day-level precision
    valid_date : bool, default False
        Whether the date passed all validation checks
    role_in_text : str, optional
        Role this date plays in the source text (e.g., 'birth_date', 'event_date')
    related_to : str, optional
        What entity or concept this date relates to

    Examples
    --------
    >>> meta = DateMeta(
    ...     text="15 March 2023",
    ...     lang="en",
    ...     precision="day",
    ...     confidence=0.95,
    ...     is_complete_date=True
    ... )
    """
    text: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    is_calendar_date: bool = False
    is_complete_date: bool = False
    valid_date: bool = False
    role_in_text: Optional[str] = None
    related_to: Optional[str] = None
    
@dataclass
class ParsedDate:
    raw: DateComponents
    standard: DateComponents
    numeric: DateComponents
    meta: DateMeta
    def __post_init__(
        self, date: Optional[dict] = None, weekday: Optional[str] = None,
        day: Optional[int] = None, month: Optional[Union[int, str]] = None,
        year: Optional[int] = None, century: Optional[Union[int, str]] = None,
        era: Optional[str] = None, calendar: Optional[str] = None, text: Optional[str] = None,
        lang: Optional[str] = None, precision: Optional[str] = None,
        confidence: Optional[float] = None, created_at: Optional[str] = None, 
        created_by: Optional[str] = None,
        role_in_text: Optional[str] = None, related_to: Optional[str] = None,
        is_calendar_date: bool = False, is_complete_date: bool = False,
        valid_date: bool = False
        ):
        """
        Post-initialization to flatten attributes for easier access.
        This method runs automatically after dataclass initialization to
        copy attributes from raw and meta into the main ParsedDate instance.
        """
        
        self.raw_date = DateComponents(
            weekday=weekday if weekday else (date.get('weekday', None) if date else None),
                day=day if day else (date.get('day', None) if date else None),
                month=month if month else (date.get('month', None) if date else None),
                year=year if year else (date.get('year', None) if date else None),
                century=century if century else (date.get('century', None) if date else None),
                era=era if era else (date.get('era', None) if date else None),
                calendar=calendar if calendar else (date.get('calendar', None) if date else None)
        )
        
        self.meta = DateMeta(
            text=text if text else (date.get('text', None) if date else None),
            lang=lang if lang else (date.get('lang', None) if date else None),
                precision=precision if precision else (date.get('precision', None) if date else None),
                confidence=confidence if confidence else (date.get('confidence', None) if date else None),
                created_at=created_at if created_at else (date.get('created_at', None) if date else None),
                created_by=created_by if created_by else (date.get('created_by', None) if date else None),
                is_calendar_date=is_calendar_date if is_calendar_date else (date.get('is_calendar_date', False) if date else False),
                is_complete_date=is_complete_date if is_complete_date else (date.get('is_complete_date', False) if date else False),
                valid_date=valid_date if valid_date else (date.get('valid_date', False) if date else False),
                role_in_text=role_in_text if role_in_text else (date.get('role_in_text', None) if date else None),
                related_to=related_to if related_to else (date.get('related_to', None) if date else None),
            )
        century = self.raw_date.century if self.raw_date.century else int(get_century_from_year(self.year) if self.year is not None else (None, None)[0]) if int(self.raw_date.year) else None
        
        self.standard = DateComponents(
            weekday= str(normalize_weekday(self.raw_date.weekday)) if self.raw_date.weekday else None,
            day= int(self.raw_date.day) if self.raw_date.day and str(self.raw_date.day).isdigit() else None,
            month= normalize_month(self.raw_date.month) if self.raw_date.month else None,
            year= int(self.raw_date.year) if self.raw_date.year and str(self.raw_date.year).lstrip('-').isdigit() else None,
            century=  century if century else None,
            era= normalize_era(self.raw_date.era) if self.raw_date.era else None,
            calendar= normalize_calendar_name(self.raw_date.calendar) if self.raw_date.calendar else ( get_calendar(self.raw_date.era) if self.raw_date.era else None)
        )
        
        self.numeric = DateComponents(
            weekday= self.standard.weekday if isinstance(self.standard.weekday, str) else None,
            day= self.standard.day,
            month= normalize_month(self.standard.month, output_format="num") if self.standard.month else None,
            year= self.standard.year,
            century= self.standard.century,
            era= self.standard.era,
            calendar= self.standard.calendar
        )
            
        # Validate confidence score range
        if self.meta.confidence is not None:
            if not (0.0 <= self.meta.confidence <= 1.0):
                raise ValueError("Confidence must be between 0.0 and 1.0")
        
        # Calculate validation flags and metadata
        if self.meta.is_calendar_date is False:
            self.meta.is_calendar_date = self._is_calendar()
        if self.meta.is_complete_date is False:
            self.meta.is_complete_date = self._is_complete()
        if self.meta.valid_date is False:
            self.meta.valid_date = self.meta.is_calendar_date and self.meta.is_complete_date
            
        if self.meta.lang is None:
            self.meta.lang = self._detect_language()
    
        
        # Set precision based on available components if not explicitly provided
        if self.meta.precision is None:
            self.meta.precision = (
            'day' if self.meta.is_complete_date else
            'month' if self.raw_date.month and self.raw_date.year else
            'year' if self.raw_date.year else
            'century' if self.raw_date.century else
            'partial'
            )
        
    @property
    def raw_date(self) -> DateComponents:
        return self.raw_date
    @property
    def text(self) -> Optional[str]:
        return self.meta.text
    @property
    def calendar(self) -> Optional[str]:
        return self.standard.calendar
    @property
    def lang(self) -> Optional[str]:
        return self.meta.lang
    @property
    def precision(self) -> Optional[str]:
        return self.meta.precision
    @property
    def confidence(self) -> Optional[float]:
        return self.meta.confidence
    @property
    def metadata(self) -> Dict[str, Any]:
        return {
            'created_at': self.meta.created_at,
            'created_by': self.meta.created_by,
            'is_calendar_date': self.meta.is_calendar_date,
            'is_complete_date': self.meta.is_complete_date,
            'valid_date': self.meta.valid_date,
            'role_in_text': self.meta.role_in_text,
            'related_to': self.meta.related_to
        }
        
    @property
    def weekday(self) -> Optional[Union[int, str]]:
        return self.standard.weekday
    @property
    def day(self) -> Optional[int]:
        return self.standard.day
    @property
    def month(self) -> Optional[Union[int, str]]:
        return self.standard.month
    @property
    def month_num(self) -> Optional[int]:
        return self.numeric.month
    @property
    def year(self) -> Optional[int]:
        return self.standard.year
    @property
    def century(self) -> Optional[Union[int, str]]:
        return self.standard.century
    @property
    def era(self) -> Optional[str]:
        return self.standard.era
    @property
    def calendar(self) -> Optional[str]:
        return self.standard.calendar
    @property
    def valid_date(self) -> bool:
        return self.meta.valid_date
    @property
    def is_complete_date(self) -> bool:
        return self.meta.is_complete_date
    @property
    def is_calendar_date(self) -> bool:
        return self.meta.is_calendar_date   
    
    
    def analysis_date(self):
        """
        Provide a human-readable analysis of the date components.

        This method generates a comprehensive summary string that describes the parsed
        date components, their values, and any inferred information. Useful for
        debugging and understanding how the date was interpreted.

        Returns
        -------
        str
            Multi-line summary of the date components and their interpretations

        Examples
        --------
        >>> date = ParsedDate(raw_weekday="Sunday", raw_day="15", raw_month="March", 
        ...                   raw_year="2023", raw_era="CE")
        >>> print(date.analysis_date())
        Input  : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: None, Era: CE, Calendar: gregorian]
        Standard Output : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Numeric Output : [Weekday: Sunday, Day: 15, Month: 3, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Date Info : Is Valid Date: True, Is Complete: True, Is Calendar: True, Precision: day, Language: en
        """
        # Format input components
        input_components = [
            f"Weekday: {self.raw_date.weekday}",
            f"Day: {self.raw_date.day}",
            f"Month: {self.raw_date.month}",
            f"Year: {self.raw_date.year}",
            f"Century: {self.raw_date.century}",
            f"Era: {self.raw_date.era}",
            f"Calendar: {self.raw_date.calendar}"
        ]
        
        # Format standard output components
        standard_components = [
            f"Weekday: {self.weekday}",
            f"Day: {self.day}",
            f"Month: {self.month}",
            f"Year: {self.year}",
            f"Century: {self.century}",
            f"Era: {self.era}",
            f"Calendar: {self.calendar}"
        ]
        
        # Format numeric output components
        numeric_components = [
            f"Weekday: {self.weekday}",
            f"Day: {self.day}",
            f"Month: {self.month_num}",
            f"Year: {self.year}",
            f"Century: {self.century}",
            f"Era: {self.era}",
            f"Calendar: {self.calendar}"
        ]
        
        # Format date info
        date_info = [
            f"Is Valid Date: {self.valid_date}",
            f"Is Complete: {self.is_complete_date}",
            f"Is Calendar: {self.is_calendar_date}",
            f"Precision: {self.precision}",
            f"Language: {self.lang}",
            f"Confidence: {self.confidence}"
        ]
        
        return (
            f"Input  : [{', '.join(input_components)}]\n"
            f"Standard Output : [{', '.join(standard_components)}]\n"
            f"Numeric Output : [{', '.join(numeric_components)}]\n"
            f"Date Info : {', '.join(date_info)}"
        )
        
    def _detect_language(self) -> Optional[str]:
        """
        Detect the language of the original text if not explicitly provided.

        Uses simple heuristics to detect language based on character sets.
        Currently supports basic English/Arabic detection.

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
        # Return explicitly set language
        if self.lang:
            return self.lang
        
        if self.text:
            # Simple heuristic: check for Arabic characters (U+0600 to U+06FF range)
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
        >>> complete._is_complete()
        True
        >>> partial = ParsedDate(raw_month="March", raw_year="2023")
        >>> partial._is_complete()
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
            True if year, era, and calendar components are all present

        Examples
        --------
        >>> date = ParsedDate(raw_year="2023", raw_era="CE", raw_calendar="gregorian")
        >>> date._is_calendar()
        True
        >>> incomplete = ParsedDate(raw_year="2023")
        >>> incomplete._is_calendar()
        False
        """
        return (
            self.year is not None and 
            self.era is not None and 
            self.calendar is not None
        )
    
    def to_dict(self, format="standard") -> Dict[str, Any]:
        """
        Convert the ParsedDate instance to a dictionary representation.

        This method provides different dictionary formats for various use cases
        like serialization, JSON export, or interfacing with other systems.

        Parameters
        ----------
        format : str, default "standard"
            Output format type. Options are:
            - "standard": normalized components with metadata
            - "numeric": numeric representations where possible
            - "raw": original raw input components
            - "all": complete information including raw and processed
            - "meta": metadata only

        Returns
        -------
        dict
            Dictionary containing date components based on specified format

        Examples
        --------
        >>> date = ParsedDate(raw_day="15", raw_month="March", raw_year="2023")
        >>> standard = date.to_dict("standard")
        >>> standard['day']
        15
        >>> numeric = date.to_dict("numeric")
        >>> numeric['month']
        3
        """
        # Build complete dictionary with all available information
        base_dict = {
            'raw_weekday': self.raw_date.weekday,
            'raw_day': self.raw_date.day,
            'raw_month': self.raw_date.month,
            'raw_year': self.raw_date.year,
            'raw_century': self.raw_date.century,
            'raw_era': self.raw_date.era,
            'raw_calendar': self.raw_date.calendar,
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
        
        # Return appropriate subset based on format
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
                'raw_weekday': self.raw_date.weekday,
                'raw_day': self.raw_date.day,
                'raw_month': self.raw_date.month,
                'raw_year': self.raw_date.year,
                'raw_century': self.raw_date.century,
                'raw_era': self.raw_date.era,
                'raw_calendar': self.raw_date.calendar
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
        else:
            # Default to standard format for unknown format strings
            return self.to_dict("standard")
        
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