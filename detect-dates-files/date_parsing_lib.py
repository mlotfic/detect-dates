import re
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union
from enum import Enum


class Era(Enum):
    """Enumeration for different era designations."""
    BCE = "BCE"
    CE = "CE"
    BC = "BC"
    AD = "AD"
    AH = "AH"  # Islamic calendar
    AM = "AM"  # Anno Mundi


class CalendarSystem(Enum):
    """Enumeration for different calendar systems."""
    GREGORIAN = "Gregorian"
    JULIAN = "Julian"
    ISLAMIC = "Islamic"
    HEBREW = "Hebrew"
    CHINESE = "Chinese"
    PERSIAN = "Persian"


class DatePrecision(Enum):
    """Enumeration for date precision levels."""
    EXACT = "exact"
    APPROXIMATE = "approximate"
    CENTURY = "century"
    DECADE = "decade"
    YEAR = "year"
    SEASON = "season"
    MONTH = "month"
    DAY = "day"


@dataclass
class ParsedDate:
    """
    Represents a single parsed date with flexible precision and optional components.
    
    Attributes:
        day: Day of the month (1-31)
        month: Month as number (1-12) or name ("January", "Jan")
        year: Full year (e.g., 2023, 1066, -44 for 45 BCE)
        weekday: Day of the week ("Monday", "Mon")
        century: Century number or description ("21st", "first")
        era: Era designation (BCE, CE, AD, BC, etc.)
        calendar: Calendar system used
        precision: Indicates the precision level of this date
        confidence: Confidence score (0.0-1.0) for parsed accuracy
        raw_text: Original text that was parsed to create this date
        metadata: Additional parsing information
    """
    weekday: Optional[str] = None
    day: Optional[int] = None
    month: Optional[Union[int, str]] = None
    year: Optional[int] = None
    century: Optional[Union[int, str]] = None
    era: Optional[Union[Era, str]] = None
    calendar: Optional[Union[CalendarSystem, str]] = None
    precision: Optional[Union[DatePrecision, str]] = None
    confidence: Optional[float] = None
    raw_text: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    def is_complete(self) -> bool:
        """Check if date has minimum required components (day, month, year)."""
        return all([self.day, self.month, self.year])
    
    def is_partial(self) -> bool:
        """Check if date has some but not all components."""
        components = [self.day, self.month, self.year]
        return any(components) and not all(components)
    
    def get_year_with_era(self) -> Optional[int]:
        """Get year adjusted for era (negative for BCE/BC)."""
        if self.year is None:
            return None
        
        era_str = ""
        if isinstance(self.era, Era):
            era_str = self.era.value
        elif self.era is not None:
            era_str = str(self.era).upper()
        
        if era_str in ["BCE", "BC"]:
            return -self.year
        else:
            return self.year
    
    def strftime(self, format_string: str) -> str:
        """
        Format the parsed date using strftime-like format codes.
        
        Supports standard strftime codes plus extensions for partial dates:
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
        - %E: Era (BCE, CE, AD, BC) or empty if None
        - %S: Calendar system or empty if None
        - %P: Precision level or empty if None
        - %%: Literal % character
        
        Args:
            format_string: Format string with % codes
            
        Returns:
            Formatted date string with missing components shown as ? marks
            
        Examples:
            >>> date = ParsedDate(day=15, month=3, year=2023)
            >>> date.strftime("%Y-%m-%d")  # "2023-03-15"
            >>> date.strftime("%B %e, %Y")  # "March 15, 2023"
            
            >>> partial_date = ParsedDate(month="March", year=2023)
            >>> partial_date.strftime("%B %Y")  # "March 2023"
            >>> partial_date.strftime("%Y-%m-%d")  # "2023-03-??"
        """        
        # Month name mappings
        month_names_full = {
            1: "January", 2: "February", 3: "March", 4: "April",
            5: "May", 6: "June", 7: "July", 8: "August", 
            9: "September", 10: "October", 11: "November", 12: "December"
        }
        
        month_names_abbr = {
            1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
            5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
            9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
        }
        
        # Handle month conversion if it's a string
        month_num = None
        if self.month is not None:
            if isinstance(self.month, int):
                month_num = self.month
            else:
                # Try to convert month name to number
                month_str = str(self.month).lower()
                for num, name in month_names_full.items():
                    if month_str in [name.lower(), month_names_abbr[num].lower()]:
                        month_num = num
                        break
        
        # Build replacements dictionary
        replacements = {}
        
        # Day formats
        if self.day is not None:
            replacements['%d'] = f"{self.day:02d}"
            replacements['%e'] = str(self.day)
        else:
            replacements['%d'] = "??"
            replacements['%e'] = "?"
            
        # Month formats
        if month_num is not None:
            replacements['%m'] = f"{month_num:02d}"
            replacements['%n'] = str(month_num)
            replacements['%b'] = month_names_abbr[month_num]
            replacements['%B'] = month_names_full[month_num]
        elif isinstance(self.month, str):
            # Use string month name directly
            replacements['%m'] = "??"
            replacements['%n'] = "?"
            replacements['%b'] = self.month[:3] if len(self.month) >= 3 else self.month
            replacements['%B'] = self.month
        else:
            replacements['%m'] = "??"
            replacements['%n'] = "?"
            replacements['%b'] = "???"
            replacements['%B'] = "???"
            
        # Year formats
        if self.year is not None:
            year_with_era = self.get_year_with_era() or self.year
            replacements['%Y'] = str(abs(year_with_era))
            replacements['%y'] = f"{abs(year_with_era) % 100:02d}"
        else:
            replacements['%Y'] = "????"
            replacements['%y'] = "??"
            
        # Century
        if self.century is not None:
            replacements['%C'] = str(self.century)
        else:
            replacements['%C'] = "??"
            
        # Weekday
        if self.weekday is not None:
            replacements['%A'] = str(self.weekday)
            replacements['%a'] = str(self.weekday)[:3] if len(str(self.weekday)) >= 3 else str(self.weekday)
        else:
            replacements['%A'] = "???"
            replacements['%a'] = "???"
            
        # Era
        era_str = ""
        if self.era is not None:
            if isinstance(self.era, Era):
                era_str = self.era.value
            else:
                era_str = str(self.era)
        replacements['%E'] = era_str
        
        # Calendar system
        cal_str = ""
        if self.calendar is not None:
            if isinstance(self.calendar, CalendarSystem):
                cal_str = self.calendar.value
            else:
                cal_str = str(self.calendar)
        replacements['%S'] = cal_str
        
        # Precision
        prec_str = ""
        if self.precision is not None:
            if isinstance(self.precision, DatePrecision):
                prec_str = self.precision.value
            else:
                prec_str = str(self.precision)
        replacements['%P'] = prec_str
        
        # Literal %
        replacements['%%'] = "%"
        
        # Apply replacements
        result = format_string
        for code, value in replacements.items():
            result = result.replace(code, value)
            
        return result
    
    def to_iso_format(self) -> str:
        """
        Convert to ISO 8601 format (YYYY-MM-DD) with missing components as ?.
        
        Returns:
            ISO formatted date string like "2023-03-15" or "2023-??-??" for partial dates
        """
        return self.strftime("%Y-%m-%d")
    
    def to_readable_format(self) -> str:
        """
        Convert to human-readable format.
        
        Returns:
            Readable date string like "March 15, 2023" or "March 2023" for partial dates
        """
        if self.day is not None:
            base_format = "%B %e, %Y"
        elif self.month is not None:
            base_format = "%B %Y"
        elif self.year is not None:
            base_format = "%Y"
        else:
            base_format = "Unknown date"
            
        result = self.strftime(base_format) if base_format != "Unknown date" else base_format
        
        # Add era if present
        if self.era is not None:
            era_str = self.era.value if isinstance(self.era, Era) else str(self.era)
            result += f" {era_str}"
            
        return result


