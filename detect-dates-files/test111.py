#!/usr/bin/env python3
"""
Created on Sun Jul 13 00:17:26 2025

@author: m
"""
date = {
    "weekday": None,
    "day": None,
    "month": None,
    "year": None,
    "century": None,
    "era": None,
    "calendar": None
}

# Method 1: Check each value individually
for key, value in date.items():
    if value is None:
        print(f"{key}: None")
    else:
        print(f"{key}: {value}")

print("\n" + "="*30 + "\n")

# Method 2: Check if all values are None
all_none = all(value is None for value in date.values())
print(f"All values are None: {all_none}")

# Method 3: Get only the keys with None values
none_keys = [key for key, value in date.items() if value is None]
print(f"Keys with None values: {none_keys}")

# Method 4: Count None values
none_count = sum(1 for value in date.values() if value is None)
print(f"Number of None values: {none_count}")

# Method 5: Check if any value is not None
has_non_none = any(value is not None for value in date.values())
print(f"Has non-None values: {has_non_none}")





from typing import Dict, List, Optional, Union, Any
from functools import reduce

# Standard date format templates
STANDARD_DATE_FORMAT = {
    "range": {
        "hijri": "{hijri_year} : {hijri_year_end} {hijri_era}",
        "gregorian": "{gregorian_year} : {gregorian_year_end} {gregorian_era}",
        "julian": "{julian_year} : {julian_year_end} {julian_era}",
        "hijri_gregorian": "{hijri_year} : {hijri_year_end} {hijri_era} / {gregorian_year} : {gregorian_year_end} {gregorian_era}",
        "hijri_julian": "{hijri_year} : {hijri_year_end} {hijri_era} / {julian_year} : {julian_year_end} {julian_era}",
        "gregorian_julian": "{gregorian_year} : {gregorian_year_end} {gregorian_era} / {julian_year} : {julian_year_end} {julian_era}"
    },
    "year": {
        "hijri": "{hijri_year} {hijri_era}",
        "gregorian": "{gregorian_year} {gregorian_era}",
        "julian": "{julian_year} {julian_era}",
        "hijri_gregorian": "{hijri_year} {hijri_era} / {gregorian_year} {gregorian_era}",
        "hijri_julian": "{hijri_year} {hijri_era} / {julian_year} {julian_era}",
        "gregorian_julian": "{gregorian_year} {gregorian_era} / {julian_year} {julian_era}"
    },
    "month_year": {
        "hijri": "{hijri_month}-{hijri_year} {hijri_era}",
        "gregorian": "{gregorian_month}-{gregorian_year} {gregorian_era}",
        "julian": "{julian_month}-{julian_year} {julian_era}",
        "hijri_gregorian": "{hijri_month}-{hijri_year} {hijri_era} / {gregorian_month}-{gregorian_year} {gregorian_era}",
        "hijri_julian": "{hijri_month}-{hijri_year} {hijri_era} / {julian_month}-{julian_year} {julian_era}",
        "gregorian_julian": "{gregorian_month}-{gregorian_year} {gregorian_era} / {julian_month}-{julian_year} {julian_era}"
    },
    "day_month_year": {
        "hijri": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
        "gregorian": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
        "julian": "{julian_day}-{julian_month}-{julian_year} {julian_era}",
        "hijri_gregorian": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
        "hijri_julian": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {julian_day}-{julian_month}-{julian_year} {julian_era}",
        "gregorian_julian": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {julian_day}-{julian_month}-{julian_year} {julian_era}"
    },
    "weekday_day_month_year": {
        "hijri": "{weekday} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
        "gregorian": "{weekday} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
        "julian": "{weekday} - {julian_day}-{julian_month}-{julian_year} {julian_era}",
        "hijri_gregorian": "{weekday} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {weekday} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
        "hijri_julian": "{weekday} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {weekday} - {julian_day}-{julian_month}-{julian_year} {julian_era}",
        "gregorian_julian": "{weekday} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {weekday} - {julian_day}-{julian_month}-{julian_year} {julian_era}"
    },
    "century": {
        "hijri": "{hijri_century} {hijri_era}",
        "gregorian": "{gregorian_century} {gregorian_era}",
        "julian": "{julian_century} {julian_era}",
        "hijri_gregorian": "{hijri_century} {hijri_era} / {gregorian_century} {gregorian_era}",
        "hijri_julian": "{hijri_century} {hijri_era} / {julian_century} {julian_era}",
        "gregorian_julian": "{gregorian_century} {gregorian_era} / {julian_century} {julian_era}"
    }
}

