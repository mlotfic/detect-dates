# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    from path_helper import add_modules_to_sys_path
    add_modules_to_sys_path()

from modules.regex_patterns import get_date_patterns
from modules.patterns import DatePatterns

try:
    # Demonstrate with Arabic language patterns
    print("\n1. Loading Arabic language patterns..")
    pattern_data = get_date_patterns(lang="ar")
    
    # Unpack pattern data with explicit naming
    base_patterns, month_patterns, era_patterns, indicator_patterns, numeric_patterns = pattern_data
    
    date_patterns = DatePatterns(
        base_patterns=base_patterns,
        month_patterns=month_patterns,
        era_patterns=era_patterns,
        indicator_patterns=indicator_patterns,
        numeric_patterns=numeric_patterns
    )
    
    print(f"   ✓ Arabic patterns loaded: {date_patterns}")
    
    # Demonstrate pattern hierarchy access
    print("\n2. Exploring pattern hierarchy..")
    all_patterns = date_patterns.get_all_patterns()
        
    for complexity, patterns in all_patterns.items():
        print(f"   {complexity.capitalize()} level: {len(patterns)} pattern types")
            
    # Demonstrate specific pattern access
    print("\n3. Accessing specific patterns..")
    try:
        complex_date_pattern = date_patterns.get_pattern_by_complexity(
            'day_month_year', 'complex'
        )
        print(f"   ✓ Complex date pattern: {type(complex_date_pattern).__name__}")
        
    except (KeyError, ValueError) as e:
        print(f"   ✗ Error accessing pattern: {e}")
            
    # Show language information
    print("\n4. Language configuration:")
    lang_info = date_patterns.get_language_info()
    for key, value in lang_info.items():
        print(f"   {key}: {value}")
        
    print("\n✓ DatePatterns demonstration completed successfully!")
        
except AttributeError as e:
    print(f"\n✗ Pattern structure error: {e}")
    print("   Please ensure numeric patterns include hijri date support")
    
except Exception as e:
    print(f"\n✗ Unexpected error: {e}")
    print("   Please check pattern data structure and module configuration.")



