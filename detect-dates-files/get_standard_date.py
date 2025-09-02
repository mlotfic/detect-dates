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


def has_values(date_dict: Dict) -> bool:
    """Check if date dictionary has any non-None values"""
    return any(value is not None for value in date_dict.values())


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


"date": {
            "weekday": None, "day": None, "month": None, "year": None,
            "century": None, "era": None, "calendar": None
        },
        "date_end": {
            "weekday": None, "day": None, "month": None, "year": None,
            "century": None, "era": None, "calendar": None
        },
        
def get_standard_date(regex_out):
    start_date = regex_out.get("date", {})
    end_date = regex_out.get("date_end", {})
    empty_start_date = all(value is None for value in start_date.values())
    empty_end_date = all(value is None for value in end_date.values())
    if empty_start_date and empty_end_date:
        return ""
    elif  (not empty_start_date) and (not empty_end_date):
        # mixed / range / mixed - range
 