# Pure functions for date processing

def extract_group_value(regex_match: Any, group_num: Union[int, List[int]]) -> Optional[str]:
    """Extract value from regex match using group number(s)"""
    if not regex_match or group_num is None:
        return None

    if isinstance(group_num, list):
        return next((regex_match.group(num) for num in group_num if regex_match.group(num)), None)

    return regex_match.group(group_num) if regex_match.group(group_num) else None


def build_date_values(regex_match: Any, date_structure: Dict) -> Dict:
    """Build date values from regex match and structure"""
    def extract_date_part(date_dict: Dict) -> Dict:
        return {
            key: extract_group_value(regex_match, value)
            for key, value in date_dict.items()
        }

    return {
        "date": extract_date_part(date_structure["date"]),
        "date_end": extract_date_part(date_structure["date_end"]) if "date_end" in date_structure else {}
    }





def detect_calendar_systems(date_values: Dict) -> List[str]:
    """Detect which calendar systems are present in the date"""
    systems = []
    date_dict = date_values["date"]

    hijri_fields = ["hijri_day", "hijri_month", "hijri_year", "hijri_century", "hijri_era"]
    gregorian_fields = ["gregorian_day", "gregorian_month", "gregorian_year", "gregorian_century", "gregorian_era"]
    julian_fields = ["julian_day", "julian_month", "julian_year", "julian_century", "julian_era"]

    if any(date_dict.get(field) for field in hijri_fields):
        systems.append("hijri")
    if any(date_dict.get(field) for field in gregorian_fields):
        systems.append("gregorian")
    if any(date_dict.get(field) for field in julian_fields):
        systems.append("julian")

    return systems


def determine_date_precision(date_values: Dict) -> str:
    """Determine the precision level of the date"""
    date_dict = date_values["date"]
    date_end_dict = date_values.get("date_end", {})

    # Check if it's a range
    if has_values(date_end_dict):
        return "range"

    # Check precision levels
    if date_dict.get("weekday"):
        return "weekday_day_month_year"
    elif any(date_dict.get(f"{cal}_day") for cal in ["hijri", "gregorian", "julian"]):
        return "day_month_year"
    elif any(date_dict.get(f"{cal}_month") for cal in ["hijri", "gregorian", "julian"]):
        return "month_year"
    elif any(date_dict.get(f"{cal}_century") for cal in ["hijri", "gregorian", "julian"]):
        return "century"
    else:
        return "year"


def create_calendar_system_key(systems: List[str]) -> str:
    """Create the key for calendar system combination"""
    return "_".join(sorted(systems))


def fill_missing_values(date_values: Dict) -> Dict:
    """Fill missing values with empty strings for formatting"""
    def fill_dict(d: Dict) -> Dict:
        return {k: v if v is not None else "" for k, v in d.items()}

    return {
        "date": fill_dict(date_values["date"]),
        "date_end": fill_dict(date_values.get("date_end", {}))
    }


def format_date_string(date_values: Dict, precision: str, calendar_key: str) -> str:
    """Format the date string using the appropriate template"""
    template = STANDARD_DATE_FORMAT.get(precision, {}).get(calendar_key, "")
    if not template:
        return ""

    # Flatten the date values for formatting
    format_values = {**date_values["date"], **date_values["date_end"]}
    filled_values = {k: v if v else "" for k, v in format_values.items()}

    try:
        return template.format(**filled_values).strip()
    except KeyError:
        return ""


def format_parsed_date(regex_match: Any, date_structure: Dict) -> str:
    """
    Main function to format a parsed date

    Args:
        regex_match: The regex match object
        date_structure: Dictionary with date field mappings to regex group numbers

    Returns:
        Formatted date string
    """
    # Pipeline of transformations
    pipeline = [
        lambda x: build_date_values(x[0], x[1]),
        lambda x: (x, detect_calendar_systems(x)),
        lambda x: (x[0], x[1], determine_date_precision(x[0])),
        lambda x: (fill_missing_values(x[0]), x[1], x[2]),
        lambda x: format_date_string(x[0], x[2], create_calendar_system_key(x[1]))
    ]

    return reduce(lambda acc, func: func(acc), pipeline, (regex_match, date_structure))


