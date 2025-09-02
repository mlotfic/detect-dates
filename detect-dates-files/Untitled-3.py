# ===================================================================================
# DATE PATTERNS
# ===================================================================================

# [ ] ============================================================
m_yr_num_pattern = rf"{NumericPatterns.month}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.year}"
d_m_num_pattern = rf"{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.month}"
d_m_yr_num_pattern = rf"{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.month}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.year}"

# [ ] ============================================================
# Hijri, Gregorian, and julian year patterns (YYYY)
hijri_y_pattern = rf"{NumericPatterns.year}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.hijri}"
hijri_y_pattern_s = rf"{NumericPatterns.year}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.hijri})?"
gregorian_y_pattern = rf"{NumericPatterns.year}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.gregorian}"
gregorian_y_pattern_s = rf"{NumericPatterns.year}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.gregorian})?"
julian_y_pattern = rf"{NumericPatterns.year}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.julian}"
julian_y_pattern_s = rf"{year_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.julian})?"

# [ ] ============================================================
# Hijri, Gregorian, and julian (MM/YYYY) patterns
hijri_m_y_pattern_num = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.hijri}"
gregorian_m_y_pattern_num = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.gregorian}"
julian_m_y_pattern_num = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.julian}"

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (MM/YYYY) patterns with optional era like "1445 هـ" or "2023 م"
hijri_m_y_pattern_num_s = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.hijri})?"
gregorian_m_y_pattern_num_s = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.gregorian})?"
julian_m_y_pattern_num_s = rf"{m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.julian})?"


# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (Month/YYYY) patterns with optional era like "محرم 1445 هـ" or "يناير 2023 م"
hijri_m_y_pattern_name = rf"{MonthPatterns.hijri}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern_s}"
gregorian_m_y_pattern_name = rf"{MonthPatterns.gregorian}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern_s}"
julian_m_y_pattern_name = rf"{MonthPatterns.julian}\s*{IndicatorPatterns.separator}?\s*{julian_y_pattern_s}"



# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (Month/YYYY) patterns [stand alone or with era]
hijri_m_y_pattern = rf"{hijri_m_y_pattern_num}|{hijri_m_y_pattern_name}"
gregorian_m_y_pattern = rf"{julian_m_y_pattern_num}|{gregorian_m_y_pattern_name}"
julian_m_y_pattern = rf"{julian_m_y_pattern_num}|{julian_m_y_pattern_name}"

# Hijri, Gregorian, and julian (Month/YYYY) patterns with optional era [start of range patterns]
hijri_m_y_pattern_s = rf"{hijri_m_y_pattern_num_s}|{hijri_m_y_pattern_name}"
gregorian_m_y_pattern_s = rf"{gregorian_m_y_pattern_num_s}|{gregorian_m_y_pattern_name}"
julian_m_y_pattern_s = rf"{julian_m_y_pattern_num_s}|{julian_m_y_pattern_name}"

# [ ] ============================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns
hijri_d_m_y_pattern_num = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.hijri}"
gregorian_d_m_y_pattern_num = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.gregorian}"
julian_d_m_y_pattern_num = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.julian}"

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era [start of range patterns]
hijri_d_m_y_pattern_num_s = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.hijri})?"
gregorian_d_m_y_pattern_num_s = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.gregorian})?"
julian_d_m_y_pattern_num_s = rf"{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.julian})?"

# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era
hijri_d_m_y_pattern_name = rf"{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.hijri}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern_s}"
gregorian_d_m_y_pattern_name = rf"{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.gregorian}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern_s}"
julian_d_m_y_pattern_name = rf"{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.julian}\s*{IndicatorPatterns.separator}?\s*{julian_y_pattern_s}"


# [ ] ===========================================================================================
# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns [combined with era for numeric and with/without named patterns]
# Natural language date patterns
hijri_d_m_y_pattern = rf"{hijri_d_m_y_pattern_num}|{hijri_d_m_y_pattern_name}"
gregorian_d_m_y_pattern = rf"{gregorian_d_m_y_pattern_num}|{gregorian_d_m_y_pattern_name}"
julian_d_m_y_pattern = rf"{julian_d_m_y_pattern_num}|{julian_d_m_y_pattern_name}"

