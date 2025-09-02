#!/usr/bin/env python3
"""
Created on Sun Jun 22 21:38:10 2025

@author: m

@description: This module provides calendar conversion utilities and functions to get calendar variants.
"""

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def h_to_g_yr_cal(h_year: int) -> int:
    """
    Convert Hijri year to Gregorian year.
    Args:
        h_year (int): Hijri year to convert.
        Returns:
        int: Corresponding Gregorian year.
    """
    # Approximate conversion formula
    # The conversion is not exact due to the differences in calendar systems
    return int(h_year * 0.97 + 622)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def g_to_h_yr_cal(g_year: int) -> int:
    """
    Convert Gregorian year to Hijri year.
    Args:
        g_year (int): Gregorian year to convert.
    Returns:
        int: Corresponding Hijri year.
    """
    # Approximate conversion formula
    # The conversion is not exact due to the differences in calendar systems
    return int((g_year - 622) / 0.97)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def s_to_g_yr_cal(s_year: int) -> int:
    """
    Convert julian year to Gregorian year.
    Args:
        s_year (int): julian year to convert.
    Returns:
        int: Corresponding Gregorian year.
    """
    # Approximate conversion formula
    return int(s_year + 621)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def g_to_s_yr_cal(g_year: int) -> int:
    """
    Convert Gregorian year to julian year.
    Args:
        g_year (int): Gregorian year to convert.
    Returns:
        int: Corresponding julian year.
    """
    # Approximate conversion formula
    # The conversion is not exact due to the differences in calendar systems
    # The julian calendar is approximately 621 years behind the Gregorian calendar
    return int(g_year - 621)


# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def s_to_h_yr_cal(s_year: int) -> int:
    """
    Convert julian year to Hijri year.
    Args:
        s_year (int): julian year to convert.
    Returns:
        int: Corresponding Hijri year.
    """
    # Approximate conversion formula
    # The conversion is not exact due to the differences in calendar systems
    # The Hijri calendar is approximately 622 years behind the julian calendar
    return int((s_year - 621) / 0.97 + 622)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def h_to_s_yr_cal(h_year: int) -> int:
    """
    Convert Hijri year to julian year.
    Args:
        h_year (int): Hijri year to convert.
    Returns:
        int: Corresponding julian year.
    """
    # Approximate conversion formula
    # The conversion is not exact due to the differences in calendar systems
    # The julian calendar is approximately 621 years behind the Hijri calendar
    return int((h_year - 622) * 0.97 + 621)