@dataclass
class DateAlternative:
    """
    Represents an alternative between two calendar systems.
    
    Examples:
    - "2023CE/1445AH" (Gregorian/Islamic)
    - "1066AD/1066CE" (Julian/Gregorian)
    """
    primary: ParsedDate
    alternative: ParsedDate
    
    def get_primary_readable(self) -> str:
        """Get readable format of primary date."""
        return self.primary.to_readable_format()
    
    def get_alternative_readable(self) -> str:
        """Get readable format of alternative date."""
        return self.alternative.to_readable_format()
    
    def to_combined_format(self, separator: str = "/") -> str:
        """Combine both dates with a separator."""
        primary_str = self.primary.to_readable_format()
        alt_str = self.alternative.to_readable_format()
        return f"{primary_str}{separator}{alt_str}"


@dataclass
class DateRange:
    """
    Represents a range between two dates.
    
    Examples:
    - "20 March 2023 to 24 March 2023 CE"
    - "Winter 1066 to Spring 1067"
    """
    start_date: ParsedDate
    end_date: ParsedDate
    range_type: Optional[str] = None  # "Range", "Alternative", "seasonal", etc.
    
    def is_single_day(self) -> bool:
        """Check if this represents a single day (start == end)."""
        return (self.start_date.day == self.end_date.day and
                self.start_date.month == self.end_date.month and
                self.start_date.year == self.end_date.year)
    
    def get_duration_estimate(self) -> Optional[dict]:
        """
        Estimate duration between start and end dates.
        Returns dict with 'days', 'months', 'years' estimates.
        """
        if not (self.start_date.is_complete() and self.end_date.is_complete()):
            return None
        
        # This is a simplified calculation - real implementation would need
        # proper date arithmetic considering calendar systems
        year_diff = (self.end_date.year or 0) - (self.start_date.year or 0)
        month_diff = (self.end_date.month or 0) - (self.start_date.month or 0)
        day_diff = (self.end_date.day or 0) - (self.start_date.day or 0)
        
        return {
            'years': year_diff,
            'months': month_diff,
            'days': day_diff
        }
    
    def to_readable_format(self) -> str:
        """Convert range to readable format."""
        start_str = self.start_date.to_readable_format()
        end_str = self.end_date.to_readable_format()
        
        if self.is_single_day():
            return start_str
        
        range_connector = " to "
        if self.range_type == "approximate":
            range_connector = " to approximately "
        elif self.range_type == "seasonal":
            range_connector = " through "
        
        return f"{start_str}{range_connector}{end_str}"


