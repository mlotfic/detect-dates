
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
    print("This module is not intended to be run directly. Import it in your code.")
    setup_src_path()

from .keywords_to_regex import keywords_to_regex

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_era_pattern(data, lang: str = "ar", calendar: str = None) -> str:
    """Generate regex pattern for era keywords.

    Args:
        data: List of data configurations, each containing language, calendar, and keywords
        lang: Language code to filter by (default: "ar" for Arabic, also supports "en")
        calendar: Optional calendar type to filter by (e.g., "hijri", "gregorian")

    Returns:
        str: Regex pattern string that matches era keywords, or empty string if language unsupported
    """

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        # Skip if language specified and doesn't match (exact or suffix match)
        if lang and not data_config["language"].endswith(lang):
            continue
        # Skip if calendar specified and doesn't match
        if calendar and data_config["calendar"] != calendar:
            continue
        matching_keywords.extend(data_config["keywords"])

    return keywords_to_regex(matching_keywords)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_month_pattern(data, lang: str = "ar", calendar: str = None) -> str:
    """Generate regex pattern for month keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "month":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        if calendar and data_config["calendar"] != calendar:
            continue
        # Collect keywords for the specified calendar
        matching_keywords.extend(data_config["keywords"])

    return keywords_to_regex(matching_keywords)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
# data = weekdays_keywords
def get_day_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for day keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "day":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return keywords_to_regex(matching_keywords)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
# data = numeric_words_keywords
def get_numeric_words_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for numeric_words keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "numeric_words":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return keywords_to_regex(matching_keywords)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_year_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "year":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return keywords_to_regex(matching_keywords)

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_year_indicator_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "year_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for year indicator keywords


# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_day_indicator_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "day_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):

            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for day indicator keywords

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_month_indicator_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "month_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for month indicator keywords

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_separator_pattern(data, lang: str = "ar") -> str:
    """"""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "separator_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for separator keywords

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_range_connector_pattern(data, lang: str = "ar") -> str:
    """"""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "range_connector_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for range connector keywords

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def get_range_starter_pattern(data, lang: str = "ar") -> str:
    """"""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "range_starter_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):
            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for range starter keywords

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
# data = indicators_keywords
def get_century_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "century_indicator":
            continue
        if lang and not data_config["language"].endswith(lang):

            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for century keywords


# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
# data = numeric_words_keywords
def get_numeric_words_pattern(data, lang: str = "ar") -> str:
    """Generate regex pattern for year keywords."""

    # Initialize list to collect matching keywords from filtered data configurations
    matching_keywords = []

    # Validate language support - Arabic, English, and Persian variants are currently supported
    if lang not in ["ar", "en", "persian_ar", "persian_en"]:
        print(f"The Language [{lang}] specified not supported...")
        return r''  # Return empty regex pattern for unsupported languages

    for data_config in data:
        if data_config["component"] != "numeric_words":
            continue
        if lang and not data_config["language"].endswith(lang):

            continue
        matching_keywords.extend(data_config["keywords"])

    return rf"(?:{keywords_to_regex(matching_keywords)})"  # Return regex pattern for century keywords


                                                                                                                                                                                                                         