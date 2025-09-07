
"""
Era Keywords Configuration Module for Date Normalization

Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

This module provides comprehensive configuration for normalizing date components across
different languages and calendar systems. It handles era detection for Hijri, Gregorian,
and Persian/Solar Hijri calendars in both Arabic and English scripts.

The module supports:
- Hijri calendar (Islamic lunar calendar): AH/BAH eras
- Gregorian calendar (Western solar calendar): CE/BCE eras  
- Persian/Solar Hijri calendar (Iranian solar calendar): SH/BSH eras

Keywords are organized by calendar system, era type (before/after), and language/script
to enable accurate date parsing and normalization across different cultural contexts.
"""

# ===================================================================================
# ERA STANDARD KEYWORDS - Quick reference mappings
# ===================================================================================

era_standard_keywords = {
    # Standard normalized representations for different era types.
    # This dictionary provides the canonical short forms used after normalization
    # for each supported calendar system and language combination.
    
    # Gregorian calendar - Arabic variations
    "after_hijrah_ar": "هـ",        # After Hijrah (Arabic)
    "before_hijrah_ar": "ق.هـ",     # Before Hijrah (Arabic) 
    "after_christ_ar": "م",         # After Christ/Common Era (Arabic)
    "before_christ_ar": "ق.م",      # Before Christ (Arabic)
    "after_Jalali_ar": "هـ.ش",      # After Solar Hijrah (Persian in Arabic script)
    "before_Jalali_ar": "ق.هـ.ش",   # Before Solar Hijrah (Persian in Arabic script)
    
    # Gregorian calendar - English variations
    "after_hijrah_en": "AH",        # After Hijrah (English)
    "before_hijrah_en": "BH",       # Before Hijrah (English)
    "after_christ_en": "AD",        # Anno Domini (English)
    "before_christ_en": "BC",       # Before Christ (English)
    "after_Jalali_en": "SH",        # Solar Hijri (English)
    "before_Jalali_en": "BSH"       # Before Solar Hijri (English)
}

# ===================================================================================
# ERA KEYWORDS DICTIONARY - Hierarchical keyword organization
# ===================================================================================

