

"""
Date Pattern Recognition Module
===============================
This module provides a comprehensive set of date patterns for various calendars,

.. moduleauthor:: m.lotfi
.. versionadded:: 1.0.0
.. versionchanged:: 1.0.0
   Initial implementation with multi-calendar support
:copyright: 2023, m.lotfi
:license: MIT
"""

# ===============================
# Module Exports
# ===============================
# Base Pattern Classes
from detect_dates.patterns import (
    BasePatterns,
    MonthPatterns,
    EraPatterns,
    IndicatorPatterns,
    NumericPatterns,
    CenturyPatterns,
    YearPatterns,
    MonthYearPatterns,
    DayMonthYearPatterns,
    NaturalLanguagePatterns,
    CompositeYearPatterns,
    CompositeMonthYearPatterns,
    CompositeDayMonthYearPatterns,
    CompositeNaturalLanguagePatterns,
    ComplexYearPatterns,
    ComplexMonthYearPatterns,
    ComplexDayMonthYearPatterns,
    ComplexNaturalLanguagePatterns,
    CompositeNumericPatterns
)

# Import constants/patterns
from detect_dates.regex_patterns import (
    get_era_pattern,  # Era pattern matching
    get_month_pattern,  # Month pattern matching
    get_day_pattern,  # Day pattern matching
    get_year_pattern,  # Year pattern matching
    get_century_pattern,  # Century pattern matching
    get_day_indicator_pattern,  # Day indicators
    get_month_indicator_pattern,  # Month indicators
    get_year_indicator_pattern,  # Year indicators
    get_separator_pattern,  # Date separators
    get_range_connector_pattern,  # Date range connectors
    get_range_starter_pattern,  # Date range starters
    get_date_patterns,  # Function to get all date patterns
)

class DatePatterns:
    """Main class to encapsulate all date patterns"""
    
    def __init__(self, lang = 'ar'):
        """
        Initializes the DatePatterns class with language-specific patterns.
        :param lang: Language code for the patterns (default is 'ar' for Arabic)
        """
        
        # Load language-specific patterns
        self.base_patterns, self.month_patterns, self.era_patterns, self.indicator_patterns, self.numeric_patterns = get_date_patterns(lang)
        
        # Initialize composite and complex patterns
        self.composite_year_patterns = CompositeYearPatterns(
            year_patterns=self.numeric_patterns,
            indicator_patterns=self.indicator_patterns
        )
        self.composite_month_year_patterns = CompositeMonthYearPatterns(
            month_patterns=self.month_patterns,
            year_patterns=self.numeric_patterns,
            indicator_patterns=self.indicator_patterns
        )
        self.composite_day_month_year_patterns = CompositeDayMonthYearPatterns(
            day_patterns=self.numeric_patterns,
            month_patterns=self.month_patterns,
            year_patterns=self.numeric_patterns,
            indicator_patterns=self.indicator_patterns
        )
        self.composite_natural_language_patterns = CompositeNaturalLanguagePatterns(
            natural_language_patterns=NaturalLanguagePatterns(),
            month_patterns=self.month_patterns,
            year_patterns=self.numeric_patterns
        )
        
        # Initialize complex patterns
        self.complex_year_patterns = ComplexYearPatterns(
            composite_year_patterns=self.composite_year_patterns
        )
        self.complex_month_year_patterns = ComplexMonthYearPatterns(
            composite_month_year_patterns=self.composite_month_year_patterns
        )
        self.complex_day_month_year_patterns = ComplexDayMonthYearPatterns(
            composite_day_month_year_patterns=self.composite_day_month_year_patterns
        )
        self.complex_natural_language_patterns = ComplexNaturalLanguagePatterns(
            composite_natural_language_patterns=self.composite_natural_language_pattern