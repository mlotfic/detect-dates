# ===============================
# Example Usage – Build and extract patterns
# ===============================
LANG = "ar"  # or "en", etc.
# lang = LANG
patterns = get_date_patterns(lang="ar")

base_patterns: BasePatterns
month_patterns: MonthPatterns
era_patterns: EraPatterns
indicator_patterns: IndicatorPatterns
numeric_patterns: NumericPatterns

month_num_pattern = NumericPatterns.month
day_num_pattern = NumericPatterns.day
year_num_pattern = NumericPatterns.year
century_num_pattern = NumericPatterns.century

separator_pattern = IndicatorPatterns.separator
range_connector_pattern = IndicatorPatterns.range_connector
range_starter_pattern = IndicatorPatterns.range_starter
day_indicator_pattern = IndicatorPatterns.day
month_indicator_pattern = IndicatorPatterns.month
year_indicator_pattern = IndicatorPatterns.year
century_indicator_pattern = IndicatorPatterns.century

hijri_era_pattern = EraPatterns.hijri
gregorian_era_pattern = EraPatterns.gregorian
julian_era_pattern = EraPatterns.julian

day_pattern = BasePatterns.weekday

hijri_month_pattern = MonthPatterns.hijri
gregorian_month_pattern = MonthPatterns.gregorian
julian_month_pattern = MonthPatterns.julian

base_patterns: BasePatterns
numeric_patterns: NumericPatterns
month_patterns: MonthPatterns
era_patterns: EraPatterns
indicator_patterns: IndicatorPatterns
numeric_patterns: NumericPatterns

# ===================================================================================

# Hijri Era Keywords - Islamic calendar system
# AH = After Hijrah (Anno Hegirae), starting from Prophet Muhammad's migration to Medina (622 CE)
era_hijri_after_hijrah_ar = era_keywords_dict["ar"]["hijri"]["after_hijrah"]["keywords"]
era_hijri_after_hijrah_ar_normalized = 

era_hijri_after_hijrah_en = era_keywords_dict["en"]["hijri"]["after_hijrah"]["keywords"]
era_hijri_after_hijrah_en_normalized = era_keywords_dict["en"]["hijri"]["after_hijrah"]["normalized"]


# BAH = Before After Hijrah - dates before the Islamic calendar epoch
era_hijri_before_hijrah_ar = era_keywords_dict["ar"]["hijri"]["before_hijrah"]["keywords"]
era_hijri_before_hijrah_ar_normalized = era_keywords_dict["ar"]["hijri"]["before_hijrah"]["normalized"]

era_hijri_before_hijrah_en = era_keywords_dict["en"]["hijri"]["before_hijrah"]["keywords"]
era_hijri_before_hijrah_en_normalized = era_keywords_dict["en"]["hijri"]["before_hijrah"]["normalized"]

# Gregorian Era Keywords - Western calendar system
# CE = Common Era (secular equivalent of AD), BCE = Before Common Era
era_gregorian_after_christ_ar = era_keywords_dict["ar"]["gregorian"]["after_christ"]["keywords"]
era_gregorian_after_christ_ar_normalized = era_keywords_dict["ar"]["gregorian"]["after_christ"]["normalized"]

era_gregorian_after_christ_en = era_keywords_dict["en"]["gregorian"]["after_christ"]["keywords"]
era_gregorian_after_christ_en_normalized = era_keywords_dict["en"]["gregorian"]["after_christ"]["normalized"]
era_gregorian_before_christ_ar = era_keywords_dict["ar"]["gregorian"]["before_christ"]["keywords"]
era_gregorian_before_christ_ar_normalized = era_keywords_dict["ar"]["gregorian"]["before_christ"]["normalized"]

era_gregorian_before_christ_en = era_keywords_dict["en"]["gregorian"]["before_christ"]["keywords"]
era_gregorian_before_christ_en_normalized = era_keywords_dict["en"]["gregorian"]["before_christ"]["normalized"]

# julian/Persian Era Keywords - Iranian solar calendar system
# SH = Solar Hijri, starting from the same epoch as Islamic calendar but using solar year
era_after_julian_ar = era_keywords_dict["ar"]["julian"]["after_hijrah"]["keywords"]
era_after_julian_ar_normalized = era_keywords_dict["ar"]["julian"]["after_hijrah"]["normalized"]

era_after_julian_en = era_keywords_dict["en"]["julian"]["after_hijrah"]["keywords"]
era_after_julian_en_normalized = 

era_before_julian_ar = era_keywords_dict["ar"]["julian"]["before_hijrah"]["keywords"]
era_before_julian_ar_normalized = era_keywords_dict["ar"]["julian"]["before_hijrah"]["normalized"]
era_before_julian_en = era_keywords_dict["en"]["julian"]["before_hijrah"]["keywords"]
era_before_julian_en_normalized = era_keywords_dict["en"]["julian"]["before_hijrah"]["normalized"]
# ===================================================================================
# DATE PATTERNS
# ===================================================================================
m_yr_num_pattern = CompositeNumericPatterns.m_yr
d_m_num_pattern = CompositeNumericPatterns.d_m

# [ ] ============================================================
# Hijri, Gregorian, and julian year patterns (YYYY)
hijri_y_pattern = YearPatterns.hijri
hijri_y_pattern_s = YearPatterns.hijri_optional
gregorian_y_pattern = YearPatterns.gregorian
gregorian_y_pattern_s = YearPatterns.gregorian_optional
julian_y_pattern = YearPatterns.julian
julian_y_pattern_s = YearPatterns.julian_optional

# [ ] ============================================================
# Hijri, Gregorian, and julian century patterns 
century_num_pattern = CenturyPatterns.numeric
hijri_century_pattern = CenturyPatterns.hijri
gregorian_century_pattern = CenturyPatterns.gregorian
julian_century_pattern = CenturyPatterns.julian

century_num_pattern_s = CenturyPatterns.numeric_optional
hijri_century_pattern_s = CenturyPatterns.hijri_optional
gregorian_century_pattern_s = CenturyPatterns.gregorian_optional
julian_century_pattern_s = CenturyPatterns.julian_optional

# [ ] ============================================================
# Hijri, Gregorian, and julian (MM/YYYY) patterns
hijri_m_y_pattern_num = MonthYearPatterns.hijri.numeric
gregorian_m_y_pattern_num = MonthYearPatterns.gregorian.numeric
julian_m_y_pattern_num = MonthYearPatterns.julian.numeric

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (MM/YYYY) patterns with optional era like "1445 هـ" or "2023 م"
hijri_m_y_pattern_num_s = MonthYearPatterns.hijri.numeric_optional
gregorian_m_y_pattern_num_s = MonthYearPatterns.gregorian.numeric_optional
julian_m_y_pattern_num_s = MonthYearPatterns.julian.numeric_optional

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (Month/YYYY) patterns with optional era like "محرم 1445 هـ" or "يناير 2023 م"
hijri_m_y_pattern_name = MonthPatterns.hijri.named
gregorian_m_y_pattern_name = MonthPatterns.gregorian.named
julian_m_y_pattern_name = MonthPatterns.julian.named

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (Month/YYYY) patterns [stand alone or with era]
hijri_m_y_pattern = MonthYearPatterns.hijri.combined
gregorian_m_y_pattern = MonthYearPatterns.gregorian.combined
julian_m_y_pattern = MonthYearPatterns.julian.combined

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (Month/YYYY) patterns with optional era [start of range patterns]
hijri_m_y_pattern_s = MonthYearPatterns.hijri.combined_optional
gregorian_m_y_pattern_s = MonthYearPatterns.gregorian.combined_optional
julian_m_y_pattern_s = MonthYearPatterns.julian.combined_optional



        

# [ ] ============================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns
hijri_d_m_y_pattern_num = DayMonthYearPatterns.hijri.numeric
gregorian_d_m_y_pattern_num = DayMonthYearPatterns.gregorian.numeric
julian_d_m_y_pattern_num = DayMonthYearPatterns.julian.numeric

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era [start of range patterns]
hijri_d_m_y_pattern_num_s = DayMonthYearPatterns.hijri.numeric_optional
gregorian_d_m_y_pattern_num_s = DayMonthYearPatterns.gregorian.numeric_optional
julian_d_m_y_pattern_num_s = DayMonthYearPatterns.julian.numeric_optional

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era
hijri_d_m_y_pattern_name = DayMonthYearPatterns.hijri.named
gregorian_d_m_y_pattern_name = DayMonthYearPatterns.gregorian.named
julian_d_m_y_pattern_name = DayMonthYearPatterns.julian.named


# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns [combined with era for numeric and with/without named patterns]
# Natural language date patterns
hijri_d_m_y_pattern = DayMonthYearPatterns.hijri.combined
gregorian_d_m_y_pattern = DayMonthYearPatterns.gregorian.combined
julian_d_m_y_pattern = DayMonthYearPatterns.julian.combined

# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era [start of range patterns]
hijri_d_m_y_pattern_s = DayMonthYearPatterns.hijri.combined_optional
gregorian_d_m_y_pattern_s = DayMonthYearPatterns.gregorian.combined_optional
julian_d_m_y_pattern_s = DayMonthYearPatterns.julian.combined_optional





# [ ] ============================================================
# Full date patterns with (day DD/MM/YYYY)
natural_hijri_d_m_y_pattern_num = NaturalLanguagePatterns.hijri.numeric
natural_gregorian_d_m_y_pattern_num = NaturalLanguagePatterns.gregorian.numeric
natural_julian_d_m_y_pattern_num = NaturalLanguagePatterns.julian.numeric


