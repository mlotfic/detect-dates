#!/usr/bin/env python3
"""
Created on Sun Jun 22 21:38:10 2025

@author: m

description: This module provides calendar conversion utilities and functions to get calendar variants.
"""
from typing import Tuple

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

from detect_dates.calendar_variants import get_ordinal_suffix

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_century_from_year(year:int)-> Tuple[int, str]:
    """
    Calculate century from year. Same calculation for all calendars, only formatting differs.
    
    Args:
        year (str/int): The year value
    
    Returns:
        tuple: (century_number, formatted_string) or (None, None) if year is invalid
        
    Note:
        - Century is calculated as (year - 1) // 100 + 1
        - Returns None for invalid input (e.g., negative years, zero, non-integers)
        - Uses get_ordinal_suffix to format century (1st, 2nd, 3rd, etc.)
    
    Examples:
        1 → (1, "1st"), 2 → (1, "1st"), 100 → (1, "1st")
        101 → (2, "2nd"), 200 → (2, "2nd"), 201 → (3, "3rd")
        300 → (3, "3rd"), 1000 → (10, "10th"), 2025 → (21, "21st")
        
    """
    # Bail early if we got nothing
    if year is None:
        return None, None
    
    try:
        # Convert to integer, handling string input - strip whitespace just in case
        year_int = int(str(year).strip())
    except (ValueError, AttributeError):
        # Invalid input - can't convert to int
        return None, None
    
    # No negative years or year zero in our world
    if year_int <= 0:
        return None, None
    
    # SAME calculation for ALL calendar systems - math doesn't change between calendars
    # Year 1-100 = 1st century, 101-200 = 2nd century, etc.
    century = (year_int - 1) // 100 + 1
    
    # Simple formatting with ordinal suffix (1st, 2nd, 3rd...)
    formatted = get_ordinal_suffix(century)
    
    return century, forma