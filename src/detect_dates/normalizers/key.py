def normalize_key(input_key: str):
    """
    Detect calendar type and language from input key.

    Args:
        input_key (str): The input key indicating calendar type and language

    Returns:
        tuple: (calendar_type, language) or (None, None) if no match found
    """
    # Define supported calendar types with their language variants
    supported_calendar_types = [
        "gregorian_ar", "hijri_ar", "persian_ar",
        "gregorian_en", "hijri_en", "persian_en"
    ]

    # Check each calendar type to find a match
    for calendar_type in supported_calendar_types:
        if input_key.startswith(calendar_type):
            language = "ar" if calendar_type.endswith("ar") else "en"
            return calendar_type, language

    # Return None values if no match is found
   return None, None