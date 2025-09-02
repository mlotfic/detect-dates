#!/usr/bin/env python3
"""
Date Pattern Recognition Module
===============================

This module provides a comprehensive set of date patterns for various calendars
and languages, supporting multi-calendar date recognition and parsing.

The module includes pattern classes for different date components (years, months,
days) and their combinations, with support for natural language date expressions
and composite pattern matching.

Example:
    Basic usage of the DatePatterns class::

        from date_patterns import DatePatterns
        from detect_dates.regex_patterns import get_date_patterns

        # Initialize with Arabic language patterns
        patterns = DatePatterns(*get_date_patterns(lang="ar"))

        # Use the patterns for date recognition
        result = patterns.dual_dd_mm_yy.match("15 يناير 2023")

.. moduleauthor:: m.lotfi
.. versionadded:: 1.0.0
.. versionchanged:: 1.0.0
   Initial implementation with multi-calendar support

:copyright: 2023, m.lotfi
:license: MIT
"""

# ===============================================================================
# Module Exports
# ===============================================================================

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

# Composite Pattern Classes
from ._composite import (
    CompositeYearPatterns,
    CompositeMonthYearPatterns,
    CompositeDayMonthYearPatterns,
    CompositeNaturalLanguagePatterns
)

# Complex Pattern Classes
from ._complex import (
    ComplexYearPatterns,
    ComplexMonthYearPatterns,
    ComplexDayMonthYearPatterns,
    ComplexNaturalLanguagePatterns,
)


