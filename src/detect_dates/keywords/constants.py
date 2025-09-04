# ===================================================================================
# CONSTANTS AND ENUMS
# ===================================================================================
from enum import Enum
from typing import Optional


class Language(Enum):
    ARABIC = "ar"
    ENGLISH = "en"

class Calendar(Enum):
    HIJRI = "hijri"
    GREGORIAN = "gregorian"
    PERSIAN = "persian"
    JULIAN = "julian"

class OutputFormat(Enum):
    NUMBER = "num"
    FULL = "full"
    ABBREVIATED = "abbr"

# Calendar system aliases for user convenience
CALENDAR_ALIASES = {
    'solar_hijri': 'julian',
    'persian': 'julian',
    'islamic': 'hijri',
    'greg': 'gregorian'
}
# Precision levels for date parsing
PRECISION_LEVELS = {
    'exact': 'Complete date with day, month, year',
    'month': 'Month and year only',
    'year': 'Year only',
    'century': 'Century only',
    'partial': 'Some components missing'
}

# Module-level constants
SUPPORTED_CALENDARS_COLUMNS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
}

WEEKDAY_COLUMN = 'Week Day'

SUPPORTED_LANGUAGES = {lang.value for lang in Language}
SUPPORTED_CALENDARS = {cal.value for cal in Calendar}
DEFAULT_LANGUAGE = Language.ARABIC.value
DEFAULT_CALENDAR = ""