# Natural language date patterns with (day DD/MM/YYYY) [start of range patterns]
natural_hijri_d_m_y_pattern_num_s = NaturalLanguagePatterns.hijri.numeric_optional
natural_gregorian_d_m_y_pattern_num_s = NaturalLanguagePatterns.gregorian.numeric_optional
natural_julian_d_m_y_pattern_num_s = NaturalLanguagePatterns.julian.numeric_optional

# Natural language date patterns with (day DD/MM/YYYY) [with/without named patterns]
natural_hijri_d_m_y_pattern_name = NaturalLanguagePatterns.hijri.named
natural_gregorian_d_m_y_pattern_name = NaturalLanguagePatterns.gregorian.named
natural_julian_d_m_y_pattern_name = NaturalLanguagePatterns.julian.named

# Natural language date patterns with (day DD/MM/YYYY) [combined with era for numeric and with/without named patterns]
natural_hijri_pattern = NaturalLanguagePatterns.hijri.combined
natural_gregorian_pattern = NaturalLanguagePatterns.gregorian.combined
natural_julian_pattern = NaturalLanguagePatterns.julian.combined

# Natural language date patterns with (day DD/MM/YYYY) [start of range patterns]
natural_hijri_pattern_s = NaturalLanguagePatterns.hijri.combined_optional
natural_gregorian_pattern_s = NaturalLanguagePatterns.gregorian.combined_optional
natural_julian_pattern_s = NaturalLanguagePatterns.julian.combined_optional

# ===================================================================================
# COMPREHENSIVE PATTERN DEFINITIONS
# ===================================================================================
# Comprehensive date component patterns
# lowest_priority = 0 (last in the list will be matched first)
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

century_pattern = CenturyPatterns()
year_pattern = YearPatterns()
month_year_pattern = MonthYearPatterns()
day_month_year_pattern = DayMonthYearPatterns()
natural_language_pattern = NaturalLanguagePatterns()

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
        
        from modules.regex_patterns import get_date_patterns
        
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
        print("   Please check your pattern data and module configuration.")

# =====================================================================
numeric_patterns_dict ={
    "metadata" : {
        "priority": 5,  # Lower priority due to ambiguity
        "match_type": "ambiguity",
    },
    "patterns" : [
        {   # Pattern 0 - Numeric Year (Ambiguous Calendar)
            "pattern": year_pattern.numeric,
            "name": "numeric",
            "description": "Numeric format - requires calendar context for disambiguation",
            "examples": [  # Original: "example": "1445, 2023, 1398"
                "1445",    # Could be Hijri (year 1445 AH ≈ 2023-2024 CE)
                "2023",    # Likely Gregorian (contemporary year)
                "1398",    # Could be julian (year 1398 SH ≈ 2019-2020 CE)
                "1446",    # Could be Hijri (year 1446 AH ≈ 2024-2025 CE)
                "2024",    # Likely Gregorian (contemporary year)
                "1401"     # Could be julian (year 1401 SH ≈ 2022-2023 CE)
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": None, 
                "year": 1,       
                "century": None, 
                "era": None, 
                "calendar": "Numeric"  
            },
        }
        {  # Pattern 0 - Month/Year Numeric (Ambiguous Calendar)
            "pattern": month_year_pattern.numeric,
            "name": "numeric_numeric",
            "description": "Numeric/Numeric format - ambiguous calendar detection required",
            "examples": [  # Original: "example": "12/1440, 01/2023, 03/1398"
                "12/1440",    # Could be Hijri (year 1440 AH ≈ 2018-2019 CE)
                "01/2023",    # Likely Gregorian (contemporary year)
                "03/1398",    # Could be julian (year 1398 SH ≈ 2019-2020 CE)
                "06/1445",    # Could be Hijri (year 1445 AH ≈ 2023-2024 CE)
                "11/2024",    # Likely Gregorian (contemporary year)
                "02/1401",    # Could be julian (year 1401 SH ≈ 2022-2023 CE)
                "12/1440",    # Could be Hijri (year 1440 AH ≈ 2018-2019 CE)
                "01/2023",    # Likely Gregorian (contemporary year)
                "1440/2024",  # This could be problematic - year/year format
                "03-1401"     # Could be julian (year 1401 SH ≈ 2022-2023 CE)
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": 1,      
                "year": 2,       
                "century": None, 
                "era": None, 
                "calendar": "Numeric"
            },
        },
        {  # Pattern 1 - Day/Month/Year Numeric (Ambiguous Calendar)
            "pattern": day_month_year_pattern.numeric,
            "name": "numeric_full_date",
            "description": "Numeric day/month/year format - requires calendar context for disambiguation",
            "examples": [  # Original: "example": "01/12/1440, 02/01/2023, 03/03/1398"
                "01/12/1440",  # 1st Dhul Hijjah 1440 AH (Hijri) or invalid Gregorian
                "02/01/2023",  # 2nd January 2023 CE (Gregorian)
                "15/03/1398",  # 15th month invalid - likely day/month confusion
                "25/12/2024",  # 25th December 2024 CE (Gregorian)
                "10/06/1445",  # Could be 10th Jumada al-Thani 1445 AH (Hijri)
                "31/01/1401"   # Could be julian format
            ],
            "date": {
                "weekday": None, 
                "day": 1,        
                "month": 2,      
                "year": 3,       
                "century": None, 
                "era": None, 
                "calendar": "Numeric"
            },
        },
        {  # Pattern 2 - Day/Month/Year with Weekday Prefix
            "pattern": natural_language_pattern.numeric,
            "name": "weekday_prefixed_numeric_date",  # Original: "day_month_year_num_pattern_with_day"
            "description": "Weekday-prefixed numeric date format - weekday can help validate calendar accuracy",
            "examples": [  # Original: "example": "الأحد 01/12/1440, الاثنين 02/01/2023, الثلاثاء 03/03/1398"
                "الأحد 01/12/1440",      # Sunday 1st Dhul Hijjah 1440 AH
                "الاثنين 02/01/2023",    # Monday 2nd January 2023 CE
                "الثلاثاء 15/03/1398",   # Tuesday - needs calendar validation
                "الأربعاء 25/12/2024",   # Wednesday 25th December 2024 CE
                "الخميس 10/06/1445",     # Thursday - Hijri date
                "الجمعة 20/11/1401"      # Friday - could be julian
            ],
            "date": {
                "weekday": 1,     (weekday name)
                "day": 2,        
                "month": 3,      
                "year": 4,       # Fourth capture group
                "century": None, 
                "era": None, 
                "calendar": "Numeric"
            },
        },   
    ]
}

