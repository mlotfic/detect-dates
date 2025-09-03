# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    def setup_src_path():
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                break
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

import re
# All date patterns
from detect_dates.patterns.classes.date import (
      DatePatterns
    )


def _fetch_composite(date_patterns: DatePatterns):
    composite = {
        "metadata": {
            "priority": 5,
            "match_type": "mixed",
        },
        "patterns": [
            {  # Pattern 0 - Hijri Year Range (start+end)
                "pattern": re.compile(date_patterns.cs_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_mm_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}?\s*{date_patterns.cs_dd_mm_yy.hijri['alternative']}", flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(rf"{date_patterns.weekday}\s*{date_patterns.indicator.separator}?\s*{date_patterns.cs_dd_mm_yy.gregorian['alternative']}", flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_dd_mm_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.cs_natural_language.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
    return composite
