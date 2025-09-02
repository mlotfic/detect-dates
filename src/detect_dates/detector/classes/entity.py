"""
Date Parsing and Calendar Conversion Module
==========================================

A comprehensive Python module for parsing dates with flexible precision and converting
between different calendar systems (Gregorian, Hijri/Islamic, Solar Hijri/Persian).

This module provides robust date parsing capabilities with support for:

* Partial dates (missing day, month, or year components)
* Multiple calendar systems with automatic conversion
* Flexible output formatting (ISO, strftime-style, human-readable)
* Confidence scoring for parsed date accuracy
* Multilingual support for date components

Classes:
    DateEntity: Base class for date representation with optional components
    DateEntity: Extended date class with calendar conversion capabilities
    DateMapping: Calendar system conversion and mapping functionality

Example:
    Basic date parsing and formatting::

        from date_parser import DateEntity, DateMapping

        # Parse a complete date
        date = DateEntity(day=15, month=3, year=2023, era='CE')
        print(date.strftime("%B %d, %Y"))  # "March 15, 2023"

        # Parse a partial date
        partial = DateEntity(month="March", year=2023)
        print(partial.to_iso_format())  # "2023-03-??"

        # Convert between calendars
        hijri_date = date.get_hijri()
        print(f"Hijri: {hijri_date.get_readable()}")

Author: m.lotfi
Version: 2.0
License: MIT
"""

import os
import pandas as pd
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any, Union, Tuple

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

from detect_dates.detector.classes.entity import ParsedDate
from detect_dates.normalizers import month, era, weekday
from data._load_data import DateMapping

# Module-level constants
SUPPORTED_CALENDARS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
}

WEEKDAY_COLUMN = 'Week Day'

# Precision levels for date parsing
PRECISION_LEVELS = {
    'exact': 'Complete date with day, month, year',
    'month': 'Month and year only',
    'year': 'Year only',
    'century': 'Century only',
    'partial': 'Some components missing'
}

