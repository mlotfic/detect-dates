*-

"""
Complex Date Pattern Recognition Module
=======================================

Advanced date pattern recognition module that builds upon composite patterns
to create highly sophisticated regex patterns for complex date scenarios.
This module handles nested patterns, multi-level calendar conversions,
and intricate date range expressions across multiple calendar systems.

This module defines complex dataclasses that compose multiple layers of
pattern complexity, enabling recognition of elaborate date expressions
found in formal documents, academic papers, and multilingual texts.

.. moduleauthor:: Anonymous
.. versionadded:: 1.0.0
.. versionchanged:: 1.0.0
   Initial implementation with multi-layered pattern complexity

Example:
    Creating complex pattern hierarchies::

        from complex_dataclass import ComplexYearPatterns
        from composite_dataclass import CompositeYearPatterns
        
        # Initialize composite patterns first
        composite = CompositeYearPatterns(year_patterns, indicator_patterns)
        
        # Build complex patterns on top
        complex_patterns = ComplexYearPatterns(composite, indicator_patterns)
        
        # Access nested mixed patterns
        pattern = complex_patterns.hijri['mixed']

Warning:
    These complex patterns can generate very long regex expressions.
    Consider performance implications when processing large text corpora.

Note:
    This module requires all base, mixin, and composite dataclass modules
    to be properly imported and initialized before use.

.. seealso::
   :mod:`base_dataclass`: Foundational pattern definitions
   :mod:`mixin_dataclass`: Mixin pattern components
   :mod:`composite_dataclass`: Composite pattern building blocks

:copyright: 2025, Anonymous
:license: MIT
"""

import re
from dataclasses import dataclass
from typing import Optional, Dict, Any, Union

# Base Pattern Classes
from base_dataclass import (
    BasePatterns,
    MonthPatterns,
    EraPatterns,
    IndicatorPatterns,
    NumericPatterns
)

# Mixin Pattern Classes
from mixin_dataclass import (
    PatternValidator,
    CenturyPatterns,
    YearPatterns,
    MonthYearPatterns,
    DayMonthYearPatterns,
    NaturalLanguagePatterns
)

# Composite Pattern Classes
from composite_dataclass import (
    CompositeYearPatterns,
    CompositeMonthYearPatterns,
    CompositeDayMonthYearPatterns,
    CompositeNaturalLanguagePatterns
)