# Comprehensive numeric patterns
# ===================================================================================
unknown_calendar = {
    "metadata" : {
        "priority": 0,
        "match_type": "ambiguity",
    },
    "patterns" : [
        {   # Pattern 0 - Numeric Year (Ambiguous Calendar)
            "pattern": date_patterns.yy.numeric,
            "name": "date_patterns.yy.numeric",
            "description": "Numeric format - requires calendar context for disambiguation",
            "examples": [  
                "1445",    # Could be Hijri (year 1445 AH ≈ 2023-2024 CE)
                "2023",    # Likely Gregorian (contemporary year)
                "1398",    # Could be julian (year 1398 SH ≈ 2019-2020 CE)
                "1446",    # Could be Hijri (year 1446 AH ≈ 2024-2025 CE)
                "2024",    # Likely Gregorian (contemporary year)
                "1401"     # Could be julian (year 1401 SH ≈ 2022-2023 CE)
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": None, "calendar": ""
            },
        },
        {  # Pattern 0 - Month/Year Numeric (Ambiguous Calendar)
            "pattern": date_patterns.mm_yy.numeric,
            "name": "date_patterns.mm_yy.numeric",
            "description": "Numeric/Numeric format - ambiguous calendar detection required",
            "examples": [  
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
            "date": { "weekday": None, "day": None, "month": 1, "year": 2, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 1 - Day/Month/Year Numeric (Ambiguous Calendar)
            "pattern": date_patterns.dd_mm_yy.numeric,
            "name": "date_patterns.dd_mm_yy.numeric",
            "description": "Numeric day/month/year format - requires calendar context for disambiguation",
            "examples": [  
                "01/12/1440",  # 1st Dhul Hijjah 1440 AH (Hijri) or invalid Gregorian
                "02/01/2023",  # 2nd January 2023 CE (Gregorian)
                "15/03/1398",  # 15th month invalid - likely day/month confusion
                "25/12/2024",  # 25th December 2024 CE (Gregorian)
                "10/06/1445",  # Could be 10th Jumada al-Thani 1445 AH (Hijri)
                "31/01/1401"   # Could be julian format
            ],
            "date": { "weekday": None, "day": 1, "month": 2, "year": 3, "century": None, "era": None,  "calendar": "" },
        },
    ]
}

# ====================================================================================
# Comprehensive date components patterns
# ====================================================================================
date_components_patterns_dict = {
    "metadata": {
        "priority": 1,  
        "match_type": "components",
    },
    "patterns": [
        {  # Pattern 0 - Weekday Component
            "pattern": date_patterns.dd,
            "name": "date_patterns.dd",
            "description": "Day component - requires calendar context for disambiguation",
            "examples": [
                "الاحد",
                "الاثنين",
                "الثلاثاء",
            ],
            "date": { "weekday": 1, "day": 2, "month": None, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 1 - Numeric Day Component (Ambiguous Calendar)
            "pattern": rf"{date_patterns.indicator.day}{date_patterns.indicator.separator}{date_patterns.numeric.day}",
            "name": "day_component",
            "description": "Day component - requires calendar context for disambiguation",
            "examples": [
                "يوم 01",
                "يوم 02",
            ],
            "date": { "weekday": 1, "day": 2, "month": None, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 1 - Numeric Day Component (Ambiguous Calendar)
            "pattern": rf"{date_patterns.indicator.month}{date_patterns.indicator.separator}{date_patterns.numeric.month}",
            "name": "month_component",
            "description": "Day component - ambiguous calendar",
            "examples": [
                "شهر 01",
                "شهر 02",
            ],
            "date": { "weekday": 1, "day": 2, "month": None, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 2 - Month Component (Hijri Calendar) 
            "pattern": date_patterns.mm.hijri,
            "name": "month_component_hijri",
            "description": "Month component - hijri calendar",
            "examples": [  
                "محرم",            
            ],
            "date": { "weekday": None, "day": None, "month": 1, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 3 - Month Component (Gregorian Calendar)
            "pattern": date_patterns.mm.gregorian,
            "name": "month_component_gregorian",
            "description": "Month component - gregorian calendar",
            "examples": [ 
                "January",
                "فبراير",              
            ],
            "date": { "weekday": None, "day": None, "month": 1, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 4 - Month Component (julian Calendar)
            "pattern": date_patterns.mm.julian,
            "name": "month_component_julian",
            "description": "Month component - julian calendar",
            "examples": [
                "فروردین",
                "اردیبهشت",
            ],
            "date": { "weekday": None, "day": None, "month": 1, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 5 - Year Component (Ambiguous Calendar)
            "pattern": rf"{date_patterns.indicator.year}{date_patterns.indicator.separator}{date_patterns.numeric.year}",
            "name": "year_component",
            "description": "Year component - ambiguous calendar",
            "examples": [
                "سنة 2023",   
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": 1, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 3 - century Component
            "pattern": rf"{date_patterns.indicator.century}{date_patterns.indicator.separator}{date_patterns.numeric.century}",
            "name": "century_component",
            "description": "Century component - ambiguous calendar",
            "examples": [
                "القرن 21",
                "القرن 20",
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": 1, "era": None, "calendar": "" },
        },
        {  # Pattern 4 - Era Component
            "pattern": date_patterns.era.hijri,
            "name": "era_component_hijri",
            "description": "Era component - hijri calendar",
            "examples": [
                "هجري",      # Hijri era
                "هجرية",     # Hijri era (feminine)
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": 1, "calendar": "" },
        },
        {  # Pattern 4 - Era Component
            "pattern": date_patterns.era.gregorian,
            "name": "era_component",
            "description": "Era component - gregorian calendar",
            "examples": [
                "ميلادي",     # Gregorian era
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": 1, "calendar": "" },
        },
        {  # Pattern 4 - Era Component
            "pattern": date_patterns.era.julian,
            "name": "era_component",
            "description": "Era component - julian calendar",
            "examples": [
                "هجری شمسی",  # julian era (Persian)
                "شمسي",      # julian era
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": 1, "calendar": "" },
        },
    ]
}

# ===================================================================================
# Comprehensive date patterns
# ===================================================================================
basic_date_pattern_dict = {
    "metadata" : {
        "priority": 5,
        "match_type": "base",
    },    
    "patterns": [
        {  # Pattern 0 - Day/Month/Year with Weekday Prefix
            "pattern": date_patterns.weekday_dd_mm_yy.numeric,
            "name": "date_patterns.weekday_dd_mm_yy.numeric",
            "description": "Weekday-prefixed numeric date format - weekday can help validate calendar accuracy",
            "examples": [
                "الأحد 01/12/1440",      # Sunday 1st Dhul Hijjah 1440 AH
                "الاثنين 02/01/2023",    # Monday 2nd January 2023 CE
                "الثلاثاء 15/03/1398",   # Tuesday - needs calendar validation
                "الأربعاء 25/12/2024",   # Wednesday 25th December 2024 CE
                "الخميس 10/06/1445",     # Thursday - Hijri date
                "الجمعة 20/11/1401"      # Friday - could be julian
            ],
            "date": { "weekday": 1, "day": 2,  "month": 3, "year": 4, "century": None, "era": None, "calendar": ""},
        },
        {  # Pattern 1 - Basic Hijri Year with Era Marker
            "pattern": date_patterns.yy.hijri.numeric,
            "name": "date_patterns.yy.hijri.numeric",
            "description": "Hijri year with explicit era marker - unambiguous calendar identification",
            "examples": [
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
        {  # Pattern 2 - Basic Gregorian Year with Era Marker
            "pattern": date_patterns.yy.gregorian.numeric,
            "name": "date_patterns.yy.gregorian.numeric",
            "description": "Gregorian year with explicit era marker - unambiguous calendar identification",
            "examples": [
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
        {  # Pattern 3 - Basic julian Year with Era Marker
            "pattern": date_patterns.yy.julian.numeric,
            "name": "date_patterns.yy.julian.numeric",
            "description": "julian/Solar Hijri year with explicit era marker - unambiguous calendar identification",
            "examples": [
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
                "year": 1,
                "century": None,
                "era": 2,
                "calendar": "julian"
            },
        },
        # ================================================= #
        {  # Pattern 4 - Hijri Month/Year with Era Marker
            "pattern": date_patterns.mm_yy.hijri.combined,
            "name": "date_patterns.mm_yy.hijri.combined",
            "description": "Hijri month/year with explicit era marker - supports both numeric and named months",
            "examples": [
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
        {  # Pattern 5 - Gregorian Month/Year with Era Marker
            "pattern": date_patterns.mm_yy.gregorian.combined,
            "name": "date_patterns.mm_yy.gregorian.combined",
            "description": "Gregorian month/year with explicit era marker - supports Arabic and English month names",
            "examples": [
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
        {  # Pattern 6 - julian Month/Year with Era Marker
            "pattern": date_patterns.mm_yy.julian.combined,
            "name": "date_patterns.mm_yy.julian.combined",
            "description": "julian month/year with explicit era marker - supports Persian month names",
            "examples": [
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
        # ===================================================== #
        {  # Pattern 7 - Complete Hijri Date with Era Marker
            "pattern": date_patterns.dd_mm_yy.hijri.combined,
            "name": "date_patterns.dd_mm_yy.hijri.combined",
            "description": "Complete Hijri date with day/month/year and explicit era marker",
            "examples": [
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
        {  # Pattern 8 - Complete Gregorian Date with Era Marker
            "pattern": date_patterns.dd_mm_yy.gregorian.combined,
            "name": "date_patterns.dd_mm_yy.gregorian.combined",
            "description": "Complete Gregorian date with day/month/year and explicit era marker",
            "examples": [
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
        {  # Pattern 9 - Complete julian Date with Era Marker
            "pattern": date_patterns.dd_mm_yy.julian.combined,
            "name": "date_patterns.dd_mm_yy.julian.combined",
            "description": "Complete julian date with day/month/year and explicit era marker",
            "examples": [
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
        # ===================================================== #
        {  # Pattern 10 - Natural Language Hijri Date
            "pattern": date_patterns.natural_language.hijri.combined,
            "name": "date_patterns.natural_language.hijri.combined",
            "description": "Natural language Hijri date with weekday, day, month name, year, and era marker",
            "examples": [
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
        {  # Pattern 11 - Natural Language Gregorian Date
            "pattern": date_patterns.natural_language.gregorian.combined,
            "name": "date_patterns.natural_language.gregorian.combined",
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
        {  # Pattern 12 - Natural Language julian Date
            "pattern": date_patterns.natural_language.julian.combined,
            "name": "date_patterns.natural_language.julian.combined",
            "description": "Natural language julian date with weekday, day, month name, year, and era marker",
            "examples": [
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

# ==================================================================================================================================
# 
# ==================================================================================================================================
date_mixed_patterns_dict = {
    "metadata": {
        "priority": 5,  
        "match_type": "mixed",
    },
    "patterns": [
        {  # Pattern 0 - Hijri Year Range (start+end)
            "pattern": date_patterns.cs_yy.hijri.mixed,
            "name": "date_patterns.cs_yy.hijri.mixed",
            "description": "Hijri year to Hijri year range using 'من .. إلى ..' format",
            "examples": [
                "من 1440 هـ إلى 1445 هـ",
                "1442هـ / 1444هـ",
                "١٤٣٠ هـ – ١٤٤٠ هـ",
                "1440 هـ / 1445 هـ",
                "١٤٣٥ هـ - ١٤٤١ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 1 - Gregorian Year Range
            "pattern": date_patterns.cs_yy.gregorian.mixed,
            "name": "date_patterns.cs_yy.gregorian.mixed",
            "description": "Gregorian year to Gregorian year range using Arabic connectors",
            "examples": [
                "من 2020 م إلى 2024 م",
                "٢٠١٠ م / ٢٠٢٠ م",
                "1995م – 2005م",
                "2020 م / 2024 م",
                "٢٠١٥ م - ٢٠٢٠ م",
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
        },
        
        {
            # Pattern 3 - 
            "pattern": date_patterns.cs_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.cs_yy.hijri.mixed_parenthetical",
            "description": "Hijri year to Hijri year range using parentheses for the second year",
            "examples": [
                "من 1440 هـ (1445 هـ)",
                "1442هـ (1444هـ)",
                "١٤٣٠ هـ (١٤٤٠ هـ)",
                "1440 هـ (1445 هـ)",
                "١٤٣٥ هـ (١٤٤١ هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },            
        },
        {
            # Pattern 4 -
            "pattern": date_patterns.cs_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.cs_yy.gregorian.mixed_parenthetical",
            "description": "Gregorian year to Gregorian year range using parentheses for the second year",
            "examples": [
                "من 2020 م (2024 م)",
                "٢٠١٠ م (٢٠٢٠ م)",
                "1995م (2005م)",
                "2020 م (2024 م)",
                "٢٠١٥ م (٢٠٢٠ م)",
                "2020 م (2024 م)",
                "٢٠١٥م (٢٠٢٢م)",
                "من 2020 م (2024 م)"
            ],
        },
        {  # Pattern 4 - Hijri/Gregorian Combined (Hijri First)
            "pattern": date_patterns.cs_yy.hijri.alternative,
            "name": "date_patterns.cs_yy.hijri.alternative",
            "description": "Hijri year followed by Gregorian year (parallel calendar style)",
            "examples": [
                "1440 هـ/2023 م",
                "١٤٤٥ هـ - ٢٠٢٤ م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },   
        {  # Pattern 5 - Gregorian/Hijri Combined (Gregorian First)
            "pattern": date_patterns.cs_yy.gregorian.alternative,
            "name": "date_patterns.cs_yy.gregorian.alternative",
            "description": "Gregorian year followed by Hijri year (parallel calendar style)",
            "examples": [
                "2023 م/1440 هـ",
                "٢٠٢٤ م - ١٤٤٥ هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 6 - Hijri/Gregorian Combined with Parentheses (Hijri First)
            "pattern": date_patterns.cs_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.cs_yy.hijri.alternative_parenthetical",
            "description": "Hijri year followed by Gregorian year in parentheses (parallel calendar style)",
            "examples": [
                "1440 هـ (2023 م)",
                "١٤٤٥ هـ - (٢٠٢٤ م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 7 - Gregorian/Hijri Combined with Parentheses (Gregorian First)
            "pattern": date_patterns.cs_yy.gregorian.alternative_parenthetical,
            "name": "date_patterns.cs_yy.gregorian.alternative_parenthetical",
            "description": "Gregorian year followed by Hijri year in parentheses (parallel calendar style)",
            "examples": [
                "2023 م (1440 هـ)",
                "٢٠٢٤ م - (١٤٤٥ هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        
        # ===================================================================================
        # 7. MONTH-YEAR PATTERNS (RANGES & MIXED CALENDARS)
        # ===================================================================================
        {  # Pattern 6 - Hijri Month-Year to Hijri Month-Year
            "pattern": date_patterns.cs_mm_yy.hijri.mixed,
            "name": "date_patterns.cs_mm_yy.hijri.mixed",
            "description": "Matches Hijri month/year range using Arabic connectors like 'من .. إلى ..'",
            "examples": [
                "من محرم 1440 هـ إلى صفر 1445 هـ",
                "ذو القعدة 1443 هـ - محرم 1444 هـ",
                "ربيع الأول 1445 هـ / رجب 1446 هـ",
                "من شعبان 1442 هـ إلى رمضان 1443 هـ",
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
        {  # Pattern 7 - Gregorian Month-Year to Gregorian Month-Year
            "pattern": date_patterns.cs_mm_yy.gregorian.mixed,
            "name": "date_patterns.cs_mm_yy.gregorian.mixed",
            "description": "Matches Gregorian month/year range using Arabic connectors",
            "examples": [
                "من يناير 2020 م إلى ديسمبر 2024 م",
                "مارس 2022 م / أغسطس 2024 م",
                "يناير 2023 م - ديسمبر 2024 م",
                "من يونيو 2021 م إلى مايو 2023 م",
                "يناير 2020 م / ديسمبر 2024 م",
                "مارس ٢٠٢٠ - يونيو ٢٠٢٣"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 8 - Hijri Month-Year to Hijri Month-Year with Parentheses
            "pattern": date_patterns.cs_mm_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.cs_mm_yy.hijri.mixed_parenthetical",
            "description": "Hijri month/year range using parentheses for the second date",
            "examples": [
                "من محرم 1440 هـ (صفر 1445 هـ)",
                "ذو القعدة 1443 هـ - (محرم 1444 هـ)",
                "ربيع الأول 1445 هـ / (رجب 1446 هـ)",
                "من شعبان 1442 هـ إلى (رمضان 1443 هـ)",
                "محرم 1440 هـ / (صفر 1445 هـ)",
                "شعبان ١٤٤٠ هـ - (رمضان ١٤٤٢ هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 9 - Gregorian Month-Year to Gregorian Month-Year with Parentheses
            "pattern": date_patterns.cs_mm_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.cs_mm_yy.gregorian.mixed_parenthetical",
            "description": "Gregorian month/year range using parentheses for the second date",
            "examples": [
                "من يناير 2020 م (ديسمبر 2024 م)",
                "مارس 2022 م / (أغسطس 2024 م)",
                "يناير 2023 م - (ديسمبر 2024 م)",
                "من يونيو 2021 م إلى (مايو 2023 م)",
                "يناير 2020 م / (ديسمبر 2024 م)",
                "مارس ٢٠٢٠ - (يونيو ٢٠٢٣)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 7 - Hijri + Gregorian M/Y combo (Hijri first)
            "pattern": date_patterns.cs_mm_yy.hijri.alternative,
            "name": "date_patterns.cs_mm_yy.hijri.alternative",
            "description": "Hijri month/year followed by Gregorian month/year (parallel calendar style)",
            "examples": [  
                "12/1440 هـ / 01/2023 م",
                "محرم 1445 هـ / يناير 2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            
        },
        {  # Pattern 8 - Gregorian + Hijri M/Y combo (Gregorian first)
            "pattern": date_patterns.cs_mm_yy.gregorian.alternative,
            "name": "date_patterns.cs_mm_yy.gregorian.alternative",
            "description": "Gregorian month/year followed by Hijri month/year (parallel calendar style)",
            "examples": [  
                "يناير 2023 م / محرم 1445 هـ",
                "01/2023 م - 01/1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 9 - Hijri + Gregorian M/Y combo with Parentheses (Hijri first)
            "pattern": date_patterns.cs_mm_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.cs_mm_yy.hijri.alternative_parenthetical",
            "description": "Hijri month/year followed by Gregorian month/year in parentheses (parallel calendar style)",
            "examples": [
                "12/1440 هـ (01/2023 م)",
                "محرم 1445 هـ (يناير 2024 م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 10 - Gregorian + Hijri M/Y combo with Parentheses (Gregorian first)
            "pattern": date_patterns.cs_mm_yy.gregorian.alternative_parenthetical,  
            "name": "single_alternative_gregorian_hijri_month_years_parenthetical",
            "description": "Gregorian month/year followed by Hijri month/year in parentheses (parallel calendar style)",
            "examples": [
                "01/2023 م (12/1440 هـ)",
                "يناير 2024 م (محرم 1445 هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        # ===================================================================================
        # 5. FULL DATE PATTERNS (day/month/year)
        # ===================================================================================
        {  # Pattern 6 - Hijri Month-Year to Hijri Month-Year
            "pattern": date_patterns.cs_dd_mm_yy.hijri.mixed,
            "name": "date_patterns.cs_dd_mm_yy.hijri.mixed",
            "description": "Hijri full date with day/month/year and explicit era marker",
            "examples": [
                "من 15/03/1445 هـ إلى 01/04/1446 هـ",
                "15/محرم/1440 هـ - 10/صفر/1445 هـ",
                "27/رمضان/1445 هـ / 01/شوال/1446 هـ",
                "من 10/ذو الحجة/1444 هـ إلى 25/محرم/1445 هـ",
                "25/12/1443 هـ / 01/01/1445 هـ",    
                "09/ربيع الأول/1445 هـ - 15/جمادى الآخرة/1446 هـ",
                "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
                "من 1 رمضان 1400 هـ إلى 10 شوال 1400 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 7 - Gregorian Full Date with Era Marker
            "pattern": date_patterns.cs_dd_mm_yy.gregorian.mixed,
            "name": "date_patterns.cs_dd_mm_yy.gregorian.mixed",
            "description": "Gregorian full date with day/month/year and explicit era marker",
            "examples": [
                "من 15/03/2023 م إلى 01/04/2024 م",
                "15/يناير/2022 م - 10/فبراير/2023 م",
                "27/ديسمبر/2024 م / 01/يناير/2025 م",
                "من 10/مارس/2021 م إلى 25/أبريل/2022 م",
                "25/12/2021 م / 01/01/2022 م",
                "09/فبراير/2023 م - 15/مارس/2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 8 - Hijri Full Date to Hijri Full Date with Parentheses
            "pattern": date_patterns.cs_dd_mm_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.cs_dd_mm_yy.hijri.mixed_parenthetical",
            "description": "Hijri full date range using parentheses for the second date",
            "examples": [
                "من 15/03/1445 هـ (01/04/1446 هـ)",
                "15/محرم/1440 هـ - (10/صفر/1445 هـ)",
                "27/رمضان/1445 هـ / (01/شوال/1446 هـ)",
                "من 10/ذو الحجة/1444 هـ إلى (25/محرم/1445 هـ)",
                "25/12/1443 هـ / (01/01/1445 هـ)",    
                "09/ربيع الأول/1445 هـ - (15/جمادى الآخرة/1446 هـ)",
                "من 15 محرم 1445 هـ (20 صفر 1445 هـ)",
                "من 1 رمضان 1400 هـ (10 شوال 1400 هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 9 - Gregorian Full Date to Gregorian Full Date with Parentheses
            "pattern": date_patterns.cs_dd_mm_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.cs_dd_mm_yy.gregorian.mixed_parenthetical",
            "description": "Gregorian full date range using parentheses for the second date",
            "examples": [
                "من 15/03/2023 م (01/04/2024 م)",
                "15/يناير/2022 م - (10/فبراير/2023 م)",
                "27/ديسمبر/2024 م / (01/يناير/2025 م)",
                "من 10/مارس/2021 م إلى (25/أبريل/2022 م)",
                "25/12/2021 م / (01/01/2022 م)",
                "09/فبراير/2023 م - (15/مارس/2024 م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 10 - Hijri full date + Gregorian full date
            "pattern": date_patterns.cs_dd_mm_yy.hijri.alternative,
            "name": "date_patterns.cs_dd_mm_yy.hijri.alternative",
            "description": "Complete Hijri date followed by Gregorian equivalent",
            "examples": [
                "15/03/1445 هـ / 15/03/2023 م",
                "١٥ محرم ١٤٤٥ هـ - ١٥ مارس ٢٠٢٣ م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {  # Pattern 11 - Gregorian full date + Hijri full date
            "pattern": date_patterns.cs_dd_mm_yy.gregorian.alternative,
            "name": "date_patterns.cs_dd_mm_yy.gregorian.alternative",
            "description": "Complete Gregorian date followed by Hijri equivalent",
            "examples": [
                "15/03/2023 م / 15/03/1445 هـ",
                "١٥ مارس ٢٠٢٣ م - ١٥ محرم ١٤٤٥ هـ",
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
        {   # Pattern 13 - Natural Language Hijri followed by Gregorian
            "pattern": rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}?\s*{date_patterns.cs_dd_mm_yy.hijri.alternative}",
            "name": "single_alternative_hijri_gregorian_full_dates_single_weekday", 
            "description": "Matches a Hijri date in natural Arabic followed by a Gregorian date",
            "examples": [  
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
        },
        {   # Pattern 14 - Natural Language Gregorian followed by Hijri
            "pattern": rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}?\s*{date_patterns.cs_dd_mm_yy.gregorian.alternative}",
            "name": "single_alternative_gregorian_hijri_full_dates_single_weekday",
            "description": "Matches a Gregorian date in natural Arabic followed by a Hijri date",
            "examples": [  
                "الجمعة 15 يناير 2023 م / 15 محرم 1445 هـ",
                "الخميس 1 فبراير 2024 م / 20 رجب 1445 هـ",
                "الأحد 30 ديسمبر 2022 م / 6 جمادى الثانية 1444 هـ",
                "الأربعاء 15/03/2023 م / 15/03/1445 هـ",
                "الثلاثاء 01/01/2024 م / 19/06/1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 16 - 
            "pattern": date_patterns.cs_dd_mm_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.cs_dd_mm_yy.hijri.alternative_parenthetical",
            "description": "Complete Hijri date followed by Gregorian equivalent in parentheses",
            "examples": [
                "15/03/1445 هـ (15/03/2023 م)",
                "١٥ محرم ١٤٤٥ هـ - (١٥ مارس ٢٠٢٣ م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 15 - 
            "pattern": date_patterns.cs_dd_mm_yy.gregorian.alternative_parenthetical,
            "name": "date_patterns.cs_dd_mm_yy.gregorian.alternative_parenthetical",
            "description": "Complete Gregorian date followed by Hijri equivalent in parentheses",
            "examples": [
                "15/03/2023 م (15/03/1445 هـ)",
                "١٥ مارس ٢٠٢٣ م - (١٥ محرم ١٤٤٥ هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },  
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            
        },
        # ===================================================================================
        # 6. DATE RANGE PATTERNS (Hijri to Hijri, Gregorian to Gregorian)
        # ===================================================================================
        {  # Pattern 54 - Hijri-to-Hijri date range with weekday
            "pattern": date_patterns.cs_natural_language.hijri.mixed,
            "name": "date_patterns.cs_natural_language.hijri.mixed",
            "description": "Matches a date range from one Hijri date to another, both possibly with weekdays",
            "examples": [  
                "من الأحد - 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
                "من الجمعة 10 صفر 1445 هـ إلى الثلاثاء 20 صفر 1445 هـ",
                "من الأحد - 15 محرم 1445 هـ إلى الاثنين 20 صفر 1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 55 - Gregorian-to-Gregorian date range with weekday
            "pattern": date_patterns.cs_natural_language.gregorian.mixed,
            "name": "date_patterns.cs_natural_language.gregorian.mixed",
            "description": "Matches Gregorian date ranges with weekday context",
            "examples": [ 
                "من الجمعة 01 مارس 2023 م إلى الاثنين 10 أبريل 2023 م",
                "من الأحد - 10 يناير 2024 م إلى الاثنين 20 ديسمبر 2024 م",
                "من الجمعة 01 مارس 2023 م إلى الأحد 19 نوفمبر 2023 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 55 -  
            "pattern": date_patterns.cs_natural_language.hijri.mixed_parenthetical,
            "name": "date_patterns.cs_natural_language.hijri.mixed_parenthetical",
            "description": "Matches a date range from one Hijri date to another, both possibly with weekdays, using parentheses for the second date",
            "examples": [
                "من الأحد - 15 محرم 1445 هـ (20 صفر 1445 هـ)",
                "من الجمعة 10 صفر 1445 هـ (20 صفر 1445 هـ)",
                "من الأحد - 15 محرم 1445 هـ (الاثنين 20 صفر 1445 هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 55 -  
            "pattern": date_patterns.cs_natural_language.gregorian.mixed_parenthetical,
            "name": "date_patterns.cs_natural_language.gregorian.mixed_parenthetical",
            "description": "Matches Gregorian date ranges with weekday context, using parentheses for the second date",
            "examples": [
                "من الجمعة 01 مارس 2023 م (الاثنين 10 أبريل 2023 م)",
                "من الأحد - 10 يناير 2024 م (الاثنين 20 ديسمبر 2024 م)",
                "من الجمعة 01 مارس 2023 م (الأحد 19 نوفمبر 2023 م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 56 - Hijri date in natural Arabic followed by Gregorian date
            "pattern": date_patterns.cs_natural_language.hijri.alternative,
            "name": "date_patterns.cs_natural_language.hijri.alternative",
            "description": "Matches a Hijri date in natural Arabic followed by a Gregorian date",
            "examples": [
                "الجمعة 15 محرم 1445 هـ إلى الجمعة 15 يناير 2023 م",
                "الأحد 1 صفر 1444 هـ إلى الأحد 1 فبراير 2024 م",
                "الاثنين 30 رجب 1444 هـ إلى الاثنين 30 ديسمبر 2022 م",
                "الأربعاء 15/03/1445 هـ إلى الأربعاء 15/03/2023 م",
                "الثلاثاء 01/01/1445 هـ إلى الثلاثاء 01/01/2024 م"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 57 - Gregorian date in natural Arabic followed by Hijri date
            "pattern": date_patterns.cs_natural_language.gregorian.alternative,
            "name": "date_patterns.cs_natural_language.gregorian.alternative",
            "description": "Matches a Gregorian date in natural Arabic followed by a Hijri date",
            "examples": [
                "الجمعة 15 يناير 2023 م إلى الجمعة 15 محرم 1445 هـ",
                "الأحد 1 فبراير 2024 م إلى الجمعة 20 رجب 1445 هـ",
                "الاثنين 30 ديسمبر 2022 م إلى الاثنين 6 جمادى الثانية 1444 هـ",
                "الأربعاء 15/03/2023 م إلى الاثنين 15/03/1445 هـ",
                "الثلاثاء 01/01/2024 م إلى الثلاثاء 19/06/1445 هـ"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 6 - Hijri/Hijri Combined with Parentheses (Hijri First)
            "pattern": date_patterns.cs_natural_language.hijri.alternative_parenthetical,
            "name": "date_patterns.cs_natural_language.hijri.alternative_parenthetical",
            "description": "Hijri date followed by Gregorian date in parentheses (parallel calendar style)",
            "examples": [
                "الجمعة 15 محرم 1445 هـ (15 يناير 2023 م)",
                "الأحد 1 صفر 1444 هـ - (1 فبراير 2024 م)",
                "الاثنين 30 رجب 1444 هـ (30 ديسمبر 2022 م)",
                "الأربعاء 15/03/1445 هـ (15/03/2023 م)",
                "الثلاثاء 01/01/1445 هـ (01/01/2024 م)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            # Pattern 7 - Gregorian/Hijri Combined with Parentheses (Gregorian First)
            "pattern": date_patterns.cs_natural_language.gregorian.alternative_parenthetical,
            "name": "date_patterns.cs_natural_language.gregorian.alternative_parenthetical",
            "description": "Gregorian date followed by Hijri date in parentheses (parallel calendar style)",
            "examples": [
                "الجمعة 15 يناير 2023 م (15 محرم 1445 هـ)",
                "الأحد 1 فبراير 2024 م - (20 رجب 1445 هـ)",
                "الاثنين 30 ديسمبر 2022 م (6 جمادى الثانية 1444 هـ)",
                "الأربعاء 15/03/2023 م (15/03/1445 هـ)",
                "الثلاثاء 01/01/2024 م (19/06/1445 هـ)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
    ]
}

# ==================================================================================================================================
# 
# ==================================================================================================================================
complex_date_patterns_dict = {
    "metadata": {
        "priority": 6,  
        "match_type": "complex_date_patterns",
    },
    "patterns": [
        {
            "pattern": date_patterns.dual_yy.hijri.mixed,
            "name": "date_patterns.dual_yy.hijri.mixed",
            "description": "Matches a range from Hijri year to Hijri year",
            "examples": [
                "من 1440 هـ إلى 1441 هـ - 1446 هـ - 1447 هـ",
                "من 1442 هـ إلى 1444 هـ - 1445 هـ - 1446 هـ",
                "من 1440 هـ إلى 1445 هـ - 1446 هـ - 1447 هـ",
                "من ١٤٤٠ هـ إلى ١٤٤١ هـ - ١٤٤٦ هـ - ١٤٤٧ هـ",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed,
            "name": "date_patterns.dual_yy.gregorian.mixed",
            "description": "Matches a range from Gregorian year to Gregorian year",
            "examples": [
                "من 2020 م إلى 2021 م - 2024 م - 2025 م",
                "من 2022 م إلى 2024 م - 2025 م - 2026 م",
                "من 2020 م إلى 2025 م - 2026 م - 2027 م",
                "من ٢٠٢٠ م إلى ٢٠٢١ م - ٢٠٢٤ م - ٢٠٢٥ م",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.dual_yy.hijri.mixed_parenthetical",
            "description": "Matches a range from Hijri year to Hijri year with parentheses for the second year",
            "examples": [
                "من 1440 هـ إلى 1441 هـ - (1446 هـ - 1447 هـ)",
                "من 1442 هـ إلى 1444 هـ - (1445 هـ - 1446 هـ)",
                "من 1440 هـ إلى 1445 هـ - (1446 هـ - 1447 هـ)",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.mixed_parenthetical",
            "description": "",
            "examples": [
                "from 2023 CE to 2024 CE - (2025 CE - 2026 CE)",
                "from 2020 CE to 2022 CE - (2023 CE - 2024 CE)",
                "2024 م - 2025 م - (2026 م - 2027 م)",
                "2023 م - 2024 م - (2025 م - 2026 م)",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.mixed_double_parenthetical,
            "name": "date_patterns.dual_yy.hijri.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "من (1440 هـ إلى 1441 هـ) - (1446 هـ - 1447 هـ)",
                "من (1442 هـ إلى 1444 هـ) - (1445 هـ - 1446 هـ)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed_double_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "from (2023 CE to 2024 CE) - (2025 CE - 2026 CE)",
                "from (2020 CE to 2022 CE) - (2023 CE - 2024 CE)",
                "(2024 م - 2025 م) - (2026 م - 2027 م)",
                "(2023 م - 2024 م) - (2025 م - 2026 م)",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.mixed_alternative,
            "name": "date_patterns.dual_yy.hijri.mixed_alternative",
            "description": "",
            "examples": [
                "من 1445 هـ إلى 1446 هـ - ٢٠٢٤ مـ - ٢٠٢٥ م",
                "من 1440 هـ إلى 1445 هـ - ٢٠٢٣ م - ٢٠٢٤ م",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed_alternative,
            "name": "date_patterns.dual_yy.gregorian.mixed_alternative",
            "description": "",
            "examples": [
                "2023 م - 2024 م - 1445 هـ - 1446 هـ",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_yy.hijri.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "من 1445 هـ إلى 1446 هـ - (٢٠٢٤ مـ - ٢٠٢٥ م)",
                "من 1440 هـ إلى 1445 هـ - (٢٠٢٣ م - ٢٠٢٤ م)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "2023 م - 2024 م - (1445 هـ - 1446 هـ)",
                "2020 م - 2022 م - (1440 هـ - 1445 هـ)",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_yy.hijri.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "من (1445 هـ إلى 1446 هـ) - (٢٠٢٤ مـ - ٢٠٢٥ م)",
                "من (1440 هـ إلى 1445 هـ) - (٢٠٢٣ م - ٢٠٢٤ م)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(2023 م - 2024 م) - (1445 هـ - 1446 هـ)",
                "(2020 م - 2022 م) - (1440 هـ - 1445 هـ)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.alternative,
            "name": "date_patterns.dual_yy.hijri.alternative",
            "description": "",
            "examples": [
                "١٤٤٥ هـ - ٢٠٢٤ مـ - 1446 هـ - ٢٠٢٤ م",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.alternative,
            "name": "date_patterns.dual_yy.gregorian.alternative",
            "description": "",
            "examples": [
                "2023 م - 1445 هـ - 2024 م - 1446 هـ",
                "2020 م - 1440 هـ - 2022 م - 1445 هـ",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.dual_yy.hijri.alternative_parenthetical",
            "description": "",
            "examples": [
                "١٤٤٥ هـ - ٢٠٢٤ مـ - (1446 هـ - ٢٠٢٤ م)",
                "١٤٤٠ هـ - ٢٠٢٣ م - (1445 هـ - ٢٠٢٤ م)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.alternative_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.alternative_parenthetical",
            "description": "",
            "examples": [
                "2023 م - 1445 هـ - (2024 م - 1446 هـ)",
                "2020 م - 1440 هـ - (2022 م - 1445 هـ)",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.hijri.alternative_double_parenthetical,
            "name": "date_patterns.dual_yy.hijri.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(١٤٤٥ هـ - ٢٠٢٤ مـ) - (1446 هـ - ٢٠٢٤ م)",
                "(١٤٤٠ هـ - ٢٠٢٣ م) - (1445 هـ - ٢٠٢٤ م)",
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_yy.gregorian.alternative_double_parenthetical,
            "name": "date_patterns.dual_yy.gregorian.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(2023 م - 1445 هـ) - (2024 م - 1446 هـ)",
                "(2020 م - 1440 هـ) - (2022 م - 1445 هـ)",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed,
            "name": "date_patterns.dual_mm_yy.hijri.mixed",
            "description": "",
            "examples": [
                "من محرم 1440 هـ إلى صفر 1441 هـ - رجب 1446 هـ - شعبان 1447 هـ", 
                "From Muharram 1440 AH to Safar 1441 AH - Rajab 1446 AH - Sha'ban 1447 AH",
                "من رمضان 1442 هـ إلى شوال 1444 هـ - ذو القعدة 1445 هـ - ذو الحجة 1446 هـ", 
                "From Ramadan 1442 AH to Shawwal 1444 AH - Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH",
                "من ربيع الأول 1440 هـ إلى ربيع الآخر 1445 هـ - جمادى الأولى 1446 هـ - جمادى الآخرة 1447 هـ", 
                "From Rabi' al-Awwal 1440 AH to Rabi' al-Akhir 1445 AH - Jumada al-Ula 1446 AH - Jumada al-Akhirah 1447 AH"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed",
            "description": "",
            "examples": [
                "from January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE", 
                "From January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE"
                "from March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE", 
                "From March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE"
                "يناير 2024 م - فبراير 2025 م - مارس 2026 م - أبريل 2027 م", 
                "January 2024 CE - February 2025 CE - March 2026 CE - April 2027 CE"
                "مايو 2023 م - يونيو 2024 م - يوليو 2025 م - أغسطس 2026 م", 
                "May 2023 CE - June 2024 CE - July 2025 CE - August 2026 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.mixed_parenthetical",
            "description": "",
            "examples": [
                "من محرم 1440 هـ إلى صفر 1441 هـ - (رجب 1446 هـ - شعبان 1447 هـ)", 
                "From Muharram 1440 AH to Safar 1441 AH - (Rajab 1446 AH - Sha'ban 1447 AH)",
                "من رمضان 1442 هـ إلى شوال 1444 هـ - (ذو القعدة 1445 هـ - ذو الحجة 1446 هـ)", 
                "From Ramadan 1442 AH to Shawwal 1444 AH - (Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH)",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed_parenthetical",
            "description": "",
            "examples": [
                "from January 2023 CE to February 2024 CE - (March 2025 CE - April 2026 CE)", 
                "From January 2023 CE to February 2024 CE - (March 2025 CE - April 2026 CE)",
                "from March 2020 CE to April 2022 CE - (May 2023 CE - June 2024 CE)", 
                "From March 2020 CE to April 2022 CE - (May 2023 CE - June 2024 CE)",
                "يناير 2024 م - فبراير 2025 م - (مارس 2026 م - أبريل 2027 م)", 
                "January 2024 CE - February 2025 CE - (March 2026 CE - April 2027 CE)",
                "مايو 2023 م - يونيو 2024 م - (يوليو 2025 م - أغسطس 2026 م)", 
                "May 2023 CE - June 2024 CE - (July 2025 CE - August 2026 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "من (محرم 1440 هـ إلى صفر 1441 هـ) - (رجب 1446 هـ - شعبان 1447 هـ)", 
                "From (Muharram 1440 AH to Safar 1441 AH) - (Rajab 1446 AH - Sha'ban 1447 AH)",
                "من (رمضان 1442 هـ إلى شوال 1444 هـ) - (ذو القعدة 1445 هـ - ذو الحجة 1446 هـ)", 
                "From (Ramadan 1442 AH to Shawwal 1444 AH) - (Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "from (January 2023 CE to February 2024 CE) - (March 2025 CE - April 2026 CE)", 
                "From (January 2023 CE to February 2024 CE) - (March 2025 CE - April 2026 CE)",
                "from (March 2020 CE to April 2022 CE) - (May 2023 CE - June 2024 CE)", 
                "From (March 2020 CE to April 2022 CE) - (May 2023 CE - June 2024 CE)"
                "(يناير 2024 م - فبراير 2025 م) - (مارس 2026 م - أبريل 2027 م)", 
                "(January 2024 CE - February 2025 CE) - (March 2026 CE - April 2027 CE)",
                "(مايو 2023 م - يونيو 2024 م) - (يوليو 2025 م - أغسطس 2026 م)",
                "(May 2023 CE - June 2024 CE) - (July 2025 CE - August 2026 CE)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed_alternative,
            "name": "date_patterns.dual_mm_yy.hijri.mixed_alternative",
            "description": "",
            "examples": [
                "من رمضان 1445 هـ إلى شوال 1446 هـ - مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م", 
                "From Ramadan 1445 AH to Shawwal 1446 AH - March 2024 CE - April 2025 CE",
                "من محرم 1440 هـ إلى صفر 1445 هـ - يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م", 
                "From Muharram 1440 AH to Safar 1445 AH - January 2023 CE - February 2024 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed_alternative,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed_alternative",
            "description": "",
            "examples": [
                "يناير 2023 م - فبراير 2024 م - محرم 1445 هـ - صفر 1446 هـ", 
                "January 2023 CE - February 2024 CE - Muharram 1445 AH - Safar 1446 AH",
                "مارس 2020 م - أبريل 2022 م - رجب 1440 هـ - شعبان 1445 هـ", 
                "March 2020 CE - April 2022 CE - Rajab 1440 AH - Sha'ban 1445 AH"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "من رمضان 1445 هـ إلى شوال 1446 هـ - (مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م)", 
                "From Ramadan 1445 AH to Shawwal 1446 AH - (March 2024 CE - April 2025 CE)",
                "من محرم 1440 هـ إلى صفر 1445 هـ - (يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م)", 
                "From Muharram 1440 AH to Safar 1445 AH - (January 2023 CE - February 2024 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "يناير 2023 م - فبراير 2024 م - (محرم 1445 هـ - صفر 1446 هـ)", 
                "January 2023 CE - February 2024 CE - (Muharram 1445 AH - Safar 1446 AH)",
                "مارس 2020 م - أبريل 2022 م - (رجب 1440 هـ - شعبان 1445 هـ)", 
                "March 2020 CE - April 2022 CE - (Rajab 1440 AH - Sha'ban 1445 AH)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "من (رمضان 1445 هـ إلى شوال 1446 هـ) - (مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م)", 
                "From (Ramadan 1445 AH to Shawwal 1446 AH) - (March 2024 CE - April 2025 CE)",
                "من (محرم 1440 هـ إلى صفر 1445 هـ) - (يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م)", 
                "From (Muharram 1440 AH to Safar 1445 AH) - (January 2023 CE - February 2024 CE)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(يناير 2023 م - فبراير 2024 م) - (محرم 1445 هـ - صفر 1446 هـ)", 
                "(January 2023 CE - February 2024 CE) - (Muharram 1445 AH - Safar 1446 AH)",
                "(مارس 2020 م - أبريل 2022 م) - (رجب 1440 هـ - شعبان 1445 هـ)", 
                "(March 2020 CE - April 2022 CE) - (Rajab 1440 AH - Sha'ban 1445 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.alternative,
            "name": "date_patterns.dual_mm_yy.hijri.alternative",
            "description": "",
            "examples": [
                "رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م - شوال 1446 هـ - أبريل ٢٠٢٤ م", 
                "Ramadan 1445 AH - March 2024 CE - Shawwal 1446 AH - April 2024 CE"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.alternative,
            "name": "date_patterns.dual_mm_yy.gregorian.alternative",
            "description": "",
            "examples": [
                "يناير 2023 م - محرم 1445 هـ - فبراير 2024 م - صفر 1446 هـ", 
                "January 2023 CE - Muharram 1445 AH - February 2024 CE - Safar 1446 AH",
                "مارس 2020 م - رجب 1440 هـ - أبريل 2022 م - شعبان 1445 هـ", 
                "March 2020 CE - Rajab 1440 AH - April 2022 CE - Sha'ban 1445 AH"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.alternative_parenthetical",
            "description": "",
            "examples": [
                "رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م - (شوال 1446 هـ - أبريل ٢٠٢٤ م)", 
                "Ramadan 1445 AH - March 2024 CE - (Shawwal 1446 AH - April 2024 CE)",
                "محرم ١٤٤٠ هـ - يناير ٢٠٢٣ م - (صفر 1445 هـ - فبراير ٢٠٢٤ م)", 
                "Muharram 1440 AH - January 2023 CE - (Safar 1445 AH - February 2024 CE)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.alternative_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.alternative_parenthetical",
            "description": "",
            "examples": [
                "يناير 2023 م - محرم 1445 هـ - (فبراير 2024 م - صفر 1446 هـ)", 
                "January 2023 CE - Muharram 1445 AH - (February 2024 CE - Safar 1446 AH)",
                "مارس 2020 م - رجب 1440 هـ - (أبريل 2022 م - شعبان 1445 هـ)", 
                "March 2020 CE - Rajab 1440 AH - (April 2022 CE - Sha'ban 1445 AH)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.hijri.alternative_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.hijri.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م) - (شوال 1446 هـ - أبريل ٢٠٢٤ م)", 
                "(Ramadan 1445 AH - March 2024 CE) - (Shawwal 1446 AH - April 2024 CE)",
                "(محرم ١٤٤٠ هـ - يناير ٢٠٢٣ م) - (صفر 1445 هـ - فبراير ٢٠٢٤ م)", 
                "(Muharram 1440 AH - January 2023 CE) - (Safar 1445 AH - February 2024 CE)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.alternative_double_parenthetical,
            "name": "date_patterns.dual_mm_yy.gregorian.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(يناير 2023 م - محرم 1445 هـ) - (فبراير 2024 م - صفر 1446 هـ)", 
                "(January 2023 CE - Muharram 1445 AH) - (February 2024 CE - Safar 1446 AH)"
                "(مارس 2020 م - رجب 1440 هـ) - (أبريل 2022 م - شعبان 1445 هـ)", 
                "(March 2020 CE - Rajab 1440 AH) - (April 2022 CE - Sha'ban 1445 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.mixed,
            "name": "date_patterns.dual_dd_mm_yy.hijri.mixed",
            "description": "",
            "examples": [
                "من 15/محرم/1440 هـ إلى 10/صفر/1441 هـ - 25/رجب/1446 هـ - 01/شعبان/1447 هـ", 
                "From 15th Muharram 1440 AH to 10th Safar 1441 AH - 25th Rajab 1446 AH - 1st Sha'ban 1447 AH",
                "من 27/رمضان/1442 هـ إلى 15/شوال/1444 هـ - 10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ", 
                "From 27th Ramadan 1442 AH to 15th Shawwal 1444 AH - 10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH",
                "من 09/ربيع الأول/1440 هـ إلى 15/ربيع الآخر/1445 هـ - 20/جمادى الأولى/1446 هـ - 05/جمادى الآخرة/1447 هـ", 
                "From 9th Rabi al-Awwal 1440 AH to 15th Rabi al-Akhir 1445 AH - 20th Jumada al-Ula 1446 AH - 5th Jumada al-Akhirah 1447 AH"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_mm_yy.gregorian.mixed,
            "name": "date_patterns.dual_mm_yy.gregorian.mixed",
            "description": "dual_mm_yy_gregorian",
            "examples": [
                "from January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE", 
                "From January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE",
                "from March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE", 
                "From March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE",
                "يناير 2024 م - فبراير 2025 م - مارس 2026 م - أبريل 2027 م", 
                "January 2024 CE - February 2025 CE - March 2026 CE - April 2027 CE",
                "مايو 2023 م - يونيو 2024 م - يوليو 2025 م - أغسطس 2026 م", 
                "May 2023 CE - June 2024 CE - July 2025 CE - August 2026 CE"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.mixed_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.hijri.mixed_parenthetical",
            "description": "",
            "examples": [
                "من 15/محرم/1440 هـ إلى 10/صفر/1441 هـ - (25/رجب/1446 هـ - 01/شعبان/1447 هـ)", 
                "From 15th Muharram 1440 AH to 10th Safar 1441 AH - (25th Rajab 1446 AH - 1st Sha'ban 1447 AH)",
                "من 27/رمضان/1442 هـ إلى 15/شوال/1444 هـ - (10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ)",
                "From 27th Ramadan 1442 AH to 15th Shawwal 1444 AH - (10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH)",
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.mixed_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.mixed_parenthetical",
            "description": "",
            "examples": [
                "from 15/January/2023 CE to 10/February/2024 CE - (25/March/2025 CE - 01/April/2026 CE)", 
                "From 15th January 2023 CE to 10th February 2024 CE - (25th March 2025 CE - 1st April 2026 CE)",
                "from 20/March/2020 CE to 15/April/2022 CE - (10/May/2023 CE - 25/June/2024 CE)", 
                "From 20th March 2020 CE to 15th April 2022 CE - (10th May 2023 CE - 25th June 2024 CE)",
                "15/يناير/2024 م - 10/فبراير/2025 م - (25/مارس/2026 م - 01/أبريل/2027 م)", 
                "15th January 2024 CE - 10th February 2025 CE - (25th March 2026 CE - 1st April 2027 CE)",
                "22/مايو/2023 م - 08/يونيو/2024 م - (17/يوليو/2025 م - 29/أغسطس/2026 م)", 
                "22nd May 2023 CE - 8th June 2024 CE - (17th July 2025 CE - 29th August 2026 CE)"  
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.mixed_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.hijri.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "من (15/محرم/1440 هـ إلى 10/صفر/1441 هـ) - (25/رجب/1446 هـ - 01/شعبان/1447 هـ)", 
                "From (15th Muharram 1440 AH to 10th Safar 1441 AH) - (25th Rajab 1446 AH - 1st Sha'ban 1447 AH)",
                "من (27/رمضان/1442 هـ إلى 15/شوال/1444 هـ) - (10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ)", 
                "From (27th Ramadan 1442 AH to 15th Shawwal 1444 AH) - (10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.mixed_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "from (15/January/2023 CE to 10/February/2024 CE) - (25/March/2025 CE - 01/April/2026 CE)", 
                "From (15th January 2023 CE to 10th February 2024 CE) - (25th March 2025 CE - 1st April 2026 CE)",
                "from (20/March/2020 CE to 15/April/2022 CE) - (10/May/2023 CE - 25/June/2024 CE)", 
                "From (20th March 2020 CE to 15th April 2022 CE) - (10th May 2023 CE - 25th June 2024 CE)",
                "(15/يناير/2024 م - 10/فبراير/2025 م) - (25/مارس/2026 م - 01/أبريل/2027 م)", 
                "(15th January 2024 CE - 10th February 2025 CE) - (25th March 2026 CE - 1st April 2027 CE)",
                "(22/مايو/2023 م - 08/يونيو/2024 م) - (17/يوليو/2025 م - 29/أغسطس/2026 م)", 
                "(22nd May 2023 CE - 8th June 2024 CE) - (17th July 2025 CE - 29th August 2026 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.mixed_alternative,
            "name": "date_patterns.dual_dd_mm_yy.hijri.mixed_alternative",
            "description": "",
            "examples": [
                "من 27/رمضان/1445 هـ إلى 01/شوال/1446 هـ - 15/مارس/٢٠٢٤ م - 10/أبريل/٢٠٢٥ م", 
                "From 27th Ramadan 1445 AH to 1st Shawwal 1446 AH - 15th March 2024 CE - 10th April 2025 CE",
                "من 15/محرم/1440 هـ إلى 10/صفر/1445 هـ - 20/يناير/٢٠٢٣ م - 25/فبراير/٢٠٢٤ م", 
                "From 15th Muharram 1440 AH to 10th Safar 1445 AH - 20th January 2023 CE - 25th February 2024 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "15/يناير/2023 م - 10/فبراير/2024 م - (20/محرم/1445 هـ - 25/صفر/1446 هـ)", 
                "15th January 2023 CE - 10th February 2024 CE - (20th Muharram 1445 AH - 25th Safar 1446 AH)",
                "20/مارس/2020 م - 15/أبريل/2022 م - (27/رجب/1440 هـ - 01/شعبان/1445 هـ)", 
                "20th March 2020 CE - 15th April 2022 CE - (27th Rajab 1440 AH - 1st Sha'ban 1445 AH)",
                "25/December/2023 CE - 31/January/2024 CE - (15/ذو الحجة/1444 هـ - 20/محرم/1445 هـ)", 
                "25th December 2023 CE - 31st January 2024 CE - (15th Dhul Hijjah 1444 AH - 20th Muharram 1445 AH)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.hijri.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "من (27/رمضان/1445 هـ إلى 01/شوال/1446 هـ) - (15/مارس/٢٠٢٤ م - 10/أبريل/٢٠٢٥ م)",
                "From (27th Ramadan 1445 AH to 1st Shawwal 1446 AH) - (15th March 2024 CE - 10th April 2025 CE)",
                "من (15/محرم/1440 هـ إلى 10/صفر/1445 هـ) - (20/يناير/٢٠٢٣ م - 25/فبراير/٢٠٢٤ م)", 
                "From (15th Muharram 1440 AH to 10th Safar 1445 AH) - (20th January 2023 CE - 25th February 2024 CE)"                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(15/يناير/2023 م - 10/فبراير/2024 م) - (20/محرم/1445 هـ - 25/صفر/1446 هـ)", 
                "(15th January 2023 CE - 10th February 2024 CE) - (20th Muharram 1445 AH - 25th Safar 1446 AH)",
                "(20/مارس/2020 م - 15/أبريل/2022 م) - (27/رجب/1440 هـ - 01/شعبان/1445 هـ)", 
                "(20th March 2020 CE - 15th April 2022 CE) - (27th Rajab 1440 AH - 1st Sha'ban 1445 AH)",
                "(25/December/2023 CE - 31/January/2024 CE) - (15/ذو الحجة/1444 هـ - 20/محرم/1445 هـ)", 
                "(25th December 2023 CE - 31st January 2024 CE) - (15th Dhul Hijjah 1444 AH - 20th Muharram 1445 AH)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.alternative,
            "name": "date_patterns.dual_dd_mm_yy.hijri.alternative",
            "description": "",
            "examples": [
                    "27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م - 01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م", 
                    "27th Ramadan 1445 AH - 15th March 2024 CE - 1st Shawwal 1446 AH - 10th April 2024 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.alternative,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.alternative",
            "description": "",
            "examples": [
                "15/يناير/2023 م - 20/محرم/1445 هـ - 10/فبراير/2024 م - 25/صفر/1446 هـ", 
                "15th January 2023 CE - 20th Muharram 1445 AH - 10th February 2024 CE - 25th Safar 1446 AH",
                "20/مارس/2020 م - 27/رجب/1440 هـ - 15/أبريل/2022 م - 01/شعبان/1445 هـ", 
                "20th March 2020 CE - 27th Rajab 1440 AH - 15th April 2022 CE - 1st Sha'ban 1445 AH",
                "25/December/2023 CE - 15/ذو الحجة/1444 هـ - 31/January/2024 CE - 20/محرم/1445 هـ", 
                "25th December 2023 CE - 15th Dhul Hijjah 1444 AH - 31st January 2024 CE - 20th Muharram 1445 AH"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.alternative_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.hijri.alternative_parenthetical",
            "description": "",
            "examples": [
                "27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م - (01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م)", 
                "27th Ramadan 1445 AH - 15th March 2024 CE - (1st Shawwal 1446 AH - 10th April 2024 CE)"
                "15/محرم/١٤٤٠ هـ - 20/يناير/٢٠٢٣ م - (10/صفر/1445 هـ - 25/فبراير/٢٠٢٤ م)", 
                "15th Muharram 1440 AH - 20th January 2023 CE - (10th Safar 1445 AH - 25th February 202"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.alternative_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.alternative_parenthetical",
            "description": "",
            "examples": [
                "15/يناير/2023 م - 20/محرم/1445 هـ - (10/فبراير/2024 م - 25/صفر/1446 هـ)", 
                "15th January 2023 CE - 20th Muharram 1445 AH - (10th February 2024 CE - 25th Safar 1446 AH)",
                "20/مارس/2020 م - 27/رجب/1440 هـ - (15/أبريل/2022 م - 01/شعبان/1445 هـ)", 
                "20th March 2020 CE - 27th Rajab 1440 AH - (15th April 2022 CE - 1st Sha'ban 1445 AH)",
                "25/December/2023 CE - 15/ذو الحجة/1444 هـ - (31/January/2024 CE - 20/محرم/1445 هـ)", 
                "25th December 2023 CE - 15th Dhul Hijjah 1444 AH - (31st January 2024 CE - 20th Muharram 1445 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.hijri.alternative_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.hijri.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م) - (01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م)", 
                "(27th Ramadan 1445 AH - 15th March 2024 CE) - (1st Shawwal 1446 AH - 10th April 2024 CE)",
                "(15/محرم/١٤٤٠ هـ - 20/يناير/٢٠٢٣ م) - (10/صفر/1445 هـ - 25/فبراير/٢٠٢٤ م)", 
                "(15th Muharram 1440 AH - 20th January 2023 CE) - (10th Safar 1445 AH - 25th February 2024 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_dd_mm_yy.gregorian.alternative_double_parenthetical,
            "name": "date_patterns.dual_dd_mm_yy.gregorian.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(15/يناير/2023 م - 20/محرم/1445 هـ) - (10/فبراير/2024 م - 25/صفر/1446 هـ)", 
                "(15th January 2023 CE - 20th Muharram 1445 AH) - (10th February 2024 CE - 25th Safar 1446 AH)",
                "(20/مارس/2020 م - 27/رجب/1440 هـ) - (15/أبريل/2022 م - 01/شعبان/1445 هـ)", 
                "(20th March 2020 CE - 27th Rajab 1440 AH) - (15th April 2022 CE - 1st Sha'ban 1445 AH)",
                "(25/December/2023 CE - 15/ذو الحجة/1444 هـ) - (31/January/2024 CE - 20/محرم/1445 هـ)",
                "(25th December 2023 CE - 15th Dhul Hijjah 1444 AH) - (31st January 2024 CE - 20th Muharram 1445 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed,
            "name": "date_patterns.dual_natural_language.hijri.mixed",
            "description": "",
            "examples": [
                "من الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ - (الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ)", 
                "From Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH - (Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH)",
                "من الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ - (الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ)", 
                "From Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH - (Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed,
            "name": "date_patterns.dual_natural_language.gregorian.mixed",
            "description": "",
            "examples": [
                "from Friday 15 January 2023 CE to Saturday 10 February 2024 CE - Sunday 25 March 2025 CE - Monday 01 April 2026 CE", 
                "From Friday 15th January 2023 CE to Saturday 10th February 2024 CE - Sunday 25th March 2025 CE - Monday 1st April 2026 CE",
                "from Tuesday 20 March 2020 CE to Wednesday 15 April 2022 CE - Thursday 10 May 2023 CE - Friday 25 June 2024 CE", 
                "From Tuesday 20th March 2020 CE to Wednesday 15th April 2022 CE - Thursday 10th May 2023 CE - Friday 25th June 2024 CE",
                "الجمعة 15 يناير 2024 م - السبت 10 فبراير 2025 م - الأحد 25 مارس 2026 م - الاثنين 01 أبريل 2027 م", 
                "Friday 15th January 2024 CE - Saturday 10th February 2025 CE - Sunday 25th March 2026 CE - Monday 1st April 2027 CE",
                "الثلاثاء 22 مايو 2023 م - الأربعاء 08 يونيو 2024 م - الخميس 17 يوليو 2025 م - الجمعة 29 أغسطس 2026 م", 
                "Tuesday 22nd May 2023 CE - Wednesday 8th June 2024 CE - Thursday 17th July 2025 CE - Friday 29th August 2026 CE",
                "من الأحد 10 سبتمبر 2023 م إلى الاثنين 15 أكتوبر 2024 م - الثلاثاء 20 نوفمبر 2025 م - الأربعاء 25 ديسمبر 2026 م", 
                "From Sunday 10th September 2023 CE to Monday 15th October 2024 CE - Tuesday 20th November 2025 CE - Wednesday 25th December 2026 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.mixed_parenthetical",
            "description": "",
            "examples": [
                "من الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ - (الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ)", 
                "From Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH - (Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH)",
                "من الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ - (الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ)",
                "From Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH - (Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.mixed_parenthetical",
            "description": "",
            "examples": [
                "from Friday 15 January 2023 CE to Saturday 10 February 2024 CE - (Sunday 25 March 2025 CE - Monday 01 April 2026 CE)", 
                "From Friday 15th January 2023 CE to Saturday 10th February 2024 CE - (Sunday 25th March 2025 CE - Monday 1st April 2026 CE)",
                "from Tuesday 20 March 2020 CE to Wednesday 15 April 2022 CE - (Thursday 10 May 2023 CE - Friday 25 June 2024 CE)", 
                "From Tuesday 20th March 2020 CE to Wednesday 15th April 2022 CE - (Thursday 10th May 2023 CE - Friday 25th June 2024 CE)",
                "الجمعة 15 يناير 2024 م - السبت 10 فبراير 2025 م - (الأحد 25 مارس 2026 م - الاثنين 01 أبريل 2027 م)", 
                "Friday 15th January 2024 CE - Saturday 10th February 2025 CE - (Sunday 25th March 2026 CE - Monday 1st April 2027 CE)",
                "الثلاثاء 22 مايو 2023 م - الأربعاء 08 يونيو 2024 م - (الخميس 17 يوليو 2025 م - الجمعة 29 أغسطس 2026 م)", 
                "Tuesday 22nd May 2023 CE - Wednesday 8th June 2024 CE - (Thursday 17th July 2025 CE - Friday 29th August 2026 CE)",
                "من الأحد 10 سبتمبر 2023 م إلى الاثنين 15 أكتوبر 2024 م - (الثلاثاء 20 نوفمبر 2025 م - الأربعاء 25 ديسمبر 2026 م)", 
                "From Sunday 10th September 2023 CE to Monday 15th October 2024 CE - (Tuesday 20th November 2025 CE - Wednesday 25th December 2026 CE)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed_double_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "من (الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ) - (الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ)",
                "From (Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH) - (Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH)",
                "من (الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ) - (الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ)", 
                "From (Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH) - (Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed_double_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.mixed_double_parenthetical",
            "description": "",
            "examples": [
                "from (Friday 15 January 2023 CE to Saturday 10 February 2024 CE) - (Sunday 25 March 2025 CE - Monday 01 April 2026 CE)", 
                "From (Friday 15th January 2023 CE to Saturday 10th February 2024 CE) - (Sunday 25th March 2025 CE - Monday 1st April 2026 CE)",
                "from (Tuesday 20 March 2020 CE to Wednesday 15 April 2022 CE) - (Thursday 10 May 2023 CE - Friday 25 June 2024 CE)", 
                "From (Tuesday 20th March 2020 CE to Wednesday 15th April 2022 CE) - (Thursday 10th May 2023 CE - Friday 25th June 2024 CE)",
                "(الجمعة 15 يناير 2024 م - السبت 10 فبراير 2025 م) - (الأحد 25 مارس 2026 م - الاثنين 01 أبريل 2027 م)", 
                "(Friday 15th January 2024 CE - Saturday 10th February 2025 CE) - (Sunday 25th March 2026 CE - Monday 1st April 2027 CE)",
                "(الثلاثاء 22 مايو 2023 م - الأربعاء 08 يونيو 2024 م) - (الخميس 17 يوليو 2025 م - الجمعة 29 أغسطس 2026 م)", 
                "(Tuesday 22nd May 2023 CE - Wednesday 8th June 2024 CE) - (Thursday 17th July 2025 CE - Friday 29th August 2026 CE)",
                "من (الأحد 10 سبتمبر 2023 م إلى الاثنين 15 أكتوبر 2024 م) - (الثلاثاء 20 نوفمبر 2025 م - الأربعاء 25 ديسمبر 2026 م)", 
                "From (Sunday 10th September 2023 CE to Monday 15th October 2024 CE) - (Tuesday 20th November 2025 CE - Wednesday 25th December 2026 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed_alternative,
            "name": "date_patterns.dual_natural_language.hijri.mixed_alternative",
            "description": "",
            "examples": [
                "من الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ - الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م", 
                "From Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH - Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE",
                "من الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ - السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م", 
                "From Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH - Saturday 20th January 2023 CE - Sunday 25th February 2024 CE"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed_alternative,
            "name": "date_patterns.dual_natural_language.gregorian.mixed_alternative",
            "description": "",
            "examples": [
                "الجمعة 15 يناير 2023 م - السبت 10 فبراير 2024 م - الأحد 20 محرم 1445 هـ - الاثنين 25 صفر 1446 هـ", 
                "Friday 15th January 2023 CE - Saturday 10th February 2024 CE - Sunday 20th Muharram 1445 AH - Monday 25th Safar 1446 AH",
                "الثلاثاء 20 مارس 2020 م - الأربعاء 15 أبريل 2022 م - الخميس 27 رجب 1440 هـ - الجمعة 01 شعبان 1445 هـ", 
                "Tuesday 20th March 2020 CE - Wednesday 15th April 2022 CE - Thursday 27th Rajab 1440 AH - Friday 1st Sha'ban 1445 AH",
                "Saturday 25 December 2023 CE - Sunday 31 January 2024 CE - Monday 15 ذو الحجة 1444 هـ - Tuesday 20 محرم 1445 هـ", 
                "Saturday 25th December 2023 CE - Sunday 31st January 2024 CE - Monday 15th Dhul Hijjah 1444 AH - Tuesday 20th Muharram 1445 AH",
                "من الأحد 10 يوليو 2022 م إلى الاثنين 15 أغسطس 2023 م - الثلاثاء 25 ذو القعدة 1443 هـ - الأربعاء 30 ذو الحجة 1444 هـ", 
                "From Sunday 10th July 2022 CE to Monday 15th August 2023 CE - Tuesday 25th Dhul Qi'dah 1443 AH - Wednesday 30th Dhul Hijjah 1444 AH"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "من الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ - (الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م)", 
                "From Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH - (Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE)",
                "من الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ - (السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م)", 
                "From Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH - (Saturday 20th January 2023 CE - Sunday 25th February 2024 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed_alternative_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.mixed_alternative_parenthetical",
            "description": "",
            "examples": [
                "الجمعة 15 يناير 2023 م - السبت 10 فبراير 2024 م - (الأحد 20 محرم 1445 هـ - الاثنين 25 صفر 1446 هـ)", 
                "Friday 15th January 2023 CE - Saturday 10th February 2024 CE - (Sunday 20th Muharram 1445 AH - Monday 25th Safar 1446 AH)",
                "الثلاثاء 20 مارس 2020 م - الأربعاء 15 أبريل 2022 م - (الخميس 27 رجب 1440 هـ - الجمعة 01 شعبان 1445 هـ)", 
                "Tuesday 20th March 2020 CE - Wednesday 15th April 2022 CE - (Thursday 27th Rajab 1440 AH - Friday 1st Sha'ban 1445 AH)",    
                "Saturday 25 December 2023 CE - Sunday 31 January 2024 CE - (Monday 15 ذو الحجة 1444 هـ - Tuesday 20 محرم 1445 هـ)", 
                "Saturday 25th December 2023 CE - Sunday 31st January 2024 CE - (Monday 15th Dhul Hijjah 1444 AH - Tuesday 20th Muharram 1445 AH)",
                "من الأحد 10 يوليو 2022 م إلى الاثنين 15 أغسطس 2023 م - (الثلاثاء 25 ذو القعدة 1443 هـ - الأربعاء 30 ذو الحجة 1444 هـ)", 
                "From Sunday 10th July 2022 CE to Monday 15th August 2023 CE - (Tuesday 25th Dhul Qi'dah 1443 AH - Wednesday 30th Dhul Hijjah 1444 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "من (الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ) - (الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م)", 
                "From (Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH) - (Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE)",
                "من (الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ) - (السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م)", 
                "From (Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH) - (Saturday 20th January 2023 CE - Sunday 25th February 2024 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.mixed_alternative_double_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.mixed_alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(الجمعة 15 يناير 2023 م - السبت 10 فبراير 2024 م) - (الأحد 20 محرم 1445 هـ - الاثنين 25 صفر 1446 هـ)", 
                "(Friday 15th January 2023 CE - Saturday 10th February 2024 CE) - (Sunday 20th Muharram 1445 AH - Monday 25th Safar 1446 AH)",
                "(الثلاثاء 20 مارس 2020 م - الأربعاء 15 أبريل 2022 م) - (الخميس 27 رجب 1440 هـ - الجمعة 01 شعبان 1445 هـ)", 
                "(Tuesday 20th March 2020 CE - Wednesday 15th April 2022 CE) - (Thursday 27th Rajab 1440 AH - Friday 1st Sha'ban 1445 AH)",
                "(Saturday 25 December 2023 CE - Sunday 31 January 2024 CE) - (Monday 15 ذو الحجة 1444 هـ - Tuesday 20 محرم 1445 هـ)", 
                "(Saturday 25th December 2023 CE - Sunday 31st January 2024 CE) - (Monday 15th Dhul Hijjah 1444 AH - Tuesday 20th Muharram 1445 AH)",
                "من (الأحد 10 يوليو 2022 م إلى الاثنين 15 أغسطس 2023 م) - (الثلاثاء 25 ذو القعدة 1443 هـ - الأربعاء 30 ذو الحجة 1444 هـ)", 
                "From (Sunday 10th July 2022 CE to Monday 15th August 2023 CE) - (Tuesday 25th Dhul Qi'dah 1443 AH - Wednesday 30th Dhul Hijjah 1444 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.alternative,
            "name": "date_patterns.dual_natural_language.hijri.alternative",
            "description": "",
            "examples": [
                "الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م - الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م", 
                "Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE - Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE",                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.alternative,
            "name": "date_patterns.dual_natural_language.gregorian.alternative",
            "description": "",
            "examples": [
                "الجمعة 15 يناير 2023 م - الأحد 20 محرم 1445 هـ - السبت 10 فبراير 2024 م - الاثنين 25 صفر 1446 هـ", 
                "Friday 15th January 2023 CE - Sunday 20th Muharram 1445 AH - Saturday 10th February 2024 CE - Monday 25th Safar 1446 AH",
                "الثلاثاء 20 مارس 2020 م - الخميس 27 رجب 1440 هـ - الأربعاء 15 أبريل 2022 م - الجمعة 01 شعبان 1445 هـ", 
                "Tuesday 20th March 2020 CE - Thursday 27th Rajab 1440 AH - Wednesday 15th April 2022 CE - Friday 1st Sha'ban 1445 AH",
                "Saturday 25 December 2023 CE - Monday 15 ذو الحجة 1444 هـ - Sunday 31 January 2024 CE - Tuesday 20 محرم 1445 هـ", 
                "Saturday 25th December 2023 CE - Monday 15th Dhul Hijjah 1444 AH - Sunday 31st January 2024 CE - Tuesday 20th Muharram 1445 AH",
                "الأحد 10 يوليو 2022 م - الثلاثاء 25 ذو القعدة 1443 هـ - الاثنين 15 أغسطس 2023 م - الأربعاء 30 ذو الحجة 1444 هـ", 
                "Sunday 10th July 2022 CE - Tuesday 25th Dhul Qi'dah 1443 AH - Monday 15th August 2023 CE - Wednesday 30th Dhul Hijjah 1444 AH"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.alternative_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.alternative_parenthetical",
            "description": "",
            "examples": [
                "الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م - (الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م)", 
                "Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE - (Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE)",
                "الخميس 15 محرم ١٤٤٠ هـ - السبت 20 يناير ٢٠٢٣ م - (الجمعة 10 صفر 1445 هـ - الأحد 25 فبراير ٢٠٢٤ م)", 
                "Thursday 15th Muharram 1440 AH - Saturday 20th January 2023 CE - (Friday 10th Safar 1445 AH - Sunday 25th February 2024 CE)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.alternative_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.alternative_parenthetical",
            "description": "",
            "examples": [
                "الجمعة 15 يناير 2023 م - الأحد 20 محرم 1445 هـ - (السبت 10 فبراير 2024 م - الاثنين 25 صفر 1446 هـ)", 
                "Friday 15th January 2023 CE - Sunday 20th Muharram 1445 AH - (Saturday 10th February 2024 CE - Monday 25th Safar 1446 AH)",
                "الثلاثاء 20 مارس 2020 م - الخميس 27 رجب 1440 هـ - (الأربعاء 15 أبريل 2022 م - الجمعة 01 شعبان 1445 هـ)", 
                "Tuesday 20th March 2020 CE - Thursday 27th Rajab 1440 AH - (Wednesday 15th April 2022 CE - Friday 1st Sha'ban 1445 AH)",
                "Saturday 25 December 2023 CE - Monday 15 ذو الحجة 1444 هـ - (Sunday 31 January 2024 CE - Tuesday 20 محرم 1445 هـ)", 
                "Saturday 25th December 2023 CE - Monday 15th Dhul Hijjah 1444 AH - (Sunday 31st January 2024 CE - Tuesday 20th Muharram 1445 AH)",
                "الأحد 10 يوليو 2022 م - الثلاثاء 25 ذو القعدة 1443 هـ - (الاثنين 15 أغسطس 2023 م - الأربعاء 30 ذو الحجة 1444 هـ)", 
                "Sunday 10th July 2022 CE - Tuesday 25th Dhul Qi'dah 1443 AH - (Monday 15th August 2023 CE - Wednesday 30th Dhul Hijjah 1444 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.hijri.alternative_double_parenthetical,
            "name": "date_patterns.dual_natural_language.hijri.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م) - (الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م)", 
                "(Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE) - (Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE)",
                "(الخميس 15 محرم ١٤٤٠ هـ - السبت 20 يناير ٢٠٢٣ م) - (الجمعة 10 صفر 1445 هـ - الأحد 25 فبراير ٢٠٢٤ م)", 
                "(Thursday 15th Muharram 1440 AH - Saturday 20th January 2023 CE) - (Friday 10th Safar 1445 AH - Sunday 25th February 2024 CE)"
                
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {
            "pattern": date_patterns.dual_natural_language.gregorian.alternative_double_parenthetical,
            "name": "date_patterns.dual_natural_language.gregorian.alternative_double_parenthetical",
            "description": "",
            "examples": [
                "(الجمعة 15 يناير 2023 م - الأحد 20 محرم 1445 هـ) - (السبت 10 فبراير 2024 م - الاثنين 25 صفر 1446 هـ)", 
                "(Friday 15th January 2023 CE - Sunday 20th Muharram 1445 AH) - (Saturday 10th February 2024 CE - Monday 25th Safar 1446 AH)",
                "(الثلاثاء 20 مارس 2020 م - الخميس 27 رجب 1440 هـ) - (الأربعاء 15 أبريل 2022 م - الجمعة 01 شعبان 1445 هـ)",
                "(Tuesday 20th March 2020 CE - Thursday 27th Rajab 1440 AH) - (Wednesday 15th April 2022 CE - Friday 1st Sha'ban 1445 AH)",
                "(Saturday 25 December 2023 CE - Monday 15 ذو الحجة 1444 هـ) - (Sunday 31 January 2024 CE - Tuesday 20 محرم 1445 هـ)", 
                "(Saturday 25th December 2023 CE - Monday 15th Dhul Hijjah 1444 AH) - (Sunday 31st January 2024 CE - Tuesday 20th Muharram 1445 AH)",
                "(الأحد 10 يوليو 2022 م - الثلاثاء 25 ذو القعدة 1443 هـ) - (الاثنين 15 أغسطس 2023 م - الأربعاء 30 ذو الحجة 1444 هـ)", 
                "(Sunday 10th July 2022 CE - Tuesday 25th Dhul Qi'dah 1443 AH) - (Monday 15th August 2023 CE - Wednesday 30th Dhul Hijjah 1444 AH)"
            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        }
    ]
}