class DatePatterns:
    """
    Main orchestrator class for comprehensive date pattern recognition across multiple calendars.

    This class provides a unified interface for date pattern matching by coordinating
    various pattern hierarchies from basic components to sophisticated pattern combinations.
    It supports multiple languages and calendar systems through configurable pattern objects.

    The class implements a four-tier pattern hierarchy:

    1. **Base patterns**: Core building blocks (months, numbers, eras, indicators)
    2. **Single patterns**: Individual date component patterns (years, month-year, full dates)
    3. **Composite patterns**: Combined pattern matching with enhanced logic
    4. **Complex patterns**: Advanced dual-layer pattern matching for maximum accuracy

    Attributes:
        era (EraPatterns): Era designation patterns (BC, AD, AH, etc.)
        indicator (IndicatorPatterns): Date separators and connecting words
        numeric (NumericPatterns): Numeric date component patterns (1-31, 1900-2100, etc.)
        mm (MonthPatterns): Month names, abbreviations, and numeric representations
        century (CenturyPatterns): Century-specific patterns and ranges
        yy (YearPatterns): Year patterns with era and indicator support
        mm_yy (MonthYearPatterns): Month-year combination patterns
        dd_mm_yy (DayMonthYearPatterns): Complete day-month-year patterns
        natural_language (NaturalLanguagePatterns): Natural language date expressions
        cs_yy (CompositeYearPatterns): Composite year pattern matching
        cs_mm_yy (CompositeMonthYearPatterns): Composite month-year pattern matching
        cs_dd_mm_yy (CompositeDayMonthYearPatterns): Composite full date pattern matching
        cs_natural_language (CompositeNaturalLanguagePatterns): Composite natural language patterns
        dual_yy (ComplexYearPatterns): Complex year pattern recognition
        dual_mm_yy (ComplexMonthYearPatterns): Complex month-year pattern recognition
        dual_dd_mm_yy (ComplexDayMonthYearPatterns): Complex full date pattern recognition
        dual_natural_language (ComplexNaturalLanguagePatterns): Complex natural language recognition

    Example:
        Initialize with language-specific patterns::

            from detect_dates.regex_patterns import get_date_patterns

            # Get Arabic language patterns
            ar_patterns = get_date_patterns(lang="ar")
            date_patterns = DatePatterns(*ar_patterns)

            # Use different complexity levels for pattern matching
            simple_match = date_patterns.dd_mm_yy.match("15/01/2023")
            complex_match = date_patterns.dual_dd_mm_yy.match("يوم 15 من يناير 2023")

    Note:
        Pattern objects are expected to be dataclass instances from their respective
        modules. The get_date_patterns factory function should return a tuple of
        (base_patterns, month_patterns, era_patterns, indicator_patterns, numeric_patterns).

    .. versionadded:: 1.0.0
    """

    def __init__(self, base_patterns, month_patterns, era_patterns,
                 indicator_patterns, numeric_patterns):
        """
        Initialize DatePatterns with language-specific pattern components.

        Creates a complete hierarchy of pattern matchers from basic components
        through sophisticated multi-layer pattern recognition systems.

        Args:
            base_patterns (BasePatterns): Fundamental patterns including words and weekdays
            month_patterns (MonthPatterns): Month names, abbreviations, and numeric forms
            era_patterns (EraPatterns): Historical era designations (BC, AD, AH, etc.)
            indicator_patterns (IndicatorPatterns): Date separators, connectors, and indicators
            numeric_patterns (NumericPatterns): Numeric patterns for days, months, and years

        Raises:
            TypeError: If pattern objects are not of expected dataclass types
            ValueError: If pattern objects contain invalid or incomplete data
            AttributeError: If required pattern attributes are missing

        Example:
            Initialize with English patterns::

                from base_dataclass import BasePatterns, MonthPatterns
                from base_dataclass import EraPatterns, IndicatorPatterns, NumericPatterns

                base = BasePatterns(language="en", words=..., weekday=...)
                months = MonthPatterns(language="en", full_names=..., abbreviations=...)
                eras = EraPatterns(language="en", bc_patterns=..., ad_patterns=...)
                indicators = IndicatorPatterns(language="en", separators=..., connectors=...)
                numerics = NumericPatterns(language="en", day_patterns=..., year_patterns=...)

                patterns = DatePatterns(base, months, eras, indicators, numerics)
        """
        # Store base pattern components with descriptive names
        self._base: BasePatterns = base_patterns
        self.weekday = base_patterns.weekday  # Weekday patterns
        self.words = base_patterns.numeric_words  # Numeric words for date components
        self.mm: MonthPatterns = month_patterns  # Month patterns
        self.era: EraPatterns = era_patterns
        self.indicator: IndicatorPatterns = indicator_patterns
        self.numeric: NumericPatterns = numeric_patterns

        # Initialize single-layer pattern matchers
        # These handle individual date components or simple combinations
        self.century = CenturyPatterns(
            numeric_patterns=self.numeric,
            indicator_patterns=self.indicator,
            era_patterns=self.era,
            base_patterns=self._base
        )

        self.yy = YearPatterns(
            numeric_patterns=self.numeric,
            indicator_patterns=self.indicator,
            era_patterns=self.era,
        )

        self.mm_yy = MonthYearPatterns(
            numeric_patterns=self.numeric,
            month_patterns=self.mm,
            year_patterns=self.yy,
            era_patterns=self.era,
            indicator_patterns=self.indicator
        )

        self.dd_mm_yy = DayMonthYearPatterns(
            numeric_patterns=self.numeric,
            month_patterns=self.mm,
            year_patterns=self.yy,
            era_patterns=self.era,
            indicator_patterns=self.indicator,
            month_year_patterns=self.mm_yy,
        )

        self.natural_language = NaturalLanguagePatterns(
            base_patterns=self._base,
            era_patterns=self.era,
            indicator_patterns=self.indicator,
            day_month_year_patterns=self.dd_mm_yy,
        )

        # Initialize composite pattern matchers
        # These combine single patterns with enhanced matching logic
        self.cs_yy = CompositeYearPatterns(
            year_patterns=self.yy,
            indicator_patterns=self.indicator
        )

        self.cs_mm_yy = CompositeMonthYearPatterns(
            month_year_patterns=self.mm_yy,
            indicator_patterns=self.indicator
        )

        self.cs_dd_mm_yy = CompositeDayMonthYearPatterns(
            day_month_year_patterns=self.dd_mm_yy,
            indicator_patterns=self.indicator
        )

        self.cs_natural_language = CompositeNaturalLanguagePatterns(
            natural_language_patterns=self.natural_language,
            indicator_patterns=self.indicator
        )

        # Initialize complex pattern matchers
        # These provide dual-layer sophisticated pattern recognition
        self.dual_yy = ComplexYearPatterns(
            year_patterns=self.cs_yy,
            indicator_patterns=self.indicator
        )

        self.dual_mm_yy = ComplexMonthYearPatterns(
            month_year_patterns=self.cs_mm_yy,
            indicator_patterns=self.indicator
        )

        self.dual_dd_mm_yy = ComplexDayMonthYearPatterns(
            day_month_year_patterns=self.cs_dd_mm_yy,
            indicator_patterns=self.indicator
        )

        self.dual_natural_language = ComplexNaturalLanguagePatterns(
            natural_language_patterns=self.cs_natural_language,
            indicator_patterns=self.indicator
        )

    def get_all_patterns(self):
        """
        Retrieve all pattern objects organized by complexity hierarchy.

        Provides structured access to all pattern matchers organized by their
        complexity level and functionality. Useful for introspection, testing,
        and selective pattern usage.

        Returns:
            dict: Nested dictionary with pattern objects organized by complexity:

                - **base**: Core pattern building blocks
                - **single**: Individual date component patterns
                - **composite**: Enhanced combination patterns
                - **complex**: Sophisticated dual-layer patterns

        Example:
            Access specific pattern levels::

                all_patterns = date_patterns.get_all_patterns()

                # Get base components
                base_month_patterns = all_patterns['base']['month']
                base_numeric_patterns = all_patterns['base']['numeric']

                # Get complex matchers
                complex_date_matcher = all_patterns['complex']['day_month_year']

                # Iterate through all single patterns
                for name, pattern in all_patterns['single'].items():
                    print(f"Single pattern {name}: {pattern}")
        """
        return {
            'base': {
                'era': self.era,
                'indicator': self.indicator,
                'numeric': self.numeric,
                'words': self._base.numeric_words,
                'weekday': self._base.weekday,
                'month': self.mm,
            },
            'single': {
                'century': self.century,
                'year': self.yy,
                'month_year': self.mm_yy,
                'day_month_year': self.dd_mm_yy,
                'weekday_day_month_year': self.natural_language
            },
            'composite': {
                'year': self.cs_yy,
                'month_year': self.cs_mm_yy,
                'day_month_year': self.cs_dd_mm_yy,
                'weekday_day_month_year': self.cs_natural_language,
            },
            'complex': {
                'year': self.dual_yy,
                'month_year': self.dual_mm_yy,
                'day_month_year': self.dual_dd_mm_yy,
                'weekday_day_month_year': self.dual_natural_language,
            }
        }

    def get_pattern_by_complexity(self, pattern_type, complexity='single'):
        """
        Retrieve a specific pattern matcher by type and complexity level.

        Provides convenient access to pattern matchers without navigating
        the full pattern hierarchy manually.

        Args:
            pattern_type (str): Type of pattern to retrieve. Valid options:

                - 'year': Year-only patterns
                - 'month_year': Month and year patterns
                - 'day_month_year': Complete date patterns
                - 'weekday_day_month_year': Natural language patterns
                - 'century': Century patterns (single complexity only)

            complexity (str, optional): Complexity level. Defaults to 'single'.
                Valid options: 'single', 'composite', 'complex'

        Returns:
            Pattern object corresponding to the requested type and complexity

        Raises:
            KeyError: If pattern_type or complexity is not valid
            ValueError: If the combination is not available (e.g., century with complex)

        Example:
            Get different complexity levels::

                # Simple year pattern
                simple_year = date_patterns.get_pattern_by_complexity('year', 'single')

                # Complex full date pattern
                complex_date = date_patterns.get_pattern_by_complexity(
                    'day_month_year', 'complex'
                )

                # Composite month-year pattern
                composite_my = date_patterns.get_pattern_by_complexity(
                    'month_year', 'composite'
                )
        """
        all_patterns = self.get_all_patterns()

        if complexity not in all_patterns:
            raise KeyError(f"Invalid complexity level: {complexity}")

        if pattern_type not in all_patterns[complexity]:
            raise KeyError(f"Pattern type '{pattern_type}' not available at '{complexity}' complexity")

        return all_patterns[complexity][pattern_type]

    def get_language_info(self):
        """
        Extract language information from the configured patterns.

        Returns:
            dict: Dictionary containing language metadata extracted from pattern objects

        Example:
            Get language information::

                lang_info = date_patterns.get_language_info()
                print(f"Configured for language: {lang_info.get('language', 'unknown')}")
        """
        return {
            'language': getattr(self._base, 'language', 'unknown'),
            'month_language': getattr(self.mm, 'language', 'unknown'),
            'era_language': getattr(self.era, 'language', 'unknown'),
            'has_base_patterns': self._base is not None,
            'has_month_patterns': self.mm is not None,
            'has_era_patterns': self.era is not None,
            'has_indicator_patterns': self.indicator is not None,
            'has_numeric_patterns': self.numeric is not None
        }

    def __repr__(self):
        """
        Return detailed string representation of the DatePatterns instance.

        Returns:
            str: Multi-line string representation showing configuration details
        """
        lang_info = self.get_language_info()
        return (
            f"DatePatterns(\n"
            f"  language='{lang_info.get('language', 'unknown')}',\n"
            f"  base_patterns={type(self._base).__name__},\n"
            f"  month_patterns={type(self.mm).__name__},\n"
            f"  era_patterns={type(self.era).__name__},\n"
            f"  indicator_patterns={type(self.indicator).__name__},\n"
            f"  numeric_patterns={type(self.numeric).__name__}\n"
            f")"
        )

    def __str__(self):
        """
        Return concise string representation for end users.

        Returns:
            str: Brief description of the DatePatterns configuration
        """
        lang_info = self.get_language_info()
        return f"DatePatterns configured for {lang_info.get('language', 'unknown')} language"



