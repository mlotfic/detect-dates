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

from ordinal_suffix import get_ordinal_suffix

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