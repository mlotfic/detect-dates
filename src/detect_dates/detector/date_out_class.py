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

from detect_dates.normalizers import normalize_month
from detect_dates.normalizers import normalize_era
from detect_dates.normalizers import normalize_weekday
from data._load_data import DateMapping

'''
Examples:
        >>> normalize_month("January", output_format="num")
        1

        >>> normalize_month("January", to_lang="ar", to_calendar="hijri", output_format="full")
        "محرم"

        >>> normalize_month(1, to_lang="en", to_calendar="gregorian", output_format="abbr")
        "Jan"
Examples:
        >>> normalize_weekday("Sunday", output_format="num")
        1

        >>> normalize_weekday("Sunday", to_lang="ar", output_format="full")
        "الأحد"

        >>> normalize_weekday(1, to_lang="en", output_format="abbr")
        "Sun"

        >>> normalize_weekday("الأحد", to_lang="en", output_format="full")
        "Sunday"

'''
@dataclass
class DateEntity:
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
    era: Optional[str] = None
    calendar: Optional[str] = None
    raw_text: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

@dataclass
class ParsedDate(DateEntity):
    """
    Represents a single parsed date with flexible precision and optional components.

    """
    # Class-level cache for date mappings
    _date_mappings: Dict[str, Dict[Tuple[int, int, int], Tuple[int, int, int]]] = {}
    _mappings_loaded: bool = False

    def _init__(self, mapper: DateMapping):
        """Validate date components after initialization."""
        if self.day is not None and not (1 <= self.day <= 31):
            raise ValueError(f"Invalid day: {self.day}")

        self.month_num = normalize_month(self.month, output_format="num")
        if self.month_num is not None and not (1 <= self.month_num <= 12):
            raise ValueError(f"Invalid month: {self.month}")

        if self.confidence is not None and not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"Confidence must be between 0.0 and 1.0: {self.confidence}")

    def is_complete(self) -> bool:
        """Check if date has minimum required components (day, month, year)."""
        return all([self.day, self.month, self.year, self.era])

    def is_partial(self) -> bool:
        """Check if date has some but not all components."""
        components = [self.day, self.month, self.year, self.era]
        return any(components) and not all(components)

    def _get_date_tuple(self) -> Optional[Tuple[int, int, int]]:
        """Get the date as a tuple (year, month, day) for lookup."""
        if not all([self.year, self.day]) or not self.month_num:
            return None
        return (self.year, self.month_num, self.day)

    def get_hijri(self) -> 'ParsedDate':
        """Convert to Hijri calendar using CSV mapping if available."""
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Hijri")
        ## check if the same clander before converting

    def get_gregorian(self) -> 'ParsedDate':
        """Convert to Gregorian calendar using CSV mapping if available."""
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Julian")

        return ParsedDate(
            day=self.day,
            month=self.month,
            year=self.year,
            weekday=self.weekday,
            era=self.era or 'CE',
            calendar='gregorian',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.5 if self.confidence else 0.5,
            metadata={
                **self.metadata,
                'converted_from': self.calendar,
                'conversion_method': 'placeholder'
            } if self.metadata else {
                'converted_from': self.calendar,
                'conversion_method': 'placeholder'
            }
        )

    def to_iso_format(self) -> str:
        """
        Convert to ISO 8601 format (YYYY-MM-DD) with missing components as ?.

        Returns:
            ISO formatted date string like "2023-03-15" or "2023-??-??" for partial dates
        """

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

    def get_julian(self) -> 'ParsedDate':
        """Convert to Julian calendar using CSV mapping if available."""
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Julian")

    def get_readable(self) -> str:
        """Return a human-readable string representation of the date."""

    def _to_datetime(self) -> Optional[datetime]:
        """Convert to Python datetime object if possible."""


    def _convert_date_via_mapping(self, target_calendar: str) -> Optional['ParsedDate']:
        """
        Convert date using the loaded CSV mappings.

        Args:
            target_calendar: Target calendar system ('gregorian', 'hijri', 'julian')

        Returns:
            ParsedDate in target calendar system or None if conversion not available
        """
        if not self._mappings_loaded:
            return None

        current_cal = self.calendar or 'gregorian'
        date_tuple = self._get_date_tuple()

        if not date_tuple:
            return None

        # Determine mapping key
        mapping_key = None
        target_era = None

        if current_cal == 'gregorian' and target_calendar == 'hijri':
            mapping_key = 'g_to_h'
            target_era = 'AH'
        elif current_cal == 'gregorian' and target_calendar == 'julian':
            mapping_key = 'g_to_j'
            target_era = self.era or 'CE'
        elif current_cal == 'hijri' and target_calendar == 'gregorian':
            mapping_key = 'h_to_g'
            target_era = 'CE'
        elif current_cal == 'hijri' and target_calendar == 'julian':
            mapping_key = 'h_to_j'
            target_era = self.era or 'CE'
        elif current_cal == 'julian' and target_calendar == 'gregorian':
            mapping_key = 'j_to_g'
            target_era = 'CE'
        elif current_cal == 'julian' and target_calendar == 'hijri':
            mapping_key = 'j_to_h'
            target_era = 'AH'
        else:
            return None

        # Look up the conversion
        if mapping_key and date_tuple in self._date_mappings[mapping_key]:
            target_year, target_month, target_day = self._date_mappings[mapping_key][date_tuple]

            return ParsedDate(
                day=target_day,
                month=target_month,
                year=target_year,
                weekday=self.weekday,  # Weekday might need recalculation
                era=target_era,
                calendar=target_calendar,
                raw_text=self.raw_text,
                lang=self.lang,
                precision=self.precision,
                confidence=self.confidence,
                metadata={
                    **self.metadata,
                    'converted_from': current_cal,
                    'conversion_method': 'csv_mapping'
                } if self.metadata else {
                    'converted_from': current_cal,
                    'conversion_method': 'csv_mapping'
                }
            )

        return None
        """Return the most specific precision level available."""
        if self.day: return "day"
        if self.month: return "month"
        if self.year: return "year"
        if self.century: return "century"
        return "unknown"

    def normalize(self) -> 'ParsedDate':
        """Normalize the date components to standard formats."""
        normalized = ParsedDate(
            weekday=self.weekday,
            day=self.day,
            month=normalize_month(self.month, output_format="num"),  # Convert month names to numbers
            year=self.year,
            century=self.century,
            era=self._normalize_era(),
            calendar=self.calendar or "gregorian",
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision or self.get_precision_level(),
            confidence=self.confidence,
            metadata=self.metadata.copy() if self.metadata else {}
        )
        return normalized

    def _normalize_era(self) -> Optional[str]:
        """Normalize era designations to standard format."""
        if not self.era:
            return None

        era_lower = self.era.lower().strip()
        if era_lower in ['bc', 'bce', 'before christ', 'before common era']:
            return 'BCE'
        elif era_lower in ['ad', 'ce', 'anno domini', 'common era']:
            return 'CE'
        return self.era

    def get_hijri(self) -> 'ParsedDate':
        """Convert to Hijri calendar using CSV mapping if available."""
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Hijri")

        # Try CSV mapping first
        csv_result = self._convert_date_via_mapping('hijri')
        if csv_result:
            return csv_result

        # Fallback to placeholder implementation if no CSV mapping
        print("Warning: No CSV mapping available, using placeholder conversion")
        hijri_date = ParsedDate(
            day=self.day,  # This would be converted properly with real algorithm
            month=self.month,  # This would be converted properly with real algorithm
            year=self.year,  # This would be converted properly with real algorithm
            era='AH',  # After Hijra
            calendar='hijri',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.5 if self.confidence else 0.5,  # Lower confidence for fallback
            metadata={
                **self.metadata,
                'converted_from': self.calendar or 'gregorian',
                'conversion_method': 'placeholder'
            } if self.metadata else {
                'converted_from': self.calendar or 'gregorian',
                'conversion_method': 'placeholder'
            }
        )

        return hijri_date

    def get_gregorian(self) -> 'ParsedDate':
        """Convert to Gregorian calendar using CSV mapping if available."""
        if self.calendar == 'gregorian' or not self.calendar:
            return self.normalize()

        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Gregorian")

        # Try CSV mapping first
        csv_result = self._convert_date_via_mapping('gregorian')
        if csv_result:
            return csv_result

        # Fallback implementation
        print("Warning: No CSV mapping available, using placeholder conversion")
        gregorian_date = ParsedDate(
            day=self.day,
            month=self.month,
            year=self.year,
            weekday=self.weekday,
            era=self.era or 'CE',
            calendar='gregorian',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.5 if self.confidence else 0.5,
            metadata={
                **self.metadata,
                'converted_from': self.calendar,
                'conversion_method': 'placeholder'
            } if self.metadata else {
                'converted_from': self.calendar,
                'conversion_method': 'placeholder'
            }
        )

        return gregorian_date

    def get_julian(self) -> 'ParsedDate':
        """Convert to Julian calendar using CSV mapping if available."""
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Julian")

        # Try CSV mapping first
        csv_result = self._convert_date_via_mapping('julian')
        if csv_result:
            return csv_result

        # Fallback implementation
        print("Warning: No CSV mapping available, using placeholder conversion")
        julian_date = ParsedDate(
            day=self.day,  # Would be adjusted for Julian conversion
            month=self.month,
            year=self.year,
            weekday=self.weekday,
            era=self.era or 'CE',
            calendar='julian',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.5 if self.confidence else 0.5,
            metadata={
                **self.metadata,
                'converted_from': self.calendar or 'gregorian',
                'conversion_method': 'placeholder'
            } if self.metadata else {
                'converted_from': self.calendar or 'gregorian',
                'conversion_method': 'placeholder'
            }
        )

        return julian_date

    def get_readable(self) -> str:
        """Return a human-readable string representation of the date."""
        parts = []

        # Add weekday if available
        if self.weekday:
            parts.append(self.weekday)

        # Add day
        if self.day:
            parts.append(str(self.day))

        # Add month
        if self.month:
            if isinstance(self.month, int):
                month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June',
                              'July', 'August', 'September', 'October', 'November', 'December']
                if 1 <= self.month <= 12:
                    parts.append(month_names[self.month])
                else:
                    parts.append(str(self.month))
            else:
                parts.append(str(self.month).title())

        # Add year
        if self.year:
            year_str = str(abs(self.year))  # Remove negative sign for BCE years
            parts.append(year_str)

        # Add era
        if self.era:
            parts.append(self.era)

        # Add century if no specific date
        if self.century and not (self.day and self.month and self.year):
            century_str = f"{self.century} century"
            parts.append(century_str)

        # Add calendar system if not Gregorian
        if self.calendar and self.calendar.lower() != 'gregorian':
            parts.append(f"({self.calendar})")

        if not parts:
            return "Unknown date"

        return " ".join(parts)

    def _to_datetime(self) -> Optional[datetime]:
        """Convert to Python datetime object if possible."""
        if not all([self.day, self.year]) or not normalize_month(self.month, output_format="num"):
            return None

        try:
            # Handle BCE years (negative years)
            year = self.year if self.year > 0 else 1  # datetime doesn't handle negative years
            return datetime(year, normalize_month(self.month, output_format="num"), self.day)
        except ValueError:
            return None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            'weekday': self.weekday,
            'day': self.day,
            'month': self.month,
            'year': self.year,
            'century': self.century,
            'era': self.era,
            'calendar': self.calendar,
            'raw_text': self.raw_text,
            'lang': self.lang,
            'precision': self.precision,
            'confidence': self.confidence,
            'metadata': self.metadata
        }

    def __str__(self) -> str:
        return self.get_readable()

    def __repr__(self) -> str:
        return f"ParsedDate({self.get_readable()}, confidence={self.confidence})"