# Example usage and test cases
def test_date_formatting():
    """Test the date formatting functionality"""

    # Mock regex match object
    class MockMatch:
        def __init__(self, groups):
            self.groups = groups

        def group(self, num):
            return self.groups.get(num, None)

    # Test case 1: Simple Hijri year
    test_structure_1 = {
        "date": {
            "hijri_year": 1,
            "hijri_era": 2,
            "weekday": None,
            "day": None,
            "month": None,
            "year": None,
            "century": None,
            "era": None,
            "calendar": None
        }
    }

    mock_match_1 = MockMatch({1: "1445", 2: "هـ"})
    result_1 = format_parsed_date(mock_match_1, test_structure_1)
    print(f"Test 1 - Hijri year: {result_1}")

    # Test case 2: Gregorian and Hijri combined
    test_structure_2 = {
        "date": {
            "hijri_year": 1,
            "hijri_era": 2,
            "gregorian_year": 3,
            "gregorian_era": 4,
            "weekday": None,
            "day": None,
            "month": None,
            "year": None,
            "century": None,
            "era": None,
            "calendar": None
        }
    }

    mock_match_2 = MockMatch({1: "1445", 2: "هـ", 3: "2023", 4: "م"})
    result_2 = format_parsed_date(mock_match_2, test_structure_2)
    print(f"Test 2 - Hijri-Gregorian year: {result_2}")

    # Test case 3: Full date with weekday
    test_structure_3 = {
        "date": {
            "weekday": 1,
            "hijri_day": 2,
            "hijri_month": 3,
            "hijri_year": 4,
            "hijri_era": 5,
            "day": None,
            "month": None,
            "year": None,
            "century": None,
            "era": None,
            "calendar": None
        }
    }

    mock_match_3 = MockMatch({1: "الجمعة", 2: "15", 3: "رمضان", 4: "1445", 5: "هـ"})
    result_3 = format_parsed_date(mock_match_3, test_structure_3)
    print(f"Test 3 - Full date with weekday: {result_3}")


if __name__ == "__main__":
    test_date_formatting()



def has_values(date_dict: Dict) -> bool:
    """Check if date dictionary has any non-None values"""
    return any(value is not None for value in date_dict.values())

def get_match_value(match, idxs):
    if idxs:
        if isinstance(idxs, int):
            return match.group(idxs)
        elif isinstance(idxs, list):
            for idx in idxs:
                if match.group(idx):
                    return match.group(idx)

Edit
This function extracts date component values from a regex match object. Here's what it does:

Purpose: Returns the first non-empty captured group from a regex match, given either a single index or a list of indices to check.

Parameters:

match: A regex match object (from re.search(), re.match(), etc.)
idxs: Either an integer (single group index) or a list of integers (multiple group indices to try)
Logic:

If idxs is an integer, it directly returns the captured group at that index
If idxs is a list, it iterates through the indices and returns the first non-empty group it finds
If idxs is falsy (None, empty list, etc.), it returns None implicitly
Potential issues:

No explicit return value when idxs is a list but no groups match (returns None)
No error handling for invalid indices that might cause IndexError
No handling for when match is None
Example usage:

python
import re
pattern = r'(\d{4})-(\d{2})-(\d{2})|(\d{2})/(\d{2})/(\d{4})'
match = re.search(pattern, '2023-12-25')
year = get_match_value(match, [1, 6])  # Try group 1, then 6
Would you like me to suggest improvements or explain any specific part in more detail?





yes

Edit
Here are some improvements I'd suggest for the function:


Improved get_match_value function
Code
Key improvements made:

Error Handling: Added proper exception handling for IndexError when indices are out of range, and TypeError for invalid input types.
None Check: Added check for when match is None (no regex match found).
Documentation: Added comprehensive docstring explaining parameters, return value, and exceptions.
Type Validation: Validates that list elements are integers and that idxs is the correct type.
Clearer Logic: Made the logic more explicit with better variable names and comments.
Test Cases: Included example usage and test cases to demonstrate functionality.
Better Return Logic: More explicit about when None is returned.
Alternative simplified version if you prefer less verbose error handling:

python
def get_match_value(match, idxs):
    if not match or not idxs:
        return None

    if isinstance(idxs, int):
        return match.group(idxs) if idxs <= (match.lastindex or 0) else None

    if isinstance(idxs, list):
        for idx in idxs:
            if isinstance(idx, int) and idx <= (match.lastindex or 0):
                if match.group(idx):
                    return match.group(idx)

    return None
