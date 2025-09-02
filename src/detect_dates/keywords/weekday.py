#!/usr/bin/env python3
'''
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi
@description: This module provides weekday name extraction and normalization utilities.
'''

# Weekday name extraction system
# Supports multiple languages and transliterations
# Index corresponds to day of week (0=Sunday, 1=Monday, etc.)
# All possible variations for each day (index corresponds to day of week)
weekdays_standard_keywords = {
    "num" : ["01", "02", "03", "04", "05", "06", "07"],
    "weekdays_ar": ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"],
    "weekdays_en": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    "weekdays_en_abbr": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "weekdays_fa_ar" : ["یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه", "شنبه"],
    "weekdays_fa_en" : ["yek-shanbe", "do-shanbe", "se-shanbe", "chahar-shanbe", "panj-shanbe", "jomeh", "shanbe"],
    }

weekdays_variations_list = {
    "num" : ["01", "02", "03", "04", "05", "06", "07"],
    "num1" : ["1", "2", "3", "4", "5", "6", "7"],

    # Arabic variations
    "weekdays_ar": ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"],
    "weekdays_ar_short": ["أحد", "اثنين", "ثلاثاء", "أربعاء", "خميس", "جمعة", "سبت"],

    # English variations
    "weekdays_en": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    "weekdays_en_lower": ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"],
    "weekdays_en_transliteration": ["al-ahad", "al-ithnayn", "al-thulatha", "al-arba", "al-khamis", "al-jumah", "as-sabt"],
    "weekdays_en_transliteration_short": ["ahad", "ithnayn", "thulatha", "arba", "khamis", "jumah", "sabt"],
    "weekdays_en_abbrev": ["sun", "mon", "tue", "wed", "thu", "fri", "sat"],
    "weekdays_en_abbrev2": ["su", "mo", "tu", "we", "th", "fr", "sa"],

    # Farsi variations
    "weekdays_fa_ar": ["یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه"],
    "weekdays_fa_ar_no_zwnj": ["یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه", "شنبه"],
    "weekdays_fa_ar_with_zwnj": ["یک‌شنبه", "دو‌شنبه", "سه‌شنبه", "چهار‌شنبه", "پنج‌شنبه", "جمعه", "شنبه"],

    # Farsi to English transliterations
    "weekdays_fa_en": ["yekshanbe", "doshanbe", "seshanbe", "chaharshanbe", "panjshanbe", "jomeh", "shanbe"],
    "weekdays_fa_en_alt": ["yek-shanbe", "do-shanbe", "se-shanbe", "chahar-shanbe", "panj-shanbe", "jomeh", "shanbe"],
}


# Initialize weekday collections by language
# English weekday variations
weekdays_en = []
# Farsi to English transliterations
weekdays_fa_en = []
# Arabic weekday variations
weekdays_ar = []
# Farsi/Persian weekday variations
weekdays_fa_ar = []

# Process weekday variations and categorize by language
for key, value in weekdays_variations_list.items():
    # Handle English weekday variations
    if key.startswith("weekdays_en"):
        weekdays_en = weekdays_en + weekdays_variations_list[key]

    # Handle Farsi to English transliterations
    elif key.startswith("weekdays_fa_en"):
        weekdays_fa_en = weekdays_fa_en + weekdays_variations_list[key]

    # Handle Arabic weekday variations
    elif key.startswith("weekdays_ar"):
        weekdays_ar = weekdays_ar + weekdays_variations_list[key]

    # Handle Farsi weekday variations (in Arabic script)
    elif key.startswith("weekdays_fa_ar"):
        weekdays_fa_ar = weekdays_fa_ar + weekdays_variations_list[key]

# Remove duplicates using set() - order doesn't matter for weekday name matching
weekdays_en     = list(set(weekdays_en))
weekdays_fa_en  = list(set(weekdays_fa_en))
weekdays_ar     = list(set(weekdays_ar))
weekdays_fa_ar  = list(set(weekdays_fa_ar))