# Example usage and testing
if __name__ == "__main__":
    # Load date mappings from CSV file
    # ParsedDate.load_date_mappings('date_mappings.csv')

    # Test complete date
    date1 = ParsedDate(
        day=15,
        month="March",
        year=2023,
        era="CE",
        calendar="gregorian",
        raw_text="March 15, 2023",
        confidence=0.95
    )

    print("Original:", date1.get_readable())
    print("Normalized:", date1.normalize().get_readable())
    print("Is complete:", date1.is_complete())

    # Test conversion (will use CSV mapping if loaded)
    try:
        hijri_date = date1.get_hijri()
        print("Hijri conversion:", hijri_date.get_readable())
        print("Conversion method:", hijri_date.metadata.get('conversion_method', 'unknown'))

        julian_date = date1.get_julian()
        print("Julian conversion:", julian_date.get_readable())
    except ValueError as e:
        print(f"Conversion error: {e}")

    # Test partial date
    date2 = ParsedDate(
        month=6,
        year=1066,
        era="CE",
        raw_text="June 1066"
    )

    print("\nPartial date:", date2.get_readable())
    print("Is partial:", date2.is_partial())
    print("Precision:", date2.get_precision_level())

    # Test century date
    date3 = ParsedDate(
        century="21st",
        raw_text="21st century"
    )

    print("\nCentury date:", date3.get_readable())

    # Test BCE date
    date4 = ParsedDate(
        day=15,
        month="March",
        year=-44,
        era="BCE",
        raw_text="March 15, 44 BCE"
    )

    print("\nBCE date:", date4.get_readable())


