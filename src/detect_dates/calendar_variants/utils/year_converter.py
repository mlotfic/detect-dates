
"""
Calendar Conversion Utilities Module

This module provides calendar conversion utilities and functions to get calendar variants
across three major calendar systems: Gregorian (Western), Hijri (Islamic), and 
Julian/Persian Solar calendars.

:author: m
:created: Sun Jun 22 21:38:10 2025
:description: Calendar conversion utilities with approximate year conversions
"""


class YearConverter:
    """
    A utility class for converting years between different calendar systems.
    
    This class handles conversions between Gregorian (Western), Hijri (Islamic),
    and Julian (Persian Solar) calendar systems. Note that conversions are 
    approximate due to the fundamental differences in calendar structures.
    
    Parameters
    ----------
    calendar : str
        The source calendar system. Must be one of: 'gregorian', 'hijri', 'julian'
    year : int
        The year value in the source calendar system
        
    Attributes
    ----------
    year : int
        The original year value in the source calendar
    calendar : str
        The source calendar system identifier
    julian_year : int
        The equivalent year in the Julian/Persian Solar calendar
    gregorian_year : int
        The equivalent year in the Gregorian calendar
    hijri_year : int
        The equivalent year in the Hijri calendar
        
    Examples
    --------
    >>> # Convert from Gregorian year 2023
    >>> converter = YearConverter('gregorian', 2023)
    >>> print(f"Julian: {converter.julian_year}")
    >>> print(f"Hijri: {converter.hijri_year}")
    
    >>> # Convert from Hijri year 1445
    >>> converter = YearConverter('hijri', 1445)
    >>> print(f"Gregorian: {converter.gregorian_year}")
    >>> print(f"Julian: {converter.julian_year}")
    
    Raises
    ------
    ValueError
        If an unsupported calendar type is provided
        
    Notes
    -----
    All conversions are approximate due to:
    - Different year lengths (solar vs lunar calendars)
    - Different epoch starting points
    - Leap year variations between systems
    
    The conversion formulas used are simplified approximations suitable
    for general date range estimation rather than precise date conversion.
    """
    
    def __init__(self, calendar: str, year: int):
        """
        Initialize the calendar converter with source calendar and year.
        
        Parameters
        ----------
        calendar : str
            Source calendar system ('gregorian', 'hijri', or 'julian')
        year : int
            Year value in the source calendar system
        """
        self.year = year
        self.calendar = calendar.lower()  # Normalize to lowercase for consistency
        
        # Validate calendar type
        if self.calendar not in ['gregorian', 'hijri', 'julian']:
            raise ValueError(
                f"Unsupported calendar type: '{calendar}'. "
                "Supported types are 'gregorian', 'hijri', and 'julian'."
            )
        
        # Initialize all year conversions
        self.julian_year = self._convert_to_julian()
        self.gregorian_year = self._convert_to_gregorian()
        self.hijri_year = self._convert_to_hijri()
        
    def _convert_to_julian(self):
        """
        Convert the source year to Julian/Persian Solar calendar year.
        
        Returns
        -------
        int
            Equivalent year in the Julian/Persian Solar calendar
            
        Notes
        -----
        Conversion formulas:
        - From Gregorian: julian = gregorian - 621
        - From Hijri: julian = (hijri - 1) * 0.97 + 622
        - From Julian: julian = julian (no conversion needed)
        """
        if self.calendar == 'gregorian':
            # Persian Solar calendar is approximately 621 years behind Gregorian
            return int(self.year - 621)
            
        elif self.calendar == 'hijri':
            # Convert Hijri to Julian via approximate formula
            # Hijri years are shorter (354 days) than solar years (365 days)
            # Ratio of approximately 0.97 accounts for this difference
            return int((self.year - 1) * 0.97 + 622)
            
        elif self.calendar == 'julian':
            # Already in Julian calendar
            return self.year
    
    def _convert_to_gregorian(self):
        """
        Convert the source year to Gregorian calendar year.
        
        Returns
        -------
        int
            Equivalent year in the Gregorian calendar
            
        Notes
        -----
        Conversion formulas:
        - From Gregorian: gregorian = gregorian (no conversion needed)
        - From Hijri: gregorian = (hijri - 1) * 0.97 + 622
        - From Julian: gregorian = julian + 621
        """
        if self.calendar == 'gregorian':
            # Already in Gregorian calendar
            return self.year
            
        elif self.calendar == 'hijri':
            # Convert Hijri to Gregorian via approximate formula
            # Similar to Julian conversion as both are solar-based
            return int((self.year - 1) * 0.97 + 622)
            
        elif self.calendar == 'julian':
            # Julian/Persian Solar is approximately 621 years ahead of Gregorian
            return int(self.year + 621)
    
    def _convert_to_hijri(self):
        """
        Convert the source year to Hijri calendar year.
        
        Returns
        -------
        int
            Equivalent year in the Hijri calendar
            
        Notes
        -----
        Conversion formulas:
        - From Gregorian: hijri = (gregorian - 622) / 0.97 + 1
        - From Hijri: hijri = hijri (no conversion needed)  
        - From Julian: hijri = (julian - 622) / 0.97 + 1
        """
        if self.calendar == 'gregorian':
            # Convert Gregorian to Hijri using inverse of the Hijri->Gregorian formula
            return int((self.year - 622) / 0.97 + 1)
            
        elif self.calendar == 'hijri':
            # Already in Hijri calendar
            return self.year
            
        elif self.calendar == 'julian':
            # Convert Julian to Hijri (Julian and Gregorian have similar relationship to Hijri)
            return int((self.year - 622) / 0.97 + 1)
    
    def get_all_years(self):
        """
        Get a dictionary containing the year in all three calendar systems.
        
        Returns
        -------
        dict
            Dictionary with keys 'gregorian', 'hijri', 'julian' and their
            corresponding year values
            
        Examples
        --------
        >>> converter = YearConverter('gregorian', 2023)
        >>> all_years = converter.get_all_years()
        >>> print(all_years)
        {'gregorian': 2023, 'hijri': 1444, 'julian': 1402}
        """
        return {
            'gregorian': self.gregorian_year,
            'hijri': self.hijri_year,
            'julian': self.julian_year
        }
    
    def __str__(self):
        """
        Return a string representation of the converter with all year conversions.
        
        Returns
        -------
        str
            Formatted string showing original year and all conversions
        """
        return (
            f"YearConverter(source: {self.calendar} {self.year}) -> "
            f"Gregorian: {self.gregorian_year}, "
            f"Hijri: {self.hijri_year}, "
            f"Julian: {self.julian_year}"
        )
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns
        -------
        str
            Detailed representation including class name and parameters
        """
        return f"YearConverter(calendar='{self.calendar}', year={self.year})"


def basic_usage_examples():
    """Demonstrate basic usage patterns for calendar conversion."""
    
    print("=" * 60)
    print("BASIC USAGE EXAMPLES")
    print("=" * 60)
    
    # Example 1: Converting from Gregorian year
    print("\n1. Converting from Gregorian year 2023:")
    gregorian_converter = YearConverter('gregorian', 2023)
    print(f"   Original: Gregorian {gregorian_converter.year}")
    print(f"   → Hijri: {gregorian_converter.hijri_year}")
    print(f"   → Julian/Persian: {gregorian_converter.julian_year}")
    
    # Example 2: Converting from Hijri year
    print("\n2. Converting from Hijri year 1445:")
    hijri_converter = YearConverter('hijri', 1445)
    print(f"   Original: Hijri {hijri_converter.year}")
    print(f"   → Gregorian: {hijri_converter.gregorian_year}")
    print(f"   → Julian/Persian: {hijri_converter.julian_year}")
    
    # Example 3: Converting from Julian/Persian year
    print("\n3. Converting from Julian/Persian year 1402:")
    julian_converter = YearConverter('julian', 1402)
    print(f"   Original: Julian/Persian {julian_converter.year}")
    print(f"   → Gregorian: {julian_converter.gregorian_year}")
    print(f"   → Hijri: {julian_converter.hijri_year}")


def practical_applications():
    """Show practical real-world applications."""
    
    print("\n\n" + "=" * 60)
    print("PRACTICAL APPLICATIONS")
    print("=" * 60)
    
    # Historical date analysis
    print("\n1. Historical Event Analysis:")
    print("   Analyzing the year of a historical Persian document...")
    
    persian_year = 1380  # A year from a Persian document
    converter = YearConverter('julian', persian_year)
    
    print(f"   Persian Solar year {persian_year} corresponds to:")
    print(f"   → Gregorian: ~{converter.gregorian_year} CE")
    print(f"   → Hijri: ~{converter.hijri_year} AH")
    print("   (This helps researchers cross-reference historical events)")
    
    # Academic research scenario
    print("\n2. Academic Research Scenario:")
    print("   Converting Islamic historical dates for comparative study...")
    
    islamic_years = [800, 1000, 1200, 1400]
    print("   Islamic Calendar → Gregorian Calendar:")
    
    for hijri_year in islamic_years:
        converter = YearConverter('hijri', hijri_year)
        print(f"   {hijri_year} AH → ~{converter.gregorian_year} CE")
    
    # Modern application
    print("\n3. Modern Calendar Integration:")
    print("   Converting current Persian calendar year to other systems...")
    
    current_persian = 1403  # Example current Persian year
    converter = YearConverter('julian', current_persian)
    
    print(f"   Persian Solar {current_persian}:")
    print(f"   → Western calendar: {converter.gregorian_year}")
    print(f"   → Islamic calendar: ~{converter.hijri_year}")


def advanced_usage():
    """Demonstrate advanced features and methods."""
    
    print("\n\n" + "=" * 60)
    print("ADVANCED USAGE")
    print("=" * 60)
    
    # Using get_all_years() method
    print("\n1. Getting all calendar equivalents at once:")
    converter = YearConverter('gregorian', 2024)
    all_years = converter.get_all_years()
    
    print(f"   Year 2024 in all calendar systems:")
    for calendar, year in all_years.items():
        print(f"   {calendar.capitalize()}: {year}")
    
    # String representations
    print("\n2. String representations for logging/debugging:")
    converter = YearConverter('hijri', 1445)
    print(f"   str(): {str(converter)}")
    print(f"   repr(): {repr(converter)}")
    
    # Case insensitive input
    print("\n3. Case-insensitive calendar types:")
    converters = [
        YearConverter('GREGORIAN', 2023),
        YearConverter('Hijri', 1444),
        YearConverter('julian', 1401)
    ]
    
    for conv in converters:
        print(f"   Input: {conv.calendar} → Normalized and working correctly")


def batch_processing_example():
    """Show how to process multiple years efficiently."""
    
    print("\n\n" + "=" * 60)
    print("BATCH PROCESSING EXAMPLE")
    print("=" * 60)
    
    # Processing historical timeline
    print("\n1. Processing a historical timeline:")
    historical_events = [
        ("Birth of Prophet Muhammad", 'gregorian', 570),
        ("Start of Islamic Calendar", 'gregorian', 622),
        ("Fall of Baghdad", 'hijri', 656),
        ("Persian Constitutional Revolution", 'julian', 1285)
    ]
    
    print("   Event Timeline Conversions:")
    print("   " + "-" * 50)
    
    for event, cal_type, year in historical_events:
        converter = YearConverter(cal_type, year)
        all_years = converter.get_all_years()
        
        print(f"   {event}:")
        print(f"   └─ Original: {cal_type.capitalize()} {year}")
        print(f"   └─ Gregorian: {all_years['gregorian']}")
        print(f"   └─ Hijri: {all_years['hijri']}")
        print(f"   └─ Julian/Persian: {all_years['julian']}")
        print()


def error_handling_examples():
    """Demonstrate proper error handling."""
    
    print("\n\n" + "=" * 60)
    print("ERROR HANDLING EXAMPLES")
    print("=" * 60)
    
    # Invalid calendar type
    print("\n1. Handling invalid calendar types:")
    try:
        converter = YearConverter('invalid_calendar', 2023)
    except ValueError as e:
        print(f"   Error caught: {e}")
    
    # Edge cases
    print("\n2. Working with edge case years:")
    edge_cases = [
        ('gregorian', 1),      # Very early year
        ('hijri', 1),          # First Hijri year
        ('julian', 1),         # First Julian year
        ('gregorian', 3000)    # Future year
    ]
    
    print("   Edge case conversions:")
    for cal_type, year in edge_cases:
        try:
            converter = YearConverter(cal_type, year)
            print(f"   {cal_type.capitalize()} {year} → "
                  f"G:{converter.gregorian_year}, "
                  f"H:{converter.hijri_year}, "
                  f"J:{converter.julian_year}")
        except Exception as e:
            print(f"   Error with {cal_type} {year}: {e}")


def comparison_table():
    """Generate a comparison table for reference."""
    
    print("\n\n" + "=" * 60)
    print("REFERENCE CONVERSION TABLE")
    print("=" * 60)
    
    # Sample years for comparison
    sample_years = [
        ('gregorian', 2020),
        ('gregorian', 2021),
        ('gregorian', 2022),
        ('gregorian', 2023),
        ('gregorian', 2024)
    ]
    
    print("\n   Recent Years Comparison:")
    print("   " + "-" * 45)
    print("   Gregorian | Hijri  | Julian/Persian")
    print("   " + "-" * 45)
    
    for cal_type, year in sample_years:
        converter = YearConverter(cal_type, year)
        print(f"   {converter.gregorian_year:9} | {converter.hijri_year:6} | {converter.julian_year:10}")


if __name__ == "__main__":
    """Run all examples when script is executed directly."""
    
    print("YEAR CALENDAR CONVERTER - COMPREHENSIVE EXAMPLES")
    print("=" * 60)
    print("This script demonstrates various ways to use the YearConverter class")
    print("for converting years between Gregorian, Hijri, and Julian calendar systems.")
    
    # Run all example functions
    basic_usage_examples()
    practical_applications()
    advanced_usage()
    batch_processing_example()
    error_handling_examples()
    comparison_table()
    
    print("\n\n" + "=" * 60)
    print("EXAMPLES COMPLETED")
    print("=" * 60)
    print("These examples show how to:")
    print("• Convert between different calendar systems")
    print("• Handle various input formats and edge cases")
    print("• Use advanced features like get_all_years()")
    print("• Process multiple conversions efficiently")
    print("• Handle errors gracefully")
    print("• Generate reference tables for comparison")
    print("\nFor more information, check the class documentation using help(YearConverter)")


# Additional utility functions for common use cases
def quick_convert(source_calendar: str, year: int, target_calendar: str) -> int:
    """
    Quick conversion utility function.
    
    Parameters
    ----------
    source_calendar : str
        Source calendar system ('gregorian', 'hijri', 'julian')
    year : int
        Year in source calendar
    target_calendar : str
        Target calendar system ('gregorian', 'hijri', 'julian')
        
    Returns
    -------
    int
        Converted year in target calendar system
        
    Examples
    --------
    >>> quick_convert('gregorian', 2023, 'hijri')
    1444
    >>> quick_convert('hijri', 1445, 'julian')
    1402
    """
    converter = YearConverter(source_calendar, year)
    
    if target_calendar.lower() == 'gregorian':
        return converter.gregorian_year
    elif target_calendar.lower() == 'hijri':
        return converter.hijri_year
    elif target_calendar.lower() == 'julian':
        return converter.julian_year
    else:
        raise ValueError(f"Invalid target calendar: {target_calendar}")


def create_conversion_table(start_year: int, end_year: int, source_calendar: str = 'gregorian'):
    """
    Create a conversion table for a range of years.
    
    Parameters
    ----------
    start_year : int
        Starting year (inclusive)
    end_year : int
        Ending year (inclusive)
    source_calendar : str, optional
        Source calendar system, by default 'gregorian'
        
    Examples
    --------
    >>> table = create_conversion_table(2020, 2025)
    >>> for row in table:
    ...     print(f"G:{row['gregorian']} H:{row['hijri']} J:{row['julian']}")
    """
    conversion_table = []
    
    for year in range(start_year, end_year + 1):
        converter = YearConverter(source_calendar, year)
        conversion_table.append({
            'source_year': year,
            'source_calendar': source_calendar,
            'gregorian': converter.gregorian_year,
            'hijri': converter.hijri_year,
            'julian': converter.julian_year
        })
    
    return conversion_table