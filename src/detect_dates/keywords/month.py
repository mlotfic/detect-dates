# --*- coding: utf-8 -*-
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize date components for different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing components like year, month, day, era, and weekday.
"""

# Standard keywords for month names
# ===================================================================================
months_standard_keywords = {
    # Numeric representations (01-12)
    "num": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        
    # Gregorian calendar - Arabic variations
    "gregorian_ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
    
    # Gregorian calendar - English variations
    "gregorian_en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    
    # Gregorian calendar - English variations Abb
    "gregorian_en_abbr": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],  # Abbreviations
    
    # Hijri/Islamic calendar - Arabic variations
    "hijri_ar": ["محرم", "صفر", "ربيع الأول", "ربيع الآخر", "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
    
    # Hijri/Islamic calendar - English variations
    "hijri_en": ["Muharram", "Safar", "Rabi Al-awwal", "Rabi Al-thani", "Jumada Al-awwal", "Jumada Al-thani", "Rajab", "Shaban", "Ramadan", "Shawwal", "Dhu Al-qadah", "Dhu Al-hijjah"],
    
    # Persian/Jalali calendar - Persian/Farsi variations
    "persian_ar": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
    
    # Persian/Jalali calendar - English transliterations
    "persian_en": ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"],
}
# ===================================================================================
# 
# ===================================================================================
# Comprehensive month name dictionary with multiple spelling variations
months_variations_list = {
        # Numeric representations (1-12 and 01-12)
        "num1": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        "num2": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        
        # Gregorian calendar - Arabic variations
        "gregorian_ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
        "gregorian_ar1": ["يناير", "فبراير", "مارس", "ابريل", "مايو", "يونيو", "يوليو", "اغسطس", "سبتمبر", "اكتوبر", "نوفمبر", "ديسمبر"],
        "gregorian_ar2": ["يناير", "فبراير", "مارس", "ابريل", "مايو", "يونيه", "يوليه", "اغسطس", "سبتمبر", "اكتوبر", "نوفمبر", "ديسمبر"],
        "gregorian_ar3": ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن", "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"],  # Persian-style Arabic
        "gregorian_ar4": ["ژانویه", "فوریه", "مارس", "آپریل", "می", "ژوئن", "ژولای", "آگوست", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"],
        "gregorian_ar5": ["جانفي", "فيفري", "مارس", "أفريل", "ماي", "جوان", "جويلية", "أوت", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],  # Maghrebi Arabic
        
        # Levantine/Syrian calendar (Gregorian with Syriac month names)
        "gregorian_ar_levantine": ["كانون الثاني", "شباط", "آذار", "نيسان", "أيار", "حزيران", "تموز", "آب", "أيلول", "تشرين الأول", "تشرين الثاني", "كانون الأول"],
        "gregorian_ar_levantine1": ["كانون الثاني", "شباط", "اذار", "نيسان", "ايار", "حزيران", "تموز", "آب", "ايلول", "تشرين الاول", "تشرين الثاني", "كانون الاول"],
        "gregorian_ar_levantine2": ["كانون ثاني", "شباط", "اذار", "نيسان", "ايار", "حزيران", "تموز", "آب", "ايلول", "تشرين أول", "تشرين ثاني", "كانون أول"],
        "gregorian_en_levantine": ["kanun al-thani", "shubat", "adhar", "nisan", "ayar", "haziran", "tammuz", "ab", "aylul", "tishrin al-awwal", "tishrin al-thani", "kanun al-awwal"],
        
        
        "gregorian_ar_mixed" : ["يناير/كانون الثاني", "فبراير/شباط", "مارس/آذار", "أبريل/نيسان", "مايو/أيار", "يونيو/حزيران", "يوليو/تموز", "أغسطس/آب", "سبتمبر/أيلول", "أكتوبر/تشرين الأول", "نوفمبر/تشرين الثاني", "ديسمبر/كانون الأول"],
        "gregorian_ar_mixed1" : ["يناير/كانون الثاني", "فبراير/شباط", "مارس/اذار", "ابريل/نيسان", "مايو/ايار", "يونيو/حزيران", "يوليو/تموز", "اغسطس/آب", "سبتمبر/ايلول", "اكتوبر/تشرين الأول", "نوفمبر/تشرين الثاني", "ديسمبر/كانون الأول"],
        "gregorian_ar_mixed2" : ["يناير/كانون الثاني", "فبراير/شباط", "مارس/اذار", "ابريل/نيسان", "مايو/ايار", "يونيو/حزيران", "يوليو/تموز", "اغسطس/آب", "سبتمبر/ايلول", "اكتوبر/تشرين الأول", "نوفمبر/تشرين الثاني", "ديسمبر/كانون الأول"],
        "gregorian_ar_mixed3" : ["يناير/كانون الثاني", "فبراير/شباط", "مارس/اذار", "ابريل/نيسان", "مايو/ايار", "يونيو/حزيران", "يوليو/تموز", "اغسطس/آب", "سبتمبر/ايلول", "اكتوبر/تشرين الأول", "نوفمبر/تشرين الثاني", "ديسمبر/كانون الأول"],
        
        # Gregorian calendar - English variations
        "gregorian_en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "gregorian_en1": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"],
        "gregorian_en2": ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],  # Abbreviations        
        
        # Hijri/Islamic calendar - Arabic variations
        "hijri_ar": ["محرم", "صفر", "ربيع الأول", "ربيع الآخر", "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
        "hijri_ar1": ["محرم", "صفر", "ربيع الاول", "ربيع الثاني", "جمادى الاولى", "جمادى الثانية", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
        "hijri_ar2": ["محرم", "صفر", "ربيع الأول", "ربيع الثاني", "جمادى الأولى", "جمادى الثانية", "رجب", "شعبان", "رمضان", "شوال", "ذي القعدة", "ذي الحجة"],
        "hijri_ar3": ["محرم", "صفر", "ربيع الأول", "ربيع آخر", "جمادى الأولى", "جمادى آخرة", "رجب", "شعبان", "رمضان", "شوال", "ذي القعدة", "ذي الحجة"],
        "hijri_ar4": ["محرم", "صفر", "ربيع الاول", "ربيع الثاني", "جمادى الاولى", "جمادى الثانية", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
        "hijri_ar5": ["محرم", "صفر", "ربيع الاول", "ربيع الآخر", "جمادى الاولى", "جمادى الثانية", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
        "hijri_ar6": ["محرم", "صفر", "ربيع الاول", "ربيع الآخر", "جمادى الاولى", "جمادى الثانية", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"],
        "hijri_ar7": ["محرم", "صفر", "ربیع الاول", "ربیع الثانی", "جمادی الاولی", "جمادی الثانیه", "رجب", "شعبان", "رمضان", "شوال", "ذی القعده", "ذی الحجه"],
        
        # Hijri/Islamic calendar - English variations
        "hijri_en": ["Muharram", "Safar", "Rabi Al-awwal", "Rabi Al-thani", "Jumada Al-awwal", "Jumada Al-thani", "Rajab", "Shaban", "Ramadan", "Shawwal", "Dhu Al-qadah", "Dhu Al-hijjah"],
        "hijri_en1": ["muharram", "safar", "rabi al-awwal", "rabi al-thani", "jumada al-awwal", "jumada al-thani", "rajab", "shaban", "ramadan", "shawwal", "dhu al-qadah", "dhu al-hijjah"],
        "hijri_en2": ["muharram", "safar", "rabi i", "rabi ii", "jumada i", "jumada ii", "rajab", "shaban", "ramadan", "shawwal", "dhu al-qadah", "dhu al-hijjah"],
        "hijri_en3": ["muh", "saf", "rab1", "rab2", "jum1", "jum2", "raj", "sha", "ram", "shaw", "dhiq", "dhih"],  # Abbreviations
        
        # Persian/Jalali calendar - Persian/Farsi variations
        "persian_ar": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
        "persian_ar1": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
        "persian_ar2": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
        
        # Persian/Jalali calendar - English transliterations
        "persian_en": ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"],
        "persian_en1": ["farvardin", "ordibehesht", "khordad", "tir", "mordad", "shahrivar", "mehr", "aban", "azar", "dey", "bahman", "esfand"],
    }


# Initialize calendar system collections
# Gregorian months - Western calendar (365-366 days/year)
months_gregorian_en = []
months_gregorian_ar = []

# Hijri months - Islamic lunar calendar (354-355 days/year, 29-30 days each)
months_hijri_en = []
months_hijri_ar = []

# Persian/julian months - Iranian solar calendar (365-366 days/year, first 6 months 31 days, next 5 months 30 days, last month 29-30 days)
months_julian_en = []
months_julian_ar = []

# Process month name variations and categorize by calendar system
for key, value in months_variations_list.items():    
    # Handle English Gregorian month variations
    if key.startswith("gregorian_en"):
        months_gregorian_en = months_gregorian_en + months_variations_list[key]
        
    # Handle English Hijri month variations
    elif key.startswith("hijri_en"):
        months_hijri_en = months_hijri_en + months_variations_list[key]
        
    # Handle English Persian month variations  
    elif key.startswith("persian_en"):
        months_julian_en = months_julian_en + months_variations_list[key]
        
    # Handle Arabic Gregorian month variations (including Levantine)
    elif key.startswith("gregorian_ar"):
        months_gregorian_ar = months_gregorian_ar + months_variations_list[key]
        
    # Handle Arabic Hijri month variations
    elif key.startswith("hijri_ar"):
        months_hijri_ar = months_hijri_ar + months_variations_list[key]
        
    # Handle Persian/Farsi month variations
    elif key.startswith("persian_ar"):
        months_julian_ar = months_julian_ar + months_variations_list[key]
        
# Remove duplicates using set() - order doesn't matter for month name matching
months_gregorian_en = list(set(months_gregorian_en))
months_gregorian_ar = list(set(months_gregorian_ar))
months_hijri_en = list(set(months_hijri_en))
months_hijri_ar = list(set(months_hijri_ar))
months_julian_en = list(set(months_julian_en))
months_julian_ar = list(set(months_julian_ar))

months_keywords = [
    # ===================================================================================
    # GREGORIAN CALENDAR MONTHS - Multiple language variants
    # ===================================================================================
    {
        "name": "gregorian_months_english_full",  # Original: months_gregorian_en
        "keywords": months_gregorian_en,  
        "description": "Full English Gregorian month names",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ],
        "language": "en",
        "priority": 100,  # Highest priority for English Gregorian months
        "component": "month",
        "calendar": "Gregorian"
    },
    {
        "name": "gregorian_months_arabic_standard",  # Original: months_gregorian_ar
        "keywords": months_gregorian_ar,  
        "description": "Standard Arabic Gregorian month names",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "يناير",      # January
            "فبراير",     # February
            "مارس",       # March
            "أبريل",      # April
            "مايو",       # May
            "يونيو",      # June
            "يوليو",      # July
            "أغسطس",      # August
            "سبتمبر",     # September
            "أكتوبر",     # October
            "نوفمبر",     # November
            "ديسمبر"      # December
        ],
        "language": "ar",
        "priority": 100,  # Highest priority for Arabic Gregorian months
        "component": "month",
        "calendar": "Gregorian"
    },
    
    # ===================================================================================
    # HIJRI CALENDAR MONTHS - Islamic lunar calendar
    # ===================================================================================
    {
        "name": "hijri_months_arabic_standard",  # Original: months_hijri_ar
        "keywords": months_hijri_ar,  
        "description": "Standard Arabic Hijri (Islamic) month names",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "محرم",            # Muharram
            "صفر",             # Safar
            "ربيع الأول",       # Rabi' al-awwal
            "ربيع الثاني",      # Rabi' al-thani
            "جمادى الأولى",     # Jumada al-awwal
            "جمادى الآخرة",     # Jumada al-thani
            "رجب",             # Rajab
            "شعبان",           # Sha'ban
            "رمضان",           # Ramadan
            "شوال",            # Shawwal
            "ذو القعدة",       # Dhu al-Qi'dah
            "ذو الحجة"         # Dhu al-Hijjah
        ],
        "language": "ar",
        "priority": 100,  # Highest priority for Arabic Hijri months
        "component": "month",
        "calendar": "Hijri"
    },
    {
        "name" : "hijri_months_english_standard",
        "keywords": months_hijri_en,  
        "description": "Standard Arabic Hijri (Islamic) month names",
        "examples": [""],
        "language": "en",
        "priority": 100,  # Highest priority for Arabic Hijri months
        "component": "month",
        "calendar": "Hijri"
    },
    
    # ===================================================================================
    # julian/PERSIAN CALENDAR MONTHS - Solar Hijri calendar
    # ===================================================================================
    {
        "name": "julian_months_persian_arabic_script",  # Original: months_julian_ar
        "keywords": months_julian_ar,  
        "description": "Persian Solar Hijri month names in Arabic script",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "فروردین",    # Farvardin
            "اردیبهشت",   # Ordibehesht
            "خرداد",      # Khordad
            "تیر",        # Tir
            "مرداد",      # Mordad
            "شهریور",     # Shahrivar
            "مهر",        # Mehr
            "آبان",       # Aban
            "آذر",        # Azar
            "دی",         # Dey
            "بهمن",       # Bahman
            "اسفند"       # Esfand
        ],
        "language": "persian_ar",
        "priority": 100,  # Highest priority for Persian in Arabic script
        "component": "month",
        "calendar": "julian"
    },
    
    {
        "name": "julian_months_persian_latin_script",  # Original: months_julian_en
        "keywords": months_julian_en,  
        "description": "Persian Solar Hijri month names in Latin script",
        "examples": [  # Original: example (single string) - Fixed to examples list
            "farvardin",     # Spring month 1
            "ordibehesht",   # Spring month 2
            "khordad",       # Spring month 3
            "tir",           # Summer month 1
            "mordad",        # Summer month 2
            "shahrivar",     # Summer month 3
            "mehr",          # Autumn month 1
            "aban",          # Autumn month 2
            "azar",          # Autumn month 3
            "dey",           # Winter month 1
            "bahman",        # Winter month 2
            "esfand"         # Winter month 3
        ],
        "language": "persian_en",
        "priority": 100,  # Highest priority for Persian in Latin script
        "component": "month",
        "calendar": "julian"
    }
]