def create_sample_csv_mappings(filename: str = 'sample_date_mappings.csv'):
    """
    Create a sample CSV file with date mappings for testing.
    This is just example data - real mappings would come from astronomical calculations.
    """
    sample_data = [
        # g_year, g_month, g_day, h_year, h_month, h_day, j_year, j_month, j_day
        ['g_year', 'g_month', 'g_day', 'h_year', 'h_month', 'h_day', 'j_year', 'j_month', 'j_day'],
        [2023, 1, 1, 1444, 5, 9, 2022, 12, 19],
        [2023, 1, 2, 1444, 5, 10, 2022, 12, 20],
        [2023, 3, 15, 1444, 8, 23, 2023, 3, 2],
        [2023, 6, 21, 1444, 12, 2, 2023, 6, 8],
        [2023, 12, 25, 1445, 6, 12, 2023, 12, 12],
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

    print(f"Created sample CSV mapping file: {filename}")
    return filename




















def to_iso_format(self) -> str:
        """
        Convert to ISO 8601 format (YYYY-MM-DD) with missing components as ?.

        Returns:
            ISO formatted date string like "2023-03-15" or "2023-??-??" for partial dates
        """

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







import re
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union


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
        self.month_num = None
        if self.month is not None:
            if isinstance(self.month, int):
                self.month_num = self.month
            else:
                # Try to convert month name to number
                month_str = str(self.month).lower()
                for num, name in month_names_full.items():
                    if month_str in [name.lower(), month_names_abbr[num].lower()]:
                        self.month_num = num
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
        if self.month_num is not None:
            replacements['%m'] = f"{self.month_num:02d}"
            replacements['%n'] = str(self.month_num)
            replacements['%b'] = month_names_abbr[self.month_num]
            replacements['%B'] = month_names_full[self.month_num]
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
    era: Optional[str] = None
    calendar: Optional[str] = None
    raw_text: Optional[str] = None
    lang: Optional[str] = None

    def is_complete(self) -> bool:
        """Check if date has minimum required components (day, month, year)."""
        return all([self.day, self.month, self.year, self.era])

    def is_partial(self) -> bool:
        """Check if date has some but not all components."""
        components = [self.day, self.month, self.year, self.era]
        return any(components) and not all(components)

    def normalize(self) -> ParsedDate:
        pass

    def get_hijri(self) -> ParsedDate:
        pass

    def get_gregorian(self) -> ParsedDate:
        pass

    def get_julian(self) -> ParsedDate:
        pass

    def get_readable(self) -> str:
        pass

    def strftime(self, format_string: str) -> str:
        pass




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