if __name__ == "__main__":
    """
    Demonstrate DatePatterns usage and perform basic validation.

    This function shows how to properly initialize and use the DatePatterns
    class, with comprehensive error handling and pattern validation.

    Note:
        This function is primarily for testing and demonstration. In production,
        import and use the DatePatterns class directly in your application code.
    """
    try:
        # Import path helper to ensure modules directory is in sys.path
        print("Initializing DatePatterns demonstration...")

        try:
            from path_helper import add_modules_to_sys_path
            add_modules_to_sys_path()
        except ImportError:
            print("Path helper not available, proceeding with default imports...")

        from detect_dates.regex_patterns import get_date_patterns

        # Demonstrate with Arabic language patterns
        print("\n1. Loading Arabic language patterns...")
        ar_pattern_data = get_date_patterns(lang="ar")
        ar_date_patterns = DatePatterns(*ar_pattern_data)

        print(f"   ✓ Arabic patterns loaded: {ar_date_patterns}")

        # Demonstrate pattern hierarchy access
        print("\n2. Exploring pattern hierarchy...")
        all_patterns = ar_date_patterns.get_all_patterns()

        for complexity, patterns in all_patterns.items():
            print(f"   {complexity.capitalize()} level: {len(patterns)} pattern types")

        # Demonstrate specific pattern access
        print("\n3. Accessing specific patterns...")
        try:
            complex_date_pattern = ar_date_patterns.get_pattern_by_complexity(
                'day_month_year', 'complex'
            )
            print(f"   ✓ Complex date pattern: {type(complex_date_pattern).__name__}")
        except (KeyError, ValueError) as e:
            print(f"   ✗ Error accessing pattern: {e}")

        # Show language information
        print("\n4. Language configuration:")
        lang_info = ar_date_patterns.get_language_info()
        for key, value in lang_info.items():
            print(f"   {key}: {value}")

        print("\n✓ DatePatterns demonstration completed successfully!")

    except ImportError as e:
        print(f"\n✗ Import error: {e}")
        print("   Please ensure all required modules are available:")
        print("   - modules.regex_patterns")
        print("   - base_dataclass, mixin_dataclass, composite_dataclass, complex_dataclass")

    except Exception as e:
        print(f"\n✗ Unexpected error during initialization: {e}")
       print("   Please check your pattern data and module configuration.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
You are a Python documentation and refactorin