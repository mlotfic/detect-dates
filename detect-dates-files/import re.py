import re
from dataclasses import dataclass
from typing import Pattern, Optional

@dataclass
class BasePatterns:
    """Base patterns imported from external patterns module"""
    weekday: str
    numeric_words_ar: str
    
@dataclass
class MonthPatterns:
    """Patterns for month names in different calendars"""
    hijri: str
    gregorian: str
    julian: str

@dataclass
class EraPatterns:
    """Patterns for different eras in date formats"""
    hijri: str
    gregorian: str
    julian: str

@dataclass
class IndicatorPatterns:
    """Patterns for date indicators"""
    day: str
    month: str
    year: str
    century: str
    separator: str
    range_connector: str
    range_starter: str

@dataclass
class NumericPatterns:
    """Basic numeric patterns for dates"""
    year: str = r"(\d{1,4})"
    month: str = r"(\d{1,2})"
    day: str = r"(\d{1,2})"
    century: str = r"(\d{1,2})"
    
    def __post_init__(self):
        # Validate patterns compile correctly
        for field_name, pattern in [
            ("year", self.year),
            ("month", self.month),
            ("day", self.day),
            ("century", self.century)
        ]:
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern for {field_name}: {e}")
