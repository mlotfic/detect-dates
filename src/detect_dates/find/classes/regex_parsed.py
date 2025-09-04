"""
Date parsing utilities using regular expressions.

This module provides a dataclass for storing parsed date components
extracted from text using regex patterns and converting them to 
structured ParsedDate objects.
"""
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
                break
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()
    
import re
from dataclasses import dataclass
from typing import Optional, Union

from ..classes.parsed import ParsedDate
from ..get_match_value import get_match_value
from detect_dates.normalizers import get_calendar


@dataclass
class RegexParsedDate:
    """
    Container for date components parsed from text using regex.
    
    This dataclass stores the results of regex pattern matching on text
    to extract various date/time components. Each field can contain either
    a single match or multiple matches depending on the regex pattern used.
    Provides validation and conversion to ParsedDate objects.
    
    Parameters
    ----------
    match : re.Match
        The regex match object containing the full match details
    weekday : Optional[Union[int, list]], optional
        Parsed weekday value(s). Can be day number (0-6) or list of matches
    day : Optional[Union[int, list]], optional  
        Parsed day of month value(s). Can be single day or list of matches
    month : Optional[Union[int, list]], optional
        Parsed month value(s). Can be month number or list of matches
    year : Optional[Union[int, list]], optional
        Parsed year value(s). Can be single year or list of matches
    century : Optional[Union[int, list]], optional
        Parsed century value(s). Can be single century or list of matches
    era : Optional[Union[int, list]], optional
        Parsed era indicator(s). Can be single era or list of matches
        
    Raises
    ------
    ValueError
        If match is not a re.Match object or if any field has invalid type
        
    Examples
    --------
    >>> import re
    >>> pattern = r"(\d{1,2})/(\d{1,2})/(\d{4})"
    >>> text = "The date is 12/25/2023"
    >>> match = re.search(pattern, text)
    >>> parsed_date = RegexParsedDate(
    ...     match=match,
    ...     month=12,
    ...     day=25, 
    ...     year=2023
    ... )
    >>> print(f"Year: {parsed_date.year}")
    Year: 2023
    """
    
    match: re.Match  # The regex match object from pattern matching
    weekday: Optional[Union[int, list]] = None
    day: Optional[Union[int, list]] = None  
    month: Optional[Union[int, list]] = None
    year: Optional[Union[int, list]] = None
    century: Optional[Union[int, list]] = None
    era: Optional[Union[int, list]] = None
    
    def __post_init__(self):
        """
        Validate input fields after dataclass initialization.
        
        Ensures that the match object is valid and all date component
        fields have the correct types (int or list).
        
        Raises
        ------
        ValueError
            If match is not a re.Match object or any field has invalid type
        """
        # Validate the core match object
        if not isinstance(self.match, re.Match):
            raise ValueError("match must be an instance of re.Match")
        
        # Validate each date component field type
        date_fields = [
            ('weekday', self.weekday),
            ('day', self.day), 
            ('month', self.month),
            ('year', self.year),
            ('century', self.century),
            ('era', self.era)
        ]
        
        for field_name, field_value in date_fields:
            if field_value is not None and not isinstance(field_value, (int, list)):
                raise ValueError(f"{field_name} must be an int or list of ints")
        
    def get_parsed_dates(self) -> ParsedDate:
        """
        Convert the regex parsed components into a ParsedDate instance.
        
        This method maps the fields from RegexParsedDate to a ParsedDate
        dataclass, extracting actual values from the regex match object
        and applying calendar normalization when applicable.
        
        Returns
        -------
        ParsedDate
            An instance of ParsedDate with the extracted and normalized components.
            Includes the original matched text and inferred calendar system.
            
        Notes
        -----
        - Uses get_match_value() to extract actual values from regex groups
        - Converts day values to integers when possible
        - Determines calendar system from era information
        - Preserves raw matched text for reference
        
        Examples
        --------
        >>> import re
        >>> match = re.search(r"(\d{2})/(\d{2})/(\d{4})", "12/25/2023")
        >>> regex_parsed = RegexParsedDate(match=match, month=1, day=2, year=3)
        >>> parsed_date = regex_parsed.get_parsed_dates()
        >>> print(parsed_date.year)
        '2023'
        """
        # Helper function to safely extract and convert day values to int
        def _safe_day_conversion():
            if self.day is None:
                return None
            day_value = get_match_value(self.match, self.day)
            if day_value is not None:
                try:
                    return int(day_value)
                except (ValueError, TypeError):
                    return None
            return None
        
        return ParsedDate(
            # Preserve the original match object for reference
            match=self.match,
            # Store raw values extracted from the match for debugging
            raw_values={
                'weekday': self.weekday,
                'day': self.day,
                'month': self.month,
                'year': self.year,
                'century': self.century,
                'era': self.era
                },
            
            # Extract weekday value from match object
            weekday=str(get_match_value(self.match, self.weekday)) if self.weekday is not None and get_match_value(self.match, self.weekday) is not None else None,
            
            # Extract and convert day to integer with safe error handling
            day=_safe_day_conversion(),
            
            # Extract month value from match object
            month=get_match_value(self.match, self.month) if self.month is not None else None,
            
            # Extract year value from match object  
            year=(
                int(year_value) if (
                    self.year is not None and 
                    (year_value := get_match_value(self.match, self.year)) is not None
                ) else None
            ),
            
            # Extract century value from match object
            century=get_match_value(self.match, self.century) if self.century is not None else None,
            
            # Extract era value from match object
            era=str(get_match_value(self.match, self.era)) if self.era is not None and get_match_value(self.match, self.era) is not None else None,
            
            # Determine calendar system based on era (e.g., Gregorian, Julian, etc.)
            calendar=(
                str(get_calendar(str(get_match_value(self.match, self.era))))
                if self.era is not None and get_match_value(self.match, self.era) is not None
                else None
            ),
            
            # Store the original matched text for reference
            raw_text=self.match.group(0) if self.match else None,
        )