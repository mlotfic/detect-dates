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


def _fetch_complex(date_patterns: DatePatterns):
    complex = {
        "metadata": {
            "priority": 6,
            "match_type": "complex_date_patterns",
        },
        "patterns": [
            {
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.hijri['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_yy.gregorian['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.hijri['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_mm_yy.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.hijri['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_dd_mm_yy.gregorian['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed_alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed_alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['mixed_alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['alternative'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['alternative_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.hijri['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
                "pattern": re.compile(date_patterns.dual_natural_language.gregorian['alternative_double_parenthetical'], flags=re.IGNORECASE | re.UNICODE),
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
    return complex
