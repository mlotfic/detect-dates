
"""
Date Pattern Recognition Module

A comprehensive module for recognizing date patterns across multiple calendar systems
including Hijri (Islamic), Gregorian (Western), and Jalali (Persian) calendars.
This module provides structured dataclasses for building complex regex patterns
to match various date formats in natural language text.

:author: m.lotfi
:version: 1.0.0
:created: 2023-10-01
:license: MIT
"""

import re
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union

# Base Pattern Classes
# =================================
# These classes define the base patterns used across different date formats.


@dataclass
class BasePatterns:
    r"""
    Base regex patterns for fundamental date components.

    This class contains the core regex patterns that are shared across all
    calendar systems in the date detection framework. These patterns form
    the foundation for more specialized date parsing functionality.

    Parameters
    ----------
    weekday : str
        Regex pattern matching weekday names in various languages
        and formats (e.g., "Monday", "Mon", "الاثنين")
    numeric_words : str
        Regex pattern matching written numbers
        (e.g., "first", "second", "الأول", "دوم")

    Examples
    --------
    >>> patterns = BasePatterns(
    ...     weekday=r"(?:Monday|Tuesday|الاثنين|الثلاثاء)",
    ...     numeric_words=r"(?:first|second|الأول|الثاني)"
    ... )

    See Also
    --------
    MonthPatterns : Calendar-specific month patterns
    EraPatterns : Era and calendar system indicators
    """
    weekday: str
    numeric_words: str

    def __post_init__(self):
        """
        Compile regex patterns to ensure they are valid.
        
        Raises
        ------
        ValueError
            If any regex pattern is invalid or cannot be compiled
        """
        # Validate each pattern by attempting to compile it
        for field_name, pattern in [
            ("weekday", self.weekday),
            ("numeric_words", self.numeric_words)
        ]:
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern for {field_name}: {e}")


@dataclass
class MonthPatterns:
    r"""
    Regex patterns for month names across different calendar systems.

    Provides comprehensive month name matching for the three major calendar
    systems supported by the date detection framework. Each pattern handles
    multiple languages and abbreviated forms.

    Parameters
    ----------
    hijri : str
        Islamic calendar months pattern. Matches Arabic month names
        like "محرم" (Muharram), "صفر" (Safar), "ربيع الأول" (Rabi' al-awwal)
    gregorian : str
        Western calendar months pattern. Matches English month
        names and abbreviations like "January", "Jan", "February", "Feb"
    Jalali : str
        Persian solar calendar months pattern. Matches Farsi month
        names like "فروردین" (Farvardin), "اردیبهشت" (Ordibehesht)

    Examples
    --------
    >>> months = MonthPatterns(
    ...     hijri=r"(?:محرم|صفر|ربیع‌الاول)",
    ...     gregorian=r"(?:January|Jan|February|Feb)",
    ...     Jalali=r"(?:فروردین|اردیبهشت|خرداد)"
    ... )

    Notes
    -----
    All patterns are case-insensitive and handle common variations
    and transliterations of month names.
    """
    hijri: str
    gregorian: str
    Jalali: str

    def __post_init__(self):
        """
        Compile regex patterns to ensure they are valid.
        
        Raises
        ------
        ValueError
            If any regex pattern is invalid or cannot be compiled
        """
        # Validate each calendar system's month pattern
        for field_name, pattern in [
            ("hijri", self.hijri),
            ("gregorian", self.gregorian),
            ("Jalali", self.Jalali)
        ]:
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern for {field_name}: {e}")


@dataclass
class EraPatterns:
    r"""
    Regex patterns for calendar era indicators and system identifiers.

    Era patterns help distinguish between different calendar systems and
    historical periods. These patterns are essential for accurate date
    interpretation in multi-calendar environments.

    Parameters
    ----------
    hijri : str
        Islamic calendar era indicators. Matches "AH" (Anno Hegirae),
        "هـ" (Hijri marker), and variations like "A.H.", "ه.ق"
    gregorian : str
        Western calendar era indicators. Matches "AD", "CE",
        "BC", "BCE" and their variations with optional periods and spacing
    Jalali : str
        Persian solar calendar indicators. Matches "ش.ه"
        (Solar Hijri), "هجری شمسی" and related Persian era markers

    Examples
    --------
    >>> eras = EraPatterns(
    ...     hijri=r"(?:AH|A\.H\.|هـ|ه\.ق)",
    ...     gregorian=r"(?:AD|A\.D\.|CE|BC|BCE)",
    ...     Jalali=r"(?:ش\.ه|هجری\s*شمسی)"
    ... )

    Warnings
    --------
    Era detection is crucial for disambiguation when dates could
    belong to multiple calendar systems.
    """
    hijri: str
    gregorian: str
    Jalali: str

    def __post_init__(self):
        """
        Compile regex patterns to ensure they are valid.
        
        Raises
        ------
        ValueError
            If any regex pattern is invalid or cannot be compiled
        """
        # Validate each era pattern for compilation errors
        for field_name, pattern in [
            ("hijri", self.hijri),
            ("gregorian", self.gregorian),
            ("Jalali", self.Jalali)
        ]:
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern for {field_name}: {e}")


