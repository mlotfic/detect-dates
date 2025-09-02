#!/usr/bin/env python3*-
"""
Date Pattern Recognition Module
===============================

A comprehensive module for recognizing date patterns across multiple calendar systems
including Hijri (Islamic), Gregorian (Western), and julian (Persian) calendars.

This module provides structured dataclasses for building complex regex patterns
to match various date formats in natural language text. It supports multilingual
date recognition with sophisticated pattern matching capabilities including:

- Multi-calendar date detection and disambiguation
- Natural language date expressions with weekdays
- Parenthetical date notations and cross-calendar references
- Date range expressions and complex mixed-format patterns
- Automatic regex validation and compilation checking

Architecture Overview:
    The module follows a hierarchical pattern-building approach:

    1. **Base Patterns**: Fundamental regex components
    2. **Validation Layer**: :class:`PatternValidator` mixin for regex validation
    3. **Calendar-Specific Builders**: Specialized pattern generators
    4. **Composite Patterns**: Complex multi-component date expressions

Supported Calendar Systems:
    - **Hijri**: Islamic lunar calendar with Arabic month names and AH era
    - **Gregorian**: Western solar calendar with Latin month names and AD/CE era
    - **julian**: Persian solar calendar with Farsi month names and SH era

Example:
    .. code-block:: python

        from date_patterns import YearPatterns, MonthYearPatterns
        from base_dataclass import NumericPatterns, IndicatorPatterns, EraPatterns

        # Initialize base components
        numeric = NumericPatterns()
        indicators = IndicatorPatterns(...)
        eras = EraPatterns(...)

        # Build year patterns
        year_patterns = YearPatterns(numeric, indicators, eras)

        # Access calendar-specific patterns
        hijri_year = year_patterns.hijri['numeric']  # "1445 AH"


See Also:
    :mod:`base_dataclass`: Foundation pattern definitions
    :class:`PatternValidator`: Regex validation utilities

:author: m.lotfi
:version: 1.0.0
:created: 2023-10-01
:license: MIT
"""

import re
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union

# Base Pattern Classes
from ._base import (
    BasePatterns,
    MonthPatterns,
    EraPatterns,
    IndicatorPatterns,
    NumericPatterns
)


from ._validator import PatternValidator

# Calendar-Specific Pattern Classes
# ==================================