@dataclass
class DateEntity(DateEntity):
    """
    Extended date class with calendar conversion and formatting capabilities.

    This class extends DateEntity to provide advanced functionality including:

    * Calendar system conversions (Gregorian ↔ Hijri ↔ Solar Hijri)
    * Multiple output formats (ISO, strftime, human-readable)
    * Date validation and completeness checking
    * Conversion confidence tracking

    The class uses pre-calculated mapping data from CSV files to ensure accurate
    conversions between calendar systems.

    Attributes:
        Inherits all attributes from DateEntity plus internal caching for conversions.

    Class Attributes:
        _date_mappings (Dict): Cache for date conversion mappings
        _mappings_loaded (bool): Flag indicating if mapping data is loaded

    Example:
        Complete date operations::

            # Create a Gregorian date
            date = DateEntity(day=15, month=3, year=2023, era='CE', calendar='gregorian')

            # Check completeness
            if date.is_complete():
                # Convert to other calendars
                hijri = date.get_hijri()
                julian = date.get_julian()

            # Format in different ways
            iso_format = date.to_iso_format()  # "2023-03-15"
            readable = date.get_readable()     # "March 15, 2023 CE"
            custom = date.strftime("%B %d, %Y")  # "March 15, 2023"

    Note:
        Calendar conversions require the date to be complete (have day, month, year, era).
        Partial dates can still be formatted and manipulated, but cannot be converted
        between calendar systems.
    """

    # Class-level cache for date mappings to avoid repeated file loads
    _date_mappings: Dict[str, Dict[Tuple[int, int, int], Tuple[int, int, int]]] = {}
    _mappings_loaded: bool = False

    def __post_init__(self) -> None:
        """
        Validate and normalize date components after initialization.

        This method is automatically called after object creation to:

        * Validate day values (1-31)
        * Normalize month to numeric format
        * Validate month values (1-12)
        * Validate confidence scores (0.0-1.0)
        * Set default values for missing components
        * Auto-detect precision level if not specified

        Raises:
            ValueError: If day, month, or confidence values are out of valid ranges
        """
        # Validate day component
        if self.day is not None and not (1 <= self.day <= 31):
            raise ValueError(f"Invalid day: {self.day}. Must be between 1 and 31.")

        # Normalize and validate month
        self.month_num = normalize_month(self.month, output_format="num")
        if self.month_num is not None and not (1 <= self.month_num <= 12):
            raise ValueError(f"Invalid month: {self.month}. Must be between 1 and 12.")

        # Validate confidence score
        if self.confidence is not None and not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"Confidence must be between 0.0 and 1.0, got: {self.confidence}")

        # Set default calendar if not specified
        if self.calendar is None:
            self.calendar = 'gregorian'

        # Set default era based on year
        if self.era is None and self.year is not None:
            self.era = 'CE' if self.year > 0 else 'BCE'

        # Auto-detect precision if not specified
        if self.precision is None:
            self.precision = self.detect_precision()

    def detect_precision(self) -> str:
        """
        Automatically detect the precision level of the date based on available components.

        This method analyzes which date components are available and determines the
        appropriate precision level according to the PRECISION_LEVELS constants.
        The precision detection follows a hierarchical approach from most specific
        to least specific.

        Returns:
            str: Detected precision level ('exact', 'month', 'year', 'century', or 'partial')

        Precision Detection Rules:
            * **exact**: Has day, month, and year (complete date)
            * **month**: Has month and year, but no day
            * **year**: Has year only (no month or day)
            * **century**: Has century but no specific year
            * **partial**: Has some components but doesn't fit other categories

        Example::

            # Exact precision
            date1 = DateEntity(day=15, month=3, year=2023)
            print(date1.detect_precision())  # "exact"

            # Month precision
            date2 = DateEntity(month="March", year=2023)
            print(date2.detect_precision())  # "month"

            # Year precision
            date3 = DateEntity(year=2023)
            print(date3.detect_precision())  # "year"

            # Century precision
            date4 = DateEntity(century="21st")
            print(date4.detect_precision())  # "century"

            # Partial precision
            date5 = DateEntity(day=15)  # Day without month/year
            print(date5.detect_precision())  # "partial"

        Note:
            This method is called automatically during initialization if no
            precision is explicitly specified. You can also call it manually
            to re-evaluate precision after modifying date components.
        """
        # Check for exact precision: day, month, and year all present
        if self.day is not None and self.month is not None and self.year is not None:
            return 'exact'

        # Check for month precision: month and year present, but no day
        if self.month is not None and self.year is not None and self.day is None:
            return 'month'

        # Check for year precision: only year present
        if self.year is not None and self.month is None and self.day is None:
            return 'year'

        # Check for century precision: century present but no specific year
        if self.century is not None and self.year is None:
            return 'century'

        # If we have some components but don't fit the above categories
        components = [self.day, self.month, self.year, self.century, self.weekday]
        if any(comp is not None for comp in components):
            return 'partial'

        # If no date components are present, still return partial
        # (this might happen with metadata-only dates)
        return 'partial'

    def get_precision_info(self) -> Dict[str, Any]:
        """
        Get detailed information about the date's precision level.

        This method provides comprehensive information about why a particular
        precision level was assigned and what components are available.

        Returns:
            Dict[str, Any]: Dictionary containing precision analysis::

                {
                    'precision': str,           # Current precision level
                    'description': str,         # Human-readable description
                    'available_components': List[str],  # Components that are present
                    'missing_components': List[str],    # Components that are missing
                    'completeness_score': float,        # 0.0-1.0 completeness ratio
                    'can_convert_calendar': bool,       # Whether calendar conversion is possible
                    'recommended_actions': List[str]    # Suggestions for improving precision
                }

        Example::

            date = DateEntity(month="March", year=2023)
            info = date.get_precision_info()

            print(f"Precision: {info['precision']}")          # "month"
            print(f"Description: {info['description']}")      # "Month and year only"
            print(f"Completeness: {info['completeness_score']:.1%}")  # "66.7%"
            print(f"Missing: {', '.join(info['missing_components'])}")  # "day"

        Note:
            This method is useful for understanding date quality and determining
            what additional information might be needed for specific operations.
        """
        current_precision = self.precision or self.detect_precision()

        # Define all possible core components for completeness calculation
        core_components = ['day', 'month', 'year']
        available_core = [comp for comp in core_components
                         if getattr(self, comp) is not None]
        missing_core = [comp for comp in core_components
                       if getattr(self, comp) is None]

        # Calculate completeness score based on core components
        completeness_score = len(available_core) / len(core_components)

        # Identify all available components (including optional ones)
        all_components = ['day', 'month', 'year', 'century', 'weekday', 'era']
        available_components = [comp for comp in all_components
                               if getattr(self, comp) is not None]

        # Generate recommendations based on missing components
        recommendations = []
        if current_precision == 'partial':
            if not self.year:
                recommendations.append("Add year information for better precision")
            if not self.month and self.year:
                recommendations.append("Add month information to achieve 'month' precision")
            if not self.day and self.month and self.year:
                recommendations.append("Add day information to achieve 'exact' precision")
        elif current_precision == 'year':
            recommendations.append("Add month information to improve to 'month' precision")
            recommendations.append("Add day information to achieve 'exact' precision")
        elif current_precision == 'month':
            recommendations.append("Add day information to achieve 'exact' precision")
        elif current_precision == 'century':
            recommendations.append("Add specific year information for better precision")

        # Add era recommendation if missing
        if not self.era and self.year:
            recommendations.append("Consider adding era information (CE/BCE) for clarity")

        return {
            'precision': current_precision,
            'description': PRECISION_LEVELS.get(current_precision, 'Unknown precision level'),
            'available_components': available_components,
            'missing_components': missing_core,
            'completeness_score': completeness_score,
            'can_convert_calendar': self.is_complete(),
            'recommended_actions': recommendations,
            'component_analysis': {
                'core_components_present': len(available_core),
                'core_components_total': len(core_components),
                'optional_components_present': len(available_components) - len(available_core),
                'has_temporal_context': any([self.weekday, self.era, self.century])
            }
        }

    def update_precision(self) -> str:
        """
        Update and return the current precision level based on current components.

        This method re-evaluates the precision level after components have been
        modified and updates the internal precision attribute.

        Returns:
            str: Updated precision level

        Example::

            date = DateEntity(year=2023)
            print(date.precision)  # "year"

            # Add month information
            date.month = 3
            updated_precision = date.update_precision()
            print(updated_precision)  # "month"
            print(date.precision)      # "month"

        Note:
            This method is useful when you modify date components after creation
            and want to ensure the precision level accurately reflects the current state.
        """
        self.precision = self.detect_precision()
        return self.precision

    def can_improve_precision_to(self, target_precision: str) -> Dict[str, Any]:
        """
        Check if the date can be improved to a target precision level.

        This method analyzes what components would be needed to achieve a
        specific precision level and whether such improvement is feasible.

        Args:
            target_precision (str): Target precision level ('exact', 'month', 'year', etc.)

        Returns:
            Dict[str, Any]: Analysis of precision improvement possibility::

                {
                    'possible': bool,               # Whether improvement is possible
                    'current_precision': str,       # Current precision level
                    'target_precision': str,        # Requested target precision
                    'missing_components': List[str], # What components are needed
                    'conflicting_components': List[str], # Components that would conflict
                    'recommendations': List[str]    # Specific suggestions
                }

        Example::

            date = DateEntity(year=2023)
            analysis = date.can_improve_precision_to('exact')

            if analysis['possible']:
                print(f"Can improve to exact precision")
                print(f"Need: {', '.join(analysis['missing_components'])}")
            else:
                print("Cannot improve to exact precision")
                print(f"Issues: {', '.join(analysis['conflicting_components'])}")

        Raises:
            ValueError: If target_precision is not a valid precision level
        """
        if target_precision not in PRECISION_LEVELS:
            raise ValueError(
                f"Invalid target precision: '{target_precision}'. "
                f"Valid levels: {list(PRECISION_LEVELS.keys())}"
            )

        current_precision = self.precision or self.detect_precision()

        # Define requirements for each precision level
        precision_requirements = {
            'exact': {'required': ['day', 'month', 'year'], 'optional': ['era', 'weekday']},
            'month': {'required': ['month', 'year'], 'optional': ['era'], 'forbidden': []},
            'year': {'required': ['year'], 'optional': ['era'], 'forbidden': []},
            'century': {'required': ['century'], 'optional': [], 'forbidden': ['year']},
            'partial': {'required': [], 'optional': [], 'forbidden': []}
        }

        target_req = precision_requirements[target_precision]
        current_components = {
            'day': self.day,
            'month': self.month,
            'year': self.year,
            'century': self.century,
            'era': self.era,
            'weekday': self.weekday
        }

        # Check what's missing for target precision
        missing_components = []
        for component in target_req['required']:
            if current_components[component] is None:
                missing_components.append(component)

        # Check for conflicting components
        conflicting_components = []
        forbidden_components = target_req.get('forbidden', [])
        for component in forbidden_components:
            if current_components[component] is not None:
                conflicting_components.append(component)

        # Determine if improvement is possible
        possible = len(missing_components) == 0 and len(conflicting_components) == 0

        # Generate recommendations
        recommendations = []
        if missing_components:
            recommendations.append(f"Add missing components: {', '.join(missing_components)}")

        if conflicting_components:
            recommendations.append(f"Remove conflicting components: {', '.join(conflicting_components)}")

        # Add specific guidance based on target precision
        if target_precision == 'exact' and not possible:
            if 'day' in missing_components:
                recommendations.append("Day is required for exact dates - consider if a specific day can be determined")
            if 'month' in missing_components:
                recommendations.append("Month is required for exact dates")
            if 'year' in missing_components:
                recommendations.append("Year is required for exact dates")

        elif target_precision == 'month' and not possible:
            if 'month' in missing_components:
                recommendations.append("Month information is essential for month-level precision")
            if 'year' in missing_components:
                recommendations.append("Year information is essential for month-level precision")

        return {
            'possible': possible,
            'current_precision': current_precision,
            'target_precision': target_precision,
            'missing_components': missing_components,
            'conflicting_components': conflicting_components,
            'recommendations': recommendations,
            'improvement_direction': self._get_improvement_direction(current_precision, target_precision)
        }

    def _get_improvement_direction(self, current: str, target: str) -> str:
        """
        Determine the direction of precision change.

        Args:
            current: Current precision level
            target: Target precision level

        Returns:
            str: 'increase', 'decrease', 'lateral', or 'incompatible'
        """
        # Define precision hierarchy (higher number = more precise)
        precision_hierarchy = {
            'partial': 0,
            'century': 1,
            'year': 2,
            'month': 3,
            'exact': 4
        }

        current_level = precision_hierarchy.get(current, 0)
        target_level = precision_hierarchy.get(target, 0)

        if target_level > current_level:
            return 'increase'
        elif target_level < current_level:
            return 'decrease'
        elif target_level == current_level:
            return 'lateral'
        else:
            return 'incompatible'
        """
        Check if date has all required components for calendar conversion.

        A complete date must have day, month, year, and era components.
        This is the minimum required for accurate calendar system conversions.

        Returns:
            bool: True if date has all required components, False otherwise

        Example::

            complete_date = DateEntity(day=15, month=3, year=2023, era='CE')
            print(complete_date.is_complete())  # True

            partial_date = DateEntity(month=3, year=2023)
            print(partial_date.is_complete())   # False
        """
        return all([self.day, self.month, self.year, self.era])

    def is_partial(self) -> bool:
        """
        Check if date has some but not all required components.

        Returns:
            bool: True if date has some components but is not complete

        Example::

            partial_date = DateEntity(month="March", year=2023)
            print(partial_date.is_partial())  # True

            empty_date = DateEntity()
            print(empty_date.is_partial())    # False
        """
        components = [self.day, self.month, self.year, self.era]
        return any(components) and not all(components)

    def _get_date_tuple(self) -> Optional[Tuple[int, int, int]]:
        """
        Get the date as a tuple (year, month, day) for lookup operations.

        Returns:
            Optional[Tuple[int, int, int]]: Date tuple or None if incomplete

        Note:
            This is an internal method used for efficient date lookups
            in the conversion mapping tables.
        """
        if not all([self.year, self.day]) or not self.month_num:
            return None
        return (self.year, self.month_num, self.day)

    def get_hijri(self) -> 'DateEntity':
        """
        Convert date to Hijri (Islamic) calendar system.

        Uses pre-calculated mapping data to convert from the current calendar
        system to the Hijri calendar. The conversion maintains accuracy by
        using historical astronomical calculations.

        Returns:
            DateEntity: New DateEntity instance in Hijri calendar system

        Raises:
            ValueError: If the date is not complete (missing required components)

        Example::

            gregorian = DateEntity(day=1, month=1, year=2024, era='CE')
            hijri = gregorian.get_hijri()
            print(f"Hijri date: {hijri.get_readable()}")

        Note:
            The confidence score of the converted date is reduced to indicate
            the additional uncertainty introduced by the conversion process.
        """
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Hijri calendar.")

        # Skip conversion if already in Hijri calendar
        if self.calendar == 'hijri':
            return self._create_copy()

        # Use DateMapping for conversion
        mapper = DateMapping()
        result = mapper.get_date_alternative_calendar(
            self.calendar, self.day, self.month_num, self.year
        )

        if result is None:
            raise ValueError(f"Cannot convert date {self.day}/{self.month_num}/{self.year} "
                           f"from {self.calendar} to Hijri: date not found in mapping data.")

        hijri_data = result['hijri']
        return DateEntity(
            day=hijri_data['day'],
            month=hijri_data['month'],
            year=hijri_data['year'],
            weekday=result['weekday'],
            era='AH',  # Anno Hegirae (After Hijra)
            calendar='hijri',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.9 if self.confidence else 0.8,
            metadata={
                **(self.metadata if self.metadata else {}),
                'converted_from': self.calendar,
                'conversion_method': 'csv_mapping',
                'original_date': f"{self.day}/{self.month_num}/{self.year}"
            }
        )

    def get_gregorian(self) -> 'DateEntity':
        """
        Convert date to Gregorian calendar system.

        Converts the current date to the Gregorian calendar system using
        pre-calculated mapping data for accuracy.

        Returns:
            DateEntity: New DateEntity instance in Gregorian calendar system

        Raises:
            ValueError: If the date is not complete

        Example::

            hijri = DateEntity(day=1, month=1, year=1445, era='AH', calendar='hijri')
            gregorian = hijri.get_gregorian()
            print(f"Gregorian date: {gregorian.get_readable()}")
        """
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Gregorian calendar.")

        # Skip conversion if already Gregorian
        if self.calendar == 'gregorian':
            return self._create_copy()

        mapper = DateMapping()
        result = mapper.get_date_alternative_calendar(
            self.calendar, self.day, self.month_num, self.year
        )

        if result is None:
            raise ValueError(f"Cannot convert date from {self.calendar} to Gregorian.")

        greg_data = result['gregorian']
        return DateEntity(
            day=greg_data['day'],
            month=greg_data['month'],
            year=greg_data['year'],
            weekday=result['weekday'],
            era='CE' if greg_data['year'] > 0 else 'BCE',
            calendar='gregorian',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.9 if self.confidence else 0.8,
            metadata={
                **(self.metadata if self.metadata else {}),
                'converted_from': self.calendar,
                'conversion_method': 'csv_mapping'
            }
        )

    def get_julian(self) -> 'DateEntity':
        """
        Convert date to Solar Hijri (Persian/Julian) calendar system.

        Returns:
            DateEntity: New DateEntity instance in Solar Hijri calendar system

        Raises:
            ValueError: If the date is not complete
        """
        if not self.is_complete():
            raise ValueError("Cannot convert incomplete date to Solar Hijri calendar.")

        if self.calendar == 'julian':
            return self._create_copy()

        mapper = DateMapping()
        result = mapper.get_date_alternative_calendar(
            self.calendar, self.day, self.month_num, self.year
        )

        if result is None:
            raise ValueError(f"Cannot convert date from {self.calendar} to Solar Hijri.")

        julian_data = result['julian']
        return DateEntity(
            day=julian_data['day'],
            month=julian_data['month'],
            year=julian_data['year'],
            weekday=result['weekday'],
            era='SH',  # Solar Hijri
            calendar='julian',
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence * 0.9 if self.confidence else 0.8,
            metadata={
                **(self.metadata if self.metadata else {}),
                'converted_from': self.calendar,
                'conversion_method': 'csv_mapping'
            }
        )

    def _create_copy(self) -> 'DateEntity':
        """Create a copy of the current DateEntity instance."""
        return DateEntity(
            weekday=self.weekday,
            day=self.day,
            month=self.month,
            year=self.year,
            century=self.century,
            era=self.era,
            calendar=self.calendar,
            raw_text=self.raw_text,
            lang=self.lang,
            precision=self.precision,
            confidence=self.confidence,
            metadata=self.metadata.copy() if self.metadata else None
        )

    def to_iso_format(self) -> str:
        """
        Convert to ISO 8601 format (YYYY-MM-DD) with missing components as question marks.

        For partial dates, missing components are represented with '?' characters:

        * Missing day: "2023-03-??"
        * Missing month: "2023-??-??"
        * Missing year: "????-??-??"

        Returns:
            str: ISO formatted date string

        Example::

            complete = DateEntity(day=15, month=3, year=2023)
            print(complete.to_iso_format())  # "2023-03-15"

            partial = DateEntity(month=3, year=2023)
            print(partial.to_iso_format())   # "2023-03-??"
        """
        year_str = f"{self.year:04d}" if self.year else "????"
        month_str = f"{self.month_num:02d}" if self.month_num else "??"
        day_str = f"{self.day:02d}" if self.day else "??"

        return f"{year_str}-{month_str}-{day_str}"

    def strftime(self, format_string: str) -> str:
        """
        Format the parsed date using strftime-like format codes with extensions.

        Supports standard strftime codes plus extensions for partial dates:

        Standard codes:
            * %d: Day with zero padding (01-31) or ?? if None
            * %e: Day without padding (1-31) or ? if None
            * %m: Month as number with padding (01-12) or ?? if None
            * %n: Month as number without padding (1-12) or ? if None
            * %b: Abbreviated month name (Jan, Feb, ...) or ??? if None
            * %B: Full month name (January, February, ...) or ??? if None
            * %y: Year without century (00-99) or ?? if None
            * %Y: Year with century (e.g. 2023, 1066) or ???? if None
            * %C: Century number or ?? if None
            * %A: Full weekday name (Monday, ...) or ??? if None
            * %a: Abbreviated weekday name (Mon, ...) or ??? if None

        Extensions:
            * %E: Era (BCE, CE, AD, BC) or empty if None
            * %S: Calendar system or empty if None
            * %P: Precision level or empty if None
            * %%: Literal % character

        Args:
            format_string (str): Format string with % codes

        Returns:
            str: Formatted date string with missing components shown as ? marks

        Example::

            date = DateEntity(day=15, month=3, year=2023)
            print(date.strftime("%Y-%m-%d"))    # "2023-03-15"
            print(date.strftime("%B %e, %Y"))   # "March 15, 2023"

            partial = DateEntity(month="March", year=2023)
            print(partial.strftime("%B %Y"))    # "March 2023"
            print(partial.strftime("%Y-%m-%d")) # "2023-03-??"
        """
        result = format_string

        # Day formatting
        if self.day:
            result = result.replace('%d', f"{self.day:02d}")
            result = result.replace('%e', str(self.day))
        else:
            result = result.replace('%d', '??')
            result = result.replace('%e', '?')

        # Month formatting
        if self.month_num:
            result = result.replace('%m', f"{self.month_num:02d}")
            result = result.replace('%n', str(self.month_num))

            # Get month names
            full_month = normalize_month(self.month_num,
                                       to_lang=self.lang or 'en',
                                       to_calendar=self.calendar or 'gregorian',
                                       output_format="full")
            abbr_month = normalize_month(self.month_num,
                                       to_lang=self.lang or 'en',
                                       to_calendar=self.calendar or 'gregorian',
                                       output_format="abbr")

            result = result.replace('%B', full_month or '???')
            result = result.replace('%b', abbr_month or '???')
        else:
            result = result.replace('%m', '??')
            result = result.replace('%n', '?')
            result = result.replace('%B', '???')
            result = result.replace('%b', '???')

        # Year formatting
        if self.year:
            result = result.replace('%Y', str(self.year))
            result = result.replace('%y', f"{abs(self.year) % 100:02d}")
            result = result.replace('%C', str((abs(self.year) // 100) + 1))
        else:
            result = result.replace('%Y', '????')
            result = result.replace('%y', '??')
            result = result.replace('%C', '??')

        # Weekday formatting
        if self.weekday:
            result = result.replace('%A', self.weekday)
            result = result.replace('%a', self.weekday[:3] if len(self.weekday) >= 3 else self.weekday)
        else:
            result = result.replace('%A', '???')
            result = result.replace('%a', '???')

        # Extension formatting
        result = result.replace('%E', self.era or '')
        result = result.replace('%S', self.calendar or '')
        result = result.replace('%P', self.precision or '')
        result = result.replace('%%', '%')

        return result

    def get_readable(self) -> str:
        """
        Return a human-readable string representation of the date.

        The format varies based on available components and calendar system:

        * Complete date: "March 15, 2023 CE (Gregorian)"
        * Partial date: "March 2023 CE" or "2023 CE"
        * With weekday: "Friday, March 15, 2023 CE"

        Returns:
            str: Human-readable date string

        Example::

            complete = DateEntity(day=15, month=3, year=2023, era='CE')
            print(complete.get_readable())  # "March 15, 2023 CE"

            partial = DateEntity(month="March", year=2023)
            print(partial.get_readable())   # "March 2023"
        """
        parts = []

        # Add weekday if available
        if self.weekday:
            parts.append(f"{self.weekday},")

        # Add month name
        if self.month:
            month_name = normalize_month(self.month,
                                       to_lang=self.lang or 'en',
                                       to_calendar=self.calendar or 'gregorian',
                                       output_format="full")
            if month_name:
                parts.append(month_name)

        # Add day
        if self.day:
            parts.append(f"{self.day},")

        # Add year
        if self.year:
            parts.append(str(self.year))

        # Add era
        if self.era:
            parts.append(self.era)

        # Add calendar system if not default
        if self.calendar and self.calendar != 'gregorian':
            parts.append(f"({self.calendar.title()})")

        return " ".join(parts)

    def _to_datetime(self) -> Optional[datetime]:
        """
        Convert to Python datetime object if possible.

        Returns:
            Optional[datetime]: Python datetime object or None if conversion not possible

        Note:
            Only works for complete Gregorian dates. Other calendar systems and
            partial dates cannot be converted to Python datetime objects.
        """
        if not self.is_complete() or self.calendar != 'gregorian':
            return None

        try:
            return datetime(self.year, self.month_num, self.day)
        except ValueError:
            return None


def create_date_from_components(day: Optional[int] = None,
                              month: Optional[Union[int, str]] = None,
                              year: Optional[int] = None,
                              era: Optional[str] = None,
                              calendar: str = 'gregorian',
                              **kwargs) -> DateEntity:
    """
    Convenience function to create a DateEntity from individual components.

    Args:
        day: Day of month (1-31)
        month: Month as number (1-12) or name
        year: Full year
        era: Era designation (CE, BCE, AD, BC, etc.)
        calendar: Calendar system ('gregorian', 'hijri', 'julian')
        **kwargs: Additional arguments passed to DateEntity constructor

    Returns:
        DateEntity: Configured DateEntity instance

    Example::

        date = create_date_from_components(
            day=15, month="March", year=2023,
            era='CE', confidence=0.95
        )
    """
    return DateEntity(
        day=day,
        month=month,
        year=year,
        era=era,
        calendar=calendar,
        **kwargs
    )

# Example usage and module demonstration
def main():
    """
    Demonstrate the date parsing and conversion capabilities.

    This function shows practical examples of how to use the date parsing
    module for various real-world scenarios.
    """
    print("Date Parsing and Calendar Conversion Module")
    print("=" * 50)
    print()

    # Example 1: Complete date parsing and formatting
    print("1. Complete Date Example:")
    date1 = DateEntity(day=15, month=3, year=2023, era='CE', calendar='gregorian')
    print(f"   Original: {date1.get_readable()}")
    print(f"   ISO format: {date1.to_iso_format()}")
    print(f"   Custom format: {date1.strftime('%B %d, %Y %E')}")
    print(f"   Auto-detected precision: {date1.precision}")

    # Show precision info
    precision_info = date1.get_precision_info()
    print(f"   Completeness: {precision_info['completeness_score']:.1%}")
    print()

    # Example 2: Partial date handling with precision detection
    print("2. Partial Date Examples with Precision Detection:")

    # Month precision
    partial_month = DateEntity(month="March", year=2023)
    print(f"   Month-level: {partial_month.get_readable()}")
    print(f"   Precision: {partial_month.precision} - {partial_month.get_precision_info()['description']}")

    # Year precision
    partial_year = DateEntity(year=2023)
    print(f"   Year-level: {partial_year.get_readable()}")
    print(f"   Precision: {partial_year.precision} - {partial_year.get_precision_info()['description']}")

    # Century precision
    partial_century = DateEntity(century="21st")
    print(f"   Century-level: {partial_century.get_readable()}")
    print(f"   Precision: {partial_century.precision} - {partial_century.get_precision_info()['description']}")

    # Partial with mixed components
    partial_mixed = DateEntity(day=15, weekday="Friday")
    print(f"   Mixed partial: {partial_mixed.get_readable()}")
    print(f"   Precision: {partial_mixed.precision} - {partial_mixed.get_precision_info()['description']}")
    print()

    # Example 3: Precision improvement analysis
    print("3. Precision Improvement Analysis:")

    # Analyze improvement from year to exact
    year_date = DateEntity(year=2023)
    improvement_analysis = year_date.can_improve_precision_to('exact')
    print(f"   Current: {improvement_analysis['current_precision']}")
    print(f"   Target: {improvement_analysis['target_precision']}")
    print(f"   Possible: {improvement_analysis['possible']}")
    print(f"   Missing: {', '.join(improvement_analysis['missing_components'])}")
    print(f"   Recommendations:")
    for rec in improvement_analysis['recommendations']:
        print(f"     - {rec}")
    print()

    # Example 4: Dynamic precision updating
    print("4. Dynamic Precision Updates:")

    # Start with year precision
    evolving_date = DateEntity(year=2023)
    print(f"   Initial precision: {evolving_date.precision}")

    # Add month
    evolving_date.month = 3
    new_precision = evolving_date.update_precision()
    print(f"   After adding month: {new_precision}")

    # Add day
    evolving_date.day = 15
    final_precision = evolving_date.update_precision()
    print(f"   After adding day: {final_precision}")
    print(f"   Final date: {evolving_date.get_readable()}")
    print()

    # Example 5: All precision levels demonstration
    print("5. All Precision Levels:")
    precision_examples = [
        DateEntity(day=15, month=3, year=2023, era='CE'),  # exact
        DateEntity(month="March", year=2023),              # month
        DateEntity(year=2023),                             # year
        DateEntity(century="21st"),                        # century
        DateEntity(day=15, weekday="Friday")               # partial
    ]

    for i, date in enumerate(precision_examples, 1):
        info = date.get_precision_info()
        print(f"   {i}. Precision: {date.precision}")
        print(f"      Description: {info['description']}")
        print(f"      Completeness: {info['completeness_score']:.1%}")
        print(f"      Available: {', '.join(info['available_components'])}")
        if info['missing_components']:
            print(f"      Missing: {', '.join(info['missing_components'])}")
        print()

    # Example 3: Calendar conversion (if complete)
    print("3. Calendar Conversion Example:")
    if date1.is_complete():
        try:
            hijri = date1.get_hijri()
            print(f"   Gregorian: {date1.get_readable()}")
            print(f"   Hijri: {hijri.get_readable()}")
            print(f"   Conversion confidence: {hijri.confidence:.2f}")
        except Exception as e:
            print(f"   Conversion error: {e}")
    print()

    # Example 4: Multiple formatting options
    print("4. Formatting Options:")
    formats = [
        ("%Y-%m-%d", "ISO-like format"),
        ("%B %d, %Y", "US format"),
        ("%d %B %Y", "European format"),
        ("%A, %B %d, %Y %E", "Full format with weekday and era")
    ]

    for fmt, description in formats:
        result = date1.strftime(fmt)
        print(f"   {description}: {result}")
    print()


if __name_