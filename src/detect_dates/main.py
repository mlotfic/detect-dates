from datetime import datetime, date
from typing import Optional, Union, Dict


# " / الاحد  | ١٨ محرم ١٤٤٧ هـ 🗓️"
class DateDetector:
    """Main class for detecting and parsing dates from text"""

    def __init__(self):
        self.date_formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%m/%d/%Y",
            "%d-%m-%Y",
            "%Y/%m/%d"
        ]

    def parse_date(self, date_string: str) -> Optional[date]:
        """
        Attempt to parse a date string using multiple common formats

        Args:
            date_string: String containing a potential date

        Returns:
            date object if successful, None if parsing fails
        """
        for fmt in self.date_formats:
            try:
                return datetime.strptime(date_string, fmt).date()
            except ValueError:
                continue
        return None

    def validate_date(self, year: int, month: int, day: int) -> bool:
        """
        Validate if a date is valid

        Args:
            year: Year as integer
            month: Month as integer
            day: Day as integer

        Returns:
            bool: True if date is valid, False otherwise
        """
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False

    def get_date_components(self, date_obj: date) -> Dict[str, int]:
        """
        Extract year, month and day from a date object

        Args:
            date_obj: datetime.date object

        Returns:
            Dict with year, month and day components
        """
        return {
            "year": date_obj.year,
            "month": date_obj.month,
            "day": date_obj.day
        }

from typing import Dict, Pattern
import re

# Dictionary containing compiled regex patterns for date detection
DATE_PATTERNS: Dict[str, Pattern] = {
    'iso': re.compile(r'^\d{4}-\d{2}-\d{2}$'),
    'usa': re.compile(r'^(?:0?[1-9]|1[0-2])/(?:0?[1-9]|[12]\d|3[01])/(?:19|20)\d{2}$'),
    'eur': re.compile(r'^(?:0?[1-9]|[12]\d|3[01])\.(?:0?[1-9]|1[0-2])\.(?:19|20)\d{2}$'),
    'text': re.compile(r'^(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
                      r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|'
                      r'Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}$', re.IGNORECASE)
}

# Make patterns available when importing the module
__all__ = ['DATE_PATTERNS']

if __name__ == "__main__":
    detector = DateDetector()

    # Example usage
    test_date = "2025-08-23"
    result = detector.parse_date(test_date)
    if result:
        print(f"Parsed date: {result}")
        print(f"Components: {detector.get_date_components(result)}")