# -- -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize date components for different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing components like year, month, day, era, and weekday.
"""

# ===================================================================================
# ERA KEYWORDS CONFIGURATION
# Support for different historical epochs across multiple languages and scripts
# ===================================================================================
era_keywords_dict = {
    "ar": {
        "hijri": {
            "after_hijrah": {
                "name": "hijri_after_hijrah_arabic_standard",
                "description": "Keywords indicating Hijri era after Hijrah in Arabic",
                "keywords": [
                    "هجري", "هجرية", "هـ", "هــ", "هـــ", "ه", "بعد الهجرة", "بعد الهجره", 
                    "بعد هجري", "بعد هجرت", "بعد هجري قمري", "بعد هجرت", "السنة الهجرية", 
                    "سنة هجرية", "هجري", "هجره", "هجرية", "بالهجري", "بالهجرية", "للهجرة", 
                    "هجری", "هجري قمري", "الهجري", "من الهجرة", "من الهجره", "من هجري",
                ],
                "normalized": "هـ"
            },
            "before_hijrah": {
                "name": "hijri_before_hijrah_arabic_standard",
                "description": "Keywords indicating Hijri era before Hijrah in Arabic",
                "keywords": [                    
                    "قبل هـ", "قبل هــ", "قبل هـــ", "قبل ه", "ق هـ", "ق هــ", "ق هـــ", 
                    "ق ه", "قبل الهجرة", "قبل الهجره", "قبل هجري", "قبل هجرت", 
                    "قبل هجري قمري", "قبل هجرت", "السنة الهجرية قبل", "سنة هجرية قبل",
                ],
                "normalized": "ق.هـ"
            }
        },
        "gregorian": {
            "after_christ": {
                "name": "gregorian_after_christ_arabic_standard",
                "description": "Keywords indicating Gregorian era after Christ in Arabic",
                "keywords": [
                    "ميلاديًا", "ميلاديً", "السنة الميلادية", "سنة ميلادية", 
                    "ميلادية", "ميلادي", "بالميلادي", "بالميلادية", 
                    "للميلاد", "المسيحية", "المسيحي", "الإفرنجية", 
                    "الإفرنجي", "الغربية", "الغربي", "مــ", "مـــ", 
                    "مـ", "م", "بعد الميلاد", "بعد م", 
                    "بعد الميلادي", "بعد مـ", "بعد مــ", "بعد مـــ", "الميلادي"
                ],
                "normalized": "م"
            },
            "before_christ": {
                "name": "gregorian_before_christ_arabic_standard",
                "description": "Keywords indicating Gregorian era before Christ in Arabic",
                "keywords": [
                    "قبل ميلاديًا", "قبل ميلاديً",  # Fixed: Added missing diacritics variants
                    "قبل الميلاد", "قبل م", "قبل الميلادي", "قبل مـ", "قبل مــ", "قبل مـــ", 
                    "قبل المسيحية", "قبل المسيحي", "قبل الإفرنجية", "قبل الإفرنجي", 
                    "قبل الغربية", "قبل الغربي", "ق.م", "ق م", "ق.مـ", "ق مـ", 
                    "ق.مــ", "ق مــ", "ق.مـــ"
                ],
                "normalized": "ق.م"
            }
        },
        "julian": {
            "after_hijrah": {
                "name": "julian_after_hijrah_persian_arabic_script",
                "description": "Keywords indicating julian era after Hijrah in Persian/Arabic script",
                "keywords": [
                    "السنة الشمسية", "سنة شمسية", "شمسي", 
                    "بالهجري الشمسي", "بالهجرية الشمسي", 
                    "للهجرة الشمسية", "هـ.ش", "هجرية شمسية", 
                    "بعد هجري شمسي", "بعد هجرت خورشيدي", 
                    "بعد هجرت", "ه‍.ش", "هجري شمسي", 
                    "هجری شمسی", "ش", "شمسية", "شمسية هجري"
                ],
                "normalized": "هـ.ش"
            },
            "before_hijrah": {
                "name": "julian_before_hijrah_persian_arabic_script",
                "description": "Keywords indicating julian era before Hijrah in Persian/Arabic script",
                "keywords": [
                    "قبل السنة الشمسية", "قبل سنة شمسية", 
                    "قبل شمسي", "قبل الهجري الشمسي", 
                    "قبل الهجرية الشمسي", 
                    "قبل للهجرة الشمسية", 
                    "ق.هـ.ش", "ق ه.ش", 
                    "ق هجرية شمسية", 
                    "قبل هجرت خورشيدي", 
                    "قبل هجري شمسي"
                ],
                "normalized": "ق.هـ.ش"
            }
        }
    },
    "en": { 
        "hijri": {
            "after_hijrah": {
                "name": "hijri_after_hijrah_english_standard",
                "description": "Keywords indicating Hijri era after Hijrah in English",
                "keywords": [
                    "AH", "Anno Hegirae", "After Hijrah", "After Hijra", "After Hijri", 
                    "After Hegira", "After Hegiri", "H", "Hijri"
                ],
                "normalized": "AH"
            },
            "before_hijrah": {
                "name": "hijri_before_hijrah_english_standard",
                "description": "Keywords indicating Hijri era before Hijrah in English",
                "keywords": [
                    "BAH", "before Anno Hegirae", "before Hijrah", 
                    "before Hijra", "before Hijri", "before Hegira", 
                    "before Hegiri", "BH"
                ],
                "normalized": "BAH"
            }
        },
        "gregorian": {
            "after_christ": {
                "name": "gregorian_after_christ_english_standard",
                "description": "Keywords indicating Gregorian era after Christ in English",
                "keywords": [
                    "AD", "CE", "Anno Domini", "Common Era", 
                    "Anno Christiani", "Christian Era", "AC", 
                    "A.D.", "C.E.", "A.C.", "Christian"
                ],
                "normalized": "CE"
            },
            "before_christ": {
                "name": "gregorian_before_christ_english_standard",
                "description": "Keywords indicating Gregorian era before Christ in English",
                "keywords": [
                    "BC", "BCE", "Before Christ", 
                    "Before Common Era", "Before Christian Era", 
                    "B.C.", "B.C.E.", "B.CE", "B.C.E.", "B.C.E", "Before Christian"
                ],
                "normalized": "BCE"
            }
        },
        "julian": {
            "after_hijrah": {
                "name": "julian_after_hijrah_persian_english_script",
                "description": "Keywords indicating julian era after Hijrah in Persian/English script",
                "keywords": [
                    "SH", "Solar Hijri", "Anno Persico", 
                    "Jalali", "After Solar Hijri", 
                    "After Hegira julian", "Persian", "AP", "S.H.", "Solar"
                ],
                "normalized": "SH"
            },
            "before_hijrah": {
                "name": "julian_before_hijrah_persian_english_script",
                "description": "Keywords indicating julian era before Hijrah in Persian/English script",
                "keywords": [
                    "BSH", "Before Solar Hijri", 
                    "Before Jalali", "Before Anno Persico", 
                    "Before Hegira julian", "B.SH", 
                    "Before Persian", "B.P.", "B.Persian", "B.S.H."
                ],
                "normalized": "BSH"
            }
        }
    }
}


# ===================================================================================
# ERA CONFIGURATION - Structured configuration for era detection
# ===================================================================================
era_keywords = [
    {
        "name": "hijri_after_hijrah_arabic_standard",  # Original: era_hijri_after_hijrah_ar
        "keywords": era_keywords_dict["ar"]["hijri"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["hijri"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era after Hijrah in Arabic",
        "examples": [  # Original: example (single string)
            "1445 هـ",
            "1445 هجري", 
            "السنة الهجرية 1445",
            "بعد الهجرة 1445",
            "1445 هجري قمري"
        ],
        "language": "ar",
        "priority": 100,
        "era": "AH",
        "calendar": "Hijri"
    },
    {
        "name": "hijri_after_hijrah_english_standard",  # Original: era_hijri_after_hijrah_en
        "keywords": era_keywords_dict["en"]["hijri"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["hijri"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era after Hijrah in English",
        "examples": [  # Original: example (single string)
            "1445 AH",
            "1445 After Hijra",
            "1445 Anno Hegirae",
            "1445 Hijri",
            "After Hijrah 1445"
        ],
        "language": "en",
        "priority": 100,
        "era": "AH",
        "calendar": "Hijri"
    },
    {
        "name": "hijri_before_hijrah_arabic_standard",  # Original: era_hijri_before_hijrah_ar
        "keywords": era_keywords_dict["ar"]["hijri"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["hijri"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era before Hijrah in Arabic",
        "examples": [  # Original: example (single string)
            "10 ق.هـ",
            "5 قبل الهجرة",
            "قبل هـ 15",
            "قبل هجري 8",
            "ق هـ 22"
        ],
        "language": "ar",
        "priority": 100,
        "era": "BAH",
        "calendar": "Hijri"
    },
    {
        "name": "hijri_before_hijrah_english_standard",  # Original: era_hijri_before_hijrah_en
        "keywords": era_keywords_dict["en"]["hijri"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["hijri"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating Hijri era before Hijrah in English",
        "examples": [  # Original: example (single string)
            "10 BAH",
            "5 before Hijrah",
            "before Hijra 15",
            "BAH 8",
            "BH 22"
        ],
        "language": "en",
        "priority": 100,
        "era": "BAH",
        "calendar": "Hijri"
    },
    {
        "name": "gregorian_after_christ_arabic_standard",  # Original: era_gregorian_after_christ_ar
        "keywords": era_keywords_dict["ar"]["gregorian"]["after_christ"]["keywords"],
        "normalized": era_keywords_dict["ar"]["gregorian"]["after_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era after Christ in Arabic",
        "examples": [  # Original: example (single string)
            "2023 م",
            "2023 ميلادي",
            "السنة الميلادية 2023",
            "بالميلادي 2023",
            "2023 بعد الميلاد"
        ],
        "language": "ar",
        "priority": 100,
        "era": "CE",
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_after_christ_english_standard",  # Original: era_gregorian_after_christ_en
        "keywords": era_keywords_dict["en"]["gregorian"]["after_christ"]["keywords"],
        "normalized": era_keywords_dict["en"]["gregorian"]["after_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era after Christ in English",
        "examples": [  # Original: example (single string)
            "2023 CE",
            "2023 AD",
            "Anno Domini 2023",
            "Common Era 2023",
            "2023 A.D."
        ],
        "language": "en",
        "priority": 100,
        "era": "CE",
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_before_christ_arabic_standard",  # Original: era_gregorian_before_christ_ar
        "keywords": era_keywords_dict["ar"]["gregorian"]["before_christ"]["keywords"],
        "normalized": era_keywords_dict["ar"]["gregorian"]["before_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era before Christ in Arabic",
        "examples": [  # Original: example (single string)
            "100 ق.م",
            "50 قبل الميلاد",
            "ق م 75",
            "قبل الميلادي 200",
            "ق.مـ 150"
        ],
        "language": "ar",
        "priority": 100,
        "era": "BC",
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_before_christ_english_standard",  # Original: era_gregorian_before_christ_en
        "keywords": era_keywords_dict["en"]["gregorian"]["before_christ"]["keywords"],
        "normalized": era_keywords_dict["en"]["gregorian"]["before_christ"]["normalized"],
        "description": "Keywords indicating Gregorian era before Christ in English",
        "examples": [  # Original: example (single string)
            "100 BCE",
            "50 BC",
            "Before Christ 75",
            "B.C. 200",
            "Before Common Era 150"
        ],
        "language": "en",
        "priority": 100,
        "era": "BC",
        "calendar": "Gregorian"
    },
    {
        "name": "julian_after_hijrah_persian_arabic_script",  # Original: era_after_julian_ar
        "keywords": era_keywords_dict["ar"]["julian"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["julian"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating julian era after Hijrah in Persian/Arabic script",
        "examples": [  # Original: example (single string)
            "1402 هـ.ش",
            "1402 شمسي",
            "السنة الشمسية 1402",
            "بالهجري الشمسي 1402",
            "1402 هجري شمسي"
        ],
        "language": "persian_ar",
        "priority": 100,
        "era": "SH",
        "calendar": "julian"
    },
    {
        "name": "julian_after_hijrah_persian_english_script",  # Original: era_after_julian_en
        "keywords": era_keywords_dict["en"]["julian"]["after_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["julian"]["after_hijrah"]["normalized"],
        "description": "Keywords indicating julian era after Hijrah in Persian/English script",
        "examples": [  # Original: example (single string)
            "1402 SH",
            "1402 Solar Hijri",
            "Jalali 1402",
            "Persian 1402",
            "1402 S.H."
        ],
        "language": "persian_en",
        "priority": 100,
        "era": "SH",
        "calendar": "julian"
    },
    {
        "name": "julian_before_hijrah_persian_arabic_script",  # Original: era_before_julian_ar
        "keywords": era_keywords_dict["ar"]["julian"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["ar"]["julian"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating julian era before Hijrah in Persian/Arabic script",
        "examples": [  # Original: example (single string)
            "10 ق.هـ.ش",
            "5 قبل شمسي",
            "قبل السنة الشمسية 15",
            "ق هـ.ش 8",
            "قبل هجري شمسي 22"
        ],
        "language": "persian_ar",
        "priority": 100,
        "era": "BSH",
        "calendar": "julian"
    },
    {
        "name": "julian_before_hijrah_persian_english_script",  # Original: era_before_julian_en
        "keywords": era_keywords_dict["en"]["julian"]["before_hijrah"]["keywords"],
        "normalized": era_keywords_dict["en"]["julian"]["before_hijrah"]["normalized"],
        "description": "Keywords indicating julian era before Hijrah in Persian/English script",
        "examples": [  # Original: example (single string)
            "10 BSH",
            "5 Before Solar Hijri",
            "Before Jalali 15",
            "B.SH 8",
            "Before Persian 22"
        ],
        "language": "persian_en",
        "priority": 100,
        "era": "BSH",
        "calendar": "julian"
    }
]
