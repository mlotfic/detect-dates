#!/usr/bin/env python3
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.
'''



# ===================================================================================
# DATE COMPONENT KEYWORDS
# Linguistic indicators for different parts of dates
# ===================================================================================

# Year indicators - words that typically precede or follow year numbers
year_keywords_ar = [
    "سنة", "عام", "في عام", "في سنة", "خلال عام", "خلال سنة",
    "في السنة", "خلال السنة", "في العام", "خلال العام",
    "في هذه السنة", "خلال هذه السنة", "في هذا العام", "خلال هذا العام",
    "سال",  # Persian loanword commonly used in Arabic
    "عام الـ", "السنة الـ", "سنة الـ"  # Added common prefixes
]

year_keywords_en = [
    "year", "in year", "during year", "in the year", "during the year",
    "this year", "that year", "the year", "year of", "the year of",
    "in", "during", "by year"  # Added common English patterns
]

# Day and month indicators - contextual words
day_indicators_keywords = [
    "يوم", "اليوم", "اليوم الموافق", "في يوم", "بيوم", "يوم الـ"
]
month_indicators_keywords = [
    "شهر", "الشهر", "الشهر الموافق", "في شهر", "بشهر", "شهر الـ"
]

# Century indicators - for historical date ranges
century_keywords_ar = ["القرن", "في القرن", "خلال القرن", "قرن", "القرن الـ"]
century_keywords_en = ["century", "in century", "during century", "the century", "century of"]

date_indicators_keywords = [
    # ===================================================================================
    # YEAR INDICATORS - Keywords that signal year references
    # ===================================================================================
    {
        "name": "year_indicators_arabic_standard",
        "keywords": year_keywords_ar,
        "description": "Standard Arabic keywords indicating a year reference",
        "examples": [
            "في عام 2023",           # In the year 2023
            "سنة 1445",             # Year 1445
            "خلال العام 2024",       # During the year 2024
            "السنة الهجرية 1445",    # The Hijri year 1445
            "هذا العام 2023",        # This year 2023
            "عام الألفين وثلاثة"     # Year two thousand and three
        ],
        "language": "ar",
        "priority": 100,
        "component": "year_indicator",
        "calendar": "numeric"  # Lowercase for consistency
    },

    {
        "name": "year_indicators_english_standard",
        "keywords": year_keywords_en,
        "description": "Standard English keywords indicating a year reference",
        "examples": [
            "in year 2023",
            "the year 1445",
            "during 2024",
            "year of 2023",
            "in the year 2024"
        ],
        "language": "en",
        "priority": 100,
        "component": "year_indicator",
        "calendar": "numeric"
    },

    # ===================================================================================
    # CENTURY INDICATORS - Keywords that signal century references
    # ===================================================================================
    {
        "name": "century_indicators_arabic_standard",
        "keywords": century_keywords_ar,
        "description": "Standard Arabic keywords indicating a century reference",
        "examples": [
            "القرن 13 هجري",         # 13th century Hijri
            "القرن الحادي عشر",      # 11th century
            "في القرن العشرين",      # In the 20th century
            "خلال القرن التاسع",     # During the 9th century
            "قرن من الزمان"         # A century of time
        ],
        "language": "ar",
        "priority": 100,
        "component": "century_indicator",
        "calendar": "numeric"
    },

    {
        "name": "century_indicators_english_standard",
        "keywords": century_keywords_en,
        "description": "Standard English keywords indicating a century reference",
        "examples": [
            "in the 20th century",
            "during 15th century",
            "the century of",
            "21st century CE"
        ],
        "language": "en",
        "priority": 100,
        "component": "century_indicator",
        "calendar": "numeric"
    },

    # ===================================================================================
    # DAY INDICATORS - Keywords that signal day references
    # ===================================================================================
    {
        "name": "day_indicators_arabic_standard",
        "keywords": day_indicators_keywords,
        "description": "Standard Arabic keywords indicating a day reference",
        "examples": [
            "يوم 1",                # Day 1
            "اليوم الموافق 5",       # The day corresponding to 5
            "في يوم",               # On day
            "يوم الجمعة",           # Friday (day of Friday)
            "هذا اليوم"             # This day
        ],
        "language": "ar",
        "priority": 100,
        "component": "day_indicator",
        "calendar": "numeric"
    },

    # ===================================================================================
    # MONTH INDICATORS - Keywords that signal month references
    # ===================================================================================
    {
        "name": "month_indicators_arabic_standard",
        "keywords": month_indicators_keywords,
        "description": "Standard Arabic keywords indicating a month reference",
        "examples": [
            "شهر 1",                # Month 1
            "الشهر الموافق 5",       # The month corresponding to 5
            "في شهر",               # In month
            "شهر رمضان",            # Month of Ramadan
            "هذا الشهر"             # This month
        ],
        "language": "ar",
        "priority": 100,
        "component": "month_indicator",
        "calendar": "numeric"
    },
]


# ===================================================================================
# DATE SEPARATORS AND CONNECTORS
# ===================================================================================
# Punctuation and linguistic connectors used in date expressions
punctuation_separators = [
    # Punctuation separators
    "/", "-", ".", " ", ":", "\\", "|", "–", "—", "=", "_", ",", ";",
    # Universal punctuation separators
    "~", "→", "←", ">>", "<<"
]

# Arabic date connectors
connectors_separators_ar = [
    # Arabic date connectors
    "الموافق", "موافق", "الموافق لـ", "- الموافق",

    # Arabic range indicators
    "إلى", "حتى", "وحتى", "لغاية", "إلى غاية",

    # Arabic starting point indicators
    "من", "منذ", "ابتداء من", "بداية من", "اعتبارا من",
]

# English date connectors
connectors_separators_en = [
    "corresponding to", "equiv.", "equivalent to", "matching", "equal to"
]

# Arabic range connectors
range_connectors_ar = [
    "-", "–", "—", "/", ":", "~",
    "الى", "إلى", "حتى", "وحتى", "لغاية", "إلى غاية"]
# English range connectors
range_connectors_en = [
    "-", "–", "—", "/", ":", "~",
    "to", "until", "through", "thru", "till", "up to",
    "up until", "through to", "and", "&", "between", "from"
]

# Arabic range starters
range_starters_ar = [
    "من", "منذ", "ابتداء من", "بداية من", "اعتبارا من", "اعتباراً من"
]
# English range starters
range_starters_en = [
    "from", "since", "starting from", "beginning from", "as of", "as from",
    "commencing", "starting", "beginning", "from the", "since the"
]

# Arabic approximation indicators
approximation_ar = [
    "حوالي", "نحو", "تقريباً", "تقريبا", "قريب من", "حول", "في حدود", "قرابة", "نحو"
]

# English approximation indicators
approximation_en = [
    "about", "around", "approximately", "circa", "ca.", "c.", "roughly",
    "near", "nearly", "close to", "some", "somewhere around", "in the region of",
    "in the vicinity of", "more or less", "give or take", "thereabouts"
]

# Arabic temporal indicators
temporal_ar = [
    "قبل", "بعد", "منذ", "حتى", "عند", "في", "خلال", "أثناء"
]

# English temporal indicators
temporal_en = [
    "before", "after", "since", "until", "at", "in", "during", "while",
    "throughout", "within", "by", "on", "over", "across", "through",
    "amid", "amidst", "for", "upon", "under"
]

separators_indicators_keywords = [
    # ===================================================================================
    # SEPARATOR INDICATORS - Punctuation and connectors
    # ===================================================================================
    {
        "name": "date_separators_standard_ar",
        "keywords": punctuation_separators,
        "description": "Standard separators and connectors used in date expressions",
        "examples": [
            "2023/12/25",           # Slash separator
            "من 2020 إلى 2023",     # Range with Arabic connectors
            "1445-01-15",           # Dash separator
            "الموافق 25 ديسمبر"     # Arabic date connector
        ],
        "language": "ar",        # Both Arabic and universal symbols
        "priority": 50,            # Lower priority than specific indicators
        "component": "separator_indicator",
        "calendar": "universal"
    },
    {
        "name": "date_separators_standard_en",
        "keywords": punctuation_separators,
        "description": "Standard separators and connectors used in date expressions",
        "examples": [
            "2023/12/25",           # Slash separator
            "من 2020 إلى 2023",     # Range with Arabic connectors
            "1445-01-15",           # Dash separator
            "الموافق 25 ديسمبر"     # Arabic date connector
        ],
        "language": "en",        # Both Arabic and universal symbols
        "priority": 50,            # Lower priority than specific indicators
        "component": "separator_indicator",
        "calendar": "universal"
    },
    {
        "name": "connectors_separators_ar",
        "keywords": connectors_separators_ar,
        "description": "Standard separators and connectors used in date expressions",
        "examples": [

        ],
        "language": "ar",        # Both Arabic and universal symbols
        "priority": 50,            # Lower priority than specific indicators
        "component": "separator_indicator",
        "calendar": "universal"
    },
    {
        "name": "connectors_separators_en",
        "keywords": connectors_separators_en,
        "description": "Standard separators and connectors used in date expressions",
        "examples": [

        ],
        "language": "en",        # Both Arabic and universal symbols
        "priority": 50,            # Lower priority than specific indicators
        "component": "separator_indicator",
        "calendar": "universal"
    },

    # ===================================================================================
    # RANGE CONNECTORS - For date ranges
    # ===================================================================================
    {
        "name": "range_connectors_arabic",
        "keywords": range_connectors_ar,
        "description": "Arabic connectors used for date ranges",
        "examples": [
            "من 2020 إلى 2023",     # From 2020 to 2023
            "1445 - 1446",          # 1445 - 1446
            "حتى عام 2025"          # Until year 2025
        ],
        "language": "ar",
        "priority": 80,
        "component": "range_connector_indicator",
        "calendar": "universal"
    },

    {
        "name": "range_connectors_english",
        "keywords": range_connectors_en,
        "description": "English connectors used for date ranges",
        "examples": [
            "from 2020 to 2023",    # From 2020 to 2023
            "1445 - 1446",          # 1445 - 1446
            "until year 2025",      # Until year 2025
            "2020 through 2023",    # 2020 through 2023
            "between 1990 and 2000" # Between 1990 and 2000
        ],
        "language": "en",
        "priority": 80,
        "component": "range_connector_indicator",
        "calendar": "universal"
    },

    # ===================================================================================
    # RANGE STARTERS - Beginning of date ranges
    # ===================================================================================
    {
        "name": "range_starters_arabic",
        "keywords": range_starters_ar,
        "description": "Arabic indicators for the start of date ranges",
        "examples": [
            "من عام 2020",          # From year 2020
            "منذ 1445",             # Since 1445
            "ابتداء من شهر مارس"    # Starting from March
        ],
        "language": "ar",
        "priority": 80,
        "component": "range_starter_indicator",
        "calendar": "universal"
    },

    {
        "name": "range_starters_english",
        "keywords": range_starters_en,
        "description": "English indicators for the start of date ranges",
        "examples": [
            "from year 2020",       # From year 2020
            "since 1445",           # Since 1445
            "starting from March",  # Starting from March
            "beginning from 2020",  # Beginning from 2020
            "as of January 2023"    # As of January 2023
        ],
        "language": "en",
        "priority": 80,
        "component": "range_starter_indicator",
        "calendar": "universal"
    },

    # ===================================================================================
    # APPROXIMATION INDICATORS - For approximate dates
    # ===================================================================================
    {
        "name": "approximation_indicators_arabic",
        "keywords": approximation_ar,
        "description": "Arabic indicators for approximate dates",
        "examples": [
            "حوالي عام 2020",        # Around year 2020
            "تقريباً في 1445",      # Approximately in 1445
            "نحو القرن العاشر"      # Around the 10th century
        ],
        "language": "ar",
        "priority": 70,
        "component": "approximation_indicator",
        "calendar": "universal"
    },

    {
        "name": "approximation_indicators_english",
        "keywords": approximation_en,
        "description": "English indicators for approximate dates",
        "examples": [
            "around year 2020",     # Around year 2020
            "circa 1445",           # Circa 1445
            "about the 10th century", # About the 10th century
            "roughly in 2023",      # Roughly in 2023
            "somewhere around 1990" # Somewhere around 1990
        ],
        "language": "en",
        "priority": 70,
        "component": "approximation_indicator",
        "calendar": "universal"
    },

    # ===================================================================================
    # TEMPORAL INDICATORS - General temporal references
    # ===================================================================================
    {
        "name": "temporal_indicators_arabic",
        "keywords": temporal_ar,
        "description": "Arabic temporal indicators for date context",
        "examples": [
            "قبل عام 2020",          # Before year 2020
            "بعد 1445",             # After 1445
            "خلال شهر رمضان"        # During Ramadan month
        ],
        "language": "ar",
        "priority": 60,
        "component": "temporal_indicator",
        "calendar": "universal"
    },

    {
        "name": "temporal_indicators_english",
        "keywords": temporal_en,
        "description": "English temporal indicators for date context",
        "examples": [
            "before year 2020",     # Before year 2020
            "after 1445",           # After 1445
            "during March",         # During March
            "throughout 2023",      # Throughout 2023
            "within the year 2024"  # Within the year 2024
        ],
        "language": "en",
        "priority": 60,
        "component": "temporal_indicator",
        "calendar": "universal"
    }
]

# ===================================================================================
# STRUCTURED INDICATORS DATA
# ===================================================================================
indicators_keywords = date_indicators_keywords + separators_indicators_keywords