# Hijri, Gregorian, and julian (DD/MM/YYYY) patterns with optional era [start of range patterns]
hijri_d_m_y_pattern_s = rf"{hijri_d_m_y_pattern_num_s}|{hijri_d_m_y_pattern_name}"
gregorian_d_m_y_pattern_s = rf"{gregorian_d_m_y_pattern_num_s}|{gregorian_d_m_y_pattern_name}"
julian_d_m_y_pattern_s = rf"{julian_d_m_y_pattern_num_s}|{julian_d_m_y_pattern_name}"


# [ ] ============================================================
# Full date patterns with (day DD/MM/YYYY)
natural_hijri_d_m_y_pattern_num = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.hijri}"
natural_gregorian_d_m_y_pattern_num = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.gregorian}"
natural_julian_d_m_y_pattern_num = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*{EraPatterns.julian}"


# Natural language date patterns with (day DD/MM/YYYY) [start of range patterns]
natural_hijri_d_m_y_pattern_num_s = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.hijri})?"
natural_gregorian_d_m_y_pattern_num_s = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.gregorian})?"
natural_julian_d_m_y_pattern_num_s = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{d_m_yr_num_pattern}\s*{IndicatorPatterns.separator}?\s*(?:{EraPatterns.julian})?"

# Natural language date patterns with (day DD/MM/YYYY) [with/without named patterns]
natural_hijri_d_m_y_pattern_name = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.hijri}\s*{IndicatorPatterns.separator}?\s*{hijri_y_pattern_s}"
natural_gregorian_d_m_y_pattern_name = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.gregorian}\s*{IndicatorPatterns.separator}?\s*{gregorian_y_pattern_s}"
natural_julian_d_m_y_pattern_name = rf"{BasePatterns.weekday}\s*{IndicatorPatterns.separator}?\s*{NumericPatterns.day}\s*{IndicatorPatterns.separator}?\s*{MonthPatterns.julian}\s*{IndicatorPatterns.separator}?\s*{julian_y_pattern_s}"

# Natural language date patterns with (day DD/MM/YYYY) [combined with era for numeric and with/without named patterns]
natural_hijri_pattern = rf"{natural_hijri_d_m_y_pattern_num}|{natural_hijri_d_m_y_pattern_name}"
natural_gregorian_pattern = rf"{natural_gregorian_d_m_y_pattern_num}|{natural_gregorian_d_m_y_pattern_name}"
natural_julian_pattern = rf"{natural_julian_d_m_y_pattern_num}|{natural_julian_d_m_y_pattern_name}"

# Natural language date patterns with (day DD/MM/YYYY) [start of range patterns]
natural_hijri_pattern_s = rf"{natural_hijri_d_m_y_pattern_num_s}|{natural_hijri_d_m_y_pattern_name}"
natural_gregorian_pattern_s = rf"({natural_gregorian_d_m_y_pattern_num_s}|{natural_gregorian_d_m_y_pattern_name})"
natural_julian_pattern_s = rf"{natural_julian_d_m_y_pattern_num_s}|{natural_julian_d_m_y_pattern_name}"

# [ ] ============================================================
# Hijri, Gregorian, and julian century patterns
century_pattern = rf"({numeric_words_pattern_ar})"

#  [start of range patterns]
century_pattern_s = rf"({numeric_words_pattern_ar})\s*{century_indicator_pattern}"