@dataclass
class DateRangeAlternative:
    """
    Represents a range with alternative calendar representations.
    
    Examples:
    - "(١٤١١ - ١٤١٢ هـ) = (١٩٩٠ - ١٩٩٢ م)" (Islamic/Gregorian range)
    - "1066-1087 AD / 1066-1087 CE" (Julian/Gregorian range)
    """
    primary_range: DateRange
    alternative_range: DateRange
    range_type: Optional[str] = None  # "exact", "approximate", "seasonal", etc.
    
    def to_combined_format(self, separator: str = " / ") -> str:
        """Combine both date ranges with a separator."""
        primary_str = self.primary_range.to_readable_format()
        alt_str = self.alternative_range.to_readable_format()
        return f"{primary_str}{separator}{alt_str}"
    
    def get_primary_duration(self) -> Optional[dict]:
        """Get duration estimate for primary range."""
        return self.primary_range.get_duration_estimate()
    
    def get_alternative_duration(self) -> Optional[dict]:
        """Get duration estimate for alternative range."""
        return self.alternative_range.get_duration_estimate()


# Example usage and factory functions
def create_simple_date(day: int, month: int, year: int, era: Era = Era.CE) -> ParsedDate:
    """Factory function to create a simple complete date."""
    return ParsedDate(
        day=day,
        month=month,
        year=year,
        era=era,
        precision=DatePrecision.EXACT,
        confidence=1.0
    )


def create_partial_date(year: Optional[int] = None, 
                       month: Optional[Union[int, str]] = None,
                       day: Optional[int] = None,
                       era: Optional[Era] = None) -> ParsedDate:
    """Factory function to create a partial date."""
    return ParsedDate(
        day=day,
        month=month,
        year=year,
        era=era,
        precision=DatePrecision.APPROXIMATE,
        confidence=0.8
    )