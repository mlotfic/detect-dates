#!/usr/bin/env python3
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi
@description: This module provides weekday name extraction and normalization utilities.
'''

from detect_dates.keywords.weekdays_keywords import (
    weekdays_variations_list,
    weekdays_standard_keywords,
    weekdays_keywords,
)

from detect_dates.keywords.era_keywords import (
    era_keywords_dict,  # All era keywords for normalization
    era_keywords,  # All era keywords for normalization
)


from detect_dates.keywords.month_keywords import (
    months_standard_keywords,  # Standard month keywords
    months_variations_list,  # Comprehensive month keywords list
    months_keywords,  # All month keywords for normalization
)


from detect_dates.keywords.numeric_words_keywords import (
    numeric_words_keywords,  # All numeric words for normalization
)

from detect_dates.keywords.search_in_keywords import search_in_keywords

from detect_dates.keywords.separators_keywords import indicators_keywords


# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    # Era normalization and keywords
    "era_keywords",  # All era keywords
    "era_keywords_dict",  # Era keywords dictionary for normalization

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
    "sear