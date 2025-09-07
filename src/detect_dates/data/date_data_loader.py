"""
Calendar date conversion module for Gregorian, Hijri, and Solar Hijri calendars.

This module provides utilities to load and process calendar mapping data from CSV files,
supporting conversions between different calendar systems used worldwide.
"""
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

from detect_dates.keywords.constants import (
    Language,
    Calendar,
    OutputFormat,
    PRECISION_LEVELS,
    CALENDAR_ALIASES,
    SUPPORTED_LANGUAGES,
    SUPPORTED_CALENDARS,
    SUPPORTED_CALENDARS_COLUMNS,
    WEEKDAY_COLUMN,
    DEFAULT_LANGUAGE,
    DEFAULT_CALENDAR,
    RelationType,
    ComplexityLevel,
)
import os
import pandas as pd
from typing import Optional, Dict, List, Union
from dataclasses import dataclass
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from utils._load_mapping_data import _load_mapping_data

class DateDataLoader:
    """
    Calendar data loader with caching and validation capabilities.

    This class provides a convenient interface for loading and caching calendar
    mapping data, supporting multiple calendar systems with validation and
    error handling.

    Parameters
    ----------
    csv_path : str, optional
        Path to the CSV file containing calendar mapping data.
        Defaults to DEFAULT_CSV_PATH.

    Attributes
    ----------
    csv_path : str
        Path to the calendar data CSV file.

    Examples
    --------
    >>> loader = DateDataLoader()
    >>> data = loader.load_data()
    >>> print(f"Loaded {len(data)} calendar records")

    >>> # Use custom CSV file
    >>> loader = DateDataLoader("/path/to/custom/data.csv")
    >>> data = loader.load_data()
    """

    def __init__(self, csv_path=None):
        """
        Initialize the calendar data loader.

        Parameters
        ----------
        csv_path : str, optional
            Path to the CSV file containing calendar mapping data.
        """
        self.csv_path = csv_path
        self._data = None  # Cache for loaded data

    def load_data(self):
        """
        Load and return the calendar mapping data with caching.

        Returns
        -------
        pandas.DataFrame
            Validated and cleaned calendar mapping data. Subsequent calls
            return cached data without reloading from disk.

        Raises
        ------
        FileNotFoundError
            If the calendar data file is not found.
        ValueError
            If the data contains invalid values or missing columns.
        RuntimeError
            If loading fails for any other reason.

        Examples
        --------
        >>> loader = DateDataLoader()
        >>> data = loader.load_data()  # Loads from disk
        >>> data2 = loader.load_data()  # Returns cached data
        >>> assert data is data2  # Same object reference
        """
        if self._data is None:
            self._data = _load_mapping_data(self.csv_path)
        return self._data

    def reload_data(self):
        """
        Force reload of calendar data from disk, bypassing cache.

        Returns
        -------
        pandas.DataFrame
            Freshly loaded calendar mapping data.

        Examples
        --------
        >>> loader = DateDataLoader()
        >>> data1 = loader.load_data()
        >>> # ... CSV file is updated externally ...
        >>> data2 = loader.reload_data()  # Loads fresh data
        """
        self._data = None  # Clear cache
        return self.load_data()

    def get_supported_calendars(self):
        """
        Get list of supported calendar systems.

        Returns
        -------
        list
            List of supported calendar system names.

        Examples
        --------
        >>> loader = DateDataLoader()
        >>> calendars = loader.get_supported_calendars()
        >>> print(calendars)  # ['gregorian', 'hijri', 'Jalali']
        """
        return list(SUPPORTED_CALENDARS_COLUMNS.keys())
    
    def date_ranges(self) -> Dict[str, Dict[str, int]]:
        """
        Get the valid date ranges for each supported calendar system.

        Returns
        -------
        dict
            Dictionary with calendar names as keys and dictionaries with
            'min_year' and 'max_year' as values.

        Examples
        --------
        >>> loader = DateDataLoader()
        >>> ranges = loader.date_ranges()
        >>> print(ranges)
        {
            'gregorian': {'min_year': 622, 'max_year': 9999},
            'hijri': {'min_year': 1, 'max_year': 1500},
            'Jalali': {'min_year': 1300, 'max_year': 1500}
        }
        """
        data = self.load_data()
        date_ranges = {}
        for calendar in SUPPORTED_CALENDARS_COLUMNS.keys():
            year_col = SUPPORTED_CALENDARS_COLUMNS[calendar][2]
            if year_col in data.columns:
                min_year = data[year_col].min()
                max_year = data[year_col].max()
                date_ranges[calendar] = {'min_year': int(min_year), 'max_year': int(max_year)}
            else:
                date_ranges[calendar] = {'min_year': None, 'max_year': None}
        return date_ranges



