
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


class CalendarUtilities:
    """
    A comprehensive utility class for calendar operations and century calculations.
    
    This class provides static methods for working with calendar years and centuries
    across different calendar systems (Gregorian, Hijri, Jalali/Persian). All methods
    are calendar-agnostic since they work with numeric year values regardless of
    the calendar system.
    
    The class focuses on:
    - Century calculation from year values
    - Year validation and normalization
    - Century range calculations
    - Era-aware formatting
    
    Examples
    --------
    >>> # Calculate century from year
    >>> century_num, century_str = CalendarUtilities.get_century_from_year(2025)
    >>> print(f"Year 2025 is in the {century_str}")  # "Year 2025 is in the 21st"
    
    >>> # Get century range
    >>> start, end = CalendarUtilities.get_century_range(21)
    >>> print(f"21st century: {start}-{end}")  # "21st century: 2001-2100"
    
    >>> # Format with era
    >>> formatted = CalendarUtilities.format_century_with_era(15, "AH")
    >>> print(formatted)  # "15th AH"
    
    Notes
    -----
    All methods are static since they don't require instance state.
    The calculations are universal across calendar systems since they
    operate on numeric year values only.
    """
    
    @staticmethod
    def get_century_from_year(year: Union[int, str]) -> Tuple[Optional[int], Optional[str]]:
        """
        Calculate century from year with ordinal formatting.
        
        This method calculates the century for any given year using the standard
        mathematical formula. The calculation is universal across all calendar systems
        (Gregorian, Hijri, Jalali/Persian) since only the year number matters, not
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
        >>> CalendarUtilities.get_century_from_year(1)
        (1, '1st')
        >>> CalendarUtilities.get_century_from_year(100)
        (1, '1st')
        >>> CalendarUtilities.get_century_from_year(101)
        (2, '2nd')
        >>> CalendarUtilities.get_century_from_year(2025)
        (21, '21st')
        >>> CalendarUtilities.get_century_from_year("1445")
        (15, '15th')
        >>> CalendarUtilities.get_century_from_year(-5)
        (None, None)
        >>> CalendarUtilities.get_century_from_year("invalid")
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
        validate_year_input : Method for validating year inputs
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

    @staticmethod
    def validate_year_input(year: Union[int, str, None]) -> Optional[int]:
        """
        Validate and normalize year input.
        
        This utility method validates year input and converts it to a normalized
        integer format. It handles various input types and edge cases consistently.
        
        Parameters
        ----------
        year : Union[int, str, None]
            Year value to validate. Can be integer, string, or None
            
        Returns
        -------
        Optional[int]
            Validated integer year if input is valid, None otherwise
            
        Examples
        --------
        >>> CalendarUtilities.validate_year_input(2025)
        2025
        >>> CalendarUtilities.validate_year_input("1445")
        1445
        >>> CalendarUtilities.validate_year_input("  2023  ")
        2023
        >>> CalendarUtilities.validate_year_input(-5)
        None
        >>> CalendarUtilities.validate_year_input("invalid")
        None
        >>> CalendarUtilities.validate_year_input(None)
        None
        """
        if year is None:
            return None
            
        try:
            year_int = int(str(year).strip())
            return year_int if year_int > 0 else None
        except (ValueError, AttributeError, TypeError):
            return None

    @staticmethod
    def get_century_range(century: int) -> Tuple[Optional[int], Optional[int]]:
        """
        Get the year range for a given century.
        
        Given a century number, this method returns the first and last year
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
        >>> CalendarUtilities.get_century_range(1)
        (1, 100)
        >>> CalendarUtilities.get_century_range(21)
        (2001, 2100)
        >>> CalendarUtilities.get_century_range(15)
        (1401, 1500)
        >>> CalendarUtilities.get_century_range(-1)
        (None, None)
        >>> CalendarUtilities.get_century_range(0)
        (None, None)
        """
        if not isinstance(century, int) or century <= 0:
            return None, None
            
        # Calculate start and end years for the century
        start_year = (century - 1) * 100 + 1
        end_year = century * 100
        
        return start_year, end_year

    @staticmethod
    def format_century_with_era(century: int, era: str = "") -> Optional[str]:
        """
        Format century with optional era indicator.
        
        This method formats a century number with ordinal suffix and
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
        >>> CalendarUtilities.format_century_with_era(21, "CE")
        '21st CE'
        >>> CalendarUtilities.format_century_with_era(15, "AH")
        '15th AH'
        >>> CalendarUtilities.format_century_with_era(14)
        '14th'
        >>> CalendarUtilities.format_century_with_era(-1)
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

    @staticmethod
    def get_year_info(year: Union[int, str]) -> dict:
        """
        Get comprehensive information about a year.
        
        This method returns a dictionary containing all available information
        about a given year, including century data and validation status.
        
        Parameters
        ----------
        year : Union[int, str]
            The year to analyze
            
        Returns
        -------
        dict
            Dictionary containing:
            - 'original_input': The original input value
            - 'validated_year': Normalized integer year or None if invalid
            - 'is_valid': Boolean indicating if the year is valid
            - 'century_number': Numeric century or None
            - 'century_formatted': Formatted century string or None
            - 'century_range': Tuple of (start_year, end_year) for the century
            
        Examples
        --------
        >>> info = CalendarUtilities.get_year_info(2025)
        >>> print(info['century_formatted'])  # '21st'
        >>> print(info['century_range'])      # (2001, 2100)
        
        >>> info = CalendarUtilities.get_year_info("invalid")
        >>> print(info['is_valid'])           # False
        """
        # Validate the input year
        validated_year = CalendarUtilities.validate_year_input(year)
        is_valid = validated_year is not None
        
        # Initialize return dictionary
        year_info = {
            'original_input': year,
            'validated_year': validated_year,
            'is_valid': is_valid,
            'century_number': None,
            'century_formatted': None,
            'century_range': (None, None)
        }
        
        # Calculate century information if year is valid
        if is_valid:
            century_num, century_str = CalendarUtilities.get_century_from_year(validated_year)
            century_range = CalendarUtilities.get_century_range(century_num) if century_num else (None, None)
            
            year_info.update({
                'century_number': century_num,
                'century_formatted': century_str,
                'century_range': century_range
            })
        
        return year_info

    @classmethod
    def demonstrate_functionality(cls):
        """
        Demonstrate all calendar utility functionality with examples.
        
        This class method provides a comprehensive demonstration of all
        available functionality with various input types and edge cases.
        """
        print("Calendar Utilities Demonstrations")
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
            century_num, century_str = cls.get_century_from_year(year)
            
            if century_num is not None:
                year_range = cls.get_century_range(century_num)
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
            formatted = cls.format_century_with_era(century, era)
            print(f"Century {century:>2} with era '{era}' → {formatted:<8} ({calendar_type})")
        
        # Demonstrate comprehensive year info
        print("\nComprehensive Year Information:")
        print("-" * 50)
        
        sample_years = [2025, "1445", "invalid"]
        for year in sample_years:
            info = cls.get_year_info(year)
            print(f"Year '{year}':")
            print(f"  Valid: {info['is_valid']}")
            if info['is_valid']:
                print(f"  Century: {info['century_formatted']}")
                print(f"  Range: {info['century_range'][0]}-{info['century_range'][1]}")
            print()