# Example of how to instantiate these dataclasses with your variables:
def create_patterns_from_variables():
    """
    Create pattern dataclass instances from your existing variables
    Assuming 'patterns' is your imported patterns module
    """

    # Base patterns (need to be imported from your patterns module)
    base_patterns = BasePatterns(
        weekday=patterns.day_pattern,  # day_pattern from your code
        numeric_words_ar=patterns.numeric_words_pattern_ar  # This should be imported
    )

    # Era patterns
    era_patterns = EraPatterns(
        hijri=patterns.hijri_era_pattern,  # hijri_era_pattern
        gregorian=patterns.gregorian_era_pattern,  # gregorian_era_pattern
        julian=patterns.julian_era_pattern  # julian_era_pattern
    )

    # Month patterns
    month_patterns = MonthPatterns(
        hijri=patterns.hijri_month_pattern,  # hijri_month_pattern
        gregorian=patterns.gregorian_month_pattern,  # gregorian_month_pattern
        julian=patterns.julian_month_pattern  # julian_month_pattern
    )

    # Indicator patterns
    indicator_patterns = IndicatorPatterns(
        day=patterns.day_indicator_pattern,  # day_indicator_pattern
        month=patterns.month_indicator_pattern,  # month_indicator_pattern
        year=patterns.year_indicator_pattern,  # year_indicator_pattern
        century=patterns.century_indicator_pattern,  # century_indicator_pattern
        separator=patterns.separator_pattern,  # separator_pattern
        range_connector=patterns.range_connector_pattern,  # range_connector_pattern
        range_starter=patterns.range_starter_pattern  # range_starter_pattern
    )

    # Numeric patterns (using defaults from dataclass)
    numeric_patterns = NumericPatterns()

    # Compound numeric patterns
    compound_numeric = CompoundNumericPatterns(
        month_year=m_yr_num_pattern,  # m_yr_num_pattern
        day_month=d_m_num_pattern,  # d_m_num_pattern
        day_month_year=d_m_yr_num_pattern  # d_m_yr_num_pattern
    )

    # Year patterns
    year_patterns = YearPatterns(
        hijri=hijri_y_pattern,  # hijri_y_pattern
        hijri_optional=hijri_y_pattern_s,  # hijri_y_pattern_s
        gregorian=gregorian_y_pattern,  # gregorian_y_pattern
        gregorian_optional=gregorian_y_pattern_s,  # gregorian_y_pattern_s
        julian=julian_y_pattern,  # julian_y_pattern
        julian_optional=julian_y_pattern_s  # julian_y_pattern_s
    )

    # Month-Year patterns
    month_year_patterns = MonthYearPatterns(
        hijri_numeric=hijri_m_y_pattern_num,  # hijri_m_y_pattern_num
        hijri_numeric_optional=hijri_m_y_pattern_num_s,  # hijri_m_y_pattern_num_s
        hijri_named=hijri_m_y_pattern_name,  # hijri_m_y_pattern_name
        hijri_combined=hijri_m_y_pattern,  # hijri_m_y_pattern
        hijri_combined_optional=hijri_m_y_pattern_s,  # hijri_m_y_pattern_s

        gregorian_numeric=gregorian_m_y_pattern_num,  # gregorian_m_y_pattern_num
        gregorian_numeric_optional=gregorian_m_y_pattern_num_s,  # gregorian_m_y_pattern_num_s
        gregorian_named=gregorian_m_y_pattern_name,  # gregorian_m_y_pattern_name
        gregorian_combined=gregorian_m_y_pattern,  # gregorian_m_y_pattern
        gregorian_combined_optional=gregorian_m_y_pattern_s,  # gregorian_m_y_pattern_s

        julian_numeric=julian_m_y_pattern_num,  # julian_m_y_pattern_num
        julian_numeric_optional=julian_m_y_pattern_num_s,  # julian_m_y_pattern_num_s
        julian_named=julian_m_y_pattern_name,  # julian_m_y_pattern_name
        julian_combined=julian_m_y_pattern,  # julian_m_y_pattern
        julian_combined_optional=julian_m_y_pattern_s  # julian_m_y_pattern_s
    )

    # Day-Month-Year patterns
    day_month_year_patterns = DayMonthYearPatterns(
        hijri_numeric=hijri_d_m_y_pattern_num,  # hijri_d_m_y_pattern_num
        hijri_numeric_optional=hijri_d_m_y_pattern_num_s,  # hijri_d_m_y_pattern_num_s
        hijri_named=hijri_d_m_y_pattern_name,  # hijri_d_m_y_pattern_name
        hijri_combined=hijri_d_m_y_pattern,  # hijri_d_m_y_pattern
        hijri_combined_optional=hijri_d_m_y_pattern_s,  # hijri_d_m_y_pattern_s

        gregorian_numeric=gregorian_d_m_y_pattern_num,  # gregorian_d_m_y_pattern_num
        gregorian_numeric_optional=gregorian_d_m_y_pattern_num_s,  # gregorian_d_m_y_pattern_num_s
        gregorian_named=gregorian_d_m_y_pattern_name,  # gregorian_d_m_y_pattern_name
        gregorian_combined=gregorian_d_m_y_pattern,  # gregorian_d_m_y_pattern
        gregorian_combined_optional=gregorian_d_m_y_pattern_s,  # gregorian_d_m_y_pattern_s

        julian_numeric=julian_d_m_y_pattern_num,  # julian_d_m_y_pattern_num
        julian_numeric_optional=julian_d_m_y_pattern_num_s,  # julian_d_m_y_pattern_num_s
        julian_named=julian_d_m_y_pattern_name,  # julian_d_m_y_pattern_name
        julian_combined=julian_d_m_y_pattern,  # julian_d_m_y_pattern
        julian_combined_optional=julian_d_m_y_pattern_s  # julian_d_m_y_pattern_s
    )

    # Natural language patterns
    natural_patterns = NaturalLanguagePatterns(
        hijri_numeric=natural_hijri_d_m_y_pattern_num,  # natural_hijri_d_m_y_pattern_num
        hijri_numeric_optional=natural_hijri_d_m_y_pattern_num_s,  # natural_hijri_d_m_y_pattern_num_s
        hijri_named=natural_hijri_d_m_y_pattern_name,  # natural_hijri_d_m_y_pattern_name
        hijri_combined=natural_hijri_pattern,  # natural_hijri_pattern
        hijri_combined_optional=natural_hijri_pattern_s,  # natural_hijri_pattern_s

        gregorian_numeric=natural_gregorian_d_m_y_pattern_num,  # natural_gregorian_d_m_y_pattern_num
        gregorian_numeric_optional=natural_gregorian_d_m_y_pattern_num_s,  # natural_gregorian_d_m_y_pattern_num_s
        gregorian_named=natural_gregorian_d_m_y_pattern_name,  # natural_gregorian_d_m_y_pattern_name
        gregorian_combined=natural_gregorian_pattern,  # natural_gregorian_pattern
        gregorian_combined_optional=natural_gregorian_pattern_s,  # natural_gregorian_pattern_s

        julian_numeric=natural_julian_d_m_y_pattern_num,  # natural_julian_d_m_y_pattern_num
        julian_numeric_optional=natural_julian_d_m_y_pattern_num_s,  # natural_julian_d_m_y_pattern_num_s
        julian_named=natural_julian_d_m_y_pattern_name,  # natural_julian_d_m_y_pattern_name
        julian_combined=natural_julian_pattern,  # natural_julian_pattern
        julian_combined_optional=natural_julian_pattern_s  # natural_julian_pattern_s
    )

    # Century patterns
    century_patterns = CenturyPatterns(
        century=century_pattern,  # century_pattern
        century_with_indicator=century_pattern_s  # century_pattern_s
    )

    return {
        'base': base_patterns,
        'era': era_patterns,
        'month': month_patterns,
        'indicator': indicator_patterns,
        'numeric': numeric_patterns,
        'compound_numeric': compound_numeric,
        'year': year_patterns,
        'month_year': month_year_patterns,
        'day_month_year': day_month_year_patterns,
        'natural': natural_patterns,
        'century': century_patterns
    }

# Usage example:
# all_patterns = create_patterns_from_variables()
# hijri_year = all_patterns['year'].hijri
# gregorian_full_date = all_patterns['day_month_year'].gregorian_combined
                                                                                                   