# Comprehensive date patterns
basic_date_pattern_dict = {
    "metadata" : {
        "priority": 5,
        "match_type": "base_calander",
    },
    "patterns": [
        {  # Pattern 4 - Basic Hijri Year with Era Marker
            "pattern": year_pattern.hijri,
            "name": "explicit_hijri_year_only",  # Original: "basic_hijri"
            "description": "Hijri year with explicit era marker - unambiguous calendar identification",
            "examples": [  # Original: "example": "1445 هـ"
                "1445 هـ",       # Year 1445 AH (≈ 2023-2024 CE)
                "1440 هجري",    # Year 1440 AH with Arabic era marker
                "1450 هـ",       # Year 1450 AH (≈ 2028-2029 CE)
                "1435 هجرية",   # Year 1435 AH with full Arabic era marker
                "1442 ه",        # Year 1442 AH with simplified marker
                "1448 هـ."       # Year 1448 AH with period
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": None, 
                "year": 1,       
                "century": None, 
                "era": 2,
                "calendar": "hijri"
            },     
        },
        {  # Pattern 5 - Basic Gregorian Year with Era Marker
            "pattern": year_pattern.gregorian,
            "name": "explicit_gregorian_year_only",  # Original: "basic_gregorian"
            "description": "Gregorian year with explicit era marker - unambiguous calendar identification",
            "examples": [  # Original: "example": "2023 م"
                "2023 م",        # Year 2023 CE with Arabic marker
                "2024 ميلادي",   # Year 2024 CE with Arabic era marker
                "2022 ميلادية",  # Year 2022 CE with feminine Arabic marker
                "2025 م.",       # Year 2025 CE with period
                "2021 AD",       # Year 2021 CE with English marker
                "2020 CE"        # Year 2020 CE with English era marker
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": None, 
                "year": 1,
                "century": None, 
                "era": 2,
                "calendar": "gregorian"
            },        
        },
        
        {  # Pattern 6 - Basic julian Year with Era Marker
            "pattern": year_pattern.julian,
            "name": "explicit_julian_year_only",  # Original: "basic_julian"
            "description": "julian/Solar Hijri year with explicit era marker - unambiguous calendar identification",
            "examples": [  # Original: "example": "1402 هـ.ش"
                "1402 هـ.ش",     # Year 1402 SH (≈ 2023-2024 CE)
                "1400 شمسی",     # Year 1400 SH with Persian marker
                "1405 ه.ش",      # Year 1405 SH with simplified marker
                "1398 هجری شمسی", # Year 1398 SH with full Persian marker
                "1401 ش",        # Year 1401 SH with abbreviated marker
                "1403 شمسى"      # Year 1403 SH with Persian marker
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": None, 
                "year": 1,        (year number)
                "century": None, 
                "era": 2,         (era marker)
                "calendar": "julian"
            },
        },
        {  # Pattern 7 - Hijri Month/Year with Era Marker
            "pattern": month_year_pattern.hijri,
            "name": "explicit_hijri_month_year",  # Original: "hijri_month_year"
            "description": "Hijri month/year with explicit era marker - supports both numeric and named months",
            "examples": [  # Original: "example": "12/1440 هـ"
                "12/1445 هـ",       # Dhul Hijjah 1445 AH
                "محرم 1446 هـ",     # Muharram 1446 AH
                "01/1440 هجري",    # Muharram 1440 AH
                "رجب 1444 هـ",      # Rajab 1444 AH
                "06/1447 ه",        # Jumada al-Thani 1447 AH
                "رمضان 1445 هجرية" # Ramadan 1445 AH
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": [1, 4],   
                "year": [2, 5],    
                "century": None, 
                "era": [3, 6],     
                "calendar": "hijri"
            },
        },
        
        {  # Pattern 8 - Gregorian Month/Year with Era Marker
            "pattern": month_year_pattern.gregorian,
            "name": "explicit_gregorian_month_year",  # Original: "gregorian_month_year"
            "description": "Gregorian month/year with explicit era marker - supports Arabic and English month names",
            "examples": [  # Original: "example": "يناير 2023 م"
                "يناير 2023 م",     # January 2023 CE (Arabic)
                "January 2024 CE",  # January 2024 CE (English)
                "12/2023 ميلادي",  # December 2023 CE (Arabic era)
                "مارس 2022 ميلادية", # March 2022 CE (Arabic feminine)
                "July 2025 AD",     # July 2025 CE (English)
                "أكتوبر 2021 م."   # October 2021 CE (Arabic with period)
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": [1, 4],   
                "year": [2, 5],    
                "century": None, 
                "era": [3, 6],     
                "calendar": "gregorian"
            },
        },
        
        {  # Pattern 9 - julian Month/Year with Era Marker
            "pattern": month_year_pattern.julian,
            "name": "explicit_julian_month_year",  # Original: "julian_month_year"
            "description": "julian month/year with explicit era marker - supports Persian month names",
            "examples": [  # Original: "example": "فروردین 1402 هـ.ش"
                "فروردین 1402 هـ.ش",  # Farvardin 1402 SH
                "مهر 1401 شمسی",      # Mehr 1401 SH
                "01/1403 ه.ش",        # Farvardin 1403 SH (numeric)
                "آبان 1400 شمسى",     # Aban 1400 SH
                "12/1404 هجری شمسی",  # Esfand 1404 SH
                "دی 1399 ش"           # Dey 1399 SH
            ],
            "date": {
                "weekday": None, 
                "day": None, 
                "month": [1, 4],   
                "year": [2, 5],    
                "century": None, 
                "era": [3, 6],     
                "calendar": "julian"
            },
        },
        
        {  # Pattern 10 - Complete Hijri Date with Era Marker
            "pattern": day_month_year_pattern.hijri,
            "name": "explicit_hijri_complete_date",  # Original: "hijri_full_date"
            "description": "Complete Hijri date with day/month/year and explicit era marker",
            "examples": [  # Original: "example": "15/03/1445 هـ"
                "15/03/1445 هـ",      # 15th Rabi al-Awwal 1445 AH
                "01/محرم/1446 هجري", # 1st Muharram 1446 AH
                "27/رمضان/1445 هـ",   # 27th Ramadan 1445 AH (Laylat al-Qadr)
                "10/ذو الحجة/1444 ه", # 10th Dhul Hijjah 1444 AH (Eid al-Adha)
                "25/12/1443 هجرية",  # 25th Dhul Hijjah 1443 AH
                "09/ربيع الأول/1445 هـ." # 9th Rabi al-Awwal 1445 AH
            ],
            "date": {
                "weekday": None, 
                "day": [1, 5],     
                "month": [2, 6],   
                "year": [3, 7],    
                "century": None, 
                "era": [4, 8],     
                "calendar": "hijri"
            },
        },
        
        {  # Pattern 11 - Complete Gregorian Date with Era Marker
            "pattern": day_month_year_pattern.gregorian,
            "name": "explicit_gregorian_complete_date",  # Original: "gregorian_full_date"
            "description": "Complete Gregorian date with day/month/year and explicit era marker",
            "examples": [  # Original: "example": "15/03/2023 م"
                "15/03/2023 م",       # 15th March 2023 CE
                "25/December/2024 CE", # 25th December 2024 CE
                "01/يناير/2022 ميلادي", # 1st January 2022 CE
                "14/فبراير/2025 م",   # 14th February 2025 CE
                "31/12/2021 ميلادية", # 31st December 2021 CE
                "04/July/2023 AD"     # 4th July 2023 CE
            ],
            "date": {
                "weekday": None, 
                "day": [1, 5],     
                "month": [2, 6],   
                "year": [3, 7],    
                "century": None, 
                "era": [4, 8],     
                "calendar": "gregorian"
            },
        },
        
        {  # Pattern 12 - Complete julian Date with Era Marker
            "pattern": day_month_year_pattern.julian,
            "name": "explicit_julian_complete_date",  # Original: "julian_full_date"
            "description": "Complete julian date with day/month/year and explicit era marker",
            "examples": [  # Original: "example": "15/03/1402 هـ.ش"
                "15/03/1402 هـ.ش",     # 15th Khordad 1402 SH
                "01/فروردین/1403 شمسی", # 1st Farvardin 1403 SH (Nowruz)
                "21/مهر/1401 ه.ش",     # 21st Mehr 1401 SH
                "29/اسفند/1400 شمسى",  # 29th Esfand 1400 SH
                "10/06/1404 هجری شمسی", # 10th Shahrivar 1404 SH
                "25/آبان/1399 ش"       # 25th Aban 1399 SH
            ],
            "date": {
                "weekday": None, 
                "day": [1, 5],     
                "month": [2, 6],   
                "year": [3, 7],    
                "century": None, 
                "era": [4, 8],     
                "calendar": "julian"
            },  
        },
        
        {  # Pattern 13 - Natural Language Hijri Date
            "pattern": natural_month_year_pattern.hijri,
            "name": "natural_language_hijri_date",  # Original: "natural_hijri"
            "description": "Natural language Hijri date with weekday, day, month name, year, and era marker",
            "examples": [  # Original: "example": "الجمعة 15 11 1445 هـ"
                "الجمعة 15 محرم 1445 هـ",    # Friday 15th Muharram 1445 AH
                "الأحد 01 رمضان 1446 هجري", # Sunday 1st Ramadan 1446 AH
                "الاثنين 27 رجب 1444 هـ",   # Monday 27th Rajab 1444 AH
                "الثلاثاء 10 ذو الحجة 1445 ه", # Tuesday 10th Dhul Hijjah 1445 AH
                "السبت 25 شعبان 1443 هجرية", # Saturday 25th Sha'ban 1443 AH
                "الخميس 14 ربيع الآخر 1447 هـ." # Thursday 14th Rabi al-Thani 1447 AH
            ],
            "date": {
                "weekday": [1, 6],   
                "day": [2, 7],       
                "month": [3, 8],     
                "year": [4, 9],      
                "century": None, 
                "era": [5, 10],      
                "calendar": "hijri"
            },
        },
        
        {  # Pattern 14 - Natural Language Gregorian Date
            "pattern": natural_month_year_pattern.gregorian,
            "name": "natural_language_gregorian_date",  # Original: "natural_gregorian"
            "description": "Natural language Gregorian date with weekday, day, month name, year, and era marker",
            "examples": [  
                "الجمعة 15 يناير 2023 ميلاديًا",  # Friday 15th January 2023 CE
                "الأحد 25 ديسمبر 2024 م",        # Sunday 25th December 2024 CE
                "Monday 04 July 2023 CE",       # Monday 4th July 2023 CE
                "الثلاثاء 14 فبراير 2025 ميلادي", # Tuesday 14th February 2025 CE
                "Saturday 31 December 2022 AD", # Saturday 31st December 2022 CE
                "الخميس 01 مارس 2024 ميلادية"   # Thursday 1st March 2024 CE
            ],
            "date": {
                "weekday": [1, 6],   
                "day": [2, 7],       
                "month": [3, 8],     
                "year": [4, 9],      
                "century": None, 
                "era": [5, 10],      
                "calendar": "gregorian"
            },
        },
        
        {  # Pattern 15 - Natural Language julian Date
            "pattern": natural_month_year_pattern.julian,
            "name": "natural_language_julian_date",  # Original: "natural_julian"
            "description": "Natural language julian date with weekday, day, month name, year, and era marker",
            "examples": [  # Original: "example": "جمعه 15 فروردین 1402 هـ.ش"
                "جمعه 15 فروردین 1402 هـ.ش",    # Friday 15th Farvardin 1402 SH
                "یکشنبه 01 فروردین 1403 شمسی", # Sunday 1st Farvardin 1403 SH (Nowruz)
                "دوشنبه 21 مهر 1401 ه.ش",      # Monday 21st Mehr 1401 SH
                "سه‌شنبه 29 اسفند 1400 شمسى",  # Tuesday 29th Esfand 1400 SH
                "پنج‌شنبه 10 آبان 1404 هجری شمسی", # Thursday 10th Aban 1404 SH
                "شنبه 25 دی 1399 ش"            # Saturday 25th Dey 1399 SH
            ],
            "date": {
                "weekday": [1, 6],
                "day": [2, 7],
                "month": [3, 8],
                "year": [4, 9],
                "century": None, 
                "era": [5, 10],
                "calendar": "julian"
            },
        },
    ]
}