@dataclass
class ComplexYearPatterns(PatternValidator):
    """
    Complex year patterns with nested composite pattern integration.
    
    This class creates sophisticated year pattern combinations by layering
    composite patterns to handle complex scenarios like nested parenthetical
    expressions, multi-level calendar conversions, and intricate year ranges
    spanning different calendar systems.
    
    The class generates advanced patterns for:
    
    * Nested mixed patterns: "1445-1446 / 2024-2025" (dual calendar ranges)
    * Complex alternatives: "1445 (2024) - 1446 (2025)" (parenthetical ranges)
    * Multi-level expressions: "(1445 AH) - (2024 AD)" (era-specific ranges)
    * Compound separations: "1445/1446 هـ - 2024/2025 م" (multi-separator)
    
    Parameters
    ----------
    year_patterns : CompositeYearPatterns
        Pre-built composite year patterns serving as building blocks
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
        
    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing complex Hijri calendar year patterns:
        
        * 'mixed': Nested mixed Hijri year patterns for complex ranges
        * 'alternative': Multi-layered Hijri-Gregorian alternative patterns
        * 'alternative_parenthetical': Dual parenthetical expressions with separators
        
    gregorian : Dict[str, str]
        Dictionary containing complex Gregorian calendar year patterns:
        
        * 'mixed': Nested mixed Gregorian year patterns for complex ranges
        * 'alternative': Multi-layered Gregorian-Hijri alternative patterns
        
    Examples
    --------
    >>> from complex_dataclass import ComplexYearPatterns
    >>> from composite_dataclass import CompositeYearPatterns
    >>> 
    >>> # Build the pattern hierarchy
    >>> composite = CompositeYearPatterns(base_year_patterns, indicators)
    >>> complex_patterns = ComplexYearPatterns(composite, indicators)
    >>> 
    >>> # Match complex year expressions
    >>> pattern = complex_patterns.hijri['alternative_parenthetical']
    >>> text = "(1445 هـ) - (2024 م)"
    >>> match = re.search(pattern, text)
    >>> if match:
    ...     print(f"Found complex year pattern: {match.group()}")
    
    Notes
    -----
    These patterns are designed for processing academic papers, legal documents,
    and formal texts where complex date expressions are common. The nested
    structure allows for matching expressions that span multiple lines or
    contain embedded formatting.
    
    Performance considerations should be taken into account when using these
    patterns on large text corpora due to their complexity.
    
    See Also
    --------
    CompositeYearPatterns : Foundation composite year patterns
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    year_patterns: CompositeYearPatterns
    indicator_patterns: IndicatorPatterns
    
    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    
    def __post_init__(self) -> None:
        """
        Initialize complex year patterns with multi-layered composition.
        
        This method creates sophisticated pattern combinations by nesting
        composite patterns within complex structures, enabling recognition
        of elaborate year expressions with multiple levels of calendar
        conversion and formatting variations.
        
        The initialization process builds patterns that can handle:
        - Nested parenthetical expressions with multiple calendar systems
        - Complex range expressions spanning different eras
        - Multi-separator patterns for formal document formats
        
        Raises
        ------
        ValidationError
            If any of the generated complex regex patterns are invalid
        RegexComplexityError
            If patterns exceed recommended complexity thresholds
        """
        
        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        
        # Build Hijri Mixed Year Patterns (financial year, range, etc.)        
        self.hijri['mixed'] = (
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['mixed']}"
        )
        
        self.hijri['mixed_parenthetical'] = (
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}"
            rf"\s*{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['mixed_double_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}"
            rf"\s*{self.indicator_patterns.parentheses_end}"
        )
        
        
        # Build Hijri Alternative Year Patterns
        self.hijri['mixed_alternative'] = (
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['mixed']}"
        )
        
        # Build Hijri Alternative Year Patterns
        self.hijri['mixed_alternative_parenthetical'] = (
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Hijri Alternative Year Patterns
        self.hijri['mixed_alternative_dual_parenthetical1'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Hijri Alternative Year Patterns
        self.hijri['alternative'] = (
            rf"{self.year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['alternative']}"
        )
        
        self.hijri['alternative_parenthetical'] = (
            rf"{self.year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['alternative_dual_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian year patterns        
        self.gregorian['mixed'] = (
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.gregorian['mixed']}"
        )
        
        self.gregorian['mixed_parenthetical'] = (
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['mixed_dual_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian alternative year patterns
        self.gregorian['mixed_alternative'] = (
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['mixed']}"
        )
        
        self.gregorian['mixed_alternative_parenthetical'] = (
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['mixed_alternative_dual_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian alternative year patterns
        self.gregorian['alternative'] = (
            rf"{self.year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.year_patterns.hijri['alternative']}"
        )
        
        self.gregorian['alternative_parenthetical'] = (
            rf"{self.year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['alternative_dual_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )         
        
        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class ComplexMonthYearPatterns(PatternValidator):
    """
    Complex month-year patterns with advanced composite integration.
    
    This class creates sophisticated month-year pattern combinations that handle
    complex scenarios involving nested expressions, multi-calendar month-year
    ranges, and intricate formatting found in academic and formal documents.
    
    The class generates advanced patterns for:
    
    * Nested month-year ranges: "Muharram 1445 - Safar 1445 / January 2024 - February 2024"
    * Complex parenthetical: "(Muharram 1445) - (January 2024)" 
    * Multi-format expressions: "01/1445 هـ - January 2024 AD"
    * Compound separations: "محرم 1445 / يناير 2024" (bilingual month-year)
    
    Parameters
    ----------
    month_year_patterns : CompositeMonthYearPatterns
        Pre-built composite month-year patterns serving as building blocks
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
        
    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing complex Hijri calendar month-year patterns:
        
        * 'mixed': Nested mixed Hijri month-year patterns for complex ranges
        * 'alternative': Multi-layered Hijri-Gregorian month-year alternatives
        * 'alternative_parenthetical': Dual parenthetical month-year expressions
        
    gregorian : Dict[str, str]
        Dictionary containing complex Gregorian calendar month-year patterns:
        
        * 'mixed': Nested mixed Gregorian month-year patterns for complex ranges
        * 'alternative': Multi-layered Gregorian-Hijri month-year alternatives
        * 'alternative_parenthetical': Dual parenthetical month-year expressions
        
    Examples
    --------
    >>> from complex_dataclass import ComplexMonthYearPatterns
    >>> 
    >>> # Initialize with composite foundation
    >>> composite = CompositeMonthYearPatterns(base_patterns, indicators)
    >>> complex_patterns = ComplexMonthYearPatterns(composite, indicators)
    >>> 
    >>> # Match complex month-year expressions
    >>> pattern = complex_patterns.hijri['alternative_parenthetical']
    >>> text = "(محرم 1445 هـ) - (January 2024 AD)"
    >>> matches = re.findall(pattern, text)
    
    Notes
    -----
    These patterns excel at processing bilingual documents, academic papers
    with mixed calendar references, and formal correspondence requiring
    precise month-year identification across calendar systems.
    
    The parenthetical patterns are particularly useful for documents that
    provide calendar conversions in a structured format.
    
    See Also
    --------
    CompositeMonthYearPatterns : Foundation composite month-year patterns
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    month_year_patterns: CompositeMonthYearPatterns
    indicator_patterns: IndicatorPatterns 
    
    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    
    def __post_init__(self) -> None:
        """
        Initialize complex month-year patterns with nested composition.
        
        This method builds sophisticated month-year pattern combinations that
        can handle multi-layered expressions, parenthetical conversions, and
        complex range specifications commonly found in formal documents.
        
        The patterns are designed to capture:
        - Dual parenthetical month-year expressions
        - Complex alternative calendar representations
        - Multi-separator month-year ranges
        
        Raises
        ------
        ValidationError
            If any of the generated complex regex patterns are invalid
        """
        
        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        
        self.hijri['mixed'] = (
            rf"{self.month_year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['mixed']}"
        )
        
        self.hijri['alternative'] = (
            rf"{self.month_year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['alternative']}"
        )
        
        self.hijri['alternative_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian month-year patterns
        self.gregorian['mixed'] = (
            rf"{self.month_year_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['mixed']}"
        )
        
        self.gregorian['alternative'] = (
            rf"{self.month_year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['alternative']}"
        )
        
        self.gregorian['alternative_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.month_year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class ComplexDayMonthYearPatterns(PatternValidator):
    """
    Complex complete date patterns with sophisticated composite integration.
    
    This class creates the most sophisticated date pattern combinations,
    handling complex scenarios with full day-month-year expressions across
    multiple calendar systems. It builds upon composite patterns to create
    intricate regex patterns for formal documents and academic texts.
    
    The class generates advanced patterns for:
    
    * Complex date ranges: "15 Muharram 1445 - 20 Muharram 1445 / 25 January 2024 - 30 January 2024"
    * Nested parenthetical dates: "(15 محرم 1445 هـ) - (25 January 2024 AD)"
    * Multi-format expressions: "15/01/1445 هـ - 25 January 2024"
    * Academic citations: "(15 Muharram 1445 AH / 25 January 2024 AD)"
    
    Parameters
    ----------
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
    day_month_year_patterns : CompositeDayMonthYearPatterns
        Pre-built composite complete date patterns serving as building blocks
        
    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing complex Hijri calendar complete date patterns:
        
        * 'mixed': Nested mixed Hijri complete date patterns for complex ranges
        * 'alternative': Multi-layered Hijri-Gregorian complete date alternatives
        * 'alternative_parenthetical': Dual parenthetical complete date expressions
        
    gregorian : Dict[str, str]
        Dictionary containing complex Gregorian calendar complete date patterns:
        
        * 'mixed': Nested mixed Gregorian complete date patterns
        * 'alternative': Multi-layered Gregorian-Hijri complete date alternatives
        
    Examples
    --------
    >>> from complex_dataclass import ComplexDayMonthYearPatterns
    >>> 
    >>> # Build pattern hierarchy
    >>> composite = CompositeDayMonthYearPatterns(indicators, base_dmy_patterns)
    >>> complex_patterns = ComplexDayMonthYearPatterns(indicators, composite)
    >>> 
    >>> # Match academic citation formats
    >>> pattern = complex_patterns.hijri['alternative_parenthetical']
    >>> citation = "The event occurred on (15 محرم 1445 هـ) - (25 January 2024 AD)"
    >>> matches = re.findall(pattern, citation)
    
    Notes
    -----
    These patterns are specifically designed for processing academic papers,
    legal documents, historical texts, and formal correspondence where
    precise date identification with calendar conversions is critical.
    
    The complexity of these patterns makes them suitable for specialized
    applications but may impact performance on large text processing tasks.
    
    See Also
    --------
    CompositeDayMonthYearPatterns : Foundation composite complete date patterns
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    indicator_patterns: IndicatorPatterns 
    day_month_year_patterns: CompositeDayMonthYearPatterns
    
    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
        
    def __post_init__(self) -> None:
        """
        Initialize complex complete date patterns with advanced composition.
        
        This method creates the most sophisticated date pattern combinations,
        building upon composite patterns to handle complex parenthetical
        expressions, nested calendar conversions, and multi-layered date
        representations found in academic and formal contexts.
        
        The patterns can handle:
        - Dual parenthetical complete date expressions
        - Complex alternative calendar date representations
        - Multi-separator complete date ranges with era indicators
        
        Raises
        ------
        ValidationError
            If any of the generated complex regex patterns are invalid
        """
        
        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        
        # Build Hijri day-month-year patterns
        self.hijri['mixed'] = (
            rf"{self.day_month_year_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.hijri['mixed']}"
        )
        
        self.hijri['alternative'] = (
            rf"{self.day_month_year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.day_month_year_patterns.gregorian['alternative']}"
        )
        
        self.hijri['alternative_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.day_month_year_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class ComplexNaturalLanguagePatterns(PatternValidator):
    """
    Complex natural language date patterns with advanced linguistic integration.
    
    This class creates the most sophisticated natural language date pattern
    combinations, handling complex scenarios with weekday integration, natural
    language expressions, and multi-cultural date representations across
    different calendar systems and languages.
    
    The class generates advanced patterns for:
    
    * Complex natural ranges: "من الاثنين 15 محرم 1445 إلى الجمعة 25 يناير 2024"
    * Bilingual expressions: "Monday 15 Muharram 1445 AH - الاثنين 25 يناير 2024"  
    * Nested parenthetical: "(الجمعة 15 محرم 1445 هـ) - (Friday 25 January 2024 AD)"
    * Academic natural language: "The period from (Monday, 15 Muharram 1445 AH) to (Friday, 25 January 2024 AD)"
    
    Parameters
    ----------
    indicator_patterns : IndicatorPatterns
        Date indicator patterns including separators and parentheses
    natural_language_patterns : CompositeNaturalLanguagePatterns
        Pre-built composite natural language patterns with weekday integration
        
    Attributes
    ----------
    hijri : Dict[str, str]
        Dictionary containing complex Hijri natural language patterns:
        
        * 'mixed': Nested mixed Hijri natural language patterns for complex expressions
        * 'alternative': Multi-layered Hijri-Gregorian natural language alternatives
        * 'alternative_parenthetical': Dual parenthetical natural language expressions
        
    gregorian : Dict[str, str]
        Dictionary containing complex Gregorian natural language patterns:
        
        * 'mixed': Nested mixed Gregorian natural language patterns
        * 'alternative': Multi-layered Gregorian-Hijri natural language alternatives  
        * 'alternative_parenthetical': Dual parenthetical natural language expressions
        
    Examples
    --------
    >>> from complex_dataclass import ComplexNaturalLanguagePatterns
    >>> 
    >>> # Initialize pattern hierarchy
    >>> composite = CompositeNaturalLanguagePatterns(indicators, base_nl_patterns)
    >>> complex_patterns = ComplexNaturalLanguagePatterns(indicators, composite)
    >>> 
    >>> # Match bilingual natural language expressions
    >>> pattern = complex_patterns.hijri['alternative']
    >>> text = "الاجتماع يوم الاثنين 15 محرم 1445 هـ - Monday 25 January 2024 AD"
    >>> matches = re.findall(pattern, text)
    
    Notes
    -----
    These patterns are ideal for processing multilingual documents, diplomatic
    correspondence, international academic papers, and cross-cultural texts
    where natural language date expressions span multiple calendar systems.
    
    The patterns handle both Arabic-English and other language combinations,
    making them suitable for global document processing applications.
    
    Performance should be considered when processing large multilingual corpora
    due to the sophisticated nature of these pattern combinations.
    
    See Also
    --------
    CompositeNaturalLanguagePatterns : Foundation composite natural language patterns
    IndicatorPatterns : Date indicator patterns
    PatternValidator : Pattern validation mixin
    """
    indicator_patterns: IndicatorPatterns 
    natural_language_patterns: CompositeNaturalLanguagePatterns
    
    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
        
    def __post_init__(self) -> None:
        """
        Initialize complex natural language patterns with multilingual support.
        
        This method creates the most sophisticated natural language date
        pattern combinations, building upon composite patterns to handle
        complex bilingual expressions, nested parenthetical natural language
        dates, and multi-cultural date representations.
        
        The patterns support:
        - Bilingual weekday-date expressions
        - Complex parenthetical natural language conversions
        - Multi-separator natural language date ranges
        - Academic citation style natural language dates
        
        Raises
        ------
        ValidationError
            If any of the generated complex regex patterns are invalid
        """
        
        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        
        # Build Hijri natural language patterns
        self.hijri['mixed'] = (
            rf"{self.natural_language_patterns.hijri['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.hijri['mixed']}"
        )
        
        self.hijri['alternative'] = (
            rf"{self.natural_language_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.gregorian['alternative']}"
        )
        
        self.hijri['alternative_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian natural language patterns
        self.gregorian['mixed'] = (
            rf"{self.natural_language_patterns.gregorian['mixed']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.gregorian['mixed']}"
        )
        
        self.gregorian['alternative'] = (
            rf"{self.natural_language_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.natural_language_patterns.hijri['alternative']}"
        )
        
        self.gregorian['alternative_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.gregorian['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.natural_language_patterns.hijri['alternative']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()

