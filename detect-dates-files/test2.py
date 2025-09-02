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


# [ ] ============================================================
# Numeric patterns for year, month, day, and century
# year_num_pattern = NumericPatterns.year
# month_num_pattern = NumericPatterns.month
# day_num_pattern = NumericPatterns.day
# century_num_pattern= NumericPatterns.century


month_num_pattern NumericPatterns.month
day_num_pattern = NumericPatterns.day
year_num_pattern = NumericPatterns.year
separator_pattern = BasePatterns.separator
century_num_pattern = NumericPatterns.century


m_yr_num_pattern = rf"{month_num_pattern}\s*{separator_pattern}?\s*{year_num_pattern}"
d_m_num_pattern = rf"{day_num_pattern}\s*{separator_pattern}?\s*{month_num_pattern}"
d_m_yr_num_pattern = rf"{day_num_pattern}\s*{separator_pattern}?\s*{month_num_pattern}\s*{separator_pattern}?\s*{year_num_pattern}"

@dataclass
class CompositeNumericPatterns:
    """Composite numeric patterns built from basic patterns"""
    base_patterns: BasePatterns
    numeric_patterns: NumericPatterns
    month_patterns: MonthPatterns
    era_patterns: EraPatterns
    indicator_patterns: IndicatorPatterns
    numeric_patterns: NumericPatterns

    """Composite patterns combining basic numeric patterns"""
    def __post_init__(self):
        self.m_yr_num_pattern = (
            f"{self.numeric_patterns.month_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.year_num_pattern}"
        )

        self.d_m_num_pattern = (
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.month_num_pattern}"
        )

        self.d_m_yr_num_pattern = (
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.month_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.year_num_pattern}"
        )

@dataclass
class CompositeNumericPatterns:
    """Composite patterns combining basic numeric patterns"""
    base_patterns: BasePatterns
    numeric: NumericPatterns

    def __post_init__(self):
        sep = self.base_patterns.separator

        # Month/Year pattern (MM/YYYY)
        self.month_year = rf"{self.numeric.month}\s*{sep}?\s*{self.numeric.year}"

        # Day/Month pattern (DD/MM)
        self.day_month = rf"{self.numeric.day}\s*{sep}?\s*{self.numeric.month}"

        # Day/Month/Year pattern (DD/MM/YYYY)
        self.day_month_year = rf"{self.numeric.day}\s*{sep}?\s*{self.numeric.month}\s*{sep}?\s*{self.numeric.year}"

        # Validate all patterns
        for pattern_name in ["month_year", "day_month", "day_month_year"]:
            pattern = getattr(self, pattern_name)
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid composite pattern {pattern_name}: {e}")

@dataclass
class CalendarYearPatterns:
    """Year patterns for different calendar systems"""
    base_patterns: BasePatterns
    numeric: NumericPatterns

    def __post_init__(self):
        sep = self.base_patterns.separator

        # Patterns with required era markers
        self.hijri_with_era = rf"{self.numeric.year}\s*{sep}?\s*{self.base_patterns.hijri_era}"
        self.gregorian_with_era = rf"{self.numeric.year}\s*{sep}?\s*{self.base_patterns.gregorian_era}"
        self.julian_with_era = rf"{self.numeric.year}\s*{sep}?\s*{self.base_patterns.julian_era}"

        # Patterns with optional era markers (for range starts)
        self.hijri_optional_era = rf"{self.numeric.year}\s*{sep}?\s*(?:{self.base_patterns.hijri_era})?"
        self.gregorian_optional_era = rf"{self.numeric.year}\s*{sep}?\s*(?:{self.base_patterns.gregorian_era})?"
        self.julian_optional_era = rf"{self.numeric.year}\s*{sep}?\s*(?:{self.base_patterns.julian_era})?"

