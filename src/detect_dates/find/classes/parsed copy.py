"""
Date Components Module for Structured Date Representation and Processing

This module provides dataclass-based structures for handling date components across
different calendar systems and precision levels. It supports raw input processing,
normalization, and validation for historical and contemporary dates.

Usage
-----
Basic date component creation:

    from date_components import DateComponents, ParsedDate

    # Create simple date components
    components = DateComponents(day=15, month=3, year=2023, era="CE", calendar="gregorian")
    
    # Create a fully parsed date with automatic normalization
    parsed = ParsedDate(
        raw=DateComponents(day="15", month="March", year="2023", era="CE"),
        standard=DateComponents(),  # Will be auto-populated
        numeric=DateComponents(),   # Will be auto-populated
        meta=DateMeta(text="15 March 2023", lang="en", confidence=0.9)
    )

Quick examples:

    # Historical date with century
    historical = DateComponents(century=15, era="CE", calendar="gregorian")
    
    # Arabic calendar date
    hijri = DateComponents(day=10, month=1, year=1445, era="AH", calendar="hijri")
    
    # Validated date components (strict ranges)
    strict = DateComponentsDefault(day=15, month=3, year=2023, era="CE")
    
    # Date with metadata for tracking
    meta = DateMeta(
        text="15th of March, 2023",
        lang="en",
        precision="day",
        confidence=0.95,
        is_complete_date=True
    )

Common operations:

    # Convert to different formats
    parsed.to_dict("standard")  # Normalized components
    parsed.to_dict("numeric")   # Numeric month format
    parsed.to_dict("raw")       # Original input
    
    # Check date completeness
    if parsed.is_complete_date:
        print(f"Complete date: {parsed}")
    
    # Analyze parsing results
    print(parsed.analysis_date())
"""

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
        # Look for 'src' directory in the path hierarchy
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
    # normalize_numeric_word, 
    get_calendar
)

from detect_dates.calendar_variants import (
    get_century_from_year,
    get_century_range,
    format_century_with_era,
)

from components import DateComponents
from components_default import DateComponentsDefault
from meta import DateMeta


