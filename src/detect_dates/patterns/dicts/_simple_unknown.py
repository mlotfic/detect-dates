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
from detect_dates.patterns.classes.date import (
    DatePatterns
    )


def _fetch_simple_unknown(date_patterns: DatePatterns):
    simple_unknown = {
        "metadata" : {
            "priority": 0,
            "match_type": "ambiguity",
        },
        "patterns" : [
            {   # Pattern 0 - Numeric Year (Ambiguous Calendar)
                "pattern": re.compile(date_patterns.yy.numeric, flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.mm_yy.numeric, flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dd_mm_yy.numeric, flags=re.IGNORECASE | re.UNICODE),
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
            {  # Pattern 0 - Day/Month/Year with Weekday Prefix
                "pattern": re.compile(date_patterns.natural_language.numeric, flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.natural_language.numeric",
                "description": "Weekday-prefixed numeric date format - weekday can help validate calendar accuracy",
                "examples": [
                    "الأحد 01/12/1440",        # Sunday 1st Dhul Hijjah 1440 AH
                    "الاثنين 02/01/2023",       # Monday 2nd January 2023 CE
                    "الثلاثاء 15/03/1398",       # Tuesday - needs calendar validation
                    "الأربعاء 25/12/2024",       # Wednesday 25th December 2024 CE
                    "الخميس 10/06/1445",      # Thursday - Hijri date
                    "الجمعة 20/11/1401"        # Friday - could be julian
                ],
                "date": { "weekday": 1, "day": 2,  "month": 3, "year": 4, "century": None, "era": None, "calendar": ""},
            },
        ]
    }
    return simple_unknown