@dataclass
class CalendarMonthYearPatterns:
    """Month/Year patterns for different calendar systems"""
    base_patterns: BasePatterns
    composite: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        sep = self.base_patterns.separator

        # Numeric month/year patterns with required era
        self.hijri_numeric_with_era = rf"{self.composite.month_year}\s*{sep}?\s*{self.base_patterns.hijri_era}"
        self.gregorian_numeric_with_era = rf"{self.composite.month_year}\s*{sep}?\s*{self.base_patterns.gregorian_era}"
        self.julian_numeric_with_era = rf"{self.composite.month_year}\s*{sep}?\s*{self.base_patterns.julian_era}"

        # Numeric month/year patterns with optional era
        self.hijri_numeric_optional_era = rf"{self.composite.month_year}\s*{sep}?\s*(?:{self.base_patterns.hijri_era})?"
        self.gregorian_numeric_optional_era = rf"{self.composite.month_year}\s*{sep}?\s*(?:{self.base_patterns.gregorian_era})?"
        self.julian_numeric_optional_era = rf"{self.composite.month_year}\s*{sep}?\s*(?:{self.base_patterns.julian_era})?"

        # Named month/year patterns
        self.hijri_named = rf"{self.base_patterns.hijri_months}\s*{sep}?\s*{self.year_patterns.hijri_optional_era}"
        self.gregorian_named = rf"{self.base_patterns.gregorian_months}\s*{sep}?\s*{self.year_patterns.gregorian_optional_era}"
        self.julian_named = rf"{self.base_patterns.julian_months}\s*{sep}?\s*{self.year_patterns.julian_optional_era}"

        # Combined patterns (numeric OR named)
        self.hijri_combined = rf"{self.hijri_numeric_with_era}|{self.hijri_named}"
        self.gregorian_combined = rf"{self.gregorian_numeric_with_era}|{self.gregorian_named}"
        self.julian_combined = rf"{self.julian_numeric_with_era}|{self.julian_named}"

        # Combined patterns with optional era (for range starts)
        self.hijri_combined_optional = rf"{self.hijri_numeric_optional_era}|{self.hijri_named}"
        self.gregorian_combined_optional = rf"{self.gregorian_numeric_optional_era}|{self.gregorian_named}"
        self.julian_combined_optional = rf"{self.julian_numeric_optional_era}|{self.julian_named}"

@dataclass
class CalendarFullDatePatterns:
    """Full date patterns (Day/Month/Year) for different calendar systems"""
    base_patterns: BasePatterns
    composite: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        sep = self.base_patterns.separator

        # Numeric full date patterns with required era
        self.hijri_numeric_with_era = rf"{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.hijri_era}"
        self.gregorian_numeric_with_era = rf"{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.gregorian_era}"
        self.julian_numeric_with_era = rf"{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.julian_era}"

        # Numeric full date patterns with optional era
        self.hijri_numeric_optional_era = rf"{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.hijri_era})?"
        self.gregorian_numeric_optional_era = rf"{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.gregorian_era})?"
        self.julian_numeric_optional_era = rf"{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.julian_era})?"

        # Named month full date patterns
        day_num = self.composite.numeric.day
        self.hijri_named = rf"{day_num}\s*{sep}?\s*{self.base_patterns.hijri_months}\s*{sep}?\s*{self.year_patterns.hijri_optional_era}"
        self.gregorian_named = rf"{day_num}\s*{sep}?\s*{self.base_patterns.gregorian_months}\s*{sep}?\s*{self.year_patterns.gregorian_optional_era}"
        self.julian_named = rf"{day_num}\s*{sep}?\s*{self.base_patterns.julian_months}\s*{sep}?\s*{self.year_patterns.julian_optional_era}"

        # Combined patterns (numeric OR named)
        self.hijri_combined = rf"{self.hijri_numeric_with_era}|{self.hijri_named}"
        self.gregorian_combined = rf"{self.gregorian_numeric_with_era}|{self.gregorian_named}"
        self.julian_combined = rf"{self.julian_numeric_with_era}|{self.julian_named}"

        # Combined patterns with optional era (for range starts)
        self.hijri_combined_optional = rf"{self.hijri_numeric_optional_era}|{self.hijri_named}"
        self.gregorian_combined_optional = rf"{self.gregorian_numeric_optional_era}|{self.gregorian_named}"
        self.julian_combined_optional = rf"{self.julian_numeric_optional_era}|{self.julian_named}"

