#!/usr/bin/env python3*-

"""
Date Pattern Recognition Module
===============================

A comprehensive module for recognizing date patterns across multiple calendar systems
including Hijri (Islamic), Gregorian (Western), and julian (Persian) calendars.
This module provides structured dataclasses for building complex regex patterns
to match various date formats in natural language text.

This module defines various dataclasses for date patterns used in the date detection module.

.. moduleauthor:: m.lotfi
.. versionadded:: 1.0.0
.. versionchanged:: 1.0.0
   Initial implementation with multi-calendar support

Example:
    Basic usage of composite patterns::

        from date_patterns import CompositeYearPatterns

        # Initialize patterns
        patterns = CompositeYearPatterns(year_patterns, indicator_patterns)

        # Access Hijri patterns
        hijri_mixed = patterns.hijri['mixed']

Note:
    This module requires the base_dataclass and mixin_dataclass modules
    to be properly imported for full functionality.

.. seealso::
   :mod:`base_dataclass`: Base pattern definitions
   :mod:`mixin_dataclass`: Mixin pattern classes

:copyright: 2023, m.lotfi
:license: MIT
"""

from dataclasses import dataclass
from typing import Dict

# Import necessary base and mixin classes
from ._validator import PatternValidator

# Base Pattern Classes
from ._base import (
    BasePatterns,
    MonthPatterns,
    EraPatterns,
    IndicatorPatterns,
    NumericPatterns
)

# Mixin Pattern Classes
from ._simple import (
    CenturyPatterns,
    YearPatterns,
    MonthYearPatterns,
    DayMonthYearPatterns,
    NaturalLanguagePatterns
)


