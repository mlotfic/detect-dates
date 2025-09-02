from dataclasses import dataclass
import re
from typing import Pattern
from abc import ABC, abstractmethod


@dataclass
class BasePatterns:
    """Base patterns from get_date_patterns function"""
    day_indicator_pattern: str
    month_indicator_pattern: str
    year_indicator_pattern: str
    century_indicator_pattern: str
    separator_pattern: str
    range_connector_pattern: str
    range_starter_pattern: str
    hijri_era_pattern: str
    gregorian_era_pattern: str
    julian_era_pattern: str
    day_pattern: str
    hijri_month_pattern: str
    gregorian_month_pattern: str
    julian_month_pattern: str


@dataclass
class NumericPatterns:
    """Basic numeric patterns for date components"""
    year_num_pattern: str = r"(\d{1,4})"
    month_num_pattern: str = r"(\d{1,2})"
    day_num_pattern: str = r"(\d{1,2})"
    century_num_pattern: str = r"(\d{1,2})"

    def __post_init__(self):
        # Validate patterns compile correctly
        for field_name, pattern in self.__dict__.items():
            try:
                re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern in {field_name}: {e}")


@dataclass
class CompositeNumericPatterns:
    """Composite numeric patterns built from basic patterns"""
    base_patterns: BasePatterns
    numeric_patterns: NumericPatterns

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

        # Validate all patterns
        for pattern_name in ['m_yr_num_pattern', 'd_m_num_pattern', 'd_m_yr_num_pattern']:
            pattern = getattr(self, pattern_name)
            try:
                re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern in {pattern_name}: {e}")


@dataclass
class CalendarYearPatterns:
    """Year patterns for different calendar systems"""
    base_patterns: BasePatterns
    numeric_patterns: NumericPatterns

    def __post_init__(self):
        # Hijri year patterns
        self.hijri_y_pattern = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_era_pattern}"
        )
        self.hijri_y_pattern_s = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.hijri_era_pattern})?"
        )

        # Gregorian year patterns
        self.gregorian_y_pattern = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_era_pattern}"
        )
        self.gregorian_y_pattern_s = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.gregorian_era_pattern})?"
        )

        # julian year patterns
        self.julian_y_pattern = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_era_pattern}"
        )
        self.julian_y_pattern_s = (
            f"{self.numeric_patterns.year_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.julian_era_pattern})?"
        )

        # Validate all patterns
        for attr_name in dir(self):
            if attr_name.endswith('_pattern') or attr_name.endswith('_pattern_s'):
                pattern = getattr(self, attr_name)
                try:
                    re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern in {attr_name}: {e}")


@dataclass
class CalendarMonthYearPatterns:
    """Month-Year patterns for different calendar systems"""
    base_patterns: BasePatterns
    composite_patterns: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        # Hijri month-year patterns
        self.hijri_m_y_pattern_num = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_era_pattern}"
        )
        self.hijri_m_y_pattern_num_s = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.hijri_era_pattern})?"
        )
        self.hijri_m_y_pattern_name = (
            f"{self.base_patterns.hijri_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.hijri_y_pattern_s}"
        )

        # Gregorian month-year patterns
        self.gregorian_m_y_pattern_num = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_era_pattern}"
        )
        self.gregorian_m_y_pattern_num_s = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.gregorian_era_pattern})?"
        )
        self.gregorian_m_y_pattern_name = (
            f"{self.base_patterns.gregorian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.gregorian_y_pattern_s}"
        )

        # julian month-year patterns
        self.julian_m_y_pattern_num = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_era_pattern}"
        )
        self.julian_m_y_pattern_num_s = (
            f"{self.composite_patterns.m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.julian_era_pattern})?"
        )
        self.julian_m_y_pattern_name = (
            f"{self.base_patterns.julian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.julian_y_pattern_s}"
        )

        # Combined patterns
        self.hijri_m_y_pattern = f"{self.hijri_m_y_pattern_num}|{self.hijri_m_y_pattern_name}"
        self.gregorian_m_y_pattern = f"{self.gregorian_m_y_pattern_num}|{self.gregorian_m_y_pattern_name}"
        self.julian_m_y_pattern = f"{self.julian_m_y_pattern_num}|{self.julian_m_y_pattern_name}"

        self.hijri_m_y_pattern_s = f"{self.hijri_m_y_pattern_num_s}|{self.hijri_m_y_pattern_name}"
        self.gregorian_m_y_pattern_s = f"{self.gregorian_m_y_pattern_num_s}|{self.gregorian_m_y_pattern_name}"
        self.julian_m_y_pattern_s = f"{self.julian_m_y_pattern_num_s}|{self.julian_m_y_pattern_name}"

        # Validate all patterns
        self._validate_patterns()

    def _validate_patterns(self):
        for attr_name in dir(self):
            if attr_name.endswith('_pattern') or attr_name.endswith('_pattern_s'):
                pattern = getattr(self, attr_name)
                try:
                    re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern in {attr_name}: {e}")


@dataclass
class CalendarDayMonthYearPatterns:
    """Day-Month-Year patterns for different calendar systems"""
    base_patterns: BasePatterns
    numeric_patterns: NumericPatterns
    composite_patterns: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        # Hijri day-month-year patterns
        self.hijri_d_m_y_pattern_num = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_era_pattern}"
        )
        self.hijri_d_m_y_pattern_num_s = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.hijri_era_pattern})?"
        )
        self.hijri_d_m_y_pattern_name = (
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.hijri_y_pattern_s}"
        )

        # Gregorian day-month-year patterns
        self.gregorian_d_m_y_pattern_num = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_era_pattern}"
        )
        self.gregorian_d_m_y_pattern_num_s = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.gregorian_era_pattern})?"
        )
        self.gregorian_d_m_y_pattern_name = (
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.gregorian_y_pattern_s}"
        )

        # julian day-month-year patterns
        self.julian_d_m_y_pattern_num = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_era_pattern}"
        )
        self.julian_d_m_y_pattern_num_s = (
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.julian_era_pattern})?"
        )
        self.julian_d_m_y_pattern_name = (
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.julian_y_pattern_s}"
        )

        # Combined patterns
        self.hijri_d_m_y_pattern = f"{self.hijri_d_m_y_pattern_num}|{self.hijri_d_m_y_pattern_name}"
        self.gregorian_d_m_y_pattern = f"{self.gregorian_d_m_y_pattern_num}|{self.gregorian_d_m_y_pattern_name}"
        self.julian_d_m_y_pattern = f"{self.julian_d_m_y_pattern_num}|{self.julian_d_m_y_pattern_name}"

        self.hijri_d_m_y_pattern_s = f"{self.hijri_d_m_y_pattern_num_s}|{self.hijri_d_m_y_pattern_name}"
        self.gregorian_d_m_y_pattern_s = f"{self.gregorian_d_m_y_pattern_num_s}|{self.gregorian_d_m_y_pattern_name}"
        self.julian_d_m_y_pattern_s = f"{self.julian_d_m_y_pattern_num_s}|{self.julian_d_m_y_pattern_name}"

        # Validate all patterns
        self._validate_patterns()

    def _validate_patterns(self):
        for attr_name in dir(self):
            if attr_name.endswith('_pattern') or attr_name.endswith('_pattern_s'):
                pattern = getattr(self, attr_name)
                try:
                    re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern in {attr_name}: {e}")


@dataclass
class NaturalLanguagePatterns:
    """Natural language date patterns with day names"""
    base_patterns: BasePatterns
    numeric_patterns: NumericPatterns
    composite_patterns: CompositeNumericPatterns
    year_patterns: CalendarYearPatterns

    def __post_init__(self):
        # Hijri natural patterns
        self.natural_hijri_d_m_y_pattern_num = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_era_pattern}"
        )
        self.natural_hijri_d_m_y_pattern_num_s = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.hijri_era_pattern})?"
        )
        self.natural_hijri_d_m_y_pattern_name = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.hijri_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.hijri_y_pattern_s}"
        )

        # Gregorian natural patterns
        self.natural_gregorian_d_m_y_pattern_num = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_era_pattern}"
        )
        self.natural_gregorian_d_m_y_pattern_num_s = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.gregorian_era_pattern})?"
        )
        self.natural_gregorian_d_m_y_pattern_name = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.gregorian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.gregorian_y_pattern_s}"
        )

        # julian natural patterns
        self.natural_julian_d_m_y_pattern_num = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_era_pattern}"
        )
        self.natural_julian_d_m_y_pattern_num_s = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.composite_patterns.d_m_yr_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"(?:{self.base_patterns.julian_era_pattern})?"
        )
        self.natural_julian_d_m_y_pattern_name = (
            f"{self.base_patterns.day_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.numeric_patterns.day_num_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.base_patterns.julian_month_pattern}\\s*"
            f"{self.base_patterns.separator_pattern}?\\s*"
            f"{self.year_patterns.julian_y_pattern_s}"
        )

        # Combined natural patterns
        self.natural_hijri_pattern = f"{self.natural_hijri_d_m_y_pattern_num}|{self.natural_hijri_d_m_y_pattern_name}"
        self.natural_gregorian_pattern = f"{self.natural_gregorian_d_m_y_pattern_num}|{self.natural_gregorian_d_m_y_pattern_name}"
        self.natural_julian_pattern = f"{self.natural_julian_d_m_y_pattern_num}|{self.natural_julian_d_m_y_pattern_name}"

        self.natural_hijri_pattern_s = f"{self.natural_hijri_d_m_y_pattern_num_s}|{self.natural_hijri_d_m_y_pattern_name}"
        self.natural_gregorian_pattern_s = f"({self.natural_gregorian_d_m_y_pattern_num_s}|{self.natural_gregorian_d_m_y_pattern_name})"
        self.natural_julian_pattern_s = f"{self.natural_julian_d_m_y_pattern_num_s}|{self.natural_julian_d_m_y_pattern_name}"

        # Validate all patterns
        self._validate_patterns()

    def _validate_patterns(self):
        for attr_name in dir(self):
            if attr_name.endswith('_pattern') or attr_name.endswith('_pattern_s'):
                pattern = getattr(self, attr_name)
                try:
                    re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern in {attr_name}: {e}")


@dataclass
class CenturyPatterns:
    """Century-related patterns"""
    base_patterns: BasePatterns
    numeric_words_pattern_ar: str  # This would need to be defined elsewhere

    def __post_init__(self):
        self.century_pattern = f"({self.numeric_words_pattern_ar})"
        self.century_pattern_s = (
            f"({self.numeric_words_pattern_ar})\\s*"
            f"{self.base_patterns.century_indicator_pattern}"
        )

        # Validate patterns
        try:
            re.compile(self.century_pattern, flags=re.IGNORECASE | re.UNICODE)
            re.compile(self.century_pattern_s, flags=re.IGNORECASE | re.UNICODE)
        except re.error as e:
           raise ValueError(f"Invalid regex pattern in century patterns: {e}")                                                                                                                                                                                                                         