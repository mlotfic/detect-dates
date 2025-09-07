"""
Date parsing utilities using regular expressions.

This module provides a dataclass for storing parsed date components
extracted from text using regex patterns and converting them to 
structured ParsedDate objects.

Usage
-----
Basic regex date parsing workflow:

    import re
    from regex_parsed_date import RegexParsedDate
    
    # Parse MM/DD/YYYY format
    pattern = r"(\d{1,2})/(\d{1,2})/(\d{4})"
    text = "The meeting is scheduled for 12/25/2023"
    match = re.search(pattern, text)
    
    if match:
        regex_parsed = RegexParsedDate(
            match=match,
            month=1,  # First capture group (12)
            day=2,    # Second capture group (25)
            year=3    # Third capture group (2023)
        )
        parsed_date = regex_parsed.get_parsed_dates()
        print(f"Parsed: {parsed_date}")  # Parsed: 25 December 2023

Advanced pattern with multiple components:

    # Complex date pattern with weekday and era
    pattern = r"(\w+day),?\s+(\w+)\s+(\d{1,2}),?\s+(\d{4})\s+(CE|BCE|AD|BC)"
    text = "The event was on Monday, March 15, 2023 CE"
    match = re.search(pattern, text)
    
    if match:
        regex_parsed = RegexParsedDate(
            match=match,
            weekday=1,  # "Monday"
            month=2,    # "March"  
            day=3,      # "15"
            year=4,     # "2023"
            era=5       # "CE"
        )
        parsed_date = regex_parsed.get_parsed_dates()
        print(f"Complete date: {parsed_date}")

Working with multiple matches (lists):

    # When regex captures multiple potential values
    regex_parsed = RegexParsedDate(
        match=match,
        year=[1, 3],  # Multiple year candidates from different groups
        month=2
    )

Error handling:

    try:
        regex_parsed = RegexParsedDate(match="not a match object")
    except ValueError as e:
        print(f"Validation error: {e}")
"""

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
    
import re
from dataclasses import dataclass
from typing import Optional, Union

from parsed import ParsedDate
from ..utils.get_match_value import get_match_value


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
    weekday : int or list, optional
        Parsed weekday value(s). Can be group index or list of group indices
    day : int or list, optional  
        Parsed day of month value(s). Can be group index or list of indices
    month : int or list, optional
        Parsed month value(s). Can be group index or list of indices
    year : int or list, optional
        Parsed year value(s). Can be group index or list of indices
    century : int or list, optional
        Parsed century value(s). Can be group index or list of indices
    era : int or list, optional
        Parsed era indicator(s). Can be group index or list of indices
    calendar : str, optional
        Calendar system name if explicitly detected ('gregorian', 'hijri', 'Jalali')
        
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
    ...     month=1,  # First capture group
    ...     day=2,    # Second capture group
    ...     year=3    # Third capture group
    ... )
    >>> print(f"Match text: {parsed_date.match.group(0)}")
    Match text: 12/25/2023
    """
    
    match: re.Match  # The regex match object from pattern matching
    weekday: Optional[Union[int, list]] = None
    day: Optional[Union[int, list]] = None  
    month: Optional[Union[int, list]] = None
    year: Optional[Union[int, list]] = None
    century: Optional[Union[int, list]] = None
    era: Optional[Union[int, list]] = None
    calendar: Optional[str] = None  # Inferred calendar system, if any
    
    def __post_init__(self):
        """
        Validate input fields after dataclass initialization.
        
        Ensures that the match object is valid and all date component
        fields have the correct types (int or list). This validation
        helps catch common errors early in the parsing pipeline.
        
        Raises
        ------
        ValueError
            If match is not a re.Match object or any field has invalid type
            
        Notes
        -----
        The validation ensures that:
        - match is a valid re.Match object with groups
        - All date component fields are either int (single group) or list (multiple groups)
        - Calendar field is a string if provided
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
                raise ValueError(f"{field_name} must be an int or list of ints, got {type(field_value)}")
        
        # Validate calendar field if provided
        if self.calendar is not None and not isinstance(self.calendar, str):
            raise ValueError("calendar must be a string")
        
    def get_parsed_dates(self) -> ParsedDate:
        """
        Convert the regex parsed components into a ParsedDate instance.
        
        This method maps the fields from RegexParsedDate to a ParsedDate
        dataclass, extracting actual values from the regex match object
        and applying calendar normalization when applicable. It handles
        both single values and lists of potential matches.
        
        Returns
        -------
        ParsedDate
            An instance of ParsedDate with the extracted and normalized components.
            Includes the original matched text and inferred calendar system.
            
        Notes
        -----
        - Uses get_match_value() to extract actual values from regex groups
        - Handles both single group indices and lists of group indices
        - Safely converts numeric strings to integers where appropriate
        - Preserves raw matched text for debugging and reference
        - Applies calendar system inference based on era information
        
        Examples
        --------
        >>> import re
        >>> match = re.search(r"(\d{2})/(\d{2})/(\d{4})", "12/25/2023")
        >>> regex_parsed = RegexParsedDate(match=match, month=1, day=2, year=3)
        >>> parsed_date = regex_parsed.get_parsed_dates()
        >>> print(parsed_date.year)
        2023
        >>> print(parsed_date.month)
        'December'
        
        With multiple potential matches:
        >>> regex_parsed = RegexParsedDate(match=match, year=[1, 3])  # Try groups 1 and 3
        >>> parsed_date = regex_parsed.get_parsed_dates()
        """        
        # Preserve the original matched text for reference and debugging
        text = self.match.group(0) if self.match else None
        
        # Extract weekday value from match object using utility function
        weekday = get_match_value(self.match, self.weekday) if self.weekday is not None else None
        
        # Extract day value and safely convert to integer if possible
        day = get_match_value(self.match, self.day) if self.day is not None else None
            
        # Extract month value from match object (could be name or number)
        month = get_match_value(self.match, self.month) if self.month is not None else None
            
        # Extract year value from match object  
        year = get_match_value(self.match, self.year) if self.year is not None else None
            
        # Extract century value from match object
        century = get_match_value(self.match, self.century) if self.century is not None else None
            
        # Extract era value from match object (CE, BCE, AD, BC, AH, etc.)
        era = get_match_value(self.match, self.era) if self.era is not None else None
        
        # Create ParsedDate with extracted components
        # The ParsedDate constructor will handle normalization and validation
        return ParsedDate(
            text=text,
            weekday=weekday, 
            day=day, 
            month=month, 
            year=year, 
            century=century, 
            era=era, 
            calendar=self.calendar
        )

    def get_match_text(self) -> str:
        """
        Get the full matched text from the regex match.
        
        Returns
        -------
        str
            The complete text that was matched by the regex pattern,
            or empty string if no match is available
            
        Examples
        --------
        >>> regex_parsed = RegexParsedDate(match=match)
        >>> regex_parsed.get_match_text()
        '12/25/2023'
        """
        return self.match.group(0) if self.match else ""
    
    def get_all_groups(self) -> tuple:
        """
        Get all capture groups from the regex match.
        
        Returns
        -------
        tuple
            All capture groups from the regex match, or empty tuple if no match
            
        Examples
        --------
        >>> regex_parsed = RegexParsedDate(match=match)
        >>> regex_parsed.get_all_groups()
        ('12', '25', '2023')
        """
        return self.match.groups() if self.match else ()
    
    def has_component(self, component: str) -> bool:
        """
        Check if a specific date component was captured.
        
        Parameters
        ----------
        component : str
            Component name to check ('weekday', 'day', 'month', 'year', 'century', 'era')
            
        Returns
        -------
        bool
            True if the component was captured and has a non-None value
            
        Examples
        --------
        >>> regex_parsed = RegexParsedDate(match=match, day=2, month=1)
        >>> regex_parsed.has_component('day')
        True
        >>> regex_parsed.has_component('century')
        False
        """
        return getattr(self, component, None) is not None
    
    def __str__(self) -> str:
        """
        Create a string representation showing captured components.
        
        Returns
        -------
        str
            Human-readable summary of captured date components
            
        Examples
        --------
        >>> print(regex_parsed)
        RegexParsedDate(match='12/25/2023', day=2, month=1, year=3)
        """
        components = []
        for field in ['weekday', 'day', 'month', 'year', 'century', 'era']:
            value = getattr(self, field)
            if value is not None:
                components.append(f"{field}={value}")
        
        match_text = self.get_match_text()
        return f"RegexParsedDate(match='{match_text}', {', '.join(components)})"


