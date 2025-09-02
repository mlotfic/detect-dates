# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

import re
# All date patterns
from ..classes.date import DatePatterns


def _fetch_simple(date_patterns: DatePatterns):
    simple = {
        "metadata" : {
            "priority": 5,
            "match_type": "base",
        },
        "patterns": [
            
            {  # Pattern 1 - Basic Hijri Year with Era Marker
                "pattern": re.compile(date_patterns.yy.hijri['numeric'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.yy.gregorian['numeric'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.yy.julian['numeric'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.mm_yy.hijri['combined'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.mm_yy.gregorian['combined'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.mm_yy.julian['combined'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dd_mm_yy.hijri['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.dd_mm_yy.hijri.combined",
                "description": "Complete Hijri date with day/month/year and explicit era marker",
                "examples": [
                    "15/03/1445 هـ",      # 15th Rabi al-Awwal 1445 AH
                    "01/محرم/1446 هجري", # 1st Muharram 1446 AH
                    "27/رمضان/1445 هـ",   # 27th Ramadan 1445 AH (Laylat al-Qadr)
                    "10/ذو الحجة/1444 ه", # 10th Dhul Hijjah 1444 AH (Eid al-Adha)
                    "25/12/1443 هجرية",  # 25th Dhul Hijjah 1443 AH
                    "09/ربيع الأول/1445 هـ.", # 9th Rabi al-Awwal 1445 AH
                    "محرم 1 1446 ه"
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
                "pattern": re.compile(date_patterns.dd_mm_yy.gregorian['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.dd_mm_yy.gregorian.combined",
                "description": "Complete Gregorian date with day/month/year and explicit era marker",
                "examples": [
                    "15/03/2023 م",       # 15th March 2023 CE
                    "25/December/2024 CE", # 25th December 2024 CE
                    "01/يناير/2022 ميلادي", # 1st January 2022 CE
                    "14/فبراير/2025 م",   # 14th February 2025 CE
                    "31/12/2021 ميلادية", # 31st December 2021 CE
                    "04/July/2023 AD",     # 4th July 2023 CE
                    "يناير 1 2025 م"
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
                "pattern": re.compile(date_patterns.dd_mm_yy.julian['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.dd_mm_yy.julian.combined",
                "description": "Complete julian date with day/month/year and explicit era marker",
                "examples": [
                    "15/03/1402 هـ.ش",     # 15th Khordad 1402 SH
                    "01/فروردین/1403 شمسی", # 1st Farvardin 1403 SH (Nowruz)
                    "21/مهر/1401 ه.ش",     # 21st Mehr 1401 SH
                    "29/اسفند/1400 شمسى",  # 29th Esfand 1400 SH
                    "10/06/1404 هجری شمسی", # 10th Shahrivar 1404 SH
                    "25/آبان/1399 ش",       # 25th Aban 1399 SH
                    "آبان 1 1399 ش"
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
                "pattern": re.compile(date_patterns.natural_language.hijri['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.natural_language.hijri.combined",
                "description": "Natural language Hijri date with weekday, day, month name, year, and era marker",
                "examples": [
                    "الجمعة 15 محرم 1445 هـ",    # Friday 15th Muharram 1445 AH
                    "الأحد 01 رمضان 1446 هجري", # Sunday 1st Ramadan 1446 AH
                    "الاثنين 27 رجب 1444 هـ",   # Monday 27th Rajab 1444 AH
                    "الثلاثاء 10 ذو الحجة 1445 ه", # Tuesday 10th Dhul Hijjah 1445 AH
                    "السبت 25 شعبان 1443 هجرية", # Saturday 25th Sha'ban 1443 AH
                    "السبت شعبان 25  1443 هجرية", # Saturday 25th Sha'ban 1443 AH
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
                "pattern": re.compile(date_patterns.natural_language.gregorian['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.natural_language.gregorian.combined",
                "description": "Natural language Gregorian date with weekday, day, month name, year, and era marker",
                "examples": [
                    "الجمعة 15 يناير 2023 ميلاديًا",  # Friday 15th January 2023 CE
                    "الأحد 25 ديسمبر 2024 م",        # Sunday 25th December 2024 CE
                    "Monday 04 July 2023 CE",       # Monday 4th July 2023 CE
                    "الثلاثاء 14 فبراير 2025 ميلادي", # Tuesday 14th February 2025 CE
                    "الثلاثاء فبراير 14 2025 ميلادي", # Tuesday 14th February 2025 CE
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
                "pattern": re.compile(date_patterns.natural_language.julian['combined'], flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.natural_language.julian.combined",
                "description": "Natural language julian date with weekday, day, month name, year, and era marker",
                "examples": [
                    "جمعه 15 فروردین 1402 هـ.ش",    # Friday 15th Farvardin 1402 SH
                    "یکشنبه 01 فروردین 1403 شمسی", # Sunday 1st Farvardin 1403 SH (Nowruz)
                    "دوشنبه 21 مهر 1401 ه.ش",      # Monday 21st Mehr 1401 SH
                    "سه‌شنبه 29 اسفند 1400 شمسى",  # Tuesday 29th Esfand 1400 SH
                    "پنج‌شنبه 10 آبان 1404 هجری شمسی", # Thursday 10th Aban 1404 SH
                    "پنج‌شنبه  آبان 10  1404 هجری شمسی", # Thursday 10th Aban 1404 SH
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
    return simple
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            