era_keywords_dict = {
    # Comprehensive dictionary of era keywords organized by language, calendar, and era type.
    #
    # Structure:
    # {
    #     "language_code": {
    #         "calendar_system": {
    #             "era_type": {
    #                 "name": "unique_identifier",
    #                 "description": "human_readable_description",
    #                 "keywords": ["list", "of", "variations"], 
    #                 "normalized": "standard_form"
    #             }
    #         }
    #     }
    # }
    #
    # This structure allows for efficient lookup and expansion of era detection capabilities.
    
    "ar": {  # Arabic script keywords
        "hijri": {
            "after_hijrah": {
                "name": "hijri_after_hijrah_arabic_standard",
                "description": "Keywords indicating Hijri era after Hijrah in Arabic",
                "keywords": [
                    # Standard Hijri indicators
                    "هجري", "هجرية", "هـ", "هــ", "هـــ", "ه", 
                    # Explicit "after Hijrah" phrases
                    "بعد الهجرة", "بعد الهجره", "بعد هجري", "بعد هجرت", 
                    "بعد هجري قمري", "بعد هجرت",
                    # Year forms
                    "السنة الهجرية", "سنة هجرية", "هجري", "هجره", "هجرية",
                    # Prepositional forms  
                    "بالهجري", "بالهجرية", "للهجرة", "هجری", "هجري قمري", 
                    "الهجري", "من الهجرة", "من الهجره", "من هجري"
                ],
                "normalized": "هـ"
            },
            "before_hijrah": {
                "name": "hijri_before_hijrah_arabic_standard", 
                "description": "Keywords indicating Hijri era before Hijrah in Arabic",
                "keywords": [
                    # Short forms with "before" indicators
                    "قبل هـ", "قبل هــ", "قبل هـــ", "قبل ه", 
                    "ق هـ", "ق هــ", "ق هـــ", "ق ه",
                    # Explicit "before Hijrah" phrases
                    "قبل الهجرة", "قبل الهجره", "قبل هجري", "قبل هجرت",
                    "قبل هجري قمري", "قبل هجرت", 
                    # Year forms with "before" qualifier
                    "السنة الهجرية قبل", "سنة هجرية قبل"
                ],
                "normalized": "ق.هـ"
            }
        },
        "gregorian": {
            "after_christ": {
                "name": "gregorian_after_christ_arabic_standard",
                "description": "Keywords indicating Gregorian era after Christ in Arabic",
                "keywords": [
                    # Standard Gregorian/Christian indicators
                    "ميلاديًا", "ميلاديً", "السنة الميلادية", "سنة ميلادية",
                    "ميلادية", "ميلادي", "بالميلادي", "بالميلادية", "للميلاد",
                    # Christian era variants
                    "المسيحية", "المسيحي", "الإفرنجية", "الإفرنجي",
                    "الغربية", "الغربي",
                    # Short forms and abbreviations
                    "مــ", "مـــ", "مـ", "م",
                    # Explicit "after birth" phrases  
                    "بعد الميلاد", "بعد م", "بعد الميلادي", 
                    "بعد مـ", "بعد مــ", "بعد مـــ", "الميلادي"
                ],
                "normalized": "م"
            },
            "before_christ": {
                "name": "gregorian_before_christ_arabic_standard", 
                "description": "Keywords indicating Gregorian era before Christ in Arabic",
                "keywords": [
                    # Explicit "before" with various forms
                    "قبل ميلاديًا", "قبل ميلاديً", "قبل الميلاد", "قبل م",
                    "قبل الميلادي", "قبل مـ", "قبل مــ", "قبل مـــ",
                    # Before Christian era variants
                    "قبل المسيحية", "قبل المسيحي", "قبل الإفرنجية", "قبل الإفرنجي",
                    "قبل الغربية", "قبل الغربي", 
                    # Abbreviated forms
                    "ق.م", "ق م", "ق.مـ", "ق مـ", "ق.مــ", "ق مــ", "ق.مـــ"
                ],
                "normalized": "ق.م"
            }
        },
        "Jalali": {  # Persian/Solar Hijri in Arabic script
            "after_hijrah": {
                "name": "Jalali_after_hijrah_persian_arabic_script",
                "description": "Keywords indicating Solar Hijri era after Hijrah in Persian/Arabic script",
                "keywords": [
                    # Solar/Persian year indicators
                    "السنة الشمسية", "سنة شمسية", "شمسي",
                    "بالهجري الشمسي", "بالهجرية الشمسي", "للهجرة الشمسية",
                    # Standard abbreviations
                    "هـ.ش", "هجرية شمسية", "ه‍.ش", "هجري شمسي", "هجری شمسی",
                    # Explicit "after" forms
                    "بعد هجري شمسي", "بعد هجرت خورشيدي", "بعد هجرت",
                    # Short forms
                    "ش", "شمسية", "شمسية هجري"
                ],
                "normalized": "هـ.ش"
            },
            "before_hijrah": {
                "name": "Jalali_before_hijrah_persian_arabic_script",
                "description": "Keywords indicating Solar Hijri era before Hijrah in Persian/Arabic script", 
                "keywords": [
                    # "Before" + solar indicators
                    "قبل السنة الشمسية", "قبل سنة شمسية", "قبل شمسي",
                    "قبل الهجري الشمسي", "قبل الهجرية الشمسي", "قبل للهجرة الشمسية",
                    # Abbreviated "before" forms
                    "ق.هـ.ش", "ق ه.ش", "ق هجرية شمسية", 
                    "قبل هجرت خورشيدي", "قبل هجري شمسي"
                ],
                "normalized": "ق.هـ.ش"
            }
        }
    },
    "en": {  # English keywords
        "hijri": {
            "after_hijrah": {
                "name": "hijri_after_hijrah_english_standard",
                "description": "Keywords indicating Hijri era after Hijrah in English",
                "keywords": [
                    # Standard abbreviations
                    "AH", "H", "Hijri",
                    # Latin forms
                    "Anno Hegirae", 
                    # English phrases
                    "After Hijrah", "After Hijra", "After Hijri", 
                    "After Hegira", "After Hegiri"
                ],
                "normalized": "AH"
            },
            "before_hijrah": {
                "name": "hijri_before_hijrah_english_standard",
                "description": "Keywords indicating Hijri era before Hijrah in English", 
                "keywords": [
                    # Standard abbreviations
                    "BAH", "BH",
                    # Full forms with "before" 
                    "before Anno Hegirae", "before Hijrah", "before Hijra",
                    "before Hijri", "before Hegira", "before Hegiri"
                ],
                "normalized": "BAH"  # Note: Original had "BAH" but structure suggests "BH"
            }
        },
        "gregorian": {
            "after_christ": {
                "name": "gregorian_after_christ_english_standard",
                "description": "Keywords indicating Gregorian era after Christ in English",
                "keywords": [
                    # Standard abbreviations (secular and religious)
                    "AD", "CE", "AC", "A.D.", "C.E.", "A.C.", 
                    # Full forms
                    "Anno Domini", "Common Era", "Anno Christiani", 
                    "Christian Era", "Christian"
                ],
                "normalized": "CE"  # Using secular standard
            },
            "before_christ": {
                "name": "gregorian_before_christ_english_standard",
                "description": "Keywords indicating Gregorian era before Christ in English",
                "keywords": [
                    # Standard abbreviations
                    "BC", "BCE", "B.C.", "B.C.E.", "B.CE", "B.C.E.", "B.C.E",
                    # Full forms
                    "Before Christ", "Before Common Era", 
                    "Before Christian Era", "Before Christian"
                ],
                "normalized": "BCE"  # Using secular standard
            }
        },
        "Jalali": {  # Persian/Solar Hijri in English script
            "after_hijrah": {
                "name": "Jalali_after_hijrah_persian_english_script",
                "description": "Keywords indicating Solar Hijri era after Hijrah in Persian/English script",
                "keywords": [
                    # Standard abbreviations
                    "SH", "S.H.", "AP", "Solar",
                    # Full forms
                    "Solar Hijri", "Anno Persico", "Jalali", "Persian",
                    # Explicit "after" forms
                    "After Solar Hijri", "After Hegira Jalali"
                ],
                "normalized": "SH"
            },
            "before_hijrah": {
                "name": "Jalali_before_hijrah_persian_english_script",
                "description": "Keywords indicating Solar Hijri era before Hijrah in Persian/English script",
                "keywords": [
                    # Standard abbreviations
                    "BSH", "B.SH", "B.S.H.", "B.P.", "B.Persian",
                    # Full "before" forms
                    "Before Solar Hijri", "Before Jalali", "Before Anno Persico",
                    "Before Hegira Jalali", "Before Persian"
                ],
                "normalized": "BSH"
            }
        }
    }
}