Which approach do you prefer - the robust version with detailed error handling, or the simpler version that fails gracefully?







# ===================================================================================
#
# ===================================================================================
def get_match_value(match, idxs):
    """
    Extract date component values from a regex match object.

    Args:
        match: A regex match object (or None if no match found)
        idxs: Either an integer (single group index) or a list of integers
              (multiple group indices to try in order)

    Returns:
        str: The first non-empty captured group value found, or None if no match

    Raises:
        IndexError: If any index in idxs is out of range for the match groups
        TypeError: If idxs is not an int, list, or None
    """
    # Handle None match (no regex match found)
    if match is None:
        return None

    # Handle None or empty idxs
    if not idxs:
        return None

    # Handle single integer index
    if isinstance(idxs, int):
        try:
            return match.group(idxs)
        except IndexError:
            raise IndexError(f"Group index {idxs} is out of range. Match has {match.lastindex or 0} groups.")

    # Handle list of indices
    elif isinstance(idxs, list):
        if not idxs:  # Empty list
            return None

        for idx in idxs:
            if not isinstance(idx, int):
                raise TypeError(f"All indices must be integers, got {type(idx).__name__}")

            try:
                group_value = match.group(idx)
                if group_value:  # Return first non-empty group
                    return group_value
            except IndexError:
                raise IndexError(f"Group index {idx} is out of range. Match has {match.lastindex or 0} groups.")

        # If we get here, all groups were None/empty
        return None

    else:
        raise TypeError(f"idxs must be int, list, or None, got {type(idxs).__name__}")

# ===================================================================================
#
# ===================================================================================


# Example usage and test cases
if __name__ == "__main__":
    import re

    # Test with different date formats
    patterns = [
        (r'(\d{4})-(\d{2})-(\d{2})', '2023-12-25'),  # ISO format
        (r'(\d{2})/(\d{2})/(\d{4})', '12/25/2023'),  # US format
        (r'(\d{1,2})\s+(\w+)\s+(\d{4})', '25 December 2023'),  # Written format
    ]

    for pattern, date_str in patterns:
        match = re.search(pattern, date_str)
        print(f"Date: {date_str}")
        print(f"  Year: {get_match_value(match, [1, 3])}")
        print(f"  Month: {get_match_value(match, [2])}")
        print(f"  Day: {get_match_value(match, [3, 1])}")
        print()

    # Test error cases
    try:
        match = re.search(r'(\d+)', '123')
        result = get_match_value(match, 5)  # Index out of range
    except IndexError as e:
        print(f"Expected error: {e}")

    try:
        result = get_match_value(match, "invalid")  # Wrong type
    except TypeError as e:
        print(f"Expected error: {e}")

match_component = {
    "date": {
        "weekday": None, "day": None, "month": None, "year": None,
        "century": None, "era": None, "calendar": None
        },
    "date_end": {
        "weekday": None, "day": None, "month": None, "year": None,
        "century": None, "era": None, "calendar": None
        },
    "date1": {
        "weekday": None, "day": None, "month": None, "year": None,
        "century": None, "era": None, "calendar": None
        },
    "date1_end": {
        "weekday": None, "day": None, "month": None, "year": None,
        "century": None, "era": None, "calendar": None
        }
}


def normalize_date_output(match_component:dict):
    n_match_component = {}
    for key, value in match_component.items():
        # n_match_component[key]
        if key =


match_component = {
        "weekday": None, "day": None, "month": None, "year": None,
        "century": None, "era": None, "calendar": None
        }

import math