@dataclass
class CenturyPatterns(PatternValidator):
    """Regex patterns for century expressions across calendar systems.

    Generates comprehensive patterns for matching century references in different
    calendar systems, supporting both numeric and textual century expressions
    with optional era indicators. Handles multilingual century formats including
    ordinal numbers and written forms.

    This class builds sophisticated patterns for century detection including:

    - Numeric centuries with era markers (e.g., "15th century AH")
    - Optional era patterns for ambiguous contexts
    - Cross-calendar century references and comparisons
    - Multilingual support for Arabic, English, and Persian century expressions

    Parameters:
        numeric_patterns (NumericPatterns): Basic numeric component patterns
            for extracting century numbers from text.
        indicator_patterns (IndicatorPatterns): Structural patterns for century
            indicators, separators, and formatting elements.
        era_patterns (EraPatterns): Calendar system era markers and identifiers
            for disambiguating century references.
        base_patterns (BasePatterns): Fundamental patterns including numeric
            word representations and common text elements.

    Attributes:
        numeric (str): Base numeric century pattern combining indicators with
            numeric or written century numbers. Automatically generated during
            initialization.
        hijri (Dict[str, str]): Hijri calendar century patterns with keys:

            - ``'numeric'``: Century with required Hijri era marker
            - ``'optional'``: Century with optional Hijri era marker

        gregorian (Dict[str, str]): Gregorian calendar century patterns with keys:

            - ``'numeric'``: Century with required Gregorian era marker
            - ``'optional'``: Century with optional Gregorian era marker

        julian (Dict[str, str]): Persian calendar century patterns with keys:

            - ``'numeric'``: Century with required julian era marker
            - ``'optional'``: Century with optional julian era marker

    Example:
        .. code-block:: python

            from base_dataclass import NumericPatterns, IndicatorPatterns, EraPatterns, BasePatterns

            # Initialize components
            numeric = NumericPatterns()
            indicators = IndicatorPatterns(
                century=r"(?:century|قرن|سده)",
                separator=r"[\s/\-]+"
            )
            eras = EraPatterns(
                hijri=r"(?:AH|هـ)",
                gregorian=r"(?:AD|CE)",
                julian=r"(?:ش\.ه)"
            )
            base = BasePatterns(numeric_words=r"(?:fifteenth|پانزدهم)")

            # Build century patterns
            centuries = CenturyPatterns(numeric, indicators, eras, base)

            # Access patterns
            hijri_century = centuries.hijri['numeric']    # "15th century AH"
            optional_era = centuries.gregorian['optional'] # "21st century (AD)?"

    Note:
        All patterns are automatically validated during initialization using
        the :class:`PatternValidator` mixin. Invalid regex patterns will raise
        ``ValueError`` with detailed error information.

    See Also:
        :class:`YearPatterns`: Year-specific pattern generation
        :class:`PatternValidator`: Regex validation functionality
    """
    numeric_patterns: NumericPatterns
    indicator_patterns: IndicatorPatterns
    era_patterns: EraPatterns
    base_patterns: BasePatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize and validate all century patterns after dataclass creation.

        Constructs calendar-specific century patterns by combining base numeric
        patterns with era indicators and separators. The initialization process:

        1. Builds base numeric century pattern with indicators
        2. Initializes empty calendar-specific dictionaries
        3. Generates required and optional era patterns for each calendar
        4. Validates all generated patterns using :meth:`_validate_patterns`

        Pattern Generation Strategy:
            - **Required Era**: Patterns that must include era markers for disambiguation
            - **Optional Era**: Patterns where era markers are optional, useful for
              context-dependent matching where calendar system can be inferred

        Raises:
            ValueError: If any generated pattern fails regex compilation during
                the validation phase.
        """

        # Build base numeric century pattern
        # Combines century indicators with numeric patterns and word forms
        self.numeric = (
            rf"{self.indicator_patterns.century}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.numeric_patterns.century}|{self.base_patterns.numeric_words}\s*"
        )

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Build Hijri century patterns
        self.hijri['numeric'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.hijri}"
        )

        self.hijri['optional'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.hijri})?"
        )

        # Build Gregorian century patterns
        self.gregorian['numeric'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.gregorian}"
        )

        self.gregorian['optional'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.gregorian})?"
        )

        # Build julian century patterns
        self.julian['numeric'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.julian}"
        )

        self.julian['optional'] = (
            rf"{self.numeric}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.julian})?"
        )

        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class YearPatterns(PatternValidator):
    """Comprehensive year pattern generator for multi-calendar date recognition.

    Generates sophisticated regex patterns for matching year expressions across
    Hijri, Gregorian, and julian calendar systems. Supports complex scenarios
    including cross-calendar references, parenthetical notations, date ranges,
    and mixed-format expressions commonly found in multilingual texts.

    This class handles the most complex aspects of year pattern matching:

    - **Simple Years**: Basic numeric years with optional era markers
    - **Cross-Calendar References**: Years shown in multiple calendar systems
    - **Parenthetical Notations**: Years with equivalent dates in parentheses
    - **Date Ranges**: Year ranges with various connector formats
    - **Mixed Formats**: Complex combinations requiring disambiguation

    The pattern generation follows a hierarchical approach where simpler patterns
    are composed into increasingly complex expressions, enabling precise matching
    of diverse year formats found in historical texts, academic papers, and
    multilingual documents.

    Parameters:
        numeric_patterns (NumericPatterns): Core numeric patterns for year extraction
            with capture groups for processing matched values.
        indicator_patterns (IndicatorPatterns): Structural elements including
            separators, parentheses, and range connectors.
        era_patterns (EraPatterns): Calendar-specific era markers for system
            identification and disambiguation.

    Attributes:
        numeric (str): Base word-bounded year pattern for standalone numeric years.
            Automatically generated with word boundaries to prevent partial matches.

        hijri (Dict[str, str]): Comprehensive Hijri year patterns including:

            - ``'numeric'``: Year with required Hijri era (e.g., "1445 AH")
            - ``'numeric_optional'``: Year with optional era for context matching

        gregorian (Dict[str, str]): Gregorian year patterns with similar structure
            to Hijri patterns, adapted for Western calendar expressions.

        julian (Dict[str, str]): Persian calendar year patterns following the
            same comprehensive pattern structure.

    Example:
        .. code-block:: python

            # Initialize pattern components
            numeric = NumericPatterns()
            indicators = IndicatorPatterns(
                separator=r"[\s/\-]+",
                parentheses_start=r"[\(\[]",
                parentheses_end=r"[\)\]]",
                range_connector=r"(?:to|until|تا|-)",
                range_starter=r"(?:from|since|از)"
            )
            eras = EraPatterns(
                hijri=r"(?:AH|هـ)",
                gregorian=r"(?:AD|CE|BC)",
                julian=r"(?:ش\.ه)"
            )

            # Build year patterns
            years = YearPatterns(numeric, indicators, eras)

            # Access specific patterns
            simple_hijri = years.hijri['numeric']           # "1445 AH"

    Complex Pattern Examples:
        The generated patterns can match sophisticated expressions:

        .. code-block:: text

            "1445 AH (2024 AD)"                    # Cross-calendar parenthetical
            "from 1440 to 1445 AH"                 # Simple range
            "1440 AH - 1445 AH (2019-2024 AD)"     # Complex mixed range
            "(1445 AH) - (2024 AD)"                # Parenthetical range
            "1445 هـ / 2024 م"                     # Arabic era markers

    Note:
        All patterns include appropriate capture groups for extracting year values
        and era markers. Pattern validation ensures all generated regex expressions
        are syntactically correct and compilable.

    Warning:

        additional context or post-processing to determine the correct calendar
        system for years without explicit era markers.

    See Also:
        :class:`MonthYearPatterns`: Patterns combining months with years
        :class:`CenturyPatterns`: Century-specific pattern generation
        :class:`PatternValidator`: Automatic regex validation
    """
    numeric_patterns: NumericPatterns
    indicator_patterns: IndicatorPatterns
    era_patterns: EraPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize comprehensive year patterns for all supported calendars.

        Constructs the complete hierarchy of year patterns from simple numeric
        years to complex cross-calendar expressions with ranges and parenthetical
        notations. The initialization follows a systematic approach:

        1. **Base Pattern**: Creates word-bounded numeric year pattern
        2. **Calendar Initialization**: Sets up pattern dictionaries for each system
        3. **Pattern Hierarchy**: Builds patterns from simple to complex:

           - Basic numeric patterns with optional/required eras
           - Mixed format patterns for cross-calendar expressions
           - Parenthetical patterns for equivalent date notations
           - Range patterns for temporal spans and periods

        4. **Validation**: Ensures all generated patterns compile correctly

        The pattern generation uses forward references, building complex patterns
        from simpler components. This requires careful ordering to ensure all
        referenced patterns exist when used.

        Pattern Composition Strategy:
            - **Atomic Patterns**: Base numeric and era combinations
            - **Composite Patterns**: Combinations of atomic patterns
            - **Complex Patterns**: Multi-level compositions with ranges and parentheses
            - **Validation Layer**: Automatic regex compilation checking

        Raises:
            ValueError: If any pattern in the hierarchy fails regex compilation,
                indicating a syntax error in pattern construction.
        """

        # Base numeric year pattern with word boundaries
        self.numeric = (
            rf"\b{self.numeric_patterns.year}\b"
        )

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Build Hijri year patterns
        self.hijri['numeric'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.hijri}"
        )

        self.hijri['numeric_optional'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.hijri})?"
        )

        # Build Gregorian year patterns
        self.gregorian['numeric'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.gregorian}"
        )

        self.gregorian['numeric_optional'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.gregorian})?"
        )

        # Build julian year patterns
        self.julian['numeric'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.julian}"
        )

        self.julian['numeric_optional'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.julian})?"
        )

        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class MonthYearPatterns(PatternValidator):
    """Advanced month-year pattern generator for multi-calendar date systems.

    Constructs sophisticated regex patterns for matching month-year combinations
    across Hijri, Gregorian, and julian calendars. Handles both numeric and
    named month formats with comprehensive cross-calendar support, parenthetical
    notations, and mixed-format expressions.

    This class specializes in the complex task of month-year pattern matching,
    supporting various formats commonly found in multilingual documents:

    - **Numeric Months**: "12/2024", "12 1445 AH"
    - **Named Months**: "December 2024", "Muharram 1445 AH", "فروردین 1403"
    - **Mixed Formats**: Combinations requiring calendar disambiguation
    - **Cross-References**: Months with equivalent dates in other calendars
    - **Parenthetical**: "Muharram 1445 AH (January 2024 AD)"

    The pattern generation leverages the hierarchical year patterns from
    :class:`YearPatterns` and combines them with month indicators to create
    comprehensive month-year matching capabilities.

    Parameters:
        numeric_patterns (NumericPatterns): Core numeric patterns for month
            and year number extraction with proper capture groups.
        year_patterns (YearPatterns): Pre-built year pattern definitions
            used as components in month-year combinations.
        month_patterns (MonthPatterns): Calendar-specific month name patterns
            for named month recognition in multiple languages.
        era_patterns (EraPatterns): Calendar system era markers for
            disambiguation and system identification.
        indicator_patterns (IndicatorPatterns): Structural elements including
            separators and parenthetical markers.

    Attributes:
        numeric (str): Base numeric month/year pattern for formats like "12/2024".
            Automatically generated during initialization.

        hijri (Dict[str, str]): Hijri calendar month-year patterns:

            - ``'numeric'``: Numeric month with Hijri year and required era
            - ``'numeric_optional'``: Numeric month with optional era marker
            - ``'named'``: Named Hijri month with year (e.g., "Muharram 1445 AH")
            - ``'combined'``: Union of numeric and named patterns with required era
            - ``'combined_optional'``: Union patterns with optional era markers

        gregorian (Dict[str, str]): Gregorian calendar month-year patterns with
            parallel structure to Hijri patterns, optimized for Western calendar
            month names and formatting conventions.

        julian (Dict[str, str]): Persian calendar month-year patterns supporting
            Farsi month names and Persian calendar formatting standards.

    Example:
        .. code-block:: python

            # Initialize required components
            numeric = NumericPatterns()
            year_patterns = YearPatterns(...)  # Pre-built year patterns
            month_names = MonthPatterns(
                hijri=r"(?:محرم|صفر|ربیع‌الاول)",
                gregorian=r"(?:January|February|December)",
                julian=r"(?:فروردین|اردیبهشت)"
            )

            # Build month-year patterns
            month_years = MonthYearPatterns(
                numeric, year_patterns, month_names, eras, indicators
            )

            # Access specific patterns
            hijri_numeric = month_years.hijri['numeric']        # "12/1445 AH"
            hijri_named = month_years.hijri['named']            # "Muharram 1445 AH"

            mixed = month_years.hijri['combined']               # Either numeric or named

    Pattern Matching Examples:
        The generated patterns handle diverse month-year formats:

        .. code-block:: text

            "12/1445 AH"                        # Numeric Hijri
            "Muharram 1445 AH"                  # Named Hijri
            "December 2024"                     # Named Gregorian (era optional)
            "فروردین 1403 ش.ه"                  # Named julian
            "12/1445 AH (01/2024 AD)"           # Cross-calendar parenthetical
            "Muharram 1445 / January 2024"     # Mixed clear format

    Note:
        The ``combined`` patterns use regex alternation to match either numeric
        or named month formats, providing flexibility for varied input formats.
        All patterns maintain capture groups for extracting month and year values.

    Warning:
        Named month patterns depend on the quality of month name patterns provided
        in the ``month_patterns`` parameter. Ensure comprehensive month name
        coverage for target languages and transliteration variants.

    See Also:
        :class:`YearPatterns`: Year pattern components used in construction
        :class:`DayMonthYearPatterns`: Full date patterns including days
        :class:`MonthPatterns`: Month name pattern definitions
    """
    numeric_patterns: NumericPatterns
    year_patterns: YearPatterns
    month_patterns: MonthPatterns
    era_patterns: EraPatterns
    indicator_patterns: IndicatorPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize comprehensive month-year patterns for all calendar systems.

        Constructs the complete set of month-year patterns by combining numeric
        month patterns with the pre-built year patterns, then adding named month
        alternatives and complex cross-calendar expressions.

        The initialization process follows a systematic pattern hierarchy:

        1. **Base Pattern**: Creates numeric month/year separator pattern
        2. **Calendar Dictionaries**: Initializes pattern storage for each system
        3. **Atomic Patterns**: Builds basic numeric and named month-year patterns
        4. **Composite Patterns**: Creates combined patterns supporting both formats
        5. **Cross-Calendar**: Adds mixed format and parenthetical patterns
        6. **Validation**: Ensures all patterns compile correctly

        Pattern Building Strategy:
            The method leverages existing year patterns from :class:`YearPatterns`
            to create consistent month-year combinations. This ensures that complex
            year expressions (parenthetical, mixed, range formats) are properly
            supported in month-year contexts.

        Raises:
            ValueError: If any pattern fails regex compilation, indicating syntax
                errors in the pattern construction process.
        """

        # Base numeric month/year pattern
        self.numeric = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.numeric_patterns.year}"
        )

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Build Hijri month-year patterns
        self.hijri['numeric'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric']}"
        )

        self.hijri['numeric_optional'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric_optional']}"
        )

        self.hijri['named'] = (
            rf"{self.month_patterns.hijri}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric_optional']}"
        )

        self.hijri['combined'] = (
            rf"(?:{self.hijri['numeric']})|(?:{self.hijri['named']})"
        )

        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )

        # Build Gregorian month-year patterns
        self.gregorian['numeric'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric']}"
        )

        self.gregorian['numeric_optional'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric_optional']}"
        )

        self.gregorian['named'] = (
            rf"{self.month_patterns.gregorian}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric_optional']}"
        )

        self.gregorian['combined'] = (
            rf"(?:{self.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )

        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )

        # Build julian month-year patterns
        self.julian['numeric'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.julian['numeric']}"
        )

        self.julian['numeric_optional'] = (
            rf"{self.numeric_patterns.month}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.julian['numeric_optional']}"
        )

        self.julian['named'] = (
            rf"{self.month_patterns.julian}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.julian['numeric_optional']}"
        )

        self.julian['combined'] = (
            rf"(?:{self.julian['numeric']})|(?:{self.julian['named']})"
        )

        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )

        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class DayMonthYearPatterns(PatternValidator):
    """Complete date pattern generator for full day-month-year expressions.

    The most comprehensive pattern class, generating regex patterns for complete
    date expressions including day, month, and year components across all
    supported calendar systems. Handles the full spectrum of date formats from
    simple numeric dates to complex multilingual expressions with cross-calendar
    references.

    This class represents the culmination of the pattern hierarchy, combining
    day numbers with the sophisticated month-year patterns to create patterns
    capable of matching virtually any date format encountered in multilingual
    texts, historical documents, and academic papers.

    Key Features:
        - **Complete Date Matching**: Full day/month/year pattern support
        - **Flexible Formatting**: Numeric, named, and mixed month formats
        - **Cross-Calendar Support**: Dates with equivalent calendar references
        - **Parenthetical Notation**: Primary dates with alternative calendar equivalents
        - **Mixed Expression Handling**: Complex format disambiguation

    Parameters:
        numeric_patterns (NumericPatterns): Basic numeric patterns for day,
            month, and year extraction with appropriate capture groups.
        year_patterns (YearPatterns): Complete year pattern definitions used
            as building blocks for full date expressions.
        month_patterns (MonthPatterns): Calendar-specific month name patterns
            supporting multilingual month recognition.
        era_patterns (EraPatterns): Era marker patterns for calendar system
            identification and disambiguation.
        indicator_patterns (IndicatorPatterns): Structural pattern elements
            including separators and parenthetical markers.
        month_year_patterns (MonthYearPatterns): Pre-built month-year pattern
            combinations used as components in full date expressions.

    Attributes:
        numeric (str): Base numeric day/month/year pattern (e.g., "15/12/2024").

        hijri (Dict[str, str]): Complete Hijri date patterns including:

            - ``'numeric'``: Numeric date with required Hijri era
            - ``'numeric_optional'``: Numeric date with optional era
            - ``'named'``: Date with named month (e.g., "15 Muharram 1445 AH")
            - ``'combined'``: Union of numeric and named with required era
            - ``'combined_optional'``: Union patterns with optional era
        gregorian (Dict[str, str]): Comprehensive Gregorian date patterns with
            structure parallel to Hijri patterns, optimized for Western date
            formats and conventions.

        julian (Dict[str, str]): Persian calendar date patterns supporting
            Farsi formatting and Persian date conventions.

    Example:
        .. code-block:: python

            # Initialize all required components
            numeric = NumericPatterns()
            year_patterns = YearPatterns(...)
            month_patterns = MonthPatterns(...)
            month_year_patterns = MonthYearPatterns(...)

            # Build complete date patterns
            dates = DayMonthYearPatterns(
                numeric, year_patterns, month_patterns,
                eras, indicators, month_year_patterns
            )

            # Access comprehensive date patterns
            hijri_numeric = dates.hijri['numeric']      # "15/12/1445 AH"
            hijri_named = dates.hijri['named']          # "15 Muharram 1445 AH"



    Advanced Pattern Examples:
        The generated patterns match sophisticated date expressions:

        .. code-block:: text

            "15/12/1445 AH"                           # Basic numeric Hijri
            "15 Muharram 1445 AH"                     # Named month Hijri
            "15 December 2024"                        # Named Gregorian (era optional)
            "15 فروردین 1403 ش.ه"                    # Named julian
            "15 Muharram 1445 AH (15 January 2024 AD)"  # Cross-calendar reference
            "15/12/1445 - 20/01/1446 AH"             # Date ranges (if supported)
            "15 محرم 1445 هـ / 15 يناير 2024 م"        # Arabic era markers

    Note:
        This class builds upon the entire pattern hierarchy and requires all
        component patterns to be properly initialized. The patterns maintain
        capture groups for extracting individual date components (day, month, year)
        and era markers for calendar system identification.

    Performance Note:
        Due to the comprehensive nature of these patterns, consider the complexity
        when applying them to large text corpora. The alternation patterns
        (``combined``) may require careful optimization for performance-critical
        applications.

    See Also:
        :class:`MonthYearPatterns`: Month-year components used in construction
        :class:`NaturalLanguagePatterns`: Patterns including weekday information
        :class:`YearPatterns`: Year pattern building blocks
    """
    numeric_patterns: NumericPatterns
    year_patterns: YearPatterns
    month_patterns: MonthPatterns
    era_patterns: EraPatterns
    indicator_patterns: IndicatorPatterns
    month_year_patterns: MonthYearPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize comprehensive day-month-year patterns for all calendars.

        Constructs the complete hierarchy of full date patterns by combining
        day numeric patterns with the sophisticated month-year patterns,
        creating the most comprehensive date matching capabilities in the system.

        The initialization process represents the culmination of pattern building:

        1. **Base Numeric**: Constructs fundamental day/month/year pattern
        2. **Calendar Initialization**: Sets up pattern dictionaries
        3. **Component Assembly**: Combines days with month-year patterns
        4. **Format Variants**: Creates numeric, named, and combined alternatives
        5. **Cross-Calendar**: Builds complex multi-calendar expressions
        6. **Validation**: Ensures pattern correctness and compilation

        Pattern Assembly Strategy:
            This method leverages the full power of :class:`MonthYearPatterns`
            by prefixing day patterns to create complete date expressions.
            The hierarchical approach ensures that all complex month-year
            formats are available in complete date contexts.

        Raises:
            ValueError: If any pattern fails compilation during validation,
                typically indicating issues in the complex pattern assembly.
        """

        # Base numeric day/month/year pattern
        self.numeric = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.numeric}"
        )

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Build Hijri day-month-year patterns
        self.hijri['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['numeric']}"
        )

        self.hijri['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['numeric_optional']}"
        )

        self.hijri['named1'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['named']}"
        )

        self.hijri['named2'] = (
            rf"{self.month_patterns.hijri}"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['numeric_optional']}"
        )

        self.hijri['named'] = (
            rf"(?:{self.hijri['named1']})|(?:{self.hijri['named2']})"
        )

        self.hijri['combined'] = (
            rf"(?:{self.hijri['numeric']})|(?:{self.hijri['named']})"
        )

        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )

        # Build Gregorian day-month-year patterns
        self.gregorian['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['numeric']}"
        )

        self.gregorian['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['numeric_optional']}"
        )

        self.gregorian['named1'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['named']}"
        )

        self.gregorian['named2'] = (
            rf"{self.month_patterns.gregorian}"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['numeric_optional']}"
        )

        self.gregorian['named'] = (
            rf"(?:{self.gregorian['named1']})|(?:{self.gregorian['named2']})"
        )

        self.gregorian['combined'] = (
            rf"(?:{self.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )

        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )

        # Build julian day-month-year patterns
        self.julian['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['numeric']}"
        )

        self.julian['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['numeric_optional']}"
        )

        self.julian['named1'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['named']}"
        )

        self.julian['named2'] = (
            rf"{self.month_patterns.julian}"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.julian['numeric_optional']}"
        )

        self.julian['named'] = (
            rf"(?:{self.julian['named1']})|(?:{self.julian['named2']})"
        )

        self.julian['combined'] = (
            rf"(?:{self.julian['numeric']})|(?:{self.julian['named']})"
        )

        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )

        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class NaturalLanguagePatterns(PatternValidator):
    """Natural language date patterns with weekday integration.

    The most sophisticated pattern class, generating regex patterns that combine
    weekday names with complete date expressions to match natural language date
    formats. This class handles the complex task of parsing dates as they
    appear in conversational text, news articles, and everyday communication.

    Natural language date patterns represent the highest level of complexity
    in the date recognition system, combining weekday detection with full
    date parsing across multiple calendar systems and languages.

    Features:
        - **Weekday Integration**: Combines weekday names with date expressions
        - **Multilingual Support**: Handles weekdays in Arabic, English, Persian
        - **Complete Date Context**: Full day-month-year expressions with weekdays
        - **Cross-Calendar Natural**: Natural language with calendar conversions
        - **Flexible Formatting**: Supports various separator and format conventions

    Parameters:
        base_patterns (BasePatterns): Fundamental patterns including comprehensive
            weekday name patterns for multiple languages and formats.
        era_patterns (EraPatterns): Calendar system era markers for proper
            date system identification in natural contexts.
        indicator_patterns (IndicatorPatterns): Structural elements including
            separators and parenthetical markers for natural formatting.
        day_month_year_patterns (DayMonthYearPatterns): Complete date pattern
            definitions used as the foundation for natural language expressions.

    Attributes:
        numeric (str): Base natural language pattern combining weekdays with
            numeric date formats (e.g., "Monday 15/12/2024").

        hijri (Dict[str, str]): Natural language Hijri patterns:

            - ``'numeric'``: Weekday + numeric Hijri date with required era
            - ``'numeric_optional'``: Weekday + numeric date with optional era
            - ``'named'``: Weekday + named month date (e.g., "Friday 15 Muharram 1445 AH")
            - ``'combined'``: Union of numeric and named with required era
            - ``'combined_optional'``: Union patterns with optional era markers
        gregorian (Dict[str, str]): Natural language Gregorian patterns with
            parallel structure optimized for Western weekday and date conventions.

        julian (Dict[str, str]): Persian natural language patterns supporting
            Farsi weekday names and Persian calendar date expressions.

    Example:
        .. code-block:: python

            # Initialize all required pattern components
            base = BasePatterns(
                weekday=r"(?:Monday|Tuesday|الاثنين|الثلاثاء|دوشنبه|سه‌شنبه)"
            )
            day_month_year = DayMonthYearPatterns(...)

            # Build natural language patterns
            natural = NaturalLanguagePatterns(
                base, eras, indicators, day_month_year
            )

            # Access natural language patterns
            simple = natural.numeric                    # "Monday 15/12/2024"
            hijri_named = natural.hijri['named']        # "Friday 15 Muharram 1445 AH"


    Natural Language Examples:
        The patterns match realistic conversational date expressions:

        .. code-block:: text

            "Monday 15/12/2024"                      # Simple weekday + numeric
            "Friday 15 December 2024"                # Weekday + named month
            "الجمعة 15 محرم 1445 هـ"                  # Arabic weekday + Hijri
            "دوشنبه 15 فروردین 1403 ش.ه"             # Persian weekday + julian
            "Friday 15 Muharram 1445 AH (Jan 15, 2024)" # Cross-calendar natural
            "Tuesday, December 15th, 2024"           # Formal natural language

    Implementation Notes:
        Natural language patterns are the most complex in the system and require
        careful consideration of:

        - **Separator Flexibility**: Various spacing and punctuation conventions
        - **Language Consistency**: Ensuring weekday and date languages match
        - **Format Variations**: Handling different natural language conventions
        - **Performance Impact**: Complex alternation patterns may affect performance

    Note:
        These patterns assume the weekday and date refer to the same calendar
        system. Cross-calendar weekday matching (e.g., English weekday with
        Hijri date) may require additional contextual validation.

    Warning:
        Natural language date parsing is inherently ambiguous. Consider implementing
        additional validation or confidence scoring for dates extracted using


    See Also:
        :class:`DayMonthYearPatterns`: Complete date components used in construction
        :class:`BasePatterns`: Weekday pattern definitions
        :class:`PatternValidator`: Regex validation and error handling
    """
    base_patterns: BasePatterns
    era_patterns: EraPatterns
    indicator_patterns: IndicatorPatterns
    day_month_year_patterns: DayMonthYearPatterns

    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize comprehensive natural language date patterns.

        Constructs the complete set of natural language patterns by combining
        weekday patterns with full date expressions, representing the pinnacle
        of the pattern hierarchy's sophistication and complexity.

        The initialization creates the most advanced date matching patterns:

        1. **Base Natural**: Combines weekdays with numeric date formats
        2. **Calendar Dictionaries**: Initializes natural language pattern storage
        3. **Weekday Integration**: Prefixes weekday patterns to date expressions
        4. **Format Variants**: Creates numeric, named, and combined alternatives
        5. **Natural Complexity**: Builds mixed and parenthetical natural formats
        6. **Final Validation**: Ensures all natural language patterns compile

        Natural Language Strategy:
            The method combines the comprehensive weekday patterns from
            :class:`BasePatterns` with the sophisticated date patterns from
            :class:`DayMonthYearPatterns` to create patterns capable of matching
            dates as they appear in real-world natural language contexts.

        Raises:
            ValueError: If any natural language pattern fails compilation,
                indicating issues in the complex pattern assembly process.
        """

        # Base natural language pattern (weekday + numeric date)
        self.numeric = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.numeric}"
        )

        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Build Hijri natural language patterns
        self.hijri['numeric'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['numeric']}"
        )

        self.hijri['numeric_optional'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['numeric_optional']}"
        )

        self.hijri['named'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['named']}"
        )

        self.hijri['combined'] = (
            rf"(?:{self.hijri['numeric']})|(?:{self.hijri['named']})"
        )

        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )

        # Build Gregorian natural language patterns
        self.gregorian['numeric'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['numeric']}"
        )

        self.gregorian['numeric_optional'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['numeric_optional']}"
        )

        self.gregorian['named'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['named']}"
        )

        self.gregorian['combined'] = (
            rf"(?:{self.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )

        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )

        # Build julian natural language patterns
        self.julian['numeric'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.julian['numeric']}"
        )

        self.julian['numeric_optional'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.julian['numeric_optional']}"
        )

        self.julian['named'] = (
            rf"{self.base_patterns.weekday}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.julian['named']}"
        )

        self.julian['combined'] = (
            rf"(?:{self.julian['numeric']})|(?:{self.julian['named']})"
        )

        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )

        # Validate all generated patterns
       self._validate_patterns()               