# Legacy function wrappers for backward compatibility
# ===================================================================================

def get_century_from_year(year: Union[int, str]) -> Tuple[Optional[int], Optional[str]]:
    """
    Legacy function wrapper for CalendarUtilities.get_century_from_year().
    
    This function provides backward compatibility for existing code that
    uses the original function interface.
    
    Parameters
    ----------
    year : Union[int, str]
        The year value to convert to century
        
    Returns
    -------
    Tuple[Optional[int], Optional[str]]
        Tuple of (century_number, formatted_string) or (None, None) if invalid
    """
    return CalendarUtilities.get_century_from_year(year)


def validate_year_input(year: Union[int, str, None]) -> Optional[int]:
    """
    Legacy function wrapper for CalendarUtilities.validate_year_input().
    
    Parameters
    ----------
    year : Union[int, str, None]
        Year value to validate
        
    Returns
    -------
    Optional[int]
        Validated integer year if valid, None otherwise
    """
    return CalendarUtilities.validate_year_input(year)


def get_century_range(century: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Legacy function wrapper for CalendarUtilities.get_century_range().
    
    Parameters
    ----------
    century : int
        The century number
        
    Returns
    -------
    Tuple[Optional[int], Optional[int]]
        Tuple of (start_year, end_year) for the century
    """
    return CalendarUtilities.get_century_range(century)


def format_century_with_era(century: int, era: str = "") -> Optional[str]:
    """
    Legacy function wrapper for CalendarUtilities.format_century_with_era().
    
    Parameters
    ----------
    century : int
        The century number to format
    era : str, optional
        Era indicator to append, by default ""
        
    Returns
    -------
    Optional[str]
        Formatted century string or None if invalid
    """
    return CalendarUtilities.format_century_with_era(century, era)


if __name__ == "__main__":
    """Run demonstrations when script is executed directly."""
    CalendarUtilities.demonstrate_functionality()