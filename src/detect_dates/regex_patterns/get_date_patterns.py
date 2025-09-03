
"""
Created on Thu Jul 24 20:01:16 2025

@author: m
"""

import re
from dataclasses import dataclass
from typing import Pattern, Optional, Tuple

from .keywords_to_regex import keywords_to_regex

from .get_pattern import (
    get_era_pattern,
    get_month_pattern,
    get_day_pattern,
    get_century_pattern,
    get_day_indicator_pattern,
    get_month_indicator_pattern,
    get_year_indicator_pattern,
    get_separator_pattern,
    get_range_connector_pattern,
    get_range_starter_pattern,
    get_numeric_words_pattern,
)

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

from detect_dates.keywords import (
    era_keywords, 
    months_keywords, 
    indicators_keywords, 
    weekdays_keywords, 
    numeric_words_keywords
)

from detect_dates.patterns.classes import (
    BasePatterns,
    MonthPatterns,
    EraPatterns,
    IndicatorPatterns,
    NumericPatterns,
)

# ===============================
# Pattern Builder – Dynamic by language
# ===============================
def get_date_patterns(lang: str) -> Tuple[BasePatterns, MonthPatterns, EraPatterns, IndicatorPatterns, NumericPatterns]:
    """    Generate date patterns based on the specified language.
    Args:
        lang (str): Language code (e.g., 'ar', 'en', etc.)
    Returns:
        DatePatterns: A dataclass containing all regex patterns for date components.

    Examples:
        >>> patterns = get_date_patterns('ar')
        >>> patterns.weekday
        'السبت|الأحد|الإثنين|الثلاثاء|الأربعاء|الخميس|الجمعة'
        >>> patterns.hijri_month
        'محرم|صفر|ربيع الأول|ربيع الآخر|جمادى الأولى|جمادى الآخرة|رجب|شعبان|رمضان|شوال|ذو القعدة|ذو الحجة'

    """
    # Return all as compiled regex pattern strings
    return BasePatterns(
            weekday         =   get_day_pattern(weekdays_keywords, lang),
            numeric_words   =   get_numeric_words_pattern(numeric_words_keywords, lang)

        ), MonthPatterns(
            hijri           = get_month_pattern(months_keywords, lang, calendar="Hijri"),
            gregorian       = get_month_pattern(months_keywords, lang, calendar="Gregorian"),
            julian          = get_month_pattern(months_keywords, f"persian_{lang}", calendar="julian")

        ), EraPatterns(
            hijri           = get_era_pattern(era_keywords, lang, calendar="Hijri"),
            gregorian       = get_era_pattern(era_keywords, lang, calendar="Gregorian"),
            julian          = get_era_pattern(era_keywords, f"persian_{lang}", calendar="julian")

        ), IndicatorPatterns(
            day             = get_day_indicator_pattern(indicators_keywords, lang),
            month           = get_month_indicator_pattern(indicators_keywords, lang),
            year            = get_year_indicator_pattern(indicators_keywords, lang),
            century         = get_century_pattern(indicators_keywords, lang),
            separator       = get_separator_pattern(indicators_keywords, lang),
            range_connector = get_range_connector_pattern(indicators_keywords, lang),
            range_starter   = get_range_starter_pattern(indicators_keywords, lang)
        ), NumericPatterns(
            year            = r"(\d{1,4})",
            month           = r"(\d{1,2})",
            day             = r"(\d{1,2})",
            century         = r"(\d{1,2})"
        )

    '''
    # DatePatterns Dataclass – Holds all regex components
# ==============================================================
# This dataclass encapsulates all regex patterns for date components, making it easy to manage and
@dataclass
class DatePatterns:
    day_indicator_pattern: str
    month_indicator_pattern: str
    year_indicator_pattern: str
    century_indicator_pattern: str
    separator_pattern: str
    range_connector_pattern: str
    range_starter_pattern: str


    hijri_era_pattern: str
    gregorian_era_pattern: str
    julian_era_pattern: str
    day_pattern: str
    hijri_month_pattern: str
    gregorian_month_pattern: str
    julian_month_pattern: str


    return DatePatterns(
        day_indicator_pattern       = rf"(?:{day_indicator})",
        month_indicator_pattern     = rf"(?:{month_indicator})",
        year_indicator_pattern      = rf"(?:{year_indicator})",
        century_indicator_pattern   = rf"(?:{century_indicator})",
        separator_pattern           = rf"(?:{separator})",
        range_connector_pattern     = rf"(?:{range_connector})",
        range_starter_pattern       = rf"(?:{range_starter})",

        hijri_era_pattern           = rf"({hijri_era})",
        gregorian_era_pattern       = rf"({gregorian_era})",
        julian_era_pattern          = rf"({julian_era})",
        day_pattern                 = rf"({day})",
        hijri_month_pattern         = rf"({hijri_month})",
        gregorian_month_pattern     = rf"({gregorian_month})",
        julian_month_pattern        = rf"({julian_month})",
    )
    '''