# ===================================================================================
# ERA KEYWORDS - Flattened configuration for processing
# ===================================================================================

era_keywords = [
    # Flattened list of era keyword configurations for efficient processing.
    #
    # Each entry contains:
    # - name: Unique identifier for the keyword set
    # - keywords: List of keyword variations to match
    # - normalized: Standard form after normalization
    # - description: Human-readable description
    # - examples: Sample usage patterns
    # - language: Language/script identifier
    # - priority: Processing priority (higher = checked first)
    # - era: Standard era abbreviation
    # - calendar: Calendar system name
    #
    # This structure enables linear processing while maintaining rich metadata.
    
    # ===============================================================================
    # HIJRI CALENDAR KEYWORDS
    # ===============================================================================
    {
        "name": "hijri_after_hijrah_arabic_standard",
        "keywords": era_keywords_dict["ar"]["hijri"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["hijri"]["after_hijrah"]["normalized"], 
        "description": "Keywords indicating Hijri era after Hijrah in Arabic",
        "examples": [
            "1445 هـ",           # Standard short form
            "1445 هجري",        # Common long form
            "السنة الهجرية 1445", # Formal year reference
            "بعد الهجرة 1445",   # Explicit "after Hijrah"
            "1445 هجري قمري"    # Lunar Hijri specification
        ],
        "language": "ar",
        "priority": 100,
        "era": "AH", 
        "calendar": "Hijri"
    },
    {
        "name": "hijri_after_hijrah_english_standard",
        "keywords": era_keywords_dict["en"]["hijri"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["hijri"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era after Hijrah in English", 
        "examples": [
            "1445 AH",              # Standard abbreviation
            "1445 After Hijra",     # Common English form
            "1445 Anno Hegirae",    # Latin scholarly form
            "1445 Hijri",           # Simple adjective form
            "After Hijrah 1445"     # Prefix form
        ],
        "language": "en",
        "priority": 100,
        "era": "AH",
        "calendar": "Hijri"
    },
    {
        "name": "hijri_before_hijrah_arabic_standard",
        "keywords": era_keywords_dict["ar"]["hijri"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["hijri"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era before Hijrah in Arabic",
        "examples": [
            "10 ق.هـ",          # Standard abbreviated form
            "5 قبل الهجرة",     # Full "before Hijrah" phrase
            "قبل هـ 15",        # Prefix form
            "قبل هجري 8",       # "Before Hijri" form
            "ق هـ 22"           # Spaced abbreviation
        ],
        "language": "ar", 
        "priority": 100,
        "era": "BAH",
        "calendar": "Hijri"
    },
    {
        "name": "hijri_before_hijrah_english_standard",
        "keywords": era_keywords_dict["en"]["hijri"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["hijri"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era before Hijrah in English",
        "examples": [
            "10 BAH",             # Before After Hijrah abbreviation
            "5 before Hijrah",    # Simple English form  
            "before Hijra 15",    # Prefix form
            "BAH 8",              # Abbreviation prefix
            "BH 22"               # Short abbreviation
        ],
        "language": "en",
        "priority": 100, 
        "era": "BAH",
        "calendar": "Hijri"
    },
    
    # ===============================================================================
    # GREGORIAN CALENDAR KEYWORDS  
    # ===============================================================================
    {
        "name": "gregorian_after_christ_arabic_standard",
        "keywords": era_keywords_dict["ar"]["gregorian"]["after_christ"]["keywords"],
        "normalized": era_keywords_dict["ar"]["gregorian"]["after_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era after Christ in Arabic",
        "examples": [
            "2023 م",              # Standard short form
            "2023 ميلادي",         # Common adjective form
            "السنة الميلادية 2023", # Formal year reference
            "بالميلادي 2023",       # Prepositional form
            "2023 بعد الميلاد"      # Explicit "after birth"
        ],
        "language": "ar",
        "priority": 100,
        "era": "CE", 
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_after_christ_english_standard", 
        "keywords": era_keywords_dict["en"]["gregorian"]["after_christ"]["keywords"],
        "normalized": era_keywords_dict["en"]["gregorian"]["after_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era after Christ in English",
        "examples": [
            "2023 CE",            # Common Era (secular)
            "2023 AD",            # Anno Domini (religious)
            "Anno Domini 2023",   # Full Latin form
            "Common Era 2023",    # Full secular form  
            "2023 A.D."           # Abbreviated with periods
        ],
        "language": "en",
        "priority": 100,
        "era": "CE",
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_before_christ_arabic_standard",
        "keywords": era_keywords_dict["ar"]["gregorian"]["before_christ"]["keywords"], 
        "normalized": era_keywords_dict["ar"]["gregorian"]["before_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era before Christ in Arabic",
        "examples": [
            "100 ق.م",           # Standard abbreviated form
            "50 قبل الميلاد",     # Full "before birth" phrase
            "ق م 75",            # Spaced abbreviation
            "قبل الميلادي 200",   # "Before Christian" form
            "ق.مـ 150"           # Extended letter form
        ],
        "language": "ar",
        "priority": 100,
        "era": "BC", 
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_before_christ_english_standard",
        "keywords": era_keywords_dict["en"]["gregorian"]["before_christ"]["keywords"],
        "normalized": era_keywords_dict["en"]["gregorian"]["before_christ"]["normalized"], 
        "description": "Keywords indicating Gregorian era before Christ in English",
        "examples": [
            "100 BCE",                # Before Common Era (secular)
            "50 BC",                  # Before Christ (religious)
            "Before Christ 75",       # Full prefix form
            "B.C. 200",              # Abbreviated with periods
            "Before Common Era 150"   # Full secular form
        ],
        "language": "en",
        "priority": 100,
        "era": "BC",
        "calendar": "Gregorian"
    },
    
    # ===============================================================================  
    # PERSIAN/SOLAR HIJRI CALENDAR KEYWORDS
    # ===============================================================================
    {
        "name": "Jalali_after_hijrah_persian_arabic_script", 
        "keywords": era_keywords_dict["ar"]["Jalali"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["Jalali"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating Solar Hijri era after Hijrah in Persian/Arabic script",
        "examples": [
            "1402 هـ.ش",             # Standard Solar Hijri form
            "1402 شمسي",            # "Solar" adjective  
            "السنة الشمسية 1402",   # "The solar year"
            "بالهجري الشمسي 1402",  # "In solar Hijri"
            "1402 هجري شمسي"       # "Hijri solar" form
        ],
        "language": "persian_ar",  # Persian in Arabic script
        "priority": 100,
        "era": "SH",
        "calendar": "Jalali"  # Persian/Solar Hijri uses Jalali naming
    },
    {
        "name": "Jalali_after_hijrah_persian_english_script",
        "keywords": era_keywords_dict["en"]["Jalali"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["Jalali"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating Solar Hijri era after Hijrah in Persian/English script", 
        "examples": [
            "1402 SH",              # Standard Solar Hijri abbreviation
            "1402 Solar Hijri",     # Full descriptive form
            "Jalali 1402",          # Persian calendar name
            "Persian 1402",         # National identifier
            "1402 S.H."            # Abbreviated with periods
        ],
        "language": "persian_en",  # Persian in English script
        "priority": 100,
        "era": "SH", 
        "calendar": "Jalali"
    },
    {
        "name": "Jalali_before_hijrah_persian_arabic_script",
        "keywords": era_keywords_dict["ar"]["Jalali"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["Jalali"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Solar Hijri era before Hijrah in Persian/Arabic script",
        "examples": [
            "10 ق.هـ.ش",            # Before Solar Hijri abbreviation
            "5 قبل شمسي",           # "Before solar" form
            "قبل السنة الشمسية 15", # "Before the solar year"
            "ق هـ.ش 8",            # Spaced abbreviation
            "قبل هجري شمسي 22"     # "Before solar Hijri"
        ],
        "language": "persian_ar",
        "priority": 100,
        "era": "BSH",
        "calendar": "Jalali"
    },
    {
        "name": "Jalali_before_hijrah_persian_english_script",
        "keywords": era_keywords_dict["en"]["Jalali"]["before_hijrah"]["keywords"], 
        "normalized": era_keywords_dict["en"]["Jalali"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Solar Hijri era before Hijrah in Persian/English script",
        "examples": [
            "10 BSH",               # Before Solar Hijri abbreviation
            "5 Before Solar Hijri", # Full descriptive form
            "Before Jalali 15",     # Persian calendar name with prefix  
            "B.SH 8",              # Abbreviated with periods
            "Before Persian 22"     # National identifier with prefix
        ],
        "language": "persian_en", 
        "priority": 100,
        "era": "BSH",
        "calendar": "Jalali"
    }
]