def get_century_from_year(year):
    """
    Calculate century from year. Same calculation for all calendars, only formatting differs.

    Args:
        year (str/int): The year value

    Returns:
        tuple: (century_number, formatted_string) or (None, None) if year is invalid
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

    return century, formatted

def get_ordinal_suffix(number):
    """
    Add ordinal suffix to number (1st, 2nd, 3rd, etc.)
    """
    # Special case: numbers ending in 11, 12, 13 always use 'th'
    # (11th, 12th, 13th - not 11st, 12nd, 13rd)
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        # Use the last digit to determine suffix
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

    return f"{number}{suffix}"

def normalize_date_output(match_component: dict, lang="ar"):
    """
    Normalize date components for different languages and calendar systems.

    Args:
        match_component (dict): Dictionary containing date components
        lang (str): Language code (default: "ar")

    Returns:
        dict: Normalized date components
    """
    # Initialize normalized components - start fresh
    n_match_component = {}
    calendar = ""
    force_calendar = False

    # Helper function to safely strip strings - handles None and non-strings gracefully
    def safe_strip(value):
        return value.strip() if isinstance(value, str) and value is not None else value

    # Process each component - handle both flat and nested structures
    # Some date parsers return nested dicts, others return flat structures
    for key, value in match_component.items():
        if isinstance(value, dict):
            # Nested structure - recursively process sub-components
            n_match_component[key] = {}
            for sub_key, sub_value in value.items():
                n_match_component[key][sub_key] = safe_strip(sub_value)
        else:
            # Flat structure - initialize as needed for normalization functions
            n_match_component[key] = safe_strip(value)

    # Extract calendar if specified - could be empty string, None, or actual calendar name
    calendar = match_component.get("calendar", "") or ""

    # Process era and extract calendar information
    # Era processing might give us calendar info (e.g., "AD" implies Gregorian)
    if match_component.get("era"):
        try:
            n_era, n_calendar = normalize_era(
                era=match_component.get("era", ""),
                lang=lang
            )
            n_match_component["era"] = n_era
            # Update calendar if not already set and normalization provides one
            if not calendar and n_calendar:
                calendar = n_calendar
        except (NameError, TypeError) as e:
            # Handle case where normalize_era function is not defined
            # Graceful degradation - just use the raw era value
            n_match_component["era"] = safe_strip(match_component.get("era"))

    # Process month - this might also give us calendar information
    # Different calendars have different month names/numbers
    if match_component.get("month"):
        try:
            n_month, meta = normalize_month(
                month=match_component.get("month", ""),
                lang=lang,
                calendar=calendar,
                force_calendar=force_calendar
            )
            n_match_component["month"] = n_month
            # Update calendar from metadata if available
            # Month names can help identify calendar system
            if meta.get("n_calendar") and not calendar:
                calendar = meta.get("n_calendar", "")
        except (NameError, TypeError) as e:
            # Fallback to raw month value if normalization fails
            n_match_component["month"] = safe_strip(match_component.get("month"))

    # Process weekday - similar to month processing
    if match_component.get("weekday"):
        try:
            n_weekday, meta = normalize_weekday(
                weekday=match_component.get("weekday", ""),
                lang=lang
            )
            n_match_component["weekday"] = n_weekday
            # Update calendar from metadata if available
            if meta.get("n_calendar") and not calendar:
                calendar = meta.get("n_calendar", "")
        except (NameError, TypeError) as e:
            # Fallback to raw weekday value
            n_match_component["weekday"] = safe_strip(match_component.get("weekday"))

    # Process simple components (day, year) - these don't need special normalization
    # Just clean them up and pass them through
    for component in ["day", "year"]:
        value = match_component.get(component)
        n_match_component[component] = safe_strip(value) if value is not None else None

    # Auto-calculate century if we have a year but no explicit century
    # Century calculation is universal across calendar systems
    if (not match_component.get("century")) and match_component.get("year"):
        n_match_component["century"] = get_century_from_year(match_component.get("year"))[0]

    # Set final calendar - this gets passed along for downstream processing
    n_match_component["calendar"] = calendar

    return n_match_component




def get_standard_date(regex_match: dict):
    if not regex_match or isinstance(regex_match, dict):
        return None

    n_match_component = {}
    for key, value in match_component.items():
        # n_match_component[key]



    match_type = "0"
    start_date = regex_out.get("date", {})
    if has_values(start_date):
        match_type = "1"
    else:
        return None

    end_date = regex_out.get("date_end", {})
    if has_values(start_date):
        match_type = "2"

    start_date1 = regex_out.get("date1", {})
    if has_values(start_date):
        match_type = "3"

    end_date1 = regex_out.get("date1_end", {})
    if has_values(start_date):
        match_type = "3"

    empty_start_date = all(value is None for value in start_date.values())
    empty_end_date = all(value is None for value in end_date.values())
    if empty_start_date and empty_end_date:
        return ""
    elif  (not empty_start_date) and (not empty_end_date):
        # mixed / range / mixed - range
                                                                                                                                                                                                                                                                                                                                           