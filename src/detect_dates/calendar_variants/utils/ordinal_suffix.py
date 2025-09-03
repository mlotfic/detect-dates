
"""
Created on Sun Jul 27 15:15:38 2025
@author: m
@description: This module provides calendar conversion utilities and functions to get calendar variants.
"""

# ====================================================================================
# UTILITY FUNCTIONS
# ====================================================================================
def get_ordinal_suffix(number:int)-> str:
    """
    Add ordinal suffix to number (1st, 2nd, 3rd, etc.)
    Args:
        number (int): The number to which the ordinal suffix will be added.
    Returns:
        str: The number with its ordinal suffix.
    Note:
        - Handles special cases for numbers ending in 11, 12, and 13.
        - Uses a dictionary to map last digits to their respective suffixes.
        - Returns the number as a string with the suffix appended.
    
    Examples:
        1 → "1st", 2 → "2nd", 3 → "3rd", 4 → "4th"
        11 → "11th", 12 → "12th", 13 → "13th" (special cases)
        21 → "21st", 22 → "22nd", 23 → "23rd"
    """
    # Special case: numbers ending in 11, 12, 13 always use 'th'
    # (11th, 12th, 13th - not 11st, 12nd, 13rd)
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        # Use the last digit to determine suffix
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    
    return f"{number}{suffix}"