@dataclass 
class ParsedDate:
    """
    Comprehensive parsed date with raw, standardized, and numeric representations.

    This is the main class for representing a fully processed date with multiple
    representation formats and rich metadata. It automatically normalizes input
    components and provides convenient property access to all date information.

    Parameters
    ----------
    raw : DateComponents
        Original raw input components before normalization
    standard : DateComponents  
        Standardized/normalized components
    numeric : DateComponents
        Numeric representations where possible
    meta : DateMeta
        Metadata about parsing context and quality

    Examples
    --------
    >>> # Create from raw components
    >>> raw_components = DateComponents(day="15", month="March", year="2023", era="CE")
    >>> meta = DateMeta(text="15 March 2023", lang="en")
    >>> date = ParsedDate(raw=raw_components, standard=DateComponents(), 
    ...                   numeric=DateComponents(), meta=meta)
    
    >>> # Access normalized properties
    >>> print(date.day)  # 15
    >>> print(date.month)  # "March" 
    >>> print(date.month_num)  # 3
    >>> print(date.is_complete_date)  # True
    
    >>> # Get analysis
    >>> print(date.analysis_date())
    """
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
        Post-initialization processing for automatic normalization and validation.
        
        This method runs automatically after dataclass initialization to:
        1. Process any legacy dictionary input format
        2. Normalize raw components into standard format
        3. Create numeric representations
        4. Calculate metadata flags and derived values
        5. Validate confidence scores and set precision levels

        Parameters
        ----------
        date : dict, optional
            Legacy dictionary format for backward compatibility
        weekday, day, month, year, century, era, calendar : various types, optional
            Individual date components (overrides date dict if provided)
        text, lang, precision, confidence, created_at, created_by : various types, optional
            Metadata components
        role_in_text, related_to : str, optional
            Contextual metadata
        is_calendar_date, is_complete_date, valid_date : bool
            Validation flags
        """
        
        # Process raw date components from individual parameters or date dict
        self.raw = DateComponents(
            weekday=weekday if weekday else (date.get('weekday', None) if date else None),
            day=day if day else (date.get('day', None) if date else None),
            month=month if month else (date.get('month', None) if date else None),
            year=year if year else (date.get('year', None) if date else None),
            century=century if century else (date.get('century', None) if date else None),
            era=era if era else (date.get('era', None) if date else None),
            calendar=calendar if calendar else (date.get('calendar', None) if date else None)
        )
        
        # Process metadata from individual parameters or date dict
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
        
        # Calculate century if not provided but year is available
        century = self.raw.century
        if not century and self.raw.year is not None:
            try:
                if str(self.raw.year).lstrip('-').isdigit():
                    century_result = get_century_from_year(int(self.raw.year))
                    # get_century_from_year returns tuple (century, era)
                    century = century_result[0] if isinstance(century_result, tuple) else century_result
            except (ValueError, TypeError):
                century = None
        
        # Create standardized components with normalization
        self.standard = DateComponents(
            weekday=str(normalize_weekday(self.raw.weekday)) if self.raw.weekday else None,
            day=int(self.raw.day) if self.raw.day and str(self.raw.day).isdigit() else None,
            month=normalize_month(self.raw.month) if self.raw.month else None,
            year=int(self.raw.year) if self.raw.year and str(self.raw.year).lstrip('-').isdigit() else None,
            century=century if century else None,
            era=normalize_era(self.raw.era) if self.raw.era else None,
            calendar=normalize_calendar_name(self.raw.calendar) if self.raw.calendar else (
                get_calendar(self.raw.era) if self.raw.era else None
            )
        )
        
        # Create numeric representation (primarily for month conversion)
        self.numeric = DateComponents(
            weekday=self.standard.weekday if isinstance(self.standard.weekday, str) else None,
            day=self.standard.day,
            month=normalize_month(self.standard.month, output_format="num") if self.standard.month else None,
            year=self.standard.year,
            century=self.standard.century,
            era=self.standard.era,
            calendar=self.standard.calendar
        )
        
        # Validate confidence score range
        if self.meta.confidence is not None:
            if not (0.0 <= self.meta.confidence <= 1.0):
                raise ValueError("Confidence must be between 0.0 and 1.0")
        
        # Calculate validation flags and metadata if not explicitly set
        if self.meta.is_calendar_date is False:
            self.meta.is_calendar_date = self._is_calendar()
        if self.meta.is_complete_date is False:
            self.meta.is_complete_date = self._is_complete()
        if self.meta.valid_date is False:
            self.meta.valid_date = self.meta.is_calendar_date and self.meta.is_complete_date
            
        # Auto-detect language if not provided
        if self.meta.lang is None:
            self.meta.lang = self._detect_language()
        
        # Set precision based on available components if not explicitly provided
        if self.meta.precision is None:
            self.meta.precision = (
                'day' if self.meta.is_complete_date else
                'month' if self.raw.month and self.raw.year else
                'year' if self.raw.year else
                'century' if self.raw.century else
                'partial'
            )

    # Property accessors for convenient access to components
    @property
    def text(self) -> Optional[str]:
        """Get the original text that was parsed."""
        return self.meta.text

    @property
    def lang(self) -> Optional[str]:
        """Get the detected or specified language."""
        return self.meta.lang

    @property
    def precision(self) -> Optional[str]:
        """Get the precision level of this date."""
        return self.meta.precision

    @property
    def confidence(self) -> Optional[float]:
        """Get the parsing confidence score."""
        return self.meta.confidence

    @property
    def metadata(self) -> Dict[str, Any]:
        """Get dictionary of metadata fields."""
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
        """Get the standardized weekday."""
        return self.standard.weekday

    @property
    def day(self) -> Optional[int]:
        """Get the standardized day of month."""
        return self.standard.day

    @property
    def month(self) -> Optional[Union[int, str]]:
        """Get the standardized month (name format)."""
        return self.standard.month

    @property
    def month_num(self) -> Optional[int]:
        """Get the month as a number (1-12)."""
        return self.numeric.month

    @property
    def year(self) -> Optional[int]:
        """Get the standardized year."""
        return self.standard.year

    @property
    def century(self) -> Optional[Union[int, str]]:
        """Get the calculated or provided century."""
        return self.standard.century

    @property
    def era(self) -> Optional[str]:
        """Get the standardized era."""
        return self.standard.era

    @property
    def calendar(self) -> Optional[str]:
        """Get the standardized calendar system."""
        return self.standard.calendar

    @property
    def valid_date(self) -> bool:
        """Check if this represents a valid, complete date."""
        return self.meta.valid_date

    @property
    def is_complete_date(self) -> bool:
        """Check if this has day-level precision."""
        return self.meta.is_complete_date

    @property
    def is_calendar_date(self) -> bool:
        """Check if this has calendar-level information (year + era)."""
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
        >>> date = ParsedDate(raw=DateComponents(weekday="Sunday", day="15", month="March", 
        ...                                     year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> print(date.analysis_date())
        Input  : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: None, Era: CE, Calendar: gregorian]
        Standard Output : [Weekday: Sunday, Day: 15, Month: March, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Numeric Output : [Weekday: Sunday, Day: 15, Month: 3, Year: 2023, Century: 21, Era: CE, Calendar: gregorian]
        Date Info : Is Valid Date: True, Is Complete: True, Is Calendar: True, Precision: day, Language: en
        """
        # Format input components
        input_components = [
            f"Weekday: {self.raw.weekday}",
            f"Day: {self.raw.day}",
            f"Month: {self.raw.month}",
            f"Year: {self.raw.year}",
            f"Century: {self.raw.century}",
            f"Era: {self.raw.era}",
            f"Calendar: {self.raw.calendar}"
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
        >>> date = ParsedDate(raw=DateComponents(), standard=DateComponents(), 
        ...                   numeric=DateComponents(), meta=DateMeta(text="15 March 2023"))
        >>> date._detect_language()
        'en'
        >>> date_ar = ParsedDate(raw=DateComponents(), standard=DateComponents(),
        ...                      numeric=DateComponents(), meta=DateMeta(text="15 مارس 2023"))
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
        >>> complete = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", era="CE"),
        ...                       standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> complete._is_complete()
        True
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial._is_complete()
        False
        """
        return (
            self.day is not None and 
            self.month is not None and 
            self.year is not None and 
            (self.era is not None or self.calendar is not None)
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
        >>> date = ParsedDate(raw=DateComponents(year="2023", era="CE", calendar="gregorian"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> date._is_calendar()
        True
        >>> incomplete = ParsedDate(raw=DateComponents(year="2023"),
        ...                         standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> incomplete._is_calendar()
        False
        """
        return (
            self.year is not None and 
            (self.era is not None or self.calendar is not None)
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

        Raises
        ------
        ValueError
            If an unknown format string is provided

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(day="15", month="March", year="2023"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> standard = date.to_dict("standard")
        >>> standard['day']
        15
        >>> numeric = date.to_dict("numeric")
        >>> numeric['month']
        3
        """
        # Build complete dictionary with all available information
        base_dict = {
            'raw_weekday': self.raw.weekday,
            'raw_day': self.raw.day,
            'raw_month': self.raw.month,
            'raw_year': self.raw.year,
            'raw_century': self.raw.century,
            'raw_era': self.raw.era,
            'raw_calendar': self.raw.calendar,
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
                'raw_weekday': self.raw.weekday,
                'raw_day': self.raw.day,
                'raw_month': self.raw.month,
                'raw_year': self.raw.year,
                'raw_century': self.raw.century,
                'raw_era': self.raw.era,
                'raw_calendar': self.raw.calendar
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
        >>> date = ParsedDate(raw=DateComponents(weekday="Monday", day="15", month="March", 
        ...                                     year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> str(date)
        'Monday, 15 March 2023 CE'
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> str(partial)
        'March 2023'
        >>> empty = ParsedDate(raw=DateComponents(), standard=DateComponents(), 
        ...                    numeric=DateComponents(), meta=DateMeta())
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

    def strftime(self, format_string: str) -> str:
        """
        Format the parsed date using strftime-like format codes with extensions.
        
        Supports standard strftime codes plus custom extensions for partial dates
        and calendar-specific information. Missing components are displayed with
        question marks to indicate incomplete data.

        Parameters
        ----------
        format_string : str
            Format string with % codes for date components

        Returns
        -------
        str
            Formatted date string with missing components shown as ? marks

        Notes
        -----
        Standard strftime codes supported:
        - %d: Day with zero padding (01-31) or ?? if None
        - %e: Day without padding (1-31) or ? if None  
        - %m: Month as number with padding (01-12) or ?? if None
        - %n: Month as number without padding (1-12) or ? if None
        - %b: Abbreviated month name (Jan, Feb, ...) or ??? if None
        - %B: Full month name (January, February, ...) or ??? if None
        - %y: Year without century (00-99) or ?? if None
        - %Y: Year with century (e.g. 2023, 1066) or ???? if None
        - %C: Century number or ?? if None
        - %A: Full weekday name (Monday, ...) or ??? if None
        - %a: Abbreviated weekday name (Mon, ...) or ??? if None

        Custom extensions:
        - %E: Era (BCE, CE, AD, BC) or empty if None
        - %S: Calendar system or empty if None  
        - %P: Precision level or empty if None
        - %%: Literal % character

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> date.strftime("%Y-%m-%d")
        '2023-03-15'
        >>> date.strftime("%B %e, %Y %E")
        'March 15, 2023 CE'
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial.strftime("%B %Y")
        'March 2023'
        >>> partial.strftime("%Y-%m-%d")
        '2023-03-??'
        """
        result = format_string
        
        # Day formatting
        if self.day is not None:
            result = result.replace('%d', f"{self.day:02d}")
            result = result.replace('%e', str(self.day))
        else:
            result = result.replace('%d', '??')
            result = result.replace('%e', '?')
        
        # Month formatting
        if self.month_num is not None:
            result = result.replace('%m', f"{self.month_num:02d}")
            result = result.replace('%n', str(self.month_num))
            
            # Use existing month name from standard components if available
            if self.month:
                # Full month name
                result = result.replace('%B', str(self.month))
                # Abbreviated month name (first 3 characters)
                abbr_month = str(self.month)[:3] if len(str(self.month)) >= 3 else str(self.month)
                result = result.replace('%b', abbr_month)
            else:
                result = result.replace('%B', '???')
                result = result.replace('%b', '???')
        else:
            result = result.replace('%m', '??')
            result = result.replace('%n', '?')
            result = result.replace('%B', '???')
            result = result.replace('%b', '???')
        
        # Year formatting
        if self.year is not None:
            result = result.replace('%Y', str(self.year))
            result = result.replace('%y', f"{abs(self.year) % 100:02d}")
            # Century calculation
            if self.century is not None:
                result = result.replace('%C', str(self.century))
            else:
                # Calculate century from year
                century_num = (abs(self.year) // 100) + 1
                result = result.replace('%C', str(century_num))
        else:
            result = result.replace('%Y', '????')
            result = result.replace('%y', '??')
            result = result.replace('%C', '??')
        
        # Weekday formatting
        if self.weekday is not None:
            weekday_str = str(self.weekday)
            result = result.replace('%A', weekday_str)
            # Abbreviated weekday (first 3 characters)
            abbr_weekday = weekday_str[:3] if len(weekday_str) >= 3 else weekday_str
            result = result.replace('%a', abbr_weekday)
        else:
            result = result.replace('%A', '???')
            result = result.replace('%a', '???')
        
        # Custom extension formatting
        result = result.replace('%E', self.era or '')
        result = result.replace('%S', self.calendar or '')
        result = result.replace('%P', self.precision or '')
        
        # Handle literal % character (must be done last)
        result = result.replace('%%', '%')
        
        return result


# Example usage and testing
if __name__ == "__main__":
    # Example 1: Basic date components
    print("=== Example 1: Basic Date Components ===")
    components = DateComponents(day=15, month=3, year=2023, era="CE", calendar="gregorian")
    print(f"Basic components: day={components.day}, month={components.month}, year={components.year}")
    
    # Example 2: Validated date components
    print("\n=== Example 2: Validated Date Components ===")
    try:
        valid_date = DateComponentsDefault(day=15, month=3, year=2023)
        print("Valid date created successfully")
        
        # This should raise an error
        # invalid_date = DateComponentsDefault(day=35, month=3, year=2023)
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Example 3: Date metadata
    print("\n=== Example 3: Date Metadata ===")
    meta = DateMeta(
        text="15 March 2023",
        lang="en", 
        precision="day",
        confidence=0.95,
        is_complete_date=True
    )
    print(f"Metadata: text='{meta.text}', confidence={meta.confidence}")
    
    # Example 4: Full parsed date
    print("\n=== Example 4: Full Parsed Date ===")
    raw_components = DateComponents(day="15", month="March", year="2023", era="CE")
    date_meta = DateMeta(text="15 March 2023", lang="en")
    
    parsed = ParsedDate(
        raw=raw_components,
        standard=DateComponents(),  # Will be auto-populated
        numeric=DateComponents(),   # Will be auto-populated  
        meta=date_meta
    )
    
    print(f"Parsed date string: {parsed}")
    print(f"Day: {parsed.day}, Month: {parsed.month}, Month number: {parsed.month_num}")
    print(f"Complete date: {parsed.is_complete_date}")
    print(f"Analysis:\n{parsed.analysis_date()}")
    
    # Example 5: Dictionary export
    print("\n=== Example 5: Dictionary Export ===")
    standard_dict = parsed.to_dict("standard")
    print(f"Standard format: {standard_dict}")
    
    numeric_dict = parsed.to_dict("numeric") 
    print(f"Numeric format: {numeric_dict}")