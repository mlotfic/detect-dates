
"""
Created on Sun Jun 22 21:38:38 2025

@author: m
"""

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def remove_date_duplicates(dict_list):
    """
    Remove duplicate dictionaries where date ranges are within ±1 day of each other.
    Keeps the first occurrence and removes subsequent duplicates.
    """
    if not dict_list:
        return []

    result = []

    for current_dict in dict_list:
        is_duplicate = False

        for existing_dict in result:
            # Helper function to safely convert to int, return None if conversion fails
            def safe_int(value):
                if value is None:
                    return None
                try:
                    return int(value)
                except (ValueError, TypeError):
                    return None

            # Convert all date values safely
            current_hijri_end = safe_int(current_dict.get("hijri_end"))
            existing_hijri_end = safe_int(existing_dict.get("hijri_end"))
            current_hijri_start = safe_int(current_dict.get("hijri_start"))
            existing_hijri_start = safe_int(existing_dict.get("hijri_start"))
            current_gregorian_start = safe_int(current_dict.get("gregorian_start"))
            existing_gregorian_start = safe_int(existing_dict.get("gregorian_start"))
            current_gregorian_end = safe_int(current_dict.get("gregorian_end"))
            existing_gregorian_end = safe_int(existing_dict.get("gregorian_end"))

            # Check if all date fields are within ±1 day of each other
            # Skip comparison if any value is None
            hijri_end_match = (
                current_hijri_end is not None and existing_hijri_end is not None and
                abs(current_hijri_end - existing_hijri_end) <= 1
            )
            hijri_start_match = (
                current_hijri_start is not None and existing_hijri_start is not None and
                abs(current_hijri_start - existing_hijri_start) <= 1
            )
            gregorian_start_match = (
                current_gregorian_start is not None and existing_gregorian_start is not None and
                abs(current_gregorian_start - existing_gregorian_start) <= 1
            )
            gregorian_end_match = (
                current_gregorian_end is not None and existing_gregorian_end is not None and
                abs(current_gregorian_end - existing_gregorian_end) <= 1
            )

            # If all conditions are met, it's a duplicate
            if hijri_end_match and hijri_start_match and gregorian_start_match and gregorian_end_match:
                is_duplicate = True
                break

        # Only add if it's not a duplicate
        if not is_duplicate:
            result.append(current_dict)

   return result