@dataclass
class NaturalLanguageDatePatterns:
    """Natural language date patterns (e.g., 'يوم الأحد 15 رمضان 1445 هـ')"""
    base_patterns: BasePatterns
    composite: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        sep = self.base_patterns.separator
        day_names = self.base_patterns.day_names

        # Natural language patterns with numeric dates and required era
        self.hijri_numeric_with_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.hijri_era}"
        self.gregorian_numeric_with_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.gregorian_era}"
        self.julian_numeric_with_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*{self.base_patterns.julian_era}"

        # Natural language patterns with numeric dates and optional era
        self.hijri_numeric_optional_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.hijri_era})?"
        self.gregorian_numeric_optional_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.gregorian_era})?"
        self.julian_numeric_optional_era = rf"{day_names}\s*{sep}?\s*{self.composite.day_month_year}\s*{sep}?\s*(?:{self.base_patterns.julian_era})?"

        # Natural language patterns with named months
        day_num = self.composite.numeric.day
        self.hijri_named = rf"{day_names}\s*{sep}?\s*{day_num}\s*{sep}?\s*{self.base_patterns.hijri_months}\s*{sep}?\s*{self.year_patterns.hijri_optional_era}"
        self.gregorian_named = rf"{day_names}\s*{sep}?\s*{day_num}\s*{sep}?\s*{self.base_patterns.gregorian_months}\s*{sep}?\s*{self.year_patterns.gregorian_optional_era}"
        self.julian_named = rf"{day_names}\s*{sep}?\s*{day_num}\s*{sep}?\s*{self.base_patterns.julian_months}\s*{sep}?\s*{self.year_patterns.julian_optional_era}"

        # Combined natural language patterns
        self.hijri_combined = rf"{self.hijri_numeric_with_era}|{self.hijri_named}"
        self.gregorian_combined = rf"{self.gregorian_numeric_with_era}|{self.gregorian_named}"
        self.julian_combined = rf"{self.julian_numeric_with_era}|{self.julian_named}"

        # Combined patterns with optional era (for range starts)
        self.hijri_combined_optional = rf"{self.hijri_numeric_optional_era}|{self.hijri_named}"
        self.gregorian_combined_optional = rf"({self.gregorian_numeric_optional_era}|{self.gregorian_named})"
        self.julian_combined_optional = rf"{self.julian_numeric_optional_era}|{self.julian_named}"

@dataclass
class CenturyPatterns:
    """Century-related patterns"""
    base_patterns: BasePatterns

    def __post_init__(self):
        # Century pattern using Arabic numeric words
        self.century = rf"({self.base_patterns.numeric_words_ar})"

        # Century pattern with indicator (for range starts)
        self.century_with_indicator = rf"({self.base_patterns.numeric_words_ar})\s*{self.base_patterns.century_indicator}"

@dataclass
class ArabicDatePatternCollection:
    """Complete collection of Arabic date patterns for all calendar systems"""

    def __init__(self, base_patterns: BasePatterns):
        self.base_patterns = base_patterns
        self.numeric = NumericPatterns()
        self.composite = CompositeNumericPatterns(base_patterns, self.numeric)
        self.years = CalendarYearPatterns(base_patterns, self.numeric)
        self.month_years = CalendarMonthYearPatterns(base_patterns, self.composite, self.years)
        self.full_dates = CalendarFullDatePatterns(base_patterns, self.composite, self.years)
        self.natural_language = NaturalLanguageDatePatterns(base_patterns, self.composite, self.years)
        self.centuries = CenturyPatterns(base_patterns)

    def get_compiled_pattern(self, pattern_string: str) -> Pattern[str]:
        """Compile a pattern string into a regex Pattern object"""
        return re.compile(pattern_string, re.IGNORECASE | re.UNICODE)

    def validate_all_patterns(self) -> bool:
        """Validate that all patterns compile successfully"""
        pattern_collections = [
            self.years, self.month_years, self.full_dates,
            self.natural_language, self.centuries
        ]

        for collection in pattern_collections:
            for attr_name in dir(collection):
                if not attr_name.startswith('_') and attr_name not in ['base_patterns', 'composite', 'numeric', 'year_patterns']:
                    pattern = getattr(collection, attr_name)
                    if isinstance(pattern, str):
                        try:
                            re.compile(pattern, re.IGNORECASE | re.UNICODE)
                        except re.error as e:
                            print(f"Invalid pattern {attr_name}: {e}")
                            return False
        return True

# Example usage:
"""
# Initialize with your base patterns
base_patterns = BasePatterns(
    day_indicator="يوم",
    month_indicator="شهر",
    year_indicator="عام",
    century_indicator="قرن",
    separator=r"[/\-\s]",
    range_connector="إلى",
    range_starter="من",
    hijri_era="هـ",
    gregorian_era="م",
    julian_era="شمسي",
    day_names=r"(الأحد|الإثنين|الثلاثاء|الأربعاء|الخميس|الجمعة|السبت)",
    hijri_months=r"(محرم|صفر|ربيع الأول|...)",  # Add all Hijri months
    gregorian_months=r"(يناير|فبراير|مارس|...)",  # Add all Gregorian months
    julian_months=r"(فروردين|أرديبهشت|...)",  # Add all julian months
    numeric_words_ar=r"(الأول|الثاني|الثالث|...)"  # Add all Arabic numeric words
)

# Create the pattern collection
patterns = ArabicDatePatternCollection(base_patterns)

# Use specific patterns
hijri_year_pattern = patterns.get_compiled_pattern(patterns.years.hijri_with_era)
gregorian_full_date = patterns.get_compiled_pattern(patterns.full_dates.gregorian_combined)

# Validate all patterns
if patterns.validate_all_patterns():
    print("All patterns are valid!")
""                                                                                                                                                                                                                                                           