# ===================================================================================
# MIXED SLASHED DATE PATTERNS (TO BE REFACTORED)
# ===================================================================================
MIXED_PURE_DATE_PATTERNS_SLASH = {
    "metadata": {
        "priority": 5,  # Lower priority due to ambiguity
        "match_type": "mixed_slash",
    },
    "patterns": [
        {  # Pattern 0 - Hijri Year Range (start+end)
            "pattern": rf'{hijri_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}',
            "name": "range_hijri_years_strict",
            "description": "Hijri year to Hijri year range using 'من ... إلى ...' format",
            "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
                "من 1440 هـ إلى 1445 هـ",
                "1442هـ / 1444هـ",
                "١٤٣٠ هـ – ١٤٤٠ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {  # Pattern 1 - Gregorian Year Range
            "pattern": rf'{gregorian_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}',
            "name": "range_gregorian_years_strict", 
            "description": "Gregorian year to Gregorian year range using Arabic connectors",
            "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
                "من 2020 م إلى 2024 م",
                "٢٠١٠ م / ٢٠٢٠ م",
                "1995م – 2005م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },    
        {  # Pattern 2 - Hijri Year Range (non-strict)
            "pattern": rf'{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}',
            "name": "range_hijri_years_basic",  # Original: "from_to_hijri_hijri_yr"
            "description": "Hijri year range without strict 'من...إلى' format",
            "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
                "1440 هـ / 1445 هـ",
                "١٤٣٥ هـ - ١٤٤١ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {  # Pattern 3 - Gregorian Year Range (non-strict)
            "pattern": rf'{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}',
            "name": "range_gregorian_years_basic",  # Original: "from_to_gregorian_gregorian_yr"
            "description": "Gregorian year range without strict connectors",
            "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
                "2020 م / 2024 م",
                "٢٠١٥م - ٢٠٢٢م",
                "من 2020 م إلى 2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }, 
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {  # Pattern 4 - Hijri/Gregorian Combined (Hijri First)
            "pattern": rf"{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}",
            "name": "pair_hijri_gregorian_years",  # Original: "basic_hijri"
            "description": "Hijri year followed by Gregorian year (parallel calendar style)",
            "examples": [  # Original: "example": "1440 هـ/2023 م"
                "1440 هـ/2023 م",
                "١٤٤٥ هـ - ٢٠٢٤ م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },   
        {  # Pattern 5 - Gregorian/Hijri Combined (Gregorian First)
            "pattern": rf"{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}",
            "name": "pair_gregorian_hijri_years",  # Original: "basic_gregorian"
            "description": "Gregorian year followed by Hijri year (parallel calendar style)",
            "examples": [  # Original: "example": "2023 م/1440 هـ"
                "2023 م/1440 هـ",
                "٢٠٢٤ م - ١٤٤٥ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "gregorian"
            },
        },
        
        # ===================================================================================
        # 7. MONTH-YEAR PATTERNS (RANGES & MIXED CALENDARS)
        # ===================================================================================

        {  # Pattern 6 - Hijri Month-Year to Hijri Month-Year
            "pattern": rf'{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}',
            "name": "range_hijri_month_year_strict",  # Original: "from_to_hijri_hijri_m_y"
            "description": "Matches Hijri month/year range using Arabic connectors like 'من ... إلى ...'",
            "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
                "من محرم 1440 هـ إلى صفر 1445 هـ",
                "ذو القعدة 1443 هـ - محرم 1444 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },

            "hijri_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
                },
            "gregorian_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
                },
            "julian_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
                }
        },
        {  # Pattern 7 - Gregorian Month-Year to Gregorian Month-Year
            "pattern": rf'{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}',
            "name": "range_gregorian_month_year_strict",  # Original: "from_to_gregorian_gregorian_m_y"
            "description": "Matches Gregorian month/year range using Arabic connectors",
            "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
                "من يناير 2020 م إلى ديسمبر 2024 م",
                "مارس 2022 م / أغسطس 2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {  # Pattern 8 - Hijri Month-Year Range (loose format)
            "pattern": rf'{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}',
            "name": "range_hijri_month_year_basic",  # Original: "from_to_hijri_hijri_m_y"
            "description": "Loose format Hijri month/year range with optional separators",
            "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
                "محرم 1440 هـ / صفر 1445 هـ",
                "شعبان ١٤٤٠ هـ - رمضان ١٤٤٢ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 19 - Gregorian Month-Year Range (loose)
            "pattern": rf'{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}',
            "name": "range_gregorian_month_year_basic",  # Original: "from_to_gregorian_gregorian_m_y"
            "description": "Loose format Gregorian month/year range",
            "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
                "يناير 2020 م / ديسمبر 2024 م",
                "مارس ٢٠٢٠ - يونيو ٢٠٢٣"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {  # Pattern 7 - Hijri + Gregorian M/Y combo (Hijri first)
            "pattern": rf"{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}",
            "name": "pair_hijri_gregorian_month_year",  # Original: "hijri_month_year"
            "description": "Hijri month/year followed by Gregorian month/year",
            "examples": [  # Original: "example": "12/1440 هـ/ 01/2023 م"
                "12/1440 هـ / 01/2023 م",
                "محرم 1445 هـ / يناير 2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
            
        },
        {  # Pattern 8 - Gregorian + Hijri M/Y combo (Gregorian first)
            "pattern": rf"{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}",
            "name": "pair_gregorian_hijri_month_year",  # Original: "gregorian_month_year"
            "description": "Gregorian month/year followed by Hijri month/year",
            "examples": [  # Original: "example": "يناير 2023 م/ محرم 1445 هـ"
                "يناير 2023 م / محرم 1445 هـ",
                "01/2023 م - 01/1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "gregorian"
                },
        },
        # ===================================================================================
        # 5. FULL DATE PATTERNS (day/month/year)
        # ===================================================================================
        {  # Pattern 10 - Hijri full date + Gregorian full date
            "pattern": rf"{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}",
            "name": "full_date_hijri_then_gregorian",  # Original: "hijri_full_date"
            "description": "Complete Hijri date followed by Gregorian equivalent",
            "examples": [  # Original: "example": "15/03/1445 هـ/ 15/03/2023 م"
                "15/03/1445 هـ / 15/03/2023 م",
                "١٥ محرم ١٤٤٥ هـ - ١٥ مارس ٢٠٢٣ م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
            "julian": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "julian"
                }
        },
        {  # Pattern 11 - Gregorian full date + Hijri full date
            "pattern": rf"{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}",
            "name": "full_date_gregorian_then_hijri",  # Original: "gregorian_full_date"
            "description": "Complete Gregorian date followed by Hijri equivalent",
            "examples": [  # Original: "example": "15/03/2023 م/ 15/03/1445 هـ"
                "15/03/2023 م / 15/03/1445 هـ",
                "١٥ مارس ٢٠٢٣ م - ١٥ محرم ١٤٤٥ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "gregorian"
                },
            
        },
        {   # Pattern 13 - Natural Language Hijri followed by Gregorian
            "pattern": rf"{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}",
            "name": "natural_hijri_then_gregorian_format",  # Original: "natural_hijri"
            "description": "Matches a Hijri date in natural Arabic followed by a Gregorian date",
            "examples": [  # Original: "example": "الجمعة 15 11 1445 هـ/ 15 11 2023 م"
                "الجمعة 15 محرم 1445 هـ / 15 نوفمبر 2023 م",
                "الخميس 1 صفر 1444 هـ / 28 أغسطس 2022 م",
                "السبت 10 رمضان 1442 هـ / 22 أبريل 2021 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                }, 
        },
        {   # Pattern 14 - Natural Language Gregorian followed by Hijri
            "pattern": rf"{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}",
            "name": "natural_gregorian_then_hijri_format",  # Original: "natural_gregorian"
            "description": "Matches a Gregorian date in natural Arabic followed by a Hijri date",
            "examples": [  # Original: "example": "الجمعة 15 يناير 2023 ميلاديًا/ 15 محرم 1445 هجريًا"
                "الجمعة 15 يناير 2023 م / 15 محرم 1445 هـ",
                "الخميس 1 فبراير 2024 م / 20 رجب 1445 هـ",
                "الأحد 30 ديسمبر 2022 م / 6 جمادى الثانية 1444 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },         "gregorian": {
                "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "gregorian"
                },
        },    
        {   # Pattern 42 - Hijri Range (Day-Month-Year to Day-Month-Year)
            "pattern": rf'{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}',
            "name": "range_hijri_to_hijri_full_format",  # Original: "from_to_hijri_hijri_d_m_y"
            "description": "Matches Hijri date ranges using full day/month/year structure",
            "examples": [  # Original: "example": "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ"
                "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
                "من 1 رمضان 1400 هـ إلى 10 شوال 1400 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },         "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                }, 
        },
        {   # Pattern 43 - Gregorian Range (Day-Month-Year to Day-Month-Year)
            "pattern": rf'{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}',
            "name": "range_gregorian_to_gregorian_full_format",  # Original: "from_to_gregorian_gregorian_d_m_y"
            "description": "Matches Gregorian date ranges using full day/month/year structure",
            "examples": [  # Original: "example": "من 10 يناير 2024 م إلى 20 ديسمبر 202 4 م"
                "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
                "من 5 مارس 2020 م إلى 15 مارس 2020 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },     
        },
        {   # Pattern 30 - Hijri range using same structure on both sides (legacy duplicate of Pattern 42)
            "pattern": rf'{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}',
            "name": "range_hijri_to_hijri_basic_format",  # Original: "from_to_hijri_hijri_d_m_y"
            "description": "Redundant pattern for Hijri date ranges. Same structure as pattern 42. Consider merging.",
            "examples": [
                "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
                "من 10 رمضان 1420 هـ إلى 25 رمضان 1420 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 40 - Gregorian range duplicate (legacy - same as pattern 43)
            "pattern": rf'{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}',
            "name": "range_gregorian_to_gregorian_basic_format",  # Original: "from_to_gregorian_gregorian_d_m_y"
            "description": "Redundant pattern for Gregorian date ranges. Matches pattern 43. Merge if possible.",
            "examples": [
                "من 1 يناير 2020 م إلى 10 يناير 2020 م",
                "من 5 مارس 2020 م إلى 6 مارس 2020 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },  
        {   # Pattern 10 - Full Hijri date followed by Gregorian equivalent (shared day)
            "pattern": rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}",
            "name": "day_hijri_then_gregorian_date",  # Original: "hijri_full_date"
            "description": "Matches a Hijri date followed by its Gregorian equivalent, starting with day name",
            "examples": [  # Original: "example": "15/03/1445 هـ/ الأربعاء 15/03/2023 م"
                "الأربعاء 15/03/1445 هـ / 15/03/2023 م",
                "الثلاثاء 01/01/1445 هـ / 19/07/2023 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
            "julian": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "julian"
                }
        },
        {   # Pattern 11 - Full Gregorian date followed by Hijri equivalent
            "pattern": rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}",
            "name": "day_gregorian_then_hijri_date",  # Original: "gregorian_full_date"
            "description": "Matches Gregorian date followed by its Hijri equivalent, both with day name",
            "examples": [  # Original: "example": "الأربعاء 15/03/2023 م/ 15/03/1445 هـ"
                "الأربعاء 15/03/2023 م / 15/03/1445 هـ",
                "الثلاثاء 01/01/2024 م / 19/06/1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
            },        
            "hijri": {
                "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "hijri"
            },
            "gregorian": {
                "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "gregorian"
                },
        },
        {  # Pattern 54 - Hijri-to-Hijri date range with weekday
            "pattern": rf'{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}',
            "name": "range_hijri_to_hijri_with_weekday",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
            "description": "Matches a date range from one Hijri date to another, both possibly with weekdays",
            "examples": [  # Original: "example": "من الأحد - 15 محرم 1445 هـ إلى 20 صفر 1445 هـ"
                "من الأحد - 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
                "من الجمعة 10 صفر 1445 هـ إلى الثلاثاء 20 صفر 1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },         "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {   # Pattern 55 - Gregorian-to-Gregorian date range with weekday
            "pattern": rf'{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}',
            "name": "range_gregorian_to_gregorian_with_weekday",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
            "description": "Matches Gregorian date ranges with weekday context",
            "examples": [  # Original: "example": "من الأحد - 10 يناير 2024 م إلى 20 ديسمبر 2024 م"
                "من الأحد - 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
                "من الجمعة 01 مارس 2023 م إلى الاثنين 10 أبريل 2023 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },         "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },  
        {  # Pattern 51 - DUPLICATE of Pattern 54 — consider merging or deleting
            "pattern": rf'{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}',
            "name": "range_hijri_to_hijri_with_weekday_duplicate",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
            "description": "Duplicate pattern of #54 for Hijri date range with weekdays — remove or reconcile",
            "examples": [
                "من الأحد - 15 محرم 1445 هـ إلى الاثنين 20 صفر 1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
                },
        },
        {   # Pattern 52 - Gregorian date range with weekdays and Arabic connector
            "pattern": rf'{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}',
            "name": "range_gregorian_to_gregorian_with_weekday_named",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
            "description": "Matches a Gregorian date range, possibly with weekdays and Arabic date connectors",
            "examples": [  # Original: "example": "من الأحد - 10 يناير 2024 م إلى  الاثنين 20 ديسمبر 2024 م"
                "من الأحد - 10 يناير 2024 م إلى الاثنين 20 ديسمبر 2024 م",
                "من الجمعة 01 مارس 2023 م إلى الأحد 19 نوفمبر 2023 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "gregorian": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        },
        
    ]
}


# ===================================================================================
# MIXED PARENTHETICAL DATE PATTERNS (TO BE REFACTORED)
# ===================================================================================
MIXED_PURE_DATE_PATTERNS_PARENTHETICAL = [ 
   {    # Pattern 9 - Hijri Year to Hijri Year (with parentheses)
        "pattern": rf'{hijri_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_year_parenthetical",  # Original: "from_to_hijri_hijri_yr"
        "description": "Matches a range from Hijri year to Hijri year enclosed in parentheses or brackets",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "من 1440 هـ (1445 هـ)",
            "1442 هـ [1446 هـ]",
            "١٤٤٠ هـ (١٤٤٥ هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 10 - Gregorian Year to Gregorian Year (with parentheses)
        "pattern": rf'{gregorian_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_year_parenthetical",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Matches a range from Gregorian year to Gregorian year with brackets or parentheses",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "من 2020 م (2024 م)",
            "2020 م [2024 م]",
            "٢٠٢٠ م (٢٠٢٤ م)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },    
    {  # Pattern 6 - Hijri Year Range (basic, not start-anchored)
        "pattern": rf'{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "hijri_year_range_basic_parenthetical",  # Original: "from_to_hijri_hijri_yr"
        "description": "Matches a Hijri year range enclosed in parentheses or brackets without leading 'من'",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "1440 هـ (1445 هـ)",
            "١٤٤٢ هـ [١٤٤٥ هـ]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {  # Pattern 7 - Gregorian Year Range (basic)
        "pattern": rf'{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "gregorian_year_range_basic_parenthetical",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Matches Gregorian year range enclosed in parentheses or brackets",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "2020 م (2024 م)",
            "٢٠٢٠ م [٢٠٢٤ م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        }, 
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {  # Pattern 3 - Hijri year followed by Gregorian year
        "pattern": rf'{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "hijri_gregorian_year_combination",  # Original: "basic_hijri"
        "description": "Matches Hijri year followed by Gregorian year inside parentheses/brackets",
        "examples": [  # Original: "example": "1440 هـ/2023 م"
            "1440 هـ (2023 م)",
            "١٤٤٠ هـ [٢٠٢٣ م]",
            "1441 هـ / (2022 م)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },   
    {  # Pattern 5 - Gregorian year followed by Hijri year
        "pattern": rf'{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "gregorian_hijri_year_combination",  # Original: "basic_gregorian"
        "description": "Matches Gregorian year followed by Hijri year inside parentheses/brackets",
        "examples": [  # Original: "example": "2023 م/1440 هـ"
            "2023 م (1440 هـ)",
            "٢٠٢٣ م [١٤٤٠ هـ]",
            "2024 م / (1445 هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "gregorian"
        },
    },
    # 7. MONTH-YEAR PATTERNS
    # 1. HIGHEST PRIORITY - COMPLEX RANGE PATTERNS (MM/YYYY style with parentheses/brackets)

    {  # Pattern 21 - Hijri month/year to Hijri month/year range (with parentheses)
        "pattern": rf'{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_month_year_parenthetical",  # Original: "from_to_hijri_hijri_m_y"
        "description": "Matches a Hijri month/year range enclosed in parentheses or brackets",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
            "من محرم 1440 هـ (صفر 1445 هـ)",
            "جمادى الأولى 1441 هـ [رمضان 1442 هـ]",
            "شوال 1443 هـ - (ذو القعدة 1444 هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },

        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }
    },
    {  # Pattern 22 - Gregorian month/year to Gregorian month/year (with parentheses)
        "pattern": rf'{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_month_year_parenthetical",  # Original: "from_to_gregorian_gregorian_m_y"
        "description": "Matches a Gregorian month/year range inside parentheses or brackets",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
            "من يناير 2020 م (ديسمبر 2024 م)",
            "مارس 2021 م [أكتوبر 2023 م]",
            "فبراير 2022 م - (نوفمبر 2024 م)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 18 - Hijri month/year to Hijri month/year (no starter anchor)
        "pattern": rf'{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "hijri_month_year_range_parenthetical",  # Original: "from_to_hijri_hijri_m_y"
        "description": "Hijri month/year range without a leading phrase like 'من'",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
            "محرم 1440 هـ (صفر 1445 هـ)",
            "ذو الحجة 1441 هـ [رمضان 1442 هـ]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {   # Pattern 19 - Gregorian month/year to Gregorian month/year (simplified)
        "pattern": rf'{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "gregorian_month_year_range_parenthetical",  # Original: "from_to_gregorian_gregorian_m_y"
        "description": "Simplified Gregorian month/year range (no prefix)",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
            "يناير 2020 م (ديسمبر 2024 م)",
            "مارس 2021 م [أكتوبر 2023 م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {  # Pattern 7 - Hijri + Gregorian month/year combination
        "pattern": rf'{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "hijri_gregorian_month_year_combination",  # Original: "hijri_month_year"
        "description": "Hijri month/year followed by Gregorian month/year inside parentheses or brackets",
        "examples": [  # Original: "example": "12/1440 هـ/ 01/2023 م"
            "محرم 1445 هـ (يناير 2024 م)",
            "12/1444 هـ [01/2023 م]",
            "ذو الحجة 1443 هـ / (سبتمبر 2022 م)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
        },
    },
    {   # Pattern 8 - Gregorian + Hijri month/year combination
        "pattern": rf'{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "gregorian_hijri_month_year_combination",  # Original: "gregorian_month_year"
        "description": "Gregorian month/year followed by Hijri month/year inside parentheses or brackets",
        "examples": [  # Original: "example": "يناير 2023 م/ محرم 1445 هـ"
            "يناير 2023 م (محرم 1445 هـ)",
            "02/2022 م [12/1443 هـ]",
            "مارس 2021 م / (رجب 1442 هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "gregorian"
            },
    },
    {  # Pattern 10 - Full Hijri/Gregorian Date (Hijri first)
        "pattern": rf'{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "full_date_hijri_then_gregorian",  # Original: "hijri_full_date"
        "description": "Matches a full Hijri date followed by Gregorian equivalent in brackets or parentheses",
        "examples": [  # Original: "15/03/1445 هـ/ 15/03/2023 م"
            "15 محرم 1445 هـ (15 مارس 2023 م)",
            "05/10/1444 هـ [25/04/2023 م]",
            "1 رمضان 1400 هـ (15 يوليو 1980 م)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        "julian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "julian"
            }
    },
    {  # Pattern 11 - Full Gregorian/Hijri Date (Gregorian first)
        "pattern": rf'{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "full_date_gregorian_then_hijri",  # Original: "gregorian_full_date"
        "description": "Matches a full Gregorian date followed by equivalent Hijri date in brackets or parentheses",
        "examples": [  # Original: "15/03/2023 م/ 15/03/1445 هـ"
            "15 مارس 2023 م (15 محرم 1445 هـ)",
            "25/04/2023 م [05/10/1444 هـ]",
            "01/01/2020 م (06 جمادى الأولى 1441 هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "gregorian"
            },
        
    },
    {  # 13 — Natural language Hijri date with Gregorian
        "pattern": rf'{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "natural_hijri_with_gregorian",
        "description": "Natural Hijri date with Gregorian reference",
        "examples": ["الجمعة 15 محرم 1445 هـ (15 مارس 2023 م)",
                     "الجمعة 15 11 1445 هـ/ 15 11 2023 م"
                     ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            }, 
    },
    {   # 14 — Natural Gregorian with Hijri
        "pattern": rf'{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*(?:[\)\]])',
        "name": "natural_gregorian_with_hijri",
        "description": "Natural Gregorian date with Hijri reference",
        "examples": ["الجمعة 15 يناير 2023 م (15 محرم 1445 هـ)"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         
        "gregorian": {
            "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "gregorian"
        },
    },
    
    # 5. FULL DATE PATTERNS (day/month/year) — e.g., "15 محرم 1445 هـ"

    {  # 42 — Hijri to Hijri full date range
        "pattern": rf'{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_full_date",
        "description": "Range from Hijri full date to Hijri full date",
        "examples": ["من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            }, 
    },
    {   # 43 — Gregorian to Gregorian full date range
        "pattern": rf'{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_full_date",
        "description": "Range from Gregorian full date to Gregorian full date",
        "examples": ["من 10 يناير 2024 م إلى 20 ديسمبر 2024 م"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },      
    },
    {   # 30 — Hijri to Hijri full date range (non-start version)
        "pattern": rf'{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_full_date_plain",
        "description": "Plain Hijri to Hijri full date range",
        "examples": ["15 محرم 1445 هـ (20 صفر 1445 هـ)"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # 40 — Gregorian to Gregorian full date range (non-start)
        "pattern": rf'{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_full_date_plain",
        "description": "Plain Gregorian to Gregorian full date range",
        "examples": ["10 يناير 2024 م (20 ديسمبر 2024 م)"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # 10 — Hijri full date followed by Gregorian in brackets
        "pattern": rf'{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "full_hijri_date_with_gregorian",
        "description": "Full Hijri date followed by Gregorian date",
        "exampleس": ["15/03/1445 هـ/ الأربعاء 15/03/2023 م"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        "julian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "julian"
            }
    },
    {  # 11 — Gregorian full date followed by Hijri in brackets
        "pattern": rf'{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "full_gregorian_date_with_hijri",
        "description": "Full Gregorian date followed by Hijri date",
        "examples": ["الأربعاء 15 مارس 2023 م (15 محرم 1445 هـ)",
                     "الأربعاء 15/03/2023 م/ 15/03/1445 هـ"],
        "date": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "gregorian"
            },
    },
    {   # 54 — Natural Hijri weekday + date range
        "pattern": rf'{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*(?:[\)\]])',
        "name": "range_natural_hijri_to_hijri_weekday",
        "description": "Range from Hijri weekday+date to Hijri weekday+date (natural language)",
        "examples": ["من الأحد - 15 محرم 1445 هـ إلى الاثنين 20 صفر 1445 هـ"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # 55 — Natural Gregorian weekday + date range
        "pattern": rf'{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "range_natural_gregorian_to_gregorian_weekday",
        "description": "Range from Gregorian weekday+date to Gregorian weekday+date (natural language)",
        "examples": ["من الأحد - 10 يناير 2024 م إلى الاثنين 20 ديسمبر 2024 م"],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },  
    {  # Pattern 52 - Gregorian Date Range with Weekdays
        "pattern": rf'{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_weekday_to_weekday",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
        "description": "Matches a range from one Gregorian date with weekday to another, using Arabic connectors",
        "examples": [  # Original: "example": "من الأحد - 10 يناير 2024 م إلى  الاثنين 20 ديسمبر 2024 م"
            "من الأحد - 10 يناير 2024 م إلى الاثنين 20 ديسمبر 2024 م",
            "من السبت 05 يونيو 2021 م إلى الاثنين 07 يونيو 2021 م",
            "من الثلاثاء 01 يناير 2019 م إلى الجمعة 04 يناير 2019 م"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    
]
# ===================================================================================
# MIXED_RANGE_PATTERNS_parenthetical [parenthetical]
# ===================================================================================
MIXED_RANGE_PATTERNS_parenthetical = [    
    {   # Pattern 9 - Hijri year range with surrounding parentheses and Gregorian shadow
        "pattern": rf'(?:[\(\[])\s*{hijri_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_parenthetical_with_gregorian",  # Original: "from_to_hijri_hijri_yr"
        "description": "Hijri year range (from-to) in brackets, with Gregorian equivalent in next bracket",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "(1440 هـ - 1445 هـ) (2019 م - 2024 م)",
            "[1442هـ–1444هـ] [2021م–2023م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 10 - Gregorian year range with surrounding parentheses and Hijri shadow
        "pattern": rf'(?:[\(\[])\s*{gregorian_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_parenthetical_with_hijri",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Gregorian year range (from-to) in brackets, with Hijri equivalent in next bracket",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "(2020 م - 2024 م) (1441 هـ - 1445 هـ)",
            "[2022م–2023م] [1443هـ–1444هـ]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },    
    {   # Pattern 6 - Hijri range only, no suffix, with Gregorian range next (non-suffixed)
        "pattern": rf'(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_raw_with_gregorian",  # Original: "from_to_hijri_hijri_yr"
        "description": "Hijri year range in brackets (without suffix), followed by raw Gregorian range",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "(1440 - 1445) (2019 - 2024)",
            "[1441–1443] [2020–2022]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 7 - Gregorian range without suffix, followed by Hijri range without suffix
        "pattern": rf'(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_raw_with_hijri",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Gregorian year range (raw) in brackets followed by Hijri year range",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "(2020 - 2024) (1441 - 1445)",
            "[2022–2023] [1443–1444]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        }, 
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 3 - Single Hijri+Gregorian pair in brackets
        "pattern": rf'(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])',
        "name": "bracketed_hijri_gregorian_double",  # Original: "basic_hijri"
        "description": "Double pair of Hijri-Gregorian year combinations in brackets",
        "examples": [  # Original: "example": "1440 هـ/2023 م"
            "(1440 هـ / 2023 م) (1441 هـ / 2024 م)",
            "[1442هـ/2021م][1443هـ/2022م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },   
    {   # Pattern 5 - Single Gregorian+Hijri pair in brackets
        "pattern": rf'(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])',
        "name": "bracketed_gregorian_hijri_double",  # Original: "basic_gregorian"
        "description": "Double pair of Gregorian-Hijri year combinations in brackets",
        "examples": [  # Original: "example": "2023 م/1440 هـ"
            "(2023 م / 1444 هـ) (2024 م / 1445 هـ)",
            "[2022م/1443هـ][2023م/1444هـ]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": 2, "calendar" : "gregorian"
        },
    },
    # 7. MONTH-YEAR PATTERNS
    {   # Pattern 21 - Hijri to Hijri range with Gregorian reference
        "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_m_y_with_gregorian_reference",  # Original: "from_to_hijri_hijri_m_y"
        "description": "Matches a range from Hijri month/year to Hijri month/year with trailing Gregorian reference",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
                    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 - ديسمبر 2023)",
                    "[01/1441 - 02/1445] [01/2020 - 12/2023]",
                    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 م - يوليو 2024 م)",
                    "[جمادى الأولى 1438 هـ إلى رمضان 1440 هـ] [فبراير 2017 م إلى يونيو 2019 م]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },

        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }
    },
    {   # Pattern 22 - Gregorian to Gregorian range with Hijri reference
        "pattern": rf'(?:[\(\[])\s*{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_m_y_with_hijri_reference",  # Original: "from_to_gregorian_gregorian_m_y"
        "description": "Matches a range from Gregorian month/year to Gregorian month/year with trailing Hijri reference",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
                    "(يناير 2020 م - ديسمبر 2024 م) (محرم 1441 هـ - ربيع 1447 هـ)",
                    "[01/2020 - 12/2024] [01/1441 - 04/1447]",
                    "(يناير 2020 م - ديسمبر 2024 م) (جمادى الثانية 1441 هـ - ذو القعدة 1446 هـ)",
                    "[مارس 2018 م إلى يونيو 2019 م] [رجب 1439 هـ إلى رمضان 1440 هـ]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 18 - Hijri to Hijri range with Gregorian in same brackets (compact)
        "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "compact_hijri_m_y_range_with_gregorian",
        "description": "Compact form of Hijri range followed by Gregorian equivalent, all in brackets",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
                    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 - ديسمبر 2023)",
                    "[1/1440 - 2/1445] [1/2019 - 12/2023]",
                    "(جمادى الأولى 1435 هـ - شعبان 1440 هـ) (مارس 2014 م - مايو 2019 م)",
                    "[صفر 1442 هـ إلى ربيع الثاني 1444 هـ] [أكتوبر 2020 م إلى نوفمبر 2022 م]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {   # Pattern 19 - Gregorian to Gregorian range followed by Hijri
        "pattern": rf'(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "compact_gregorian_m_y_range_with_hijri",
        "description": "Compact form of Gregorian range followed by Hijri equivalent, all in brackets",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
                        "(يناير 2020 م - ديسمبر 2024 م) (محرم 1441 هـ - ربيع 1447 هـ)",
                        "[1/2020 - 12/2024] [1/1441 - 4/1447]",
                        "(يناير 2020 م - ديسمبر 2024 م) (جمادى الأولى 1441 هـ - ذو الحجة 1446 هـ)",
                        "[مارس 2018 م إلى يونيو 2019 م] [جمادى الآخرة 1439 هـ إلى رمضان 1440 هـ]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 7 - Mixed Hijri/Gregorian Month-Year Format
        "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
        "name": "alternating_hijri_gregorian_m_y_pairs",
        "description": "Matches alternating Hijri/Gregorian month-year pairs with brackets",
        "examples": [  # Original: "example": "12/1440 هـ/ 01/2023 م"
            "(12/1440 هـ / 01/2023 م) (01/1441 هـ / 02/2023 م)",
            "[جمادى الأولى 1442 هـ / يناير 2021 م] [رجب 1443 هـ / مارس 2022 م]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
    },
    {   # Pattern 8 - Gregorian/Hijri Cross Match Bracketed
        "pattern": rf'(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
        "name": "alternating_gregorian_hijri_m_y_pairs",
        "description": "Matches alternating Gregorian/Hijri month-year pairs",
        "examples": [  # Original: "example": "يناير 2023 م/ محرم 1445 هـ"
            "(يناير 2023 م / محرم 1445 هـ) (فبراير 2023 م / صفر 1445 هـ)",
            "[مارس 2022 م / رجب 1443 هـ] [إبريل 2022 م / شعبان 1443 هـ]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": [1, 4], "year": [2, 5], "century": None, "era": [3, 6], "calendar" : "gregorian"
            },
    },
    {   # Pattern 10 - Hijri/Gregorian Pair in (Hijri/Gregorian) (Hijri/Gregorian) Format
        "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "paired_hijri_gregorian_full_dates",  # Original: "hijri_full_date"
        "description": "Matches paired full Hijri and Gregorian dates wrapped in brackets",
        "examples": [  # Original: "example": "15/03/1445 هـ/ 15/03/2023 م"
            "(15/03/1445 هـ / 15/03/2023 م) (16/03/1445 هـ / 16/03/2023 م)",
            "[01/01/1400 هـ / 01/01/1980 م] [02/01/1400 هـ / 02/01/1980 م]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        "julian": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "julian"
            }
    },
    {   # Pattern 11 - Gregorian/Hijri Pair in (Gregorian/Hijri) (Gregorian/Hijri) Format
        "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "paired_gregorian_hijri_full_dates",  # Original: "gregorian_full_date"
        "description": "Matches paired full Gregorian and Hijri dates wrapped in brackets",
        "examples": [  # Original: "example": "15/03/2023 م/ 15/03/1445 هـ"
            "(15/03/2023 م / 15/03/1445 هـ) (16/03/2023 م / 16/03/1445 هـ)",
            "[01/01/1980 م / 01/01/1400 هـ] [02/01/1980 م / 02/01/1400 هـ]"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": None, "day": None, "month": None, "month_name": None, "year": None, "century": None, "era": None, "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": [1, 5], "month": [2, 6], "year": [3, 7], "century": None, "era": [4, 8], "calendar" : "gregorian"
            },
        
    },
    # 6. NATURAL LANGUAGE DATE PATTERNS
    {   # Pattern 13 - Natural Hijri-Gregorian Pair in Brackets with Day Name   
        "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "natural_language_hijri_gregorian_pair",  # Original: "natural_hijri"
        "description": "Matches natural language Hijri and Gregorian dates with day name, inside brackets",
        "examples": [  # Original: "example": "الجمعة 15 11 1445 هـ/ 15 11 2023 م"
            "(الجمعة 15 محرم 1445 هـ / 15 يناير 2023 م) (السبت 16 محرم 1445 هـ / 16 يناير 2023 م)"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "hijri": {
            "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "hijri"
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
        }, 
    },
    {   # Pattern 14 - Natural Gregorian-Hijri Pair in Brackets with Day Name
        "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
        "name": "natural_language_gregorian_hijri_pair",  # Original: "natural_gregorian"
        "description": "Matches natural language Gregorian and Hijri dates with day name, inside brackets",
        "examples": [  # Original: "example": "الجمعة 15 يناير 2023 ميلاديًا/ 15 محرم 1445 هجريًا"
            "(الجمعة 15 يناير 2023 م / 15 محرم 1445 هـ) (السبت 16 يناير 2023 م / 16 محرم 1445 هـ)"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": [1, 6], "day": [2, 7], "month": [3, 8], "year": [4, 9], "century": None, "era": [5, 10], "calendar" : "gregorian"
            },
    },
    # 5. FULL DATE PATTERNS (day/month/year)  "15 محرم 1445",## 
    {   # Pattern 42 - Hijri to Hijri range with symbolic and full pattern
        "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_symbolic",  # Original: "from_to_hijri_hijri_d_m_y"
        "description": "Matches a Hijri to Hijri range with symbolic suffixes (e.g., هـ)",
        "examples": [
            "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
            "من 01 رمضان 1444 هـ إلى 10 رمضان 1444 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            }, 
    },
    {   # Pattern 43 - Gregorian to Gregorian range with symbolic suffixes
        "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_symbolic",  # Original: "from_to_gregorian_gregorian_d_m_y"
        "description": "Matches a Gregorian to Gregorian date range with symbolic suffixes (e.g., م)",
        "examples": [
            "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
            "من 01 مارس 2022 م إلى 15 أبريل 2022 م"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },      
    },
    {   # Pattern 30 - Duplicate of Pattern 42 (Consider deprecating)
        "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_basic",  # Original: "from_to_hijri_hijri_d_m_y"
        "description": "Hijri-Hijri range without symbolic suffixes",
        "examples": [
            "من 15 محرم 1445 إلى 20 صفر 1445"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 40 - Duplicate of Pattern 43 (Consider merging)
        "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_basic",  # Original: "from_to_gregorian_gregorian_d_m_y"
        "description": "Gregorian date range without suffixes",
        "examples": [
            "من 10 يناير 2024 إلى 20 ديسمبر 2024"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 54 - Hijri range with weekdays
        "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_to_hijri_weekday",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
        "description": "Matches Hijri range with weekday labels",
        "examples": [
            "من الأحد - 15 محرم 1445 هـ إلى الثلاثاء - 20 صفر 1445 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 55 - Gregorian range with weekdays
        "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_to_gregorian_weekday",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
        "description": "Gregorian range including weekday names",
        "examples": ["من الأحد - 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
                     "من الأحد - 10 يناير 2024 م إلى الأربعاء - 20 ديسمبر 2024 م"],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },         "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },  
    # 1. HIGHEST PRIORITY - COMPLEX RANGE PATTERNS (week_day - DD/MM/YYYY)
    {   # Pattern 51 - Hijri range with natural weekday format
        "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
        "name": "range_hijri_natural_weekday",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
        "description": "Hijri-Hijri range using natural weekday pattern",
        "examples": [
            "من الأحد - 15 محرم 1445 هـ إلى الاثنين - 20 صفر 1445 هـ"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
    },
    {   # Pattern 52 - Gregorian range with natural weekday
        "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
        "name": "range_gregorian_natural_weekday",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
        "description": "Gregorian-Gregorian range using weekday and full date",
        "examples": [
            "من الأحد - 10 يناير 2024 م إلى الاثنين - 20 ديسمبر 2024 م"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
        },
    },
]

# ===================================================================================
# RANGE-BASED FULL CALENDAR MAPPINGS (TO BE REFACTORED)
# ===================================================================================
match_type": "range",
FULL_DATE_RANGE_PATTERNS = [
    {  # Pattern 1 - Hijri Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_y_pattern}\b',
        "name": "range_hijri_year_to_year",  # Original: "from_to_hijri_hijri_yr"
        "description": "Matches a range from Hijri year to Hijri year with Arabic range indicators",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "من 1440 هـ إلى 1445 هـ",
            "1441 هـ إلى 1443 هـ",
            "عام 1430 هـ إلى 1440 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }   
    },
    {  # Pattern 2 - Gregorian Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_y_pattern}\b',
        "name": "range_gregorian_year_to_year",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Matches a range from Gregorian year to Gregorian year using Arabic connectors",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "من 2020 م إلى 2024 م",
            "2021 م حتى 2023 م",
            "بين عامي 2019 م و 2022 م"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 3 - julian Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+({julian_y_pattern})\s+{IndicatorPatterns.range_connector}\s+{julian_y_pattern}\b',
        "name": "range_julian_year_to_year",  # Original: "from_to_julian_julian_yr"
        "description": "Matches a range from julian year to julian year using Arabic/Persian connectors",
        "examples": [  # Original: "example": "من 1402 هـ.ش إلى 1405 هـ.ش"
            "من 1402 هـ.ش إلى 1405 هـ.ش",
            "1400 هـ.ش حتى 1403 هـ.ش"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }
        
    },
    {  # Pattern 4 - Hijri Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_y_pattern}\b',
        "name": "range_hijri_year_alt_suffixed",  # Original: "from_to_hijri_hijri_yr"
        "description": "Matches an alternate Hijri year range where start year has a suffix pattern",
        "examples": [  # Original: "example": "من 1440 هـ إلى 1445 هـ"
            "من 1440 هـ إلى 1445 هـ",
            "1442 هـ إلى 1444"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }   
    },
    {  # Pattern 5 - Gregorian Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_y_pattern}\b',
        "name": "range_gregorian_year_alt_suffixed",  # Original: "from_to_gregorian_gregorian_yr"
        "description": "Matches an alternate Gregorian year range where start year has a suffix",
        "examples": [  # Original: "example": "من 2020 م إلى 2024 م"
            "من 2020 م إلى 2024 م",
            "2021 م إلى 2023"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 6 - julian Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+({julian_y_pattern_s})\s+{IndicatorPatterns.range_connector}\s+{julian_y_pattern}\b',
        "name": "range_julian_year_alt_suffixed",  # Original: "from_to_julian_julian_yr"
        "description": "Matches an alternate julian year range where start year has a suffix",
        "examples": [  # Original: "example": "من 1402 هـ.ش إلى 1405 هـ.ش"
            "من 1402 هـ.ش إلى 1405 هـ.ش",
            "1403 هـ.ش إلى 1406"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }
    },
    {  # Pattern 7 - Hijri Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_m_y_pattern}\b',
        "name": "range_hijri_month_year_to_month_year",  # Original: "from_to_hijri_hijri_m_y"
        "description": "Matches a range from Hijri month/year to Hijri month/year with Arabic connectors",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
            "من محرم 1440 هـ إلى صفر 1445 هـ",
            "رجب 1435 هـ حتى شعبان 1440 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": 1, "year": 2, "century": None, "era": 3, "calendar": "hijri"
        },
        "date_end": {
            "weekday": None, "day": None, "month": 4, "year": 5, "century": None, "era": 6, "calendar": "hijri"
        }
    },
    {  # Pattern 8 - Gregorian Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_m_y_pattern}\b',
        "name": "range_gregorian_month_year_to_month_year",  # Original: "from_to_gregorian_gregorian_m_y"
        "description": "Matches a range from Gregorian month/year to Gregorian month/year with Arabic connectors",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
            "من يناير 2020 م إلى ديسمبر 2024 م",
            "مارس 2022 م حتى أكتوبر 2023 م"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 9 - julian Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{julian_m_y_pattern}\b',
        "name": "range_julian_month_year_to_month_year",  # Original: "from_to_julian_julian_m_y"
        "description": "Matches a range from julian month/year to julian month/year with Arabic or Persian connectors",
        "examples": [  # Original: "example": "من فروردین 1402 هـ.ش إلى خرداد  1405 هـ.ش"
            "من فروردین 1402 هـ.ش إلى خرداد 1405 هـ.ش",
            "مرداد 1399 هـ.ش حتى فروردین 1403 هـ.ش"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 10 - Hijri Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_m_y_pattern}\b',
        "name": "range_hijri_month_year_alt_suffixed",  # Original: "from_to_hijri_hijri_m_y"
        "description": "Alternate Hijri month/year range: start with suffix, end without",
        "examples": [  # Original: "example": "من محرم 1440 هـ إلى صفر 1445 هـ"
            "من محرم 1440 هـ إلى صفر 1445 هـ",
            "ربيع الأول 1435 هـ إلى رجب 1440"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }
    },
    {  # Pattern 11 - Gregorian Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_m_y_pattern}\b',
        "name": "range_gregorian_month_year_alt_suffixed",  # Original: "from_to_gregorian_gregorian_m_y"
        "description": "Alternate Gregorian month/year range: start has suffix",
        "examples": [  # Original: "example": "من يناير 2020 م إلى ديسمبر 2024 م"
            "من يناير 2020 م إلى ديسمبر 2024 م",
            "مارس 2022 م إلى نوفمبر 2024"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 12 - julian Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{julian_m_y_pattern}\b',
        "name": "range_julian_month_year_alt_suffixed",  # Original: "from_to_julian_julian_m_y"
        "description": "Alternate julian month/year range: start suffixed, end plain",
        "examples": [  # Original: "example": "من فروردین 1402 هـ.ش إلى خرداد  1405 هـ.ش"
            "من فروردین 1402 هـ.ش إلى خرداد 1405 هـ.ش",
            "تیر 1399 هـ.ش إلى اسفند 1403"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 13 - Hijri Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_d_m_y_pattern}\b',
        "name": "range_hijri_day_month_year_to_day_month_year",  # Original: "from_to_hijri_hijri_d_m_y"
        "description": "Matches a range from Hijri full date to Hijri full date with Arabic connectors",
        "examples": [  # Original: "example": "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ"
            "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
            "10 رجب 1430 هـ حتى 25 شعبان 1442 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 14 - Gregorian Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_d_m_y_pattern}\b',
        "name": "range_gregorian_day_month_year_to_day_month_year",  # Original: "from_to_gregorian_gregorian_d_m_y"
        "description": "Matches a range from Gregorian full date to Gregorian full date with Arabic connectors",
        "examples": [  # Original: "example": "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م"
            "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
            "1 مارس 2020 م حتى 15 أكتوبر 2021 م"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }         
    },
    {  # Pattern 15 - julian Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{julian_d_m_y_pattern}\b',
        "name": "range_julian_day_month_year_to_day_month_year",  # Original: "from_to_julian_julian_d_m_y"
        "description": "Matches a range from julian full date to julian full date with Arabic or Persian connectors",
        "examples": [  # Original: "example": "من 10 فروردین 1402 هـ.ش إلى 20 خرداد 1405 هـ.ش"
            "من 10 فروردین 1402 هـ.ش إلى 20 خرداد 1405 هـ.ش",
            "5 اسفند 1398 هـ.ش حتى 1 فروردین 1403 هـ.ش"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    
    {  # Pattern 16 - Hijri Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_d_m_y_pattern}\b',
        "name": "range_hijri_day_month_year_alt_suffixed",  # Original: "from_to_hijri_hijri_d_m_y"
        "description": "Alternate Hijri full date range: suffix on first date only",
        "examples": [
            "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
            "1 رمضان 1440 هـ حتى 10 شوال 1440"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 17 - Gregorian Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_d_m_y_pattern}\b',
        "name": "range_gregorian_day_month_year_alt_suffixed",  # Original: "from_to_gregorian_gregorian_d_m_y"
        "description": "Alternate Gregorian full date range: suffix on start date only",
        "examples": [
            "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
            "5 فبراير 2021 م حتى 18 مايو 2022"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            }         
    },
    {  # Pattern 18 - julian Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{julian_d_m_y_pattern}\b',
        "name": "range_julian_day_month_year_alt_suffixed",  # Original: "from_to_julian_julian_d_m_y"
        "description": "Alternate julian full date range: suffix on start date only",
        "examples": [
            "من 10 فروردین 1402 هـ.ش إلى 20 خرداد 1405 هـ.ش",
            "1 دی 1399 هـ.ش حتى 15 بهمن 1403"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    
    {  # Pattern 20 - Hijri Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_hijri_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_hijri_pattern}\b',
        "name": "range_hijri_weekday_day_month_year",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
        "description": "Matches a range from Hijri date (with weekday) to Hijri date using Arabic connectors",
        "examples": [  # Original: "example": "من الأحد - 15 محرم 1445 هـ إلى 20 صفر 1445 هـ"
            "من الأحد - 15 محرم 1445 هـ إلى الخميس - 20 صفر 1445 هـ",
            "السبت 5 رجب 1432 هـ حتى الثلاثاء 10 شعبان 1432 هـ"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 21 - Gregorian Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_gregorian_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_gregorian_pattern}\b',
        "name": "range_gregorian_weekday_day_month_year",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
        "description": "Matches a range from Gregorian date (with weekday) to Gregorian date using Arabic connectors",
        "examples": [
            "من الأحد - 10 يناير 2024 م إلى الخميس - 20 ديسمبر 2024 م",
            "الثلاثاء 5 مارس 2023 م حتى الجمعة 10 أبريل 2023"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 22 - julian Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_julian_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_julian_pattern}\b',
        "name": "range_julian_weekday_day_month_year",  # Original: "from_to_julian_julian_week_day_d_m_y"
        "description": "Matches a range from julian date (with weekday) to julian date using Arabic or Persian connectors",
        "examples": [
            "من شنبه - 10 فروردین 1402 هـ.ش إلى پنج‌شنبه - 20 خرداد 1405 هـ.ش",
            "سه‌شنبه 1 اسفند 1399 هـ.ش حتى جمعه 10 فروردین 1400 هـ.ش"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 23 - Hijri Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_hijri_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_hijri_pattern}\b',
        "name": "range_hijri_weekday_day_month_year_alt_suffixed",  # Original: "from_to_hijri_hijri_week_day_d_m_y"
        "description": "Alternate Hijri date range: suffix on first date only (with weekday)",
        "examples": [
            "من الأحد - 15 محرم 1445 هـ إلى الخميس - 20 صفر 1445 هـ",
            "الثلاثاء - 10 رمضان 1435 هـ حتى الجمعة 20 شوال 1435"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {  # Pattern 24 - Gregorian Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_gregorian_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_gregorian_pattern}\b',
        "name": "range_gregorian_weekday_day_month_year_alt_suffixed",  # Original: "from_to_gregorian_gregorian_week_day_d_m_y"
        "description": "Alternate Gregorian date range: suffix on start date only (with weekday)",
        "examples": [
            "من الأحد - 10 يناير 2024 م إلى الخميس - 20 ديسمبر 2024 م",
            "الاثنين - 5 فبراير 2021 م حتى الخميس 18 مايو 2022"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },
    {   # Pattern 25 - julian Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_julian_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_julian_pattern}\b',
        "name": "range_julian_weekday_day_month_year_alt_suffixed",  # Original: "from_to_julian_julian_week_day_d_m_y"
        "description": "Alternate julian date range: suffix on first date only (with weekday)",
        "examples": [
            "من شنبه - 10 فروردین 1402 هـ.ش إلى پنج‌شنبه - 20 خرداد 1405 هـ.ش",
            "جمعه - 1 آذر 1397 هـ.ش حتى دوشنبه 12 دی 1400 هـ.ش"
        ],
        
        
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },        
        
        "gregorian": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : "gregorian"
            },
        
        "hijri_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "gregorian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        "julian_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            } 
    },    
]