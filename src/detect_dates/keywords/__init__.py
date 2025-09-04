
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi
@description: This module provides weekday name extraction and normalization utilities.
'''


from .constants import (
    Language,
    Calendar,
    OutputFormat,
    PRECISION_LEVELS,
    CALENDAR_ALIASES,
    SUPPORTED_LANGUAGES,
    SUPPORTED_CALENDARS,
    SUPPORTED_CALENDARS_COLUMNS,
    WEEKDAY_COLUMN,
    DEFAULT_LANGUAGE,
    DEFAULT_CALENDAR,
)

from .weekday import (
    weekdays_variations_list,
    weekdays_standard_keywords,
    weekdays_keywords,
)

from .era import (
    era_standard_keywords,  # All era keywords for normalization
    era_keywords,  # All era keywords for normalization
)


from .month import (
    months_standard_keywords,  # Standard month keywords
    months_variations_list,  # Comprehensive month keywords list
    months_keywords,  # All month keywords for normalization
)


from .numeric_words import (
    numeric_words_keywords,  # All numeric words for normalization
)

from .search import search_in_keywords

from .separator import indicators_keywords


# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    # Era normalization and keywords
    "era_keywords",  # All era keywords
    "era_standard_keywords",  # Era keywords dictionary for normalization

    # Month normalization and keywords
    "months_standard_keywords",  # Standard month keywords
    "months_variations_list",  # Comprehensive month keywords list
    "months_keywords",  # All month keywords

    # Weekday normalization and keywords
    "weekdays_variations_list",  # All weekday variations
    "weekdays_standard_keywords",  # Normalized weekday names
    "weekdays_keywords",  # All weekday keywords

    # Date indicators and separators
    "indicators_keywords",  # Date component indicators

    # Numeric word normalization
    "numeric_words_keywords",  # numeric words
    "search_in_keywords",      # search-in keywords
    
    # Constants
    "Language",
    "Calendar",
    "OutputFormat",
    "CALENDAR_ALIASES",
    "PRECISION_LEVELS",
    "SUPPORTED_LANGUAGES",
    "SUPPORTED_CALENDARS",
    "DEFAULT_LANGUAGE",
    "DEFAULT_CALENDAR",
    "SUPPORTED_CALENDARS_COLUMNS",
    "WEEKDAY_COLUMN",

]