@dataclass
class CompositeYearPatterns(PatternValidator):
    """
    Composite year patterns for different calendar systems.

    This class handles standalone year patterns across multiple calendar systems,
    supporting both simple numeric years and years with era indicators. It builds
    complex patterns for mixed calendar scenarios and alternative representations.

    The class generates patterns for:

    * Simple numeric years: "1445", "2024"
    * Years with era indicators: "1445 AH", "2024 AD", "1403 ش.ه"
    * Mixed calendar patterns: "1445-2024" (Hijri-Gregorian)
    * Parenthetical alternatives: "1445 (2024)"

    Parameters
    ----------
    year_patterns : YearPatterns
        Base year pattern definitions for different calendar systems
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses

    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing Hijri calendar year patterns with keys:

        * 'mixed': Mixed Hijri year patterns (e.g., "1445-1446")
        * 'alternative': Hijri with Gregorian alternative (e.g., "1445-2024")
        * 'alternative_parenthetical': Hijri with parenthetical Gregorian (e.g., "1445 (2024)")

    gregorian : Dict[str, str]
        Dictionary containing Gregorian calendar year patterns with keys:

        * 'mixed': Mixed Gregorian year patterns (e.g., "2024-2025")
        * 'alternative': Gregorian with Hijri alternative (e.g., "2024-1445")
        * 'alternative_parenthetical': Gregorian with parenthetical Hijri (e.g., "2024 (1445)")

    Examples
    --------
    >>> from date_patterns import CompositeYearPatterns
    >>> year_patterns = YearPatterns(...)
    >>> indicator_patterns = IndicatorPatterns(...)
    >>> composite = CompositeYearPatterns(year_patterns, indicator_patterns)
    >>>
    >>> # Access Hijri mixed pattern
    >>> hijri_pattern = composite.hijri['mixed']
    >>> print(hijri_pattern)
    '1[34][0-9]{2}\\s*[-/]?\\s*1[34][0-9]{2}'

    Notes
    -----
    All patterns are automatically validated using the inherited PatternValidator
    functionality. Invalid regex patterns will raise validation errors during
    initialization.

    The patterns support flexible separators and optional whitespace to handle
    various formatting styles commonly found in text.

    See Also
    --------
    YearPatterns : Base year pattern definitions
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    year_patterns: YearPatterns
    indicator_patterns: IndicatorPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None

    def __post_init__(self) -> None:
        """
        Initialize all year patterns after dataclass creation.

        This method is automatically called after the dataclass is initialized.
        It builds all calendar-specific pattern dictionaries and validates them.

        Raises
        ------
        ValidationError
            If any of the generated regex patterns are invalid
        """

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}

        # Build Hijri Mixed Year Patterns (financial year, range, etc.)
        self.hijri['mixed'] = (
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric']}"
        )

        self.hijri['mixed_parenthetical'] = (
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Hijri Alternative Year Patterns
        self.hijri['alternative'] = (
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric']}"
        )

        self.hijri['alternative_parenthetical'] = (
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Gregorian year patterns
        self.gregorian['mixed'] = (
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric']}"
        )

        self.gregorian['mixed_parenthetical'] = (
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Gregorian alternative year patterns
        self.gregorian['alternative'] = (
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric']}"
        )

        self.gregorian['alternative_parenthetical'] = (
            rf"{self.year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class CompositeMonthYearPatterns(PatternValidator):
    """
    Composite month-year patterns for different calendar systems.

    This class handles month-year combinations across multiple calendar systems,
    supporting both numeric and named month formats with various year representations.
    It builds complex patterns for mixed calendar scenarios and alternative formats.

    The class generates patterns for:

    * Numeric month-year: "12/2024", "03-1445"
    * Named month-year: "December 2024", "Muharram 1445 AH"
    * Mixed calendar patterns: "December 2024 - Muharram 1445"
    * Parenthetical alternatives: "December 2024 (Muharram 1445)"

    Parameters
    ----------
    month_year_patterns : MonthYearPatterns
        Base month-year pattern definitions for different calendar systems
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses

    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing Hijri calendar month-year patterns with keys:

        * 'mixed': Mixed Hijri month-year patterns
        * 'alternative': Hijri with Gregorian alternative
        * 'alternative_parenthetical': Hijri with parenthetical Gregorian

    gregorian : Dict[str, str]
        Dictionary containing Gregorian calendar month-year patterns with keys:

        * 'mixed': Mixed Gregorian month-year patterns
        * 'alternative': Gregorian with Hijri alternative
        * 'alternative_parenthetical': Gregorian with parenthetical Hijri

    Examples
    --------
    >>> from date_patterns import CompositeMonthYearPatterns
    >>> month_year_patterns = MonthYearPatterns(...)
    >>> indicator_patterns = IndicatorPatterns(...)
    >>> composite = CompositeMonthYearPatterns(month_year_patterns, indicator_patterns)
    >>>
    >>> # Access Gregorian alternative pattern
    >>> pattern = composite.gregorian['alternative']
    >>>
    >>> # Use pattern for matching
    >>> import re
    >>> match = re.search(pattern, "December 2024 - Muharram 1445")

    Notes
    -----
    The patterns support flexible formatting including optional separators,
    whitespace handling, and various month name formats (full names, abbreviations).

    All generated patterns undergo automatic validation to ensure regex correctness.

    See Also
    --------
    MonthYearPatterns : Base month-year pattern definitions
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    month_year_patterns: MonthYearPatterns
    indicator_patterns: IndicatorPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None

    def __post_init__(self) -> None:
        """
        Initialize all month-year patterns after dataclass creation.

        This method builds all calendar-specific pattern dictionaries by combining
        base month-year patterns with indicators for mixed and alternative formats.

        Raises
        ------
        ValidationError
            If any of the generated regex patterns are invalid
        """

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}

        self.hijri['mixed'] = (
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['combined']}"
        )

        self.hijri['mixed_parenthetical'] = (
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.hijri['alternative'] = (
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['combined']}"
        )

        self.hijri['alternative_parenthetical'] = (
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Gregorian month-year patterns
        self.gregorian['mixed'] = (
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['combined']}"
        )

        self.gregorian['mixed_parenthetical'] = (
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.gregorian['alternative'] = (
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['combined']}"
        )

        self.gregorian['alternative_parenthetical'] = (
            rf"{self.month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class CompositeDayMonthYearPatterns(PatternValidator):
    """
    Composite day-month-year patterns for different calendar systems.

    This class handles complete date patterns across multiple calendar systems,
    supporting various formats including numeric dates, named months, and mixed
    calendar representations with era indicators.

    The class generates patterns for:

    * Numeric dates: "15/12/2024", "25-03-1445"
    * Mixed format: "15 December 2024", "25 Muharram 1445"
    * With era indicators: "15 Muharram 1445 AH", "15 December 2024 AD"
    * Mixed calendar patterns: "15 December 2024 - 25 Muharram 1445"
    * Parenthetical alternatives: "15 December 2024 (25 Muharram 1445)"

    Parameters
    ----------
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
    day_month_year_patterns : DayMonthYearPatterns
        Base day-month-year pattern definitions for different calendar systems

    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing Hijri calendar day-month-year patterns with keys:

        * 'mixed': Mixed Hijri date patterns
        * 'alternative': Hijri with Gregorian alternative
        * 'alternative_parenthetical': Hijri with parenthetical Gregorian

    gregorian : Dict[str, str]
        Dictionary containing Gregorian calendar day-month-year patterns with keys:

        * 'mixed': Mixed Gregorian date patterns
        * 'alternative': Gregorian with Hijri alternative
        * 'alternative_parenthetical': Gregorian with parenthetical Hijri

    Examples
    --------
    >>> from date_patterns import CompositeDayMonthYearPatterns
    >>> indicator_patterns = IndicatorPatterns(...)
    >>> dmy_patterns = DayMonthYearPatterns(...)
    >>> composite = CompositeDayMonthYearPatterns(indicator_patterns, dmy_patterns)
    >>>
    >>> # Access Hijri mixed pattern for date ranges
    >>> pattern = composite.hijri['mixed']
    >>>
    >>> # Use for matching date ranges
    >>> import re
    >>> text = "من 15 محرم 1445 إلى 20 محرم 1445"
    >>> matches = re.findall(pattern, text)

    Notes
    -----
    These patterns are designed to handle real-world date formats found in
    multilingual documents, including flexible separators, optional whitespace,
    and various cultural date formatting conventions.

    The patterns support both left-to-right (LTR) and right-to-left (RTL)
    text directions for proper Arabic and Persian date handling.

    See Also
    --------
    DayMonthYearPatterns : Base complete date pattern definitions
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    indicator_patterns: IndicatorPatterns
    day_month_year_patterns: DayMonthYearPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None

    def __post_init__(self) -> None:
        """
        Initialize all day-month-year patterns after dataclass creation.

        This method builds comprehensive date patterns by combining base
        day-month-year patterns with various indicators for alternative
        calendar representations and formatting styles.

        Raises
        ------
        ValidationError
            If any of the generated regex patterns are invalid
        """

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}

        # Build Hijri day-month-year patterns
        self.hijri['mixed'] = (
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['combined']}"
        )

        self.hijri['mixed_parenthetical'] = (
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.hijri['alternative'] = (
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['combined']}"
        )

        self.hijri['alternative_parenthetical'] = (
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Gregorian day-month-year patterns
        self.gregorian['mixed'] = (
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['combined']}"
        )

        self.gregorian['mixed_parenthetical'] = (
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.gregorian['alternative'] = (
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['combined']}"
        )

        self.gregorian['alternative_parenthetical'] = (
            rf"{self.day_month_year_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class CompositeNaturalLanguagePatterns(PatternValidator):
    """
    Composite natural language date patterns with weekday integration.

    This class handles natural language date expressions that combine weekdays
    with complete date patterns across multiple calendar systems. It supports
    various cultural conventions for expressing dates in natural language.

    The class generates patterns for:

    * Weekday with numeric date: "Monday 15/12/2024", "الاثنين 15/12/1445"
    * Weekday with named month: "Friday 15 December 2024", "الجمعة 15 محرم 1445"
    * Mixed calendar expressions: "Monday 15 December 2024 - الاثنين 15 محرم 1445"
    * Parenthetical alternatives: "Friday 15 December 2024 (الجمعة 15 محرم 1445)"

    Parameters
    ----------
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
    natural_language_patterns : NaturalLanguagePatterns
        Base natural language pattern definitions including weekday combinations

    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing Hijri calendar natural language patterns with keys:

        * 'mixed': Mixed Hijri natural language patterns
        * 'alternative': Hijri with Gregorian alternative
        * 'alternative_parenthetical': Hijri with parenthetical Gregorian

    gregorian : Dict[str, str]
        Dictionary containing Gregorian calendar natural language patterns with keys:

        * 'mixed': Mixed Gregorian natural language patterns
        * 'alternative': Gregorian with Hijri alternative
        * 'alternative_parenthetical': Gregorian with parenthetical Hijri

    Examples
    --------
    >>> from date_patterns import CompositeNaturalLanguagePatterns
    >>> indicator_patterns = IndicatorPatterns(...)
    >>> nl_patterns = NaturalLanguagePatterns(...)
    >>> composite = CompositeNaturalLanguagePatterns(indicator_patterns, nl_patterns)
    >>>
    >>> # Access Gregorian mixed pattern
    >>> pattern = composite.gregorian['mixed']
    >>>
    >>> # Match natural language date expressions
    >>> import re
    >>> text = "The meeting is scheduled for Monday 15 December 2024 to Wednesday 17 December 2024"
    >>> matches = re.findall(pattern, text)

    Notes
    -----
    These patterns are particularly useful for processing documents, emails,
    and other text sources where dates are expressed in natural language
    rather than structured formats.

    The patterns handle multilingual weekday names and support both Arabic
    and English natural language date expressions.

    See Also
    --------
    NaturalLanguagePatterns : Base natural language pattern definitions
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    indicator_patterns: IndicatorPatterns
    natural_language_patterns: NaturalLanguagePatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None

    def __post_init__(self) -> None:
        """
        Initialize all natural language patterns after dataclass creation.

        This method builds natural language date patterns by combining base
        weekday-date patterns with indicators for mixed calendar representations
        and alternative formatting styles.

        Raises
        ------
        ValidationError
            If any of the generated regex patterns are invalid
        """

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}

        # Build Hijri natural language patterns
        self.hijri['mixed'] = (
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.hijri['combined']}"
        )

        self.hijri['mixed_parenthetical'] = (
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.hijri['alternative'] = (
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.gregorian['combined']}"
        )

        self.hijri['alternative_parenthetical'] = (
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        # Build Gregorian natural language patterns
        self.gregorian['mixed'] = (
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.gregorian['combined']}"
        )

        self.gregorian['mixed_parenthetical'] = (
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )

        self.gregorian['alternative'] = (
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.hijri['combined']}"
        )

        self.gregorian['alternative_parenthetical'] = (
            rf"{self.natural_language_patterns.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.hijri['combined']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        # Validate all generated patterns
        self._validate_patterns()