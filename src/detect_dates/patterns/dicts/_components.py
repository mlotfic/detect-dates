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


def _fetch_components(date_patterns: DatePatterns):
    components = {
        "metadata": {
            "priority": 1,
            "match_type": "components",
        },
        "patterns": [
            {  # Pattern 0 - Weekday Component
                "pattern": re.compile(date_patterns.weekday, flags=re.IGNORECASE | re.UNICODE),
                "name": "date_patterns.dd",
                "description": "Day component - requires calendar context for disambiguation",
                "examples": [
                    "الاحد",
                    "الاثنين",
                    "الثلاثاء",
                ],
                "date": {
                    "weekday": 1,
                },
            },
            {  # Pattern 1 - Numeric Day Component (Ambiguous Calendar)
                "pattern": re.compile(rf"{date_patterns.indicator.day}\s*{date_patterns.indicator.separator}?\s*{date_patterns.numeric.day}", flags=re.IGNORECASE | re.UNICODE),
                "name": "day_component",
                "description": "Day component - requires calendar context for disambiguation",
                "examples": [
                    "يوم 01",
                    "يوم 02",
                ],
                "date": {
                    "day": 3,
                },
            },
            {  # Pattern 2 - Numeric Day Component (Ambiguous Calendar)
                "pattern": re.compile(rf"{date_patterns.indicator.month}\s*{date_patterns.indicator.separator}?\s*{date_patterns.numeric.month}", flags=re.IGNORECASE | re.UNICODE),
                "name": "month_component",
                "description": "Day component - ambiguous calendar",
                "examples": [
                    "شهر 01",
                    "شهر 02",
                ],
                "date": {
                    "year": 3
                },
            },
            {  # Pattern 3 - Month Component (Hijri Calendar)
                "pattern": re.compile(date_patterns.mm.hijri, flags=re.IGNORECASE | re.UNICODE),
                "name": "month_component_hijri",
                "description": "Month component - hijri calendar",
                "examples": [
                    "محرم",
                ],
                "date": {
                    "month": 1,
                    "calendar": "hijri"
                },
            },
            {  # Pattern 4 - Month Component (Gregorian Calendar)
                "pattern": re.compile(date_patterns.mm.gregorian, flags=re.IGNORECASE | re.UNICODE),
                "name": "month_component_gregorian",
                "description": "Month component - gregorian calendar",
                "examples": [
                    "January",
                    "فبراير",
                ],
                "date": {
                    "month": 1,
                    "calendar": "gregorian"
                },
            },
            {  # Pattern 5 - Month Component (Jalali Calendar)
                "pattern": re.compile(date_patterns.mm.Jalali, flags=re.IGNORECASE | re.UNICODE),
                "name": "month_component_Jalali",
                "description": "Month component - Jalali calendar",
                "examples": [
                    "فروردین",
                    "اردیبهشت",
                ],
                "date": {
                    "month": 1,
                    "calendar": "Jalali"
                },
            },
            {  # Pattern 6 - Year Component (Ambiguous Calendar)
                "pattern": re.compile(rf"{date_patterns.indicator.year}\s*{date_patterns.indicator.separator}?\s*{date_patterns.numeric.year}", flags=re.IGNORECASE | re.UNICODE),
                "name": "year_component",
                "description": "Year component - ambiguous calendar",
                "examples": [
                    "سنة 2023",
                ],
                "date": {
                    "year": 3
                },
            },
            {  # Pattern 7 - century Component
                "pattern": re.compile(rf"{date_patterns.indicator.century}\s*{date_patterns.indicator.separator}?\s*{date_patterns.numeric.century}", flags=re.IGNORECASE | re.UNICODE),
                "name": "century_component",
                "description": "Century component - ambiguous calendar",
                "examples": [
                    "القرن 21",
                    "القرن 20",
                ],
                "date": {
                    "century": 3
                },
            },
            {  # Pattern 8 - Era Component
                "pattern": re.compile(date_patterns.era.hijri, flags=re.IGNORECASE | re.UNICODE),
                "name": "era_component_hijri",
                "description": "Era component - hijri calendar",
                "examples": [
                    "هجري",      # Hijri era
                    "هجرية",     # Hijri era (feminine)
                ],
                "date": {
                    "era": 1,
                    "calendar": "hijri"
                },
            },
            {  # Pattern 9 - Era Component
                "pattern": re.compile(date_patterns.era.gregorian, flags=re.IGNORECASE | re.UNICODE),
                "name": "era_component",
                "description": "Era component - gregorian calendar",
                "examples": [
                    "ميلادي",     # Gregorian era
                ],
                "date": {
                    "era": 1,
                    "calendar": "gregorian"
                },
            },
            {  # Pattern 10 - Era Component
                "pattern": re.compile(date_patterns.era.Jalali, flags=re.IGNORECASE | re.UNICODE),
                "name": "era_component",
                "description": "Era component - Jalali calendar",
                "examples": [
                    "هجری شمسی",  # Jalali era (Persian)
                    "شمسي",      # Jalali era
                ],
                "date": {
                    "era": 1,
                    "calendar": "Jalali"
                    },
            }
        ]
    }
    
    return components