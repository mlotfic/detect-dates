import math

# Example usage and test cases:
"""
# Century calculation examples:
get_century_from_year(2023) → (21, "21st")
get_century_from_year(1) → (1, "1st")
get_century_from_year(100) → (1, "1st")
get_century_from_year(101) → (2, "2nd")
get_century_from_year("1445") → (15, "15th")  # Islamic calendar year
get_century_from_year(None) → (None, None)

# Ordinal suffix examples:
get_ordinal_suffix(1) → "1st"
get_ordinal_suffix(22) → "22nd"
get_ordinal_suffix(13) → "13th"  # Special case
get_ordinal_suffix(101) → "101st"

# Date normalization examples:
normalize_date_output({"year": "2023", "month": "January"})
→ {"year": "2023", "month": "January", "century": 21, "calendar": ""}

normalize_date_output({"era": "هـ", "year": "1445", "month": "رمضان"}, lang="ar")
→ {"era": "AH", "year": "1445", "month": "Ramadan", "century": 15, "calendar": "islamic"}
"""

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

def normalize_date_output(match_component: dict, lang="ar"):
    """
    Normalize date components for different languages and calendar systems.

    Args:
        match_component (dict): Dictionary containing date components
        lang (str): Language code (default: "ar")

    Returns:
        dict: Normalized date components

    Examples:
        # Simple Gregorian date
        {"year": "2023", "month": "December", "day": "25"}
        → {"year": "2023", "month": "December", "day": "25", "century": 21, "calendar": ""}

        # Arabic Islamic date with era
        {"era": "هـ", "year": "1445", "month": "رمضان", "day": "15"}
        → {"era": "AH", "year": "1445", "month": "Ramadan", "day": "15", "century": 15, "calendar": "islamic"}

        # Nested structure from complex parser
        {"date": {"year": "1400", "month": {"name": "محرم", "number": "1"}}, "calendar": "hijri"}
        → {"date": {"year": "1400", "month": {"name": "Muharram", "number": "1"}}, "century": 14, "calendar": "hijri"}

        # Mixed components with weekday
        {"year": "2024", "month": "March", "weekday": "الجمعة", "day": "15"}
        → {"year": "2024", "month": "March", "weekday": "Friday", "day": "15", "century": 21, "calendar": ""}
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
    # Era processing might give us calendar info (e.g., "AD" implies Gregorian, "هـ" implies Islamic)
    # Examples: "AD"/"CE" → Gregorian, "AH"/"هـ" → Islamic, "BE" → Buddhist
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
    # Examples: "January" → Gregorian, "رمضان" → Islamic, "Tishrei" → Hebrew
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
    # Examples: "الجمعة" → "Friday", "Sunday" → "Sunday", "יום ראשון" → "Sunday"
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

   return n_match_component                                                                                                                                         