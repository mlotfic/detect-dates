"""
Utility module for Arabic date processing and calendar conversions.
This module provides functions for date normalization, pattern matching,
and calendar system conversions.
"""

# Data cleaning and preparation utilities
from detect_dates.utils.remove_date_duplicates import remove_date_duplicates
from detect_dates.utils.ordinal_suffix import get_ordinal_suffix

__all__ = [
    'remove_date_duplicates',
    'get_ordinal_suffix'
]


