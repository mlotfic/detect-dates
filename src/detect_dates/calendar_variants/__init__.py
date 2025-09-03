
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.

'''

# Calendar conversion utilities
# ===================================================================================
# These functions handle the conversion of years between different calendar systems
from .utils.century_utils import (
    get_century_from_year,
    get_century_range,
    format_century_with_era,
)

# Functions for calendar variants
# ===================================================================================
# These functions handle the conversion of dates between different calendar systems
from .date_variants import (
    DateVariants, 
)

# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    "get_century_from_year",
    "get_century_range",
    "format_century_with_era",
    "DateVariants",
]