# Complete weekdays keywords structure
weekdays_keywords = [
    # ===================================================================================
    # WEEKDAY NAMES - Full and abbreviated day names in multiple languages
    # ===================================================================================
    {
        "name": "weekday_names_english_full",  # Original: weekdays_en
        "keywords": weekdays_en,
        "description": "English weekday names (full, abbreviated, and transliterated variants)",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",  # Full names
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",  # Abbreviated
            "al-ahad", "al-ithnayn", "al-thulatha", "al-arba'a", "al-khamis", "al-jum'a", "al-sabt"  # Transliterated Arabic
        ],
        "language": "en",
        "priority": 100,  # Highest priority for comprehensive English weekdays
        "component": "day",
        "calendar": "Numeric"  # Weekdays are calendar-independent
    },

    {
        "name": "weekday_names_arabic_standard",  # Original: weekdays_ar
        "keywords": weekdays_ar,
        "description": "Standard Arabic weekday names",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "الأحد",      # Sunday
            "الاثنين",    # Monday
            "الثلاثاء",   # Tuesday
            "الأربعاء",   # Wednesday
            "الخميس",     # Thursday
            "الجمعة",     # Friday
            "السبت"      # Saturday
        ],
        "language": "ar",
        "priority": 100,  # Highest priority for standard Arabic
        "component": "day",
        "calendar": "Numeric"  # Weekdays are calendar-independent
    },

    {
        "name": "weekday_names_persian_arabic_script",  # Original: weekdays_fa_ar
        "keywords": weekdays_fa_ar,
        "description": "Persian weekday names written in Arabic script",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "یکشنبه",     # Sunday
            "دوشنبه",     # Monday
            "سه‌شنبه",     # Tuesday
            "چهارشنبه",   # Wednesday
            "پنج‌شنبه",    # Thursday
            "جمعه",       # Friday
            "شنبه"       # Saturday
        ],
        "language": "persian_ar",
        "priority": 100,  # Highest priority for Persian in Arabic script
        "component": "day",
        "calendar": "Numeric"  # Weekdays are calendar-independent
    },

    {
        "name": "weekday_names_persian_latin_script",  # Original: weekdays_fa_en
        "keywords": weekdays_fa_en,
        "description": "Persian weekday names written in Latin script",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "yekshanbeh",   # Sunday
            "doshanbeh",    # Monday
            "seshhanbeh",   # Tuesday
            "chaharshanbeh", # Wednesday
            "panjshanbeh",  # Thursday
            "jomeh",        # Friday
            "shanbeh"       # Saturday
        ],
        "language": "persian_en",
        "priority": 100,  # Highest priority for Persian in Latin script
        "component": "day",
        "calendar": "Numeric"  # Weekdays are calendar-independent
    },
    {
        "name": "weekdays_ar",
        "keywords": weekdays_ar,
        "normalized": "",
        "description": "Arabic weekday names",
        "examples": [
            "الأحد",  # Sunday
            "الاثنين",  # Monday
            "الثلاثاء",  # Tuesday
            "الأربعاء",  # Wednesday
            "الخميس",  # Thursday
            "الجمعة",  # Friday
            "السبت"   # Saturday
        ],
        "language": "ar",
        "priority": 100,
        "component": "day",
        "calendar": "Gregorian"
    },
    {
        "name": "weekdays_en",
        "keywords": weekdays_en,
        "normalized": "",
        "description": "English weekday names",
        "examples": [
            "monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday",
            "mon", "tue", "wed", "thu", "fri", "sat", "sun"
        ],
        "language": "en",
        "priority": 100,
        "component": "day",
        "calendar": "Gregorian"
    },
    {
        "name": "weekdays_fa_en",
        "keywords": weekdays_fa_en,
        "normalized": "",
        "description": "Persian weekday names in Latin script",
        "examples": [
            "shanbeh", "yekshanbeh", "doshanbeh", "seshhanbeh",
            "chaharshanbeh", "panjshanbeh", "jomeh"
        ],
        "language": "persian_en",
        "priority": 90,
        "component": "day",
        "calendar": "Persian"
    },
    {
        "name": "weekdays_fa_ar",
        "keywords": weekdays_fa_ar,
        "normalized": "",
        "description": "Persian weekday names in Arabic script",
        "examples": [
            "شنبه",      # Saturday
            "یکشنبه",    # Sunday
            "دوشنبه",    # Monday
            "سه‌شنبه",   # Tuesday
            "چهارشنبه",  # Wednesday
            "پنج‌شنبه",  # Thursday
            "جمعه"      # Friday
        ],
        "language": "persian_ar",
        "priority": 95,
        "component": "day",
        "calendar": "Persian"
    }
