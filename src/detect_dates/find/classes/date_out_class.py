from dataclasses import dataclass, field
from typing import Optional, Union, Dict, Any, Tuple
import re
from datetime import datetime, date
import calendar
import csv
import os
from pathlib import Path

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

from parsed import ParsedDate

@dataclass
class DateEntity:
    raw_start: ParsedDate  
    raw_start_alt: Optional[ParsedDate] = None  
    raw_end: Optional[ParsedDate] = None
    raw_end_alt: Optional[ParsedDate] = None
    
    calendar_input_count: int = 1
    complicity : Optional[str] = None  # "component"1, "simple_unknown" 1, "simple" 1, "composite" 2, "seasonal"2,4, "complex"4.
    relation: Optional[str] = None  # "simple", "simple-range" 2, "simple-financial"2, "complex-range"4, "complex-financial"4
    text: Optional[str] = None
    
    
    def __post_init__(self):
        start_hijri: Optional[ParsedDate] = None
        end_hijri: Optional[ParsedDate] = None
        start_gregorian: Optional[ParsedDate] = None
        end_gregorian: Optional[ParsedDate] = None
        
    def start_hijri(self) -> Optional[ParsedDate]:
        """Get the Hijri date for the start date, if available."""
        if self.raw_start.calendar == 'hijri':
            return self.raw_start
        if self.raw_start_alt and self.raw_start_alt.calendar == 'hijri':
            return self.raw_start_alt
        return None
    
    def end_hijri(self) -> Optional[ParsedDate]:
        """Get the Hijri date for the end date, if available."""
        if self.raw_end and self.raw_end.calendar == 'hijri':
            return self.raw_end
        if self.raw_end_alt and self.raw_end_alt.calendar == 'hijri':
            return self.raw_end_alt
        return None
    
    def start_gregorian(self) -> Optional[ParsedDate]:
        """Get the Gregorian date for the start date, if available."""
        if self.raw_start.calendar == 'gregorian':
            return self.raw_start
        if self.raw_start_alt and self.raw_start_alt.calendar == 'gregorian':
            return self.raw_start_alt
        return None
    
    def end_gregorian(self) -> Optional[ParsedDate]:
        """Get the Gregorian date for the end date, if available."""
        if self.raw_end and self.raw_end.calendar == 'gregorian':
            return self.raw_end
        if self.raw_end_alt and self.raw_end_alt.calendar == 'gregorian':
            return self.raw_end_alt
        return None
    
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

@dataclass
class DateAlternative:
    """
    Represents a alternative between two calendar system.

    Examples:
    - "2023CE/1445AH"
    """
    raw: ParsedDate
    alternative: ParsedDate


@dataclass
class DateRange:
    """
    Represents a range between two dates.

    Examples:
    - "20 March 2023 to 24 March 2023 CE"
    """
    start_date: DateAlternative
    end_date: DateAlternative
    range_type: Optional[str] = None  # "exact", "approximate", "seasonal", etc.

    def is_single_day(self) -> bool:
        """Check if this represents a single day (start == end)."""
        start_primary = self.start_date.primary
        end_primary = self.end_date.primary

        return (start_primary.day == end_primary.day and
                start_primary.month == end_primary.month and
                start_primary.year == end_primary.year)

    def get_duration_estimate(self) -> Optional[dict]:
        """
        Estimate duration between start and end dates.
        Returns dict with 'days', 'months', 'years' estimates.
        """
        start = self.start_date.primary
        end = self.end_date.primary

        if not (start.is_complete() and end.is_complete()):
            return None

        # This is a simplified calculation - real implementation would need
        # proper date arithmetic considering calendar systems
        year_diff = (end.year or 0) - (start.year or 0)
        month_diff = (end.month or 0) - (start.month or 0)
        day_diff = (end.day or 0) - (start.day or 0)

        return {
            'years': year_diff,
            'months': month_diff,
            'days': day_diff
        }



@dataclass
class DateRangeAlternative:
    """
    Represents a range between two dates.

    Examples:
    - "(١٤١١ - ١٤١٢ هـ) = (١٩٩٠ - ١٩٩٢ م)"
    """
    start_date: DateRange
    end_date: DateRange
   range_type: Optional[str] = None  # "exact", "approximate", "s