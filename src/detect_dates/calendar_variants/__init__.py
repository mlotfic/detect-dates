#!/usr/bin/env python3
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.

'''

# Calendar conversion utilities
# ===================================================================================
# These functions handle the conversion of years between different calendar systems
from detect_dates.calendar_variants.calender_yr_to_yr_cal import (
    h_to_g_yr_cal,  # Convert Hijri year to Gregorian year
    g_to_h_yr_cal,  # Convert Gregorian year to Hijri year
    s_to_g_yr_cal,  # Convert julian year to Gregorian year
    g_to_s_yr_cal,  # Convert Gregorian year to julian year
    h_to_s_yr_cal,  # Convert Hijri year to julian year
    s_to_h_yr_cal,  # Convert julian year to Hijri year    
)

# Functions for calendar variants
# ===================================================================================
# These functions handle the conversion of dates between different calendar systems
from detect_dates.calendar_variants.get_calendar_variants import (
    get_calendar_variants,  # Convert dates between calendar systems
    get_calendar_variants_by_lang,  # Language-specific calendar conversion
)

# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    
    # Calendar conversion utilities
    "h_to_g_yr_cal",  # Convert Hijri year to Gregorian year
    "g_to_h_yr_cal",  # Convert Gregorian year to Hijri year
    "s_to_g_yr_cal",  # Convert julian year to Gregorian year
    "g_to_s_yr_cal",  # Convert Gregorian year to julian year
    "h_to_s_yr_cal",  # Convert Hijri year to julian year
    "s_to_h_yr_cal",  # Convert julian year to Hijri year 
    
    # Functions for calendar variants
    "get_calendar_variants",
    "get_calendar_variants_by_