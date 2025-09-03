
# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("INFO: Run Main File : adding file parent src to path ...")
    from path_helper import add_modules_to_sys_path
    add_modules_to_sys_path()

from modules.regex_patterns import get_date_patterns
from modules.patterns import DatePatterns

try:
    # Demonstrate with Arabic language patterns
    print("\n1. Loading Arabic language patterns...")
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
    print("\n2. Exploring pattern hierarchy...")
    all_patterns = date_patterns.get_all_patterns()

    for complexity, patterns in all_patterns.items():
        print(f"   {complexity.capitalize()} level: {len(patterns)} pattern types")

    # Demonstrate specific pattern access
    print("\n3. Accessing specific patterns...")
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
numeric_patterns_dict = {
    "metadata" : {
        "priority": 0,
        "match_type": "ambiguity",
    },
    "patterns" : [
        {   # Pattern 0 - Numeric Year (Ambiguous Calendar)
            "pattern": date_patterns.yy.numeric,
            "name": "numeric",
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
            "name": "numeric_numeric",
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
            "date": "date": { "weekday": None, "day": None, "month": 1, "year": 2, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 1 - Day/Month/Year Numeric (Ambiguous Calendar)
            "pattern": date_patterns.dd_mm_yy.numeric,
            "name": "numeric_full_date",
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
            "pattern": rf"{date_patterns.dd}",
            "name": "Weekday_component",
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
            "pattern": rf"{date_patterns.mm.hijri}",
            "name": "month_component_hijri",
            "description": "Month component - hijri calendar",
            "examples": [
                "محرم",
            ],
            "date": { "weekday": None, "day": None, "month": 1, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 3 - Month Component (Gregorian Calendar)
            "pattern": rf"{date_patterns.mm.gregorian}",
            "name": "month_component_gregorian",
            "description": "Month component - gregorian calendar",
            "examples": [
                "January",
                "فبراير",
            ],
            "date": { "weekday": None, "day": None, "month": 1, "year": None, "century": None, "era": None, "calendar": "" },
        },
        {  # Pattern 4 - Month Component (julian Calendar)
            "pattern": rf"{date_patterns.mm.julian}",
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
            "pattern": rf"{date_patterns.era.hijri}",
            "name": "era_component_hijri",
            "description": "Era component - hijri calendar",
            "examples": [
                "هجري",      # Hijri era
                "هجرية",     # Hijri era (feminine)
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": 1, "calendar": "" },
        },
        {  # Pattern 4 - Era Component
            "pattern": rf"{date_patterns.era.gregorian}",
            "name": "era_component",
            "description": "Era component - gregorian calendar",
            "examples": [
                "ميلادي",     # Gregorian era
            ],
            "date": { "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": 1, "calendar": "" },
        },
        {  # Pattern 4 - Era Component
            "pattern": rf"{date_patterns.era.julian}",
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
            "name": "weekday_dd_mm_yy",
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
            "name": "yy_hijri",
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
            "name": "yy_gregorian",
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
            "name": "yy_julian",
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
            "name": "mm_yy_hijri",
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
            "name": "mm_yy_gregorian",
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
            "name": "mm_yy_julian",
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
            "name": "dd_mm_yy_hijri",
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
            "name": "dd_mm_yy_gregorian",
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
            "name": "dd_mm_yy_julian",
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
            "name": "natural_language_hijri",
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
            "name": "natural_language_gregorian",
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
            "name": "natural_language_julian",
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

# MIXED SLASHED DATE PATTERNS
# ===================================================================================
date_mixed_slash_date_patterns = {
    "metadata": {
        "priority": 5,
        "match_type": "mixed_slash",
    },
    "patterns": [
        {  # Pattern 0 - Hijri Year Range (start+end)
            "pattern": date_patterns.cs_yy.hijri.mixed,
            "name": "single_mixed_yy_hijri",
            "description": "Hijri year to Hijri year range using 'من ... إلى ...' format",
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
            "name": "single_mixed_yy_gregorian",
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
        {  # Pattern 4 - Hijri/Gregorian Combined (Hijri First)
            "pattern": date_patterns.cs_yy.hijri.alternative,
            "name": "single_alternative_hijri_gregorian_years",
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
            "name": "single_alternative_gregorian_hijri_years",
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

        # ===================================================================================
        # 7. MONTH-YEAR PATTERNS (RANGES & MIXED CALENDARS)
        # ===================================================================================
        {  # Pattern 6 - Hijri Month-Year to Hijri Month-Year
            "pattern": date_patterns.cs_mm_yy.hijri.mixed,
            "name": "single_mixed_mm_yy_hijri",
            "description": "Matches Hijri month/year range using Arabic connectors like 'من ... إلى ...'",
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
            "name": "single_mixed_mm_yy_gregorian",
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
        {  # Pattern 7 - Hijri + Gregorian M/Y combo (Hijri first)
            "pattern": date_patterns.cs_mm_yy.hijri.alternative,
            "name": "single_alternative_hijri_gregorian_month_years",
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
            "name": "single_alternative_gregorian_hijri_month_years",
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
        # ===================================================================================
        # 5. FULL DATE PATTERNS (day/month/year)
        # ===================================================================================
        {  # Pattern 6 - Hijri Month-Year to Hijri Month-Year
            "pattern": date_patterns.cs_dd_mm_yy.hijri.mixed,
            "name": "single_mixed_dd_mm_yy_hijri",
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
            "name": "single_mixed_dd_mm_yy_gregorian",
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
        {  # Pattern 10 - Hijri full date + Gregorian full date
            "pattern": date_patterns.cs_dd_mm_yy.hijri.alternative,
            "name": "single_alternative_hijri_gregorian_full_dates",
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
            "name": "single_alternative_gregorian_hijri_full_dates",
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
        # ===================================================================================
        # 6. DATE RANGE PATTERNS (Hijri to Hijri, Gregorian to Gregorian)
        # ===================================================================================
        {  # Pattern 54 - Hijri-to-Hijri date range with weekday
            "pattern": date_patterns.cs_natural_language.hijri.mixed,
            "name": "single_mixed_cs_natural_language_hijri",
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
            "name": "single_mixed_cs_natural_language_gregorian",
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
        {   # Pattern 56 - Hijri date in natural Arabic followed by Gregorian date
            "pattern": date_patterns.cs_natural_language.hijri.alternative,
            "name": "single_alternative_hijri_gregorian_natural_language",
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
            "name": "single_alternative_gregorian_hijri_natural_language",
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
    ]
}


# ===================================================================================
# MIXED PARENTHETICAL DATE PATTERNS (TO BE REFACTORED)
# ===================================================================================
date_mixed_slash_date_patterns_parenthetical = {
    "metadata": {
        "priority": 6,
        "match_type": "mixed_parenthetical",
    },
    "patterns": [
    {   # Pattern 0 - Hijri Year to Hijri Year (with parentheses)
        "pattern": date_patterns.cs_yy.hijri.mixed_parenthetical,
        "name": "single_mixed_yy_hijri_parenthetical",
        "description": "Matches a range from Hijri year to Hijri year enclosed in parentheses or brackets",
        "examples": [
            "من 1440 هـ (1445 هـ)",
            "1442 هـ [1446 هـ]",
            "١٤٤٠ هـ (١٤٤٥ هـ)",
            "1440 هـ (1445 هـ)",
            "١٤٤٢ هـ [١٤٤٥ هـ]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 3 - Hijri year followed by Gregorian year
        "pattern": date_patterns.cs_yy.hijri.alternative_parenthetical,
        "name": "single_alternative_hijri_gregorian_years_parenthetical",
        "description": "Matches Hijri year followed by Gregorian year inside parentheses/brackets",
        "examples": [
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
    },
    {   # Pattern 1 - Gregorian Year to Gregorian Year (with parentheses)
        "pattern": date_patterns.cs_yy.gregorian.mixed_parenthetical,
        "name": "single_mixed_yy_gregorian_parenthetical",
        "description": "Matches a range from Gregorian year to Gregorian year enclosed in parentheses or brackets",
        "examples": [
            "من 2020 م (2024 م)",
            "2020 م [2024 م]",
            "٢٠٢٠ م (٢٠٢٤ م)",
            "2020 م (2024 م)",
            "٢٠٢٠ م [٢٠٢٤ م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 5 - Gregorian year followed by Hijri year
        "pattern": date_patterns.cs_yy.gregorian.alternative_parenthetical,
        "name": "single_alternative_gregorian_hijri_years_parenthetical",
        "description": "Matches Gregorian year followed by Hijri year inside parentheses/brackets",
        "examples": [
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
    },
    # ===================================================================================
    # 6. MONTH-YEAR PATTERNS (RANGES & MIXED CALENDARS)
    # ===================================================================================
    {  # Pattern 21 - Hijri month/year to Hijri month/year range (with parentheses)
        "pattern": date_patterns.cs_mm_yy.hijri.mixed_parenthetical,
        "name": "single_mixed_mm_yy_hijri_parenthetical",
        "description": "Matches a Hijri month/year range enclosed in parentheses or brackets",
        "examples": [
            "من محرم 1440 هـ (صفر 1445 هـ)",
            "جمادى الأولى 1441 هـ [رمضان 1442 هـ]",
            "شوال 1443 هـ - (ذو القعدة 1444 هـ)",
            "ربيع الآخر 1445 هـ (جمادى الآخرة 1446 هـ)",
            "شعبان ١٤٤٠ هـ - (رمضان ١٤٤٢ هـ)",
            "من رجب 1440 هـ إلى شعبان 1441 هـ",
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
    {  # Pattern 7 - Hijri + Gregorian month/year combination
        "pattern": date_patterns.cs_mm_yy.hijri.alternative_parenthetical,
        "name": "single_alternative_hijri_gregorian_month_years_parenthetical",
        "description": "Hijri month/year followed by Gregorian month/year inside parentheses or brackets",
        "examples": [
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
    },
    {  # Pattern 22 - Gregorian month/year to Gregorian month/year (with parentheses)
        "pattern": date_patterns.cs_mm_yy.gregorian.mixed_parenthetical,
        "name": "single_mixed_mm_yy_gregorian_parenthetical",
        "description": "Matches a Gregorian month/year range enclosed in parentheses or brackets",
        "examples": [
            "من يناير 2020 م (ديسمبر 2024 م)",
            "مارس 2021 م [أكتوبر 2023 م]",
            "فبراير 2022 م - (نوفمبر 2024 م)",
            "يونيو 2023 م (سبتمبر 2024 م)",
            "يناير 2020 م - (ديسمبر 2024 م)",
            "مارس ٢٠٢٠ م - (يونيو ٢٠٢٣ م)",
            "يناير 2020 م (ديسمبر 2024 م)",
            "مارس 2021 م [أكتوبر 2023 م]"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {   # Pattern 8 - Gregorian + Hijri month/year combination
        "pattern": date_patterns.cs_mm_yy.gregorian.alternative_parenthetical,
        "name": "single_alternative_gregorian_hijri_month_years_parenthetical",
        "description": "Gregorian month/year followed by Hijri month/year inside parentheses or brackets",
        "examples": [
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
    },

    # ===================================================================================
    # 5. FULL DATE PATTERNS (day/month/year) — e.g., "15 محرم 1445 هـ"
    # ===================================================================================
    {  # Pattern 10 - Full Hijri/Gregorian Date (Hijri first)
        "pattern": date_patterns.cs_dd_mm_yy.hijri.mixed_parenthetical,
        "name": "single_alternative_hijri_gregorian_full_dates_parenthetical",
        "description": "Matches a full Hijri date followed by Gregorian equivalent in brackets or parentheses",
        "examples": [
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
    },
    {  # Pattern 11 - Full Gregorian/Hijri Date (Gregorian first)
        "pattern": date_patterns.cs_dd_mm_yy.gregorian.mixed_parenthetical,
        "name": "single_alternative_gregorian_hijri_full_dates_parenthetical",
        "description": "Matches a full Gregorian date followed by equivalent Hijri date in brackets or parentheses",
        "examples": [
            "15 مارس 2023 م (15 محرم 1445 هـ)",
            "25/04/2023 م [05/10/1444 هـ]",
            "01/01/2020 م (06 جمادى الأولى 1441 هـ)"
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # 13 — Natural language Hijri date with Gregorian
        "pattern": rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}\s*{date_patterns.cs_dd_mm_yy.hijri.alternative}",
        "name": "single_alternative_hijri_gregorian_full_dates_single_weekday",
        "description": "Natural Hijri date with Gregorian reference",
        "examples": [
            "الجمعة 15 محرم 1445 هـ (15 مارس 2023 م)",
            "الاثنين 01 صفر 1444 هـ (01 فبراير 2024 م)",
            "الأحد 30 رجب 1444 هـ (30 ديسمبر 2022 م)",
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
    {   # 14 — Natural Gregorian with Hijri
        "pattern": rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}\s*{date_patterns.cs_dd_mm_yy.gregorian.alternative}",
        "name": "single_alternative_gregorian_hijri_full_dates_single_weekday",
        "description": "Natural Gregorian date with Hijri reference",
        "examples": [
            "الجمعة 15 يناير 2023 م (15 محرم 1445 هـ)"
            "الاثنين 01 يناير 2024 م (19 رجب 1445 هـ)",
            "الأحد 30 ديسمبر 2022 م (6 جمادى الثانية 1444 هـ)",
            "الأربعاء 15/03/2023 م (15/03/1445 هـ)",],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    # ===================================================================================
    # 6. NATURAL LANGUAGE DATE PATTERNS (Hijri and Gregorian)
    # ===================================================================================
    {  # 12 — Natural language Hijri date with Gregorian}
        "pattern": date_patterns.cs_natural_language.hijri.mixed_parenthetical,
        "name": "single_alternative_hijri_full_dates_single_weekday_parenthetical",
        "description": "Natural Hijri date with Gregorian reference in parentheses or brackets",
        "examples": [
            "الجمعة 15 محرم 1445 هـ (الجمعة 15 محرم 1445 هـ)",
            "الاثنين 01 صفر 1444 هـ (الاثنين 01 صفر 1444 هـ)",
            "الأحد 30 رجب 1444 هـ (الأحد 30 رجب 1444 هـ)",
            "الأربعاء 15/03/1445 هـ (الأربعاء 15/03/1445 هـ)",
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        }
    },
    {   # 13 — Natural language Gregorian date with Hijri
        "pattern": date_patterns.cs_natural_language.gregorian.mixed_parenthetical,
        "name": "single_alternative_gregorian_full_dates_single_weekday_parenthetical",
        "description": "Natural Gregorian date with Hijri reference in parentheses or brackets",
        "examples": [
            "الجمعة 15 يناير 2023 م (الجمعة 15 يناير 2023 م)",
            "الاثنين 01 فبراير 2024 م (الاثنين 01 فبراير 2024 م)",
            "الأحد 30 ديسمبر 2022 م (الأحد 30 ديسمبر 2022 م)",
            "الأربعاء 15/03/2023 م (الأربعاء 15/03/2023 م)",
        ],
        "date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        }
    },
]
}

# ===================================================================================
# DUAL PARENTHETICAL DATE PATTERNS (Hijri and Gregorian)
# ===================================================================================
dual_date_patterns = {
    "metadata": {
        "priority": 6,
        "match_type": "dual_parenthetical",
    },
    "patterns": [
        {   # Pattern 9 - Hijri year range with surrounding parentheses and Gregorian shadow
            "pattern": date_patterns.dual_yy.hijri.mixed,
            "name": "dual_hijri_yy",
            "description": "Hijri year range (from-to) in brackets, with Gregorian equivalent in next bracket",
            "examples": [
                "1440 / هـ إلى 1446 ه -  من 1445 هـ إلى 1441 هـ",

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 6 - Hijri range only, no suffix, with Gregorian range next (non-suffixed)
            "pattern": date_patterns.dual_yy.hijri.alternative,
            "name": "range_hijri_raw_with_gregorian",
            "description": "Hijri year range in brackets (without suffix), followed by raw Gregorian range",
            "examples": [
                "1440 / هـ إلى 1446 ه -  من 1445 هـ إلى 1441 هـ",

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 10 - Gregorian year range with surrounding parentheses and Hijri shadow
            "pattern": date_patterns.dual_yy.hijri.alternative_parenthetical,
            "name": "range_gregorian_parenthetical_with_hijri",
            "description": "Gregorian year range (from-to) in brackets, with Hijri equivalent in next bracket",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },

        {   # Pattern 7 - Gregorian range without suffix, followed by Hijri range without suffix
            "pattern": rf'(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_raw_with_hijri",
            "description": "Gregorian year range (raw) in brackets followed by Hijri year range",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },

        },
        {   # Pattern 3 - Single Hijri+Gregorian pair in brackets
            "pattern": rf'(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern}\s*(?:[\)\]])',
            "name": "bracketed_hijri_gregorian_double",
            "description": "Double pair of Hijri-Gregorian year combinations in brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 5 - Single Gregorian+Hijri pair in brackets
            "pattern": rf'(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern}\s*(?:[\)\]])',
            "name": "bracketed_gregorian_hijri_double",
            "description": "Double pair of Gregorian-Hijri year combinations in brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        # 7. MONTH-YEAR PATTERNS
        {   # Pattern 21 - Hijri to Hijri range with Gregorian reference
            "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_hijri_m_y_with_gregorian_reference",
            "description": "Matches a range from Hijri month/year to Hijri month/year with trailing Gregorian reference",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 22 - Gregorian to Gregorian range with Hijri reference
            "pattern": rf'(?:[\(\[])\s*{gregorian_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_m_y_with_hijri_reference",
            "description": "Matches a range from Gregorian month/year to Gregorian month/year with trailing Hijri reference",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 18 - Hijri to Hijri range with Gregorian in same brackets (compact)
            "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
            "name": "compact_hijri_m_y_range_with_gregorian",
            "description": "Compact form of Hijri range followed by Gregorian equivalent, all in brackets",
            "examples": [

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
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 7 - Mixed Hijri/Gregorian Month-Year Format
            "pattern": rf'(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_m_y_pattern}\s*(?:[\)\]])',
            "name": "alternating_hijri_gregorian_m_y_pairs",
            "description": "Matches alternating Hijri/Gregorian month-year pairs with brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 8 - Gregorian/Hijri Cross Match Bracketed
            "pattern": rf'(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_m_y_pattern}\s*(?:[\)\]])',
            "name": "alternating_gregorian_hijri_m_y_pairs",
            "description": "Matches alternating Gregorian/Hijri month-year pairs",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 10 - Hijri/Gregorian Pair in (Hijri/Gregorian) (Hijri/Gregorian) Format
            "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "paired_hijri_gregorian_full_dates",
            "description": "Matches paired full Hijri and Gregorian dates wrapped in brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 11 - Gregorian/Hijri Pair in (Gregorian/Hijri) (Gregorian/Hijri) Format
            "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "paired_gregorian_hijri_full_dates",
            "description": "Matches paired full Gregorian and Hijri dates wrapped in brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        # 6. NATURAL LANGUAGE DATE PATTERNS
        {   # Pattern 13 - Natural Hijri-Gregorian Pair in Brackets with Day Name
            "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
            "name": "natural_language_hijri_gregorian_pair",
            "description": "Matches natural language Hijri and Gregorian dates with day name, inside brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 14 - Natural Gregorian-Hijri Pair in Brackets with Day Name
            "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
            "name": "natural_language_gregorian_hijri_pair",
            "description": "Matches natural language Gregorian and Hijri dates with day name, inside brackets",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        # 5. FULL DATE PATTERNS (day/month/year)  "15 محرم 1445",##
        {   # Pattern 42 - Hijri to Hijri range with symbolic and full pattern
            "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_hijri_to_hijri_symbolic",
            "description": "Matches a Hijri to Hijri range with symbolic suffixes (e.g., هـ)",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 43 - Gregorian to Gregorian range with symbolic suffixes
            "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern_s}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_to_gregorian_symbolic",
            "description": "Matches a Gregorian to Gregorian date range with symbolic suffixes (e.g., م)",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 30 - Duplicate of Pattern 42 (Consider deprecating)
            "pattern": rf'(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_hijri_to_hijri_basic",
            "description": "Hijri-Hijri range without symbolic suffixes",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 40 - Duplicate of Pattern 43 (Consider merging)
            "pattern": rf'(?:[\(\[])\s*{gregorian_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{gregorian_d_m_y_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{hijri_d_m_y_pattern}\s*{IndicatorPatterns.separator}?\s*{hijri_d_m_y_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_to_gregorian_basic",
            "description": "Gregorian date range without suffixes",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 54 - Hijri range with weekdays
            "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
            "name": "range_hijri_to_hijri_weekday",
            "description": "Matches Hijri range with weekday labels",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 55 - Gregorian range with weekdays
            "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern_s}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_to_gregorian_weekday",
            "description": "Gregorian range including weekday names",
            "examples": [
                ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        # 1. HIGHEST PRIORITY - COMPLEX RANGE PATTERNS (week_day - DD/MM/YYYY)
        {   # Pattern 51 - Hijri range with natural weekday format
            "pattern": rf'(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])',
            "name": "range_hijri_natural_weekday",
            "description": "Hijri-Hijri range using natural weekday pattern",
            "examples": [

            ],
            "date": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
            "date_end": {
                "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
            },
        },
        {   # Pattern 52 - Gregorian range with natural weekday
            "pattern": rf'(?:[\(\[])\s*{natural_gregorian_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_gregorian_pattern}\s*(?:[\)\]])\s*(?:[\(\[])\s*{natural_hijri_pattern}\s*{IndicatorPatterns.separator}?\s*{natural_hijri_pattern}\s*(?:[\)\]])',
            "name": "range_gregorian_natural_weekday",
            "description": "Gregorian-Gregorian range using weekday and full date",
            "examples": [

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

# ===================================================================================
# RANGE-BASED FULL CALENDAR MAPPINGS (TO BE REFACTORED)
# ===================================================================================
#match_type": "range",
FULL_DATE_RANGE_PATTERNS = [
    {  # Pattern 1 - Hijri Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_y_pattern}\b',
        "name": "range_hijri_year_to_year",
        "description": "Matches a range from Hijri year to Hijri year with Arabic range indicators",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 2 - Gregorian Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_y_pattern}\b',
        "name": "range_gregorian_year_to_year",
        "description": "Matches a range from Gregorian year to Gregorian year using Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 3 - julian Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+({julian_y_pattern})\s+{IndicatorPatterns.range_connector}\s+{julian_y_pattern}\b',
        "name": "range_julian_year_to_year",
        "description": "Matches a range from julian year to julian year using Arabic/Persian connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },

    },
    {  # Pattern 4 - Hijri Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_y_pattern}\b',
        "name": "range_hijri_year_alt_suffixed",
        "description": "Matches an alternate Hijri year range where start year has a suffix pattern",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 5 - Gregorian Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_y_pattern}\b',
        "name": "range_gregorian_year_alt_suffixed",
        "description": "Matches an alternate Gregorian year range where start year has a suffix",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 6 - julian Year Range (alt pattern with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+({julian_y_pattern_s})\s+{IndicatorPatterns.range_connector}\s+{julian_y_pattern}\b',
        "name": "range_julian_year_alt_suffixed",
        "description": "Matches an alternate julian year range where start year has a suffix",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 7 - Hijri Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_m_y_pattern}\b',
        "name": "range_hijri_month_year_to_month_year",
        "description": "Matches a range from Hijri month/year to Hijri month/year with Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": 1, "year": 2, "century": None, "era": 3, "calendar": "hijri"
        },
        "date_end": {
            "weekday": None, "day": None, "month": 4, "year": 5, "century": None, "era": 6, "calendar": "hijri"
        }
    },
    {  # Pattern 8 - Gregorian Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_m_y_pattern}\b',
        "name": "range_gregorian_month_year_to_month_year",
        "description": "Matches a range from Gregorian month/year to Gregorian month/year with Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 9 - julian Month-Year Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{julian_m_y_pattern}\b',
        "name": "range_julian_month_year_to_month_year",
        "description": "Matches a range from julian month/year to julian month/year with Arabic or Persian connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 10 - Hijri Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_m_y_pattern}\b',
        "name": "range_hijri_month_year_alt_suffixed",
        "description": "Alternate Hijri month/year range: start with suffix, end without",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 11 - Gregorian Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_m_y_pattern}\b',
        "name": "range_gregorian_month_year_alt_suffixed",
        "description": "Alternate Gregorian month/year range: start has suffix",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 12 - julian Month-Year Range (alt suffix on start)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{julian_m_y_pattern}\b',
        "name": "range_julian_month_year_alt_suffixed",
        "description": "Alternate julian month/year range: start suffixed, end plain",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 13 - Hijri Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{hijri_d_m_y_pattern}\b',
        "name": "range_hijri_day_month_year_to_day_month_year",
        "description": "Matches a range from Hijri full date to Hijri full date with Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 14 - Gregorian Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{gregorian_d_m_y_pattern}\b',
        "name": "range_gregorian_day_month_year_to_day_month_year",
        "description": "Matches a range from Gregorian full date to Gregorian full date with Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 15 - julian Full Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_d_m_y_pattern}\s+{IndicatorPatterns.range_connector}\s+{julian_d_m_y_pattern}\b',
        "name": "range_julian_day_month_year_to_day_month_year",
        "description": "Matches a range from julian full date to julian full date with Arabic or Persian connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 16 - Hijri Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{hijri_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{hijri_d_m_y_pattern}\b',
        "name": "range_hijri_day_month_year_alt_suffixed",
        "description": "Alternate Hijri full date range: suffix on first date only",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 17 - Gregorian Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{gregorian_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{gregorian_d_m_y_pattern}\b',
        "name": "range_gregorian_day_month_year_alt_suffixed",
        "description": "Alternate Gregorian full date range: suffix on start date only",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 18 - julian Full Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{julian_d_m_y_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{julian_d_m_y_pattern}\b',
        "name": "range_julian_day_month_year_alt_suffixed",
        "description": "Alternate julian full date range: suffix on start date only",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },

    {  # Pattern 20 - Hijri Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_hijri_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_hijri_pattern}\b',
        "name": "range_hijri_weekday_day_month_year",
        "description": "Matches a range from Hijri date (with weekday) to Hijri date using Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 21 - Gregorian Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_gregorian_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_gregorian_pattern}\b',
        "name": "range_gregorian_weekday_day_month_year",
        "description": "Matches a range from Gregorian date (with weekday) to Gregorian date using Arabic connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 22 - julian Weekday-Date Range
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_julian_pattern}\s+{IndicatorPatterns.range_connector}\s+{natural_julian_pattern}\b',
        "name": "range_julian_weekday_day_month_year",
        "description": "Matches a range from julian date (with weekday) to julian date using Arabic or Persian connectors",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 23 - Hijri Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_hijri_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_hijri_pattern}\b',
        "name": "range_hijri_weekday_day_month_year_alt_suffixed",
        "description": "Alternate Hijri date range: suffix on first date only (with weekday)",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {  # Pattern 24 - Gregorian Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_gregorian_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_gregorian_pattern}\b',
        "name": "range_gregorian_weekday_day_month_year_alt_suffixed",
        "description": "Alternate Gregorian date range: suffix on start date only (with weekday)",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
    {   # Pattern 25 - julian Weekday-Date Range (start with suffix)
        "pattern": rf'\b{IndicatorPatterns.range_starter}?\s+{natural_julian_pattern_s}\s+{IndicatorPatterns.range_connector}\s+{natural_julian_pattern}\b',
        "name": "range_julian_weekday_day_month_year_alt_suffixed",
        "description": "Alternate julian date range: suffix on first date only (with weekday)",
        "examples": [

        ],"date": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None, "century": None, "era": None, "calendar" : None
        },
    },
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               