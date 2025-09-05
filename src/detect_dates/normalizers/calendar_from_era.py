# ===================================================================================
# Calendar Normalization Utilities
# ===================================================================================
"""
Calendar normalization utilities for date detection systems.

This module provides functionality to normalize calendar names and eras, supporting
multiple calendar systems including Gregorian, Hijri, and Julian calendars.

Usage
-----
Basic usage for normalizing calendar names from era strings::

    from calendar_normalization import normalize_calendar_from_era
    
    # Normalize from era abbreviations
    calendar = normalize_calendar_from_era("AD")      # Returns: "gregorian"
    calendar = normalize_calendar_from_era("AH")      # Returns: "hijri"
    calendar = normalize_calendar_from_era("BCE")     # Returns: "julian"
    
    # Normalize from calendar names/aliases
    calendar = normalize_calendar_from_era("islamic") # Returns: "hijri"
    calendar = normalize_calendar_from_era("christian") # Returns: "gregorian"
    
    # Handle invalid/unknown inputs
    calendar = normalize_calendar_from_era("unknown") # Returns: None
    calendar = normalize_calendar_from_era(None)      # Returns: None

Installation requirements::

    # Ensure your project structure has:
    # src/detect_dates/keywords/constants.py
    # src/detect_dates/normalizers.py
"""

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    
    def setup_src_path():
        """
        Add the src directory to Python path for proper module importing.
        
        This function traverses up the directory structure looking for a 'src'
        folder and adds it to sys.path if not already present.
        """
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        
        # Look for 'src' directory in the path hierarchy
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                    print(f"Added to sys.path: {src_second_path}")
                break
    
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

from typing import Optional
from src.detect_dates.keywords.constants import CALENDAR_ALIASES, SUPPORTED_CALENDARS
from detect_dates.normalizers import (
    normalize_era,
    normalize_month, 
    normalize_weekday,
    normalize_calendar_name,
    get_calendar,
)


def normalize_calendar_from_era(era: Optional[str]) -> Optional[str]:
    """
    Get the normalized calendar name from an era string or calendar name.
    
    This function accepts era abbreviations (like 'AD', 'AH', 'BCE') or calendar 
    names/aliases and returns the standardized calendar name. It handles multiple
    input formats and provides fallback behavior for unknown inputs.

    Parameters
    ----------
    era : str or None
        Era string (e.g., 'AD', 'AH', 'CE', 'BCE') or calendar name/alias.
        Can be None or empty string.

    Returns
    -------
    str or None
        Normalized calendar name ('gregorian', 'hijri', 'julian') if recognized,
        None if input is invalid or not recognized.

    Examples
    --------
    >>> normalize_calendar_from_era("AD")
    'gregorian'
    
    >>> normalize_calendar_from_era("AH")  
    'hijri'
    
    >>> normalize_calendar_from_era("islamic")
    'hijri'
    
    >>> normalize_calendar_from_era("unknown")
    None
    
    >>> normalize_calendar_from_era(None)
    None
    
    Notes
    -----
    The function performs the following checks in order:
    1. Returns None for empty/None input
    2. Checks if input is a supported calendar name
    3. Checks if input is a calendar alias
    4. Treats input as era abbreviation and normalizes
    5. Returns None if no matches found
    """
    if not era:
        return None
    
    # Convert to lowercase for case-insensitive comparison
    era_lower = era.lower()
    
    # First, check if input is already a supported calendar name
    if era_lower in SUPPORTED_CALENDARS:
        return era_lower
    
    # Check if input is a known calendar alias
    if era_lower in CALENDAR_ALIASES:
        return CALENDAR_ALIASES[era_lower]

    # Otherwise, treat as era abbreviation and attempt normalization
    normalized_era = normalize_era(era)
    if normalized_era:
        # Get the calendar system associated with this era
        calendar = get_calendar(normalized_era)
        if calendar:
            return normalize_calendar_name(calendar)
    
    # Fallback: return None for unrecognized input
    return None