# Example usage and testing
if __name__ == "__main__":
    import re
    
    print("=== Example 1: Basic MM/DD/YYYY Pattern ===")
    pattern = r"(\d{1,2})/(\d{1,2})/(\d{4})"
    text = "The meeting is scheduled for 12/25/2023"
    match = re.search(pattern, text)
    
    if match:
        regex_parsed = RegexParsedDate(
            match=match,
            month=1,  # First capture group (12)
            day=2,    # Second capture group (25) 
            year=3    # Third capture group (2023)
        )
        
        print(f"Regex parsed: {regex_parsed}")
        print(f"All groups: {regex_parsed.get_all_groups()}")
        print(f"Has day component: {regex_parsed.has_component('day')}")
        
        parsed_date = regex_parsed.get_parsed_dates()
        print(f"Parsed date: {parsed_date}")
        print(f"Analysis: {parsed_date.analysis_date()}")
    
    print("\n=== Example 2: Complex Pattern with Weekday and Era ===")
    pattern = r"(\w+day),?\s+(\w+)\s+(\d{1,2}),?\s+(\d{4})\s+(CE|BCE|AD|BC)"
    text = "The event was on Monday, March 15, 2023 CE"
    match = re.search(pattern, text)
    
    if match:
        regex_parsed = RegexParsedDate(
            match=match,
            weekday=1,  # "Monday"
            month=2,    # "March"
            day=3,      # "15"
            year=4,     # "2023" 
            era=5       # "CE"
        )
        
        print(f"Complex regex parsed: {regex_parsed}")
        parsed_date = regex_parsed.get_parsed_dates()
        print(f"Complete parsed date: {parsed_date}")
    
    print("\n=== Example 3: Error Handling ===")
    try:
        # This should raise a ValueError
        invalid_parsed = RegexParsedDate(match="not a match object")
    except ValueError as e:
        print(f"Caught validation error: {e}")
    
    print("\n=== Example 4: Multiple Group Candidates ===")
    pattern = r"(\d{4})-(\d{1,2})-(\d{1,2})|(\d{1,2})/(\d{1,2})/(\d{4})"
    text = "Date could be 2023-03-15 or 03/15/2023"
    match = re.search(pattern, text)
    
    if match:
        # Try multiple groups for year (first or last capture group)
        regex_parsed = RegexParsedDate(
            match=match,
            year=[1, 6],  # Could be in group 1 or 6
            month=[2, 4], # Could be in group 2 or 4
            day=[3, 5]    # Could be in group 3 or 5
        )
        
        print(f"Multi-group parsed: {regex_parsed}")
        parsed_date = regex_parsed.get_parsed_dates()
        print(f"Final parsed date: {parsed_date}")