@dataclass
class IndicatorPatterns:
    r"""
    Comprehensive patterns for date component indicators and structural elements.

    This class provides regex patterns for identifying and parsing various
    structural elements within date expressions, including component indicators,
    separators, and range connectors across multiple languages.

    Parameters
    ----------
    day : str
        Day component indicators like "day", "يوم", "روز", including
        ordinal suffixes and abbreviated forms
    month : str
        Month component indicators such as "month", "شهر", "ماه",
        with common abbreviations and linguistic variations
    year : str
        Year component indicators including "year", "سال", "عام",
        and related temporal markers
    century : str
        Century indicators like "century", "قرن", "سده",
        supporting ordinal and cardinal forms
    separator : str
        Date separator patterns matching "/", "-", ".",
        whitespace, and Unicode separators
    range_connector : str
        Range connecting patterns like "to", "until",
        "تا", "-", "إلى" for date ranges
    range_starter : str
        Range starting indicators such as "from", "since",
        "من", "از" that begin date range expressions
    parentheses_start : str, optional
        Opening parenthetical markers for date ranges
        or additional date information, by default r'(?:[\(\[])'
    parentheses_end : str, optional
        Closing parenthetical markers, by default r'(?:[\)\]])'

    Examples
    --------
    >>> indicators = IndicatorPatterns(
    ...     day=r"(?:day|يوم|روز|يوماً)",
    ...     month=r"(?:month|شهر|ماه|شهری)",
    ...     year=r"(?:year|سال|عام|سنة)",
    ...     century=r"(?:century|قرن|سده)",
    ...     separator=r"[/\\-\\.\\s]+",
    ...     range_connector=r"(?:to|until|تا|إلى|-)",
    ...     range_starter=r"(?:from|since|من|از)"
    ... )

    See Also
    --------
    NumericPatterns : Numeric component patterns
    BasePatterns : Foundation pattern class
    """
    day: str
    month: str
    year: str
    century: str
    separator: str
    range_connector: str
    range_starter: str
    parentheses_start: str = r'(?:[\(\[])'
    parentheses_end: str = r'(?:[\)\]])'

    def __post_init__(self):
        """
        Compile regex patterns to ensure they are valid.
        
        Raises
        ------
        ValueError
            If any regex pattern is invalid or cannot be compiled
        """
        # Validate all indicator patterns including defaults
        patterns_to_validate = [
            ("day", self.day),
            ("month", self.month),
            ("year", self.year),
            ("century", self.century),
            ("separator", self.separator),
            ("range_connector", self.range_connector),
            ("range_starter", self.range_starter),
            ("parentheses_start", self.parentheses_start),
            ("parentheses_end", self.parentheses_end)
        ]
        
        for field_name, pattern in patterns_to_validate:
            try:
                re.compile(pattern, re.IGNORECASE | re.UNICODE)
            except re.error as e:
                raise ValueError(f"Invalid regex pattern for {field_name}: {e}")


@dataclass
class NumericPatterns:
    r"""
    Regex capture patterns for numeric date components.

    Defines standardized capture groups for extracting numeric values
    from date strings. All patterns use capturing groups to facilitate
    easy extraction of matched values.

    Parameters
    ----------
    year : str, optional
        Year capture pattern matching 1-4 digits. Handles years
        from single digits (e.g., "5" for 2005) to full 4-digit years,
        by default r"(\d{1,4})"
    month : str, optional
        Month number capture pattern for values 1-12.
        Supports both single and double-digit months,
        by default r"(\d{1,2})"
    day : str, optional
        Day number capture pattern for values 1-31.
        Handles single and double-digit day values,
        by default r"(\d{1,2})"
    century : str, optional
        Century number capture pattern for values 1-99.
        Supports ordinal century references,
        by default r"(\d{1,2})"

    Examples
    --------
    >>> # Using default patterns
    >>> numeric = NumericPatterns()
    
    >>> # Custom patterns with validation
    >>> custom_numeric = NumericPatterns(
    ...     year=r"(\d{4})",  # Only 4-digit years
    ...     month=r"(0?[1-9]|1[0-2])",  # Months 1-12 with validation
    ...     day=r"(0?[1-9]|[12]\d|3[01])"  # Days 1-31 with validation
    ... )

    Notes
    -----
    All patterns use capturing groups ``()`` to enable extraction
    of matched numeric values for further processing.

    Warnings
    --------
    These patterns capture raw numeric strings without validation.
    Additional logic should verify that captured values represent
    valid dates (e.g., month ≤ 12, day ≤ 31).
    """
    year: str = r"(\d{1,4})"
    month: str = r"(\d{1,2})"
    day: str = r"(\d{1,2})"
    century: str = r"(\d{1,2})"

    def __post_init__(self):
        """
        Validate regex patterns after initialization.
        
        Raises
        ------
        ValueError
            If any regex pattern is invalid or cannot be compiled
        """
        # Validate all numeric patterns for proper regex syntax
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