
'''
Created on Sun Jun 22 21:38:10 2025
@author: m.lotfi
@description: This module provides calendar conversion utilities and functions to get calendar variants.
'''


# Era normalization and keywords
# ===================================================================================
# This module provides functions to normalize era terms in different languages and calendars.
from .era import (
    normalize_era,  # Main era normalization function
    get_calendar, # 
    get_era_info  # Get calendar and language info from era text
)

# Month normalization and keywords
# ===================================================================================
# This module provides functions to normalize month names in different languages and calendars.
from .month import (
    normalize_month,  # Main month normalization function
    get_month_info,  # Get month information for a given month name
)

# Weekday normalization and keywords
# ===================================================================================
# This module provides functions to normalize weekday names in different languages.
from .weekday import (
    normalize_weekday,  # Main weekday normalization function
    get_weekday_info,
)

# Numeric word normalization
# ===================================================================================
# This module provides functions to normalize numeric words in Arabic.
from .numeric_words import (
    numeric_words_pattern_ar,  # Regex pattern for Arabic numeric words
)

from .calendar import (
    normalize_calendar_name,
    get_calendar_info
)

# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    # Era normalization and keywords
    "normalize_era",  # Main era normalization function

    # Month normalization and keywords
    "normalize_month",  # Main month normalization function
    "get_month_info",  # Get month information for a given month name

    # Weekday normalization and keywords
    "normalize_weekday",  # Main weekday normalization function
    "get_weekday_info",  # All weekday keywords

    # Numeric word normalization
    "numeric_words_pattern_ar",  # Regex pattern for Arabic numeric words

    "normalize_calendar_name",
    "get_calendar_info",
    "get_calendar",
    "get_era_info"
    
]