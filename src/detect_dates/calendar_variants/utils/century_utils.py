
"""
Calendar Utilities Module

This module provides calendar conversion utilities and functions to get calendar variants.
Includes century calculation utilities that work across all calendar systems.

:author: m
:created: Sun Jun 22 21:38:10 2025
:description: Calendar conversion utilities and century calculation functions
"""

from typing import Tuple, Optional, Union

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """
        Setup the source path for module imports.
        
        This function locates the 'src' directory in the current file path
        and adds it to sys.path to enable proper module imports.
        """
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        
        # Look for 'src' directory in the path hierarchy
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                break
                
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

from detect_dates.calendar_variants.utils.ordinal_suffix import get_ordinal_suffix

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================

def get_century_from_year(year: Union[int, str]) -> Tuple[Optional[int], Optional[str]]:
    """
    Calculate century from year with ordinal formatting.
    
    This function calculates the century for any given year using the standard
    mathematical formula. The calculation is universal across all calendar systems
    (Gregorian, Hijri, Julian/Persian) since only the year number matters, not
    the calendar type.
    
    Parameters
    ----------
    year : Union[int, str]
        The year value to convert to century. Can be integer or string
        representation of a positive integer
        
    Returns
    -------
    Tuple[Optional[int], Optional[str]]
        A tuple containing:
        - century_number: The numeric century (e.g., 21 for year 2025)
        - formatted_string: The formatted century with ordinal suffix (e.g., "21st")
        Returns (None, None) if the input year is invalid
        
    Examples
    --------
    >>> get_century_from_year(1)
    (1, '1st')
    >>> get_century_from_year(100)
    (1, '1st')
    >>> get_century_from_year(101)
    (2, '2nd')
    >>> get_century_from_year(2025)
    (21, '21st')
    >>> get_century_from_year("1445")
    (15, '15th')
    >>> get_century_from_year(-5)
    (None, None)
    >>> get_century_from_year("invalid")
    (None, None)
        
    Notes
    -----
    - Century calculation formula: (year - 1) // 100 + 1
    - Year 1-100 belongs to 1st century, 101-200 to 2nd century, etc.
    - This is the standard historical/mathematical definition of centuries
    - Works for any positive integer year value
    - Invalid inputs (negative, zero, non-numeric) return (None, None)
    
    Raises
    ------
    No exceptions are raised. Invalid inputs are handled gracefully
    by returning (None, None).
    
    See Also
    --------
    get_ordinal_suffix : Function used for formatting ordinal numbers
    """
    # Handle None input early
    if year is None:
        return None, None
    
    try:
        # Convert to integer, handling both string and integer input
        # Strip whitespace to handle padded string input
        year_int = int(str(year).strip())
    except (ValueError, AttributeError, TypeError):
        # Invalid input - cannot convert to integer
        return None, None
    
    # Validate year is positive (no negative years or year zero)
    if year_int <= 0:
        return None, None
    
    # Calculate century using standard mathematical formula
    # This formula is universal across all calendar systems
    # Year 1-100 = 1st century, 101-200 = 2nd century, etc.
    century = (year_int - 1) // 100 + 1
    
    # Format with ordinal suffix (1st, 2nd, 3rd, 4th, etc.)
    formatted = get_ordinal_suffix(century)
    
    return century, formatted


def get_century_range(century: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Get the year range for a given century.
    
    Given a century number, this function returns the first and last year
    that belong to that century.
    
    Parameters
    ----------
    century : int
        The century number (e.g., 21 for 21st century)
        
    Returns
    -------
    Tuple[Optional[int], Optional[int]]
        A tuple containing (start_year, end_year) for the century,
        or (None, None) if century is invalid
        
    Examples
    --------
    >>> get_century_range(1)
    (1, 100)
    >>> get_century_range(21)
    (2001, 2100)
    >>> get_century_range(15)
    (1401, 1500)
    >>> get_century_range(-1)
    (None, None)
    >>> get_century_range(0)
    (None, None)
    """
    if not isinstance(century, int) or century <= 0:
        return None, None
        
    # Calculate start and end years for the century
    start_year = (century - 1) * 100 + 1
    end_year = century * 100
    
    return start_year, end_year


def format_century_with_era(century: int, era: str = "") -> Optional[str]:
    """
    Format century with optional era indicator.
    
    This function formats a century number with ordinal suffix and
    an optional era indicator (e.g., "CE", "AH", "SH").
    
    Parameters
    ----------
    century : int
        The century number to format
    era : str, optional
        Era indicator to append (e.g., "CE", "AH", "SH"), by default ""
        
    Returns
    -------
    Optional[str]
        Formatted century string, or None if century is invalid
        
    Examples
    --------
    >>> format_century_with_era(21, "CE")
    '21st CE'
    >>> format_century_with_era(15, "AH")
    '15th AH'
    >>> format_century_with_era(14)
    '14th'
    >>> format_century_with_era(-1)
    None
    """
    if not isinstance(century, int) or century <= 0:
        return None
        
    # Get ordinal formatting
    formatted_century = get_ordinal_suffix(century)
    
    # Add era if provided
    if era and era.strip():
        return f"{formatted_century} {era.strip()}"
    
    return formatted_century


# ===================================================================================
# TESTING AND DEMONSTRATION
# ===================================================================================

def demonstrate_century_calculations():
    """
    Demonstrate century calculation functionality with various examples.
    
    This function provides a comprehensive demonstration of the century
    calculation utilities with various input types and edge cases.
    """
    print("Century Calculation Demonstrations")
    print("=" * 50)
    
    # Test cases covering various scenarios
    test_cases = [
        # (year, description)
        (1, "First year of history"),
        (100, "Last year of 1st century"),
        (101, "First year of 2nd century"),
        (2000, "Last year of 20th century"),
        (2001, "First year of 21st century"),
        (2025, "Current example year"),
        (1445, "Example Hijri year"),
        (1402, "Example Persian year"),
        ("2023", "String input"),
        ("  1999  ", "Padded string input"),
        (-5, "Negative year (invalid)"),
        (0, "Year zero (invalid)"),
        ("invalid", "Non-numeric string (invalid)"),
        (None, "None input (invalid)")
    ]
    
    print("\nCentury Calculations:")
    print("-" * 50)
    
    for year, description in test_cases:
        century_num, century_str = get_century_from_year(year)
        
        if century_num is not None:
            year_range = get_century_range(century_num)
            print(f"Year {year:>8} → {century_str:<6} "
                  f"(covers years {year_range[0]}-{year_range[1]}) - {description}")
        else:
            print(f"Year {str(year):>8} → Invalid input - {description}")
    
    # Demonstrate era formatting
    print("\nCentury with Era Indicators:")
    print("-" * 50)
    
    era_examples = [
        (21, "CE", "Gregorian/Western"),
        (15, "AH", "Islamic/Hijri"), 
        (14, "SH", "Persian Solar"),
        (1, "", "No era specified")
    ]
    
    for century, era, calendar_type in era_examples:
        formatted = format_century_with_era(century, era)
        print(f"Century {century:>2} with era '{era}' → {formatted:<8} ({calendar_type})")


if __name__ == "__main__":
    """Run demonstrations when script is executed directly."""
    demonstrate_century_calculations()