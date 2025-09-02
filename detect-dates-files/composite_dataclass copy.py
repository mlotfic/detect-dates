#!/usr/bin/env python3*-

"""
Created on Thu Jul 24 20:01:16 2025



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

@dataclass
class CompositeYearPatterns(PatternValidator):
    """
    Year patterns for different calendar systems.
    
    Handles standalone year patterns like:
    - "1445" (numeric only)
    - "1445 AH" (Hijri with era)
    - "2024 AD" (Gregorian with era)
    - "1403 ش.ه" (julian with era)
    
    Attributes:
        numeric_patterns (NumericPatterns): Basic numeric patterns
        indicator_patterns (IndicatorPatterns): Date indicator patterns  
        era_patterns (EraPatterns): Era indicator patterns
        hijri (Dict[str, str]): Hijri year patterns
        gregorian (Dict[str, str]): Gregorian year patterns
        julian (Dict[str, str]): julian year patterns
    """
    year_patterns: YearPatterns
    indicator_patterns: IndicatorPatterns
    
    # Calendar-specific pattern dictionaries
    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None
    
    def __post_init__(self):
        """Initialize all year patterns after dataclass creation."""
        
        # Initialize calendar-specific dictionaries
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}
        
        # Build Hijri Mixed Year Patterns (financial year, range, etc.)        
        self.hijri['mixed'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.hijri['numeric']}"
        )
        
        self.hijri['alternative_g'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.gregorian['numeric']}"
        )
        
        self.hijri['alternative_s'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.julian['numeric']}"
        )
        
        self.hijri['complex_mixed_parenthetical'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['mixed_tricky']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['mixed_tricky']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
        )
        
        self.hijri['complex_mixed_parenthetical_g'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['g_mixed_clear']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['g_mixed_clear']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
        )
        
        self.hijri['complex_mixed_parenthetical_s'] = (
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['s_mixed_clear']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
            rf"{self.indicator_patterns.separator}\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{self.hijri['s_mixed_clear']}\s*"
            rf"{self.indicator_patterns.parentheses_end}\s*"
        )

        self.hijri['hh_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hg_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hs_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['range'] = (
            rf"{self.indicator_patterns.range_starter}\s*"
            rf"{self.hijri['numeric_optional']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{year_patterns.hijri['numeric']}"
        )
        
        self.hijri['range_parenthetical'] = (
            rf"{self.indicator_patterns.range_starter}\s*"
            rf"{self.hijri['numeric_optional']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['range_mixed'] = (
            rf"{self.indicator_patterns.range_starter}\s*"
            rf"{self.hijri['mixed_tricky']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.hijri['mixed_tricky']}\s*"
        )
        
        self.hijri['range_mixed_g'] = (
            rf"{self.indicator_patterns.range_starter}\s*"
            rf"{self.hijri['g_mixed_clear']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.hijri['g_mixed_clear']}\s*"
        )
        
        self.hijri['range_mixed_s'] = (
            rf"{self.indicator_patterns.range_starter}\s*"
            rf"{self.hijri['s_mixed_clear']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.hijri['s_mixed_clear']}\s*"
        ) 
        
        # Build Gregorian year patterns
        year_patterns.gregorian['numeric'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.gregorian}"
        )
        
        self.gregorian['numeric_optional'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.gregorian})?"
        )
        
        self.gregorian['mixed_clear'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.gregorian['numeric']}"
        )
        
        self.gregorian['mixed_tricky'] = (
            rf"{self.gregorian['numeric_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.gregorian['numeric']}"
        )
        
        self.gregorian['gg_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gh_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gs_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build julian year patterns
        year_patterns.julian['numeric'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.era_patterns.julian}"
        )
        
        self.julian['numeric_optional'] = (
            rf"{self.numeric_patterns.year}\s*"
            rf"{self.indicator_patterns.separator}?\s*(?:{self.era_patterns.julian})?"
        )
        
        self.julian['mixed_clear'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.julian['numeric']}"
        )
        
        self.julian['mixed_tricky'] = (
            rf"{self.julian['numeric_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{year_patterns.julian['numeric']}"
        )
        
        self.julian['ss_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sh_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sg_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class CompositeMonthYearPatterns(PatternValidator):
    """
    Month-Year patterns for different calendar systems.
    
    Handles month-year combinations like:
    - "12/2024" (numeric month/year)
    - "December 2024" (named month year)
    - "Muharram 1445 AH" (named Hijri month with era)
    
    Attributes:
        numeric_patterns (NumericPatterns): Basic numeric patterns
        year_patterns (YearPatterns): Year pattern definitions
        month_patterns (MonthPatterns): Month name patterns
        era_patterns (EraPatterns): Era indicator patterns
        indicator_patterns (IndicatorPatterns): Date indicator patterns
        hijri (Dict[str, str]): Hijri month-year patterns
        gregorian (Dict[str, str]): Gregorian month-year patterns  
        julian (Dict[str, str]): julian month-year patterns
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
        """Initialize all month-year patterns after dataclass creation."""
        
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
        year_patterns.hijri['numeric'] = (
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
            rf"(?:{year_patterns.hijri['numeric']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['mixed_clear'] = (
            rf"{self.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['mixed_tricky'] = (
            rf"{self.hijri['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['hh_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hg_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hs_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian month-year patterns
        year_patterns.gregorian['numeric'] = (
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
            rf"(?:{year_patterns.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['mixed_clear'] = (
            rf"{self.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
                
        self.gregorian['mixed_tricky'] = (
            rf"{self.gregorian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
        
        self.gregorian['gg_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gh_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gs_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build julian month-year patterns
        year_patterns.julian['numeric'] = (
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
            rf"(?:{year_patterns.julian['numeric']})|(?:{self.julian['named']})"
        )
        
        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )
        
        self.julian['mixed_clear'] = (
            rf"{self.julian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['mixed_tricky'] = (
            rf"{self.julian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['ss_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sh_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sg_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()


@dataclass
class CompositeDayMonthYearPatterns(PatternValidator):
    """
    Day-Month-Year patterns for different calendar systems.
    
    Handles complete date patterns like:
    - "15/12/2024" (numeric day/month/year)
    - "15 December 2024" (numeric day with named month)
    - "15 Muharram 1445 AH" (complete Hijri date)
    
    Attributes:
        numeric_patterns (NumericPatterns): Basic numeric patterns
        year_patterns (YearPatterns): Year pattern definitions
        month_patterns (MonthPatterns): Month name patterns
        era_patterns (EraPatterns): Era indicator patterns
        indicator_patterns (IndicatorPatterns): Date indicator patterns
        month_year_patterns (MonthYearPatterns): Month-year pattern combinations
        hijri (Dict[str, str]): Hijri day-month-year patterns
        gregorian (Dict[str, str]): Gregorian day-month-year patterns
        julian (Dict[str, str]): julian day-month-year patterns
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
        """Initialize all day-month-year patterns after dataclass creation."""
        
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
        year_patterns.hijri['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['numeric']}"
        )
        
        self.hijri['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['numeric_optional']}"
        )
        
        self.hijri['named'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.hijri['named']}"
        )
        
        self.hijri['combined'] = (
            rf"(?:{year_patterns.hijri['numeric']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['mixed_clear'] = (
            rf"{self.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['mixed_tricky'] = (
            rf"{self.hijri['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['hh_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hg_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hs_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build Gregorian day-month-year patterns
        year_patterns.gregorian['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['numeric']}"
        )
        
        self.gregorian['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['numeric_optional']}"
        )
        
        self.gregorian['named'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.gregorian['named']}"
        )
        
        self.gregorian['combined'] = (
            rf"(?:{year_patterns.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['mixed_clear'] = (
            rf"{self.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
        
        self.gregorian['mixed_tricky'] = (
            rf"{self.gregorian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
        
        self.gregorian['gg_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"  
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gh_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"  
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )   
        
        self.gregorian['gs_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build julian day-month-year patterns
        year_patterns.julian['numeric'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['numeric']}"
        )
        
        self.julian['numeric_optional'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['numeric_optional']}"
        )
        
        self.julian['named'] = (
            rf"{self.numeric_patterns.day}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.month_year_patterns.julian['named']}"
        )
        
        self.julian['combined'] = (
            rf"(?:{year_patterns.julian['numeric']})|(?:{self.julian['named']})"
        )
        
        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )
        
        self.julian['mixed_clear'] = (
            rf"{self.julian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['mixed_tricky'] = (
            rf"{self.julian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['ss_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sh_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sg_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()

@dataclass
class CompositeNaturalLanguagePatterns(PatternValidator):
    """
    Natural language date patterns combining weekdays with dates.
    
    Handles natural language date expressions like:
    - "Monday 15/12/2024" (weekday + numeric date)
    - "Friday 15 December 2024" (weekday + named month date)
    - "الجمعة 15 محرم 1445 هـ" (Arabic weekday + Hijri date)
    
    Attributes:
        base_patterns (BasePatterns): Base patterns including weekdays
        era_patterns (EraPatterns): Era indicator patterns
        indicator_patterns (IndicatorPatterns): Date indicator patterns
        day_month_year_patterns (DayMonthYearPatterns): Complete date patterns
        hijri (Dict[str, str]): Hijri natural language patterns
        gregorian (Dict[str, str]): Gregorian natural language patterns
        julian (Dict[str, str]): julian natural language patterns
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
        """Initialize all natural language patterns after dataclass creation."""
        
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
        year_patterns.hijri['numeric'] = (
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
            rf"(?:{year_patterns.hijri['numeric']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )
        
        self.hijri['mixed_clear'] = (
            rf"{self.hijri['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['mixed_tricky'] = (
            rf"{self.hijri['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.hijri['combined']}"
        )
        
        self.hijri['hh_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hg_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.hijri['hs_parenthetical'] = (
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
                        
        # Build Gregorian natural language patterns
        year_patterns.gregorian['numeric'] = (
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
            rf"(?:{year_patterns.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )
        
        self.gregorian['mixed_clear'] = (
            rf"{self.gregorian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
        
        self.gregorian['mixed_tricky'] = (
            rf"{self.gregorian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.gregorian['combined']}"
        )
        
        self.gregorian['gg_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gh_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.gregorian['gs_parenthetical'] = (
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Build julian natural language patterns
        year_patterns.julian['numeric'] = (
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
            rf"(?:{year_patterns.julian['numeric']})|(?:{self.julian['named']})"
        )
        
        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )
        
        self.julian['mixed_clear'] = (
            rf"{self.julian['combined']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['mixed_tricky'] = (
            rf"{self.julian['combined_optional']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.julian['combined']}"
        )
        
        self.julian['ss_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sh_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        self.julian['sg_parenthetical'] = (
            rf"{year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.separator}?\s*"
            rf"{self.indicator_patterns.parentheses_start}\s*"
            rf"{year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.parentheses_end}"
        )
        
        # Validate all generated patterns
        self._validate_patterns()





    




# ================================
# Date Range Patterns
# ================================
@dataclass
class DateRangePatterns(PatternValidator):
    """
    Date range patterns for different calendar systems.
    
    Handles expressions indicating a range of dates, such as:
    - "15/12/2024 to 20/12/2024"
    - "15–17 December 2024"
    - "من 1 محرم 1445 هـ إلى 10 محرم 1445 هـ"
    
    Attributes:
        indicator_patterns (IndicatorPatterns): Contains range starters and connectors.
        day_month_year_patterns (DayMonthYearPatterns): Complete date patterns for each calendar.
        hijri (Dict[str, str]): Hijri date range patterns.
        gregorian (Dict[str, str]): Gregorian date range patterns.
        julian (Dict[str, str]): julian date range patterns.
    """
    indicator_patterns: IndicatorPatterns
    day_month_year_patterns: DayMonthYearPatterns

    hijri: Dict[str, str] = None
    gregorian: Dict[str, str] = None
    julian: Dict[str, str] = None

    def __post_init__(self):
        """Initialize all date range patterns after dataclass creation."""
        
        # Base generic date range (no calendar-specific era enforced)
        self.numeric = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.numeric}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.numeric}"
        )

        # Init dicts
        self.hijri = {}
        self.gregorian = {}
        self.julian = {}

        # Hijri date range patterns
        year_patterns.hijri['numeric'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.hijri['numeric']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.hijri['numeric']}"
        )
        self.hijri['numeric_optional'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.hijri['numeric_optional']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.hijri['numeric_optional']}"
        )
        self.hijri['named'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.hijri['named']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.hijri['named']}"
        )
        self.hijri['combined'] = (
            rf"(?:{year_patterns.hijri['numeric']})|(?:{self.hijri['named']})"
        )
        self.hijri['combined_optional'] = (
            rf"(?:{self.hijri['numeric_optional']})|(?:{self.hijri['named']})"
        )

        # Gregorian date range patterns
        year_patterns.gregorian['numeric'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.gregorian['numeric']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.gregorian['numeric']}"
        )
        self.gregorian['numeric_optional'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.gregorian['numeric_optional']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.gregorian['numeric_optional']}"
        )
        self.gregorian['named'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.gregorian['named']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.gregorian['named']}"
        )
        self.gregorian['combined'] = (
            rf"(?:{year_patterns.gregorian['numeric']})|(?:{self.gregorian['named']})"
        )
        self.gregorian['combined_optional'] = (
            rf"(?:{self.gregorian['numeric_optional']})|(?:{self.gregorian['named']})"
        )

        # julian date range patterns
        year_patterns.julian['numeric'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.julian['numeric']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.julian['numeric']}"
        )
        self.julian['numeric_optional'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.julian['numeric_optional']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.julian['numeric_optional']}"
        )
        self.julian['named'] = (
            rf"(?:{self.indicator_patterns.range_starter}\s*)?"
            rf"{self.day_month_year_patterns.julian['named']}\s*"
            rf"{self.indicator_patterns.range_connector}\s*"
            rf"{self.day_month_year_patterns.julian['named']}"
        )
        self.julian['combined'] = (
            rf"(?:{year_patterns.julian['numeric']})|(?:{self.julian['named']})"
        )
        self.julian['combined_optional'] = (
            rf"(?:{self.julian['numeric_optional']})|(?:{self.julian['named']})"
        )

        # Validate patterns
        self._validate_patterns()