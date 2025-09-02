example_julian = [
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # variable: date_patterns.yy.julian.numeric
    # type: "numeric", name : "yy_julian", format: [YYYY-ERA], calendar: julian  
    "1402 هـ.ش",     # Year 1402 SH (≈ 2023-2024 CE)
    "1400 شمسی",     # Year 1400 SH with Persian marker
    "1405 ه.ش",      # Year 1405 SH with simplified marker
    "1398 هجری شمسی", # Year 1398 SH with full Persian marker
    "1401 ش",        # Year 1401 SH with abbreviated marker
    "1403 شمسى",      # Year 1403 SH with Persian marker
    # variable: date_patterns.mm_yy.julian.combined 
    # type:"combined", name:"mm_yy_julian", format:[MM-YYYY-ERA], calendar: julian 
    "فروردین 1402 هـ.ش",    # Farvardin 1402 SH
    "مهر 1401 شمسی",      # Mehr 1401 SH
    "01/1403 ه.ش",          # Farvardin 1403 SH (numeric)
    "آبان 1400 شمسى",       # Aban 1400 SH
    "12/1404 هجری شمسی",  # Esfand 1404 SH
    "دی 1399 ش",           # Dey 1399 SH

    # variable: date_patterns.dd_mm_yy.julian.combined
    # type: "combined", name : "dd_mm_yy_julian", format: [DD-MM-YYYY-ERA], calendar: julian
    "15/03/1402 هـ.ش",     # 15th Khordad 1402 SH
    "01/فروردین/1403 شمسی", # 1st Farvardin 1403 SH (Nowruz)
    "21/مهر/1401 ه.ش",     # 21st Mehr 1401 SH
    "29/اسفند/1400 شمسى",  # 29th Esfand 1400 SH
    "10/06/1404 هجری شمسی", # 10th Shahrivar 1404 SH
    "25/آبان/1399 ش",       # 25th Aban 1399 SH

    # variable: date_patterns.natural_language.julian.combined
    # type: "combined", name : "natural_language_julian", format: [WD-MM-YYYY-ERA], calendar: julian
    "جمعه 15 فروردین 1402 هـ.ش",    # Friday 15th Farvardin 1402 SH
    "یکشنبه 01 فروردین 1403 شمسی", # Sunday 1st Farvardin 1403 SH (Nowruz)
    "دوشنبه 21 مهر 1401 ه.ش",      # Monday 21st Mehr 1401 SH
    "سه‌شنبه 29 اسفند 1400 شمسى",  # Tuesday 29th Esfand 1400 SH
    "پنج‌شنبه 10 آبان 1404 هجری شمسی", # Thursday 10th Aban 1404 SH
    "شنبه 25 دی 1399 ش",           # Saturday 25th Dey 1399 SH
]


year_examples_hijri = [
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # variable: date_patterns.yy.hijri.numeric
    # type: "numeric", name : "yy_hijri", format: [YYYY-ERA], calendar: HIJRI  
    "1445 هـ",       # Year 1445 AH (≈ 2023-2024 CE)
    "1440 هجري",    # Year 1440 AH with Arabic era marker
    "1450 هـ",       # Year 1450 AH (≈ 2028-2029 CE)
    "1435 هجرية",   # Year 1435 AH with full Arabic era marker
    "1442 ه",        # Year 1442 AH with simplified marker
    "1448 هـ.",       # Year 1448 AH with period
    
    # variable: date_patterns.cs_yy.hijri.mixed
    # type: "numeric", name : "single_mixed_yy_hijri", format: [YYYY-ERA]-[YYYY-ERA], calendar: HIJRI  
    "من 1440 هـ إلى 1445 هـ",
    "1442هـ / 1444هـ",
    "١٤٣٠ هـ – ١٤٤٠ هـ",
    "1440 هـ / 1445 هـ",
    "١٤٣٥ هـ - ١٤٤١ هـ",
    
    # variable: date_patterns.cs_yy.hijri.mixed_parenthetical
    # type: "numeric", name : "single_mixed_yy_hijri_parenthetical", format: [YYYY-ERA]-([YYYY-ERA]), calendar: HIJRI
    "من 1440 هـ إلى (1445 هـ)",
    "1442 هـ - (1444 هـ)",
    "من 1430 هـ إلى (1440 هـ)",
    
    # variable: date_patterns.cs_yy.hijri.alternative
    # type: "numeric", name : "single_alternative_hijri_gregorian_years", format: [YYYY-ERA]-[YYYY-ERA], calendar: HIJRI-GREGORIAN  
    "1440 هـ/2023 م",
    "١٤٤٥ هـ - ٢٠٢٤ م",
    "من 1440 هـ إلى 1445 هـ",
    "من 1442 هـ إلى 1444 هـ",
    
    # variable: date_patterns.yy.hijri.alternative_parenthetical
    # type: "combined", name : "single_alternative_hijri_gregorian_years_parenthetical", format: [YYYY-ERA]-([YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "1440 هـ/(2023 م)",
    "١٤٤٥ هـ - (٢٠٢٤ م)",
    "من 1440 هـ إلى (٢٠٢٤ م)",
    
    # variable: date_patterns.dual_yy.hijri.mixed
    # type: "numeric", name : "dual_yy_hijri", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: HIJRI
    "من 1440 هـ إلى 1441 هـ - 1446 هـ - 1447 هـ",
    "من 1442 هـ إلى 1444 هـ - 1445 هـ - 1446 هـ",
    "من 1440 هـ إلى 1445 هـ - 1446 هـ - 1447 هـ",
    
    
    # variable: date_patterns.dual_yy.hijri.mixed_parenthetical
    # type: "numeric", name : "dual_yy_hijri_parenthetical", format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI
    "من 1440 هـ إلى 1441 هـ - (1446 هـ - 1447 هـ)",
    "من 1442 هـ إلى 1444 هـ - (1445 هـ - 1446 هـ)",
    
    # variable: date_patterns.dual_yy.hijri.mixed_double_parenthetical
    # type: "numeric", name : "dual_yy_hijri_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI
    "من (1440 هـ إلى 1441 هـ) - (1446 هـ - 1447 هـ)",
    "من (1442 هـ إلى 1444 هـ) - (1445 هـ - 1446 هـ)",
    
    # variable: date_patterns.dual_yy.hijri.mixed_alternative
    # type: "numeric", name : "dual_yy_alternative_hijri", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: HIJRI-GREGORIAN
    "من 1445 هـ إلى 1446 هـ - ٢٠٢٤ مـ - ٢٠٢٥ م",
    "من 1440 هـ إلى 1445 هـ - ٢٠٢٣ م - ٢٠٢٤ م",
    
    # variable: date_patterns.dual_yy.hijri.mixed_alternative_parenthetical
    # type: "numeric", name : "dual_yy_alternative_hijri_parenthetical", format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من 1445 هـ إلى 1446 هـ - (٢٠٢٤ مـ - ٢٠٢٥ م)",
    "من 1440 هـ إلى 1445 هـ - (٢٠٢٣ م - ٢٠٢٤ م)",
    
    # variable: date_patterns.dual_yy.hijri.mixed_alternative_double_parenthetical
    # type: "numeric", name : "dual_yy_alternative_hijri_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من (1445 هـ إلى 1446 هـ) - (٢٠٢٤ مـ - ٢٠٢٥ م)",
    "من (1440 هـ إلى 1445 هـ) - (٢٠٢٣ م - ٢٠٢٤ م)",
    
    # variable: date_patterns.dual_yy.hijri.alternative
    # type: "numeric", name : "dual_yy_alternative_hijri", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: HIJRI-GREGORIAN
    "١٤٤٥ هـ - ٢٠٢٤ مـ - 1446 هـ - ٢٠٢٤ م",

    # variable: date_patterns.dual_yy.hijri.alternative_parenthetical
    # type: "numeric", name : "dual_yy_alternative_hijri_parenthetical", format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "١٤٤٥ هـ - ٢٠٢٤ مـ - (1446 هـ - ٢٠٢٤ م)",
    "١٤٤٠ هـ - ٢٠٢٣ م - (1445 هـ - ٢٠٢٤ م)",
    
    # variable: date_patterns.dual_yy.hijri.alternative_double_parenthetical
    # type: "numeric", name : "dual_yy_alternative_hijri_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "(١٤٤٥ هـ - ٢٠٢٤ مـ) - (1446 هـ - ٢٠٢٤ م)",
    "(١٤٤٠ هـ - ٢٠٢٣ م) - (1445 هـ - ٢٠٢٤ م)",
]

year_examples_gregorian = [
    # variable: date_patterns.yy.gregorian.numeric
    # type: "numeric", name : "yy_gregorian", format: [YYYY-ERA], calendar: GREGORIAN  
    "2023 م",        # Year 2023 CE with Arabic marker
    "2024 ميلادي",   # Year 2024 CE with Arabic era marker
    "2022 ميلادية",  # Year 2022 CE with feminine Arabic marker
    "2025 م.",       # Year 2025 CE with period
    "2021 AD",       # Year 2021 CE with English marker
    "2020 CE",        # Year 2020 CE with English era marker
    
    # variable: date_patterns.cs_yy.gregorian.mixed
    # type: "numeric", name : "single_mixed_yy_gregorian", format: [YYYY-ERA]-[YYYY-ERA], calendar: GREGORIAN  
    "من 2020 م إلى 2024 م",
    "٢٠١٠ م / ٢٠٢٠ م",
    "1995م – 2005م",
    "2020 م / 2024 م",
    "٢٠١٥ م - ٢٠٢٠ م",
    "2020 م / 2024 م",
    "٢٠١٥م - ٢٠٢٢م",
    "من 2020 م إلى 2024 م",
    
    # variable: date_patterns.cs_yy.gregorian.mixed_parenthetical
    # type: "numeric", name : "single_mixed_yy_gregorian_parenthetical", format: [YYYY-ERA]-([YYYY-ERA]), calendar: GREGORIAN
    "من 2020 م إلى (2024 م)",
    "2020 م - (2024 م)",
    "من 2010 م إلى (2020 م)",
    "1995م - (2005م)",
    
    # variable: date_patterns.cs_yy.gregorian.alternative, ,
    # type: "numeric", name : "single_alternative_gregorian_hijri_years", format: [YYYY-ERA]-[YYYY-ERA], calendar: GREGORIAN-HIJRI  
    "2023 م/1440 هـ",
    "٢٠٢٤ م - ١٤٤٥ هـ",
    "2020 CE - 1445 AH",
    "2020 CE - 1446 AH",
    
    # variable: date_patterns.yy.gregorian.alternative_parenthetical
    # type: "combined", name : "single_alternative_gregorian_hijri_years_parenthetical", format: [YYYY-ERA]-([YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "2023 م/(1440 هـ)",
    "٢٠٢٤ م - (١٤٤٥ هـ)",
    "2020 CE - (1445 AH)",
    "2020 CE - (1446 AH)",
    
    # variable: date_patterns.dual_yy.gregorian.mixed
    # type: "numeric", name : "dual_yy_gregorian", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: GREGORIAN
    "from 2023 CE to 2024 CE - 2025 CE - 2026 CE",
    "from 2020 CE to 2022 CE - 2023 CE - 2024 CE",
    "2024 م - 2025 م - 2026 م - 2027 م",
    "2023 م - 2024 م - 2025 م - 2026 م",
    
    # variable: date_patterns.dual_yy.gregorian.mixed_parenthetical
    # type: "numeric", name : "dual_yy_gregorian_parenthetical", format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN
    "from 2023 CE to 2024 CE - (2025 CE - 2026 CE)",
    "from 2020 CE to 2022 CE - (2023 CE - 2024 CE)",
    "2024 م - 2025 م - (2026 م - 2027 م)",
    "2023 م - 2024 م - (2025 م - 2026 م)",
    
    # variable: date_patterns.dual_yy.gregorian.mixed_double_parenthetical
    # type: "numeric", name : "dual_yy_gregorian_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN
    "from (2023 CE to 2024 CE) - (2025 CE - 2026 CE)",
    "from (2020 CE to 2022 CE) - (2023 CE - 2024 CE)",
    "(2024 م - 2025 م) - (2026 م - 2027 م)",
    "(2023 م - 2024 م) - (2025 م - 2026 م)",
    
    # variable: date_patterns.dual_yy.gregorian.mixed_alternative
    # type: "numeric", name : "dual_yy_alternative_gregorian", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: GREGORIAN-HIJRI
    "2023 م - 2024 م - 1445 هـ - 1446 هـ",
    
    # variable: date_patterns.dual_yy.gregorian.mixed_alternative_parenthetical
    # type: "numeric", name : "dual_yy_alternative_gregorian_parenthetical", format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "2023 م - 2024 م - (1445 هـ - 1446 هـ)",
    "2020 م - 2022 م - (1440 هـ - 1445 هـ)",
    
    # variable: date_patterns.dual_yy.gregorian.mixed_alternative_double_parenthetical
    # type: "numeric", name : "dual_yy_alternative_gregorian_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(2023 م - 2024 م) - (1445 هـ - 1446 هـ)",
    "(2020 م - 2022 م) - (1440 هـ - 1445 هـ)",
    
    # variable: date_patterns.dual_yy.gregorian.alternative
    # type: "numeric", name : "dual_yy_alternative_gregorian", format: [YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA]-[YYYY-ERA], calendar: GREGORIAN-HIJRI
    "2023 م - 1445 هـ - 2024 م - 1446 هـ",
    "2020 م - 1440 هـ - 2022 م - 1445 هـ",
    
    # variable: date_patterns.dual_yy.gregorian.alternative_parenthetical
    # type: "numeric", name : "dual_yy_alternative_gregorian_parent, format: [YYYY-ERA]-[YYYY-ERA]-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "2023 م - 1445 هـ - (2024 م - 1446 هـ)",
    "2020 م - 1440 هـ - (2022 م - 1445 هـ)",
    
    # variable: date_patterns.dual_yy.gregorian.alternative_double_parenthetical
    # type: "numeric", name : "dual_yy_alternative_gregorian_double_parenthetical", format: ([YYYY-ERA]-[YYYY-ERA])-([YYYY-ERA]-[YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(2023 م - 1445 هـ) - (2024 م - 1446 هـ)",
    "(2020 م - 1440 هـ) - (2022 م - 1445 هـ)",
]

month_year_examples_hijri = [
    # variable: date_patterns.mm_yy.hijri.combined 
    # type: "combined", name : "mm_yy_hijri", format: [MM-YYYY-ERA], calendar: HIJRI  
    "12/1445 هـ",       # Dhul Hijjah 1445 AH
    "محرم 1446 هـ",     # Muharram 1446 AH
    "محرم 1446",        # Muharram 1446 AH
    "01/1440 هجري",    # Muharram 1440 AH
    "رجب 1444 هـ",      # Rajab 1444 AH
    "06/1447 ه",        # Jumada al-Thani 1447 AH
    "رمضان 1445 هجرية", # Ramadan 1445 AH
    "09/1443 هـ.",      # Ramadan 1443 AH
    
    # variable: date_patterns.cs_mm_yy.hijri.mixed
    # type: "combined", name : "single_mixed_mm_yy_hijri", format: [MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: HIJRI 
    "من محرم 1440 هـ إلى صفر 1445 هـ",   # From Muharram 1440 AH to Safar 1445 AH
    "من شعبان 1440 هـ إلى رمضان 1442 هـ", # From Sha'ban 1440 AH to Ramadan 1442 AH
    "من شعبان 1440 إلى رمضان 1442 هـ",   # From Sha'ban 1440 to Ramadan 1442 AH
    "من شعبان 1440 إلى رمضان 1442",      # From Sha'ban 1440 to Ramadan 1442
    "ذو القعدة 1443 هـ - محرم 1444 هـ",  # Dhul Qi'dah 1443 AH - Muharram 1444 AH
    "ربيع الأول 1445 هـ / رجب 1446 هـ",  # Rabi' al-Awwal 1445 AH / Rajab 1446 AH
    "من شعبان 1442 هـ إلى رمضان 1443 هـ", # From Sha'ban 1442 AH to Ramadan 1443 AH
    "محرم 1440 هـ / صفر 1445 هـ",        # Muharram 1440 AH / Safar 1445 AH
    "شعبان ١٤٤٠ هـ - رمضان ١٤٤٢ هـ",    # Sha'ban 1440 AH - Ramadan 1442 AH
    "جمادى الآخرة 1441 هـ / ذو الحجة 1443 هـ", # Jumada al-Akhirah 1441 AH / Dhul Hijjah 1443 AH
    
    # variable: date_patterns.cs_mm_yy.hijri.mixed_parenthetical
    # type: "combined", name : "single_mixed_mm_yy_hijri_parenthetical", format: [MM-YYYY-ERA]-([MM-YYYY-ERA]), calendar: HIJRI
    "من محرم 1440 هـ إلى (صفر 1445 هـ)",   # From Muharram 1440 AH to (Safar 1445 AH)
    "شعبان 1442 هـ - (رمضان 1443 هـ)",    # Sha'ban 1442 AH - (Ramadan 1443 AH)
    "من ربيع الأول 1440 هـ إلى (رجب 1441 هـ)", # From Rabi' al-Awwal 1440 AH to (Rajab 1441 AH)
    "ذو القعدة 1443 هـ - (محرم 1444 هـ)", # Dhul Qi'dah 1443 AH - (Muharram 1444 AH)
    
    # variable: date_patterns.cs_mm_yy.hijri.alternative
    # type: "combined", name : "single_alternative_mm_yy_hijri_gregorian", format: [MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: HIJRI-GREGORIAN  
    "محرم 1440 هـ/يناير 2023 م",         # Muharram 1440 AH/January 2023 CE
    "رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م",      # Ramadan 1445 AH - March 2024 CE
    "من شعبان 1440 هـ إلى أبريل 2023 م", # From Sha'ban 1440 AH to April 2023 CE
    "رجب 1442 هـ إلى فبراير 2024 م",     # Rajab 1442 AH to February 2024 CE
    
    # variable: date_patterns.mm_yy.hijri.alternative_parenthetical
    # type: "combined", name : "single_alternative_mm_yy_hijri_gregorian_parenthetical", format: [MM-YYYY-ERA]-([MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "محرم 1440 هـ/(يناير 2023 م)",       # Muharram 1440 AH/(January 2023 CE)
    "رمضان ١٤٤٥ هـ - (مارس ٢٠٢٤ م)",    # Ramadan 1445 AH - (March 2024 CE)
    "من شعبان 1440 هـ إلى (أبريل 2023 م)", # From Sha'ban 1440 AH to (April 2023 CE)
    "رجب 1442 هـ - (فبراير 2024 م)",     # Rajab 1442 AH - (February 2024 CE)
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed
    # type: "combined", name : "dual_mm_yy_hijri", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: HIJRI
    "من محرم 1440 هـ إلى صفر 1441 هـ - رجب 1446 هـ - شعبان 1447 هـ", # From Muharram 1440 AH to Safar 1441 AH - Rajab 1446 AH - Sha'ban 1447 AH
    "من رمضان 1442 هـ إلى شوال 1444 هـ - ذو القعدة 1445 هـ - ذو الحجة 1446 هـ", # From Ramadan 1442 AH to Shawwal 1444 AH - Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH
    "من ربيع الأول 1440 هـ إلى ربيع الآخر 1445 هـ - جمادى الأولى 1446 هـ - جمادى الآخرة 1447 هـ", # From Rabi' al-Awwal 1440 AH to Rabi' al-Akhir 1445 AH - Jumada al-Ula 1446 AH - Jumada al-Akhirah 1447 AH
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed_parenthetical
    # type: "combined", name : "dual_mm_yy_hijri_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI
    "من محرم 1440 هـ إلى صفر 1441 هـ - (رجب 1446 هـ - شعبان 1447 هـ)", # From Muharram 1440 AH to Safar 1441 AH - (Rajab 1446 AH - Sha'ban 1447 AH)
    "من رمضان 1442 هـ إلى شوال 1444 هـ - (ذو القعدة 1445 هـ - ذو الحجة 1446 هـ)", # From Ramadan 1442 AH to Shawwal 1444 AH - (Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed_double_parenthetical
    # type: "combined", name : "dual_mm_yy_hijri_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI
    "من (محرم 1440 هـ إلى صفر 1441 هـ) - (رجب 1446 هـ - شعبان 1447 هـ)", # From (Muharram 1440 AH to Safar 1441 AH) - (Rajab 1446 AH - Sha'ban 1447 AH)
    "من (رمضان 1442 هـ إلى شوال 1444 هـ) - (ذو القعدة 1445 هـ - ذو الحجة 1446 هـ)", # From (Ramadan 1442 AH to Shawwal 1444 AH) - (Dhul Qi'dah 1445 AH - Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed_alternative
    # type: "combined", name : "dual_mm_yy_alternative_hijri", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "من رمضان 1445 هـ إلى شوال 1446 هـ - مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م", # From Ramadan 1445 AH to Shawwal 1446 AH - March 2024 CE - April 2025 CE
    "من محرم 1440 هـ إلى صفر 1445 هـ - يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م", # From Muharram 1440 AH to Safar 1445 AH - January 2023 CE - February 2024 CE
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed_alternative_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_hijri_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من رمضان 1445 هـ إلى شوال 1446 هـ - (مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م)", # From Ramadan 1445 AH to Shawwal 1446 AH - (March 2024 CE - April 2025 CE)
    "من محرم 1440 هـ إلى صفر 1445 هـ - (يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م)", # From Muharram 1440 AH to Safar 1445 AH - (January 2023 CE - February 2024 CE)
    
    # variable: date_patterns.dual_mm_yy.hijri.mixed_alternative_double_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_hijri_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من (رمضان 1445 هـ إلى شوال 1446 هـ) - (مارس ٢٠٢٤ م - أبريل ٢٠٢٥ م)", # From (Ramadan 1445 AH to Shawwal 1446 AH) - (March 2024 CE - April 2025 CE)
    "من (محرم 1440 هـ إلى صفر 1445 هـ) - (يناير ٢٠٢٣ م - فبراير ٢٠٢٤ م)", # From (Muharram 1440 AH to Safar 1445 AH) - (January 2023 CE - February 2024 CE)
    
    # variable: date_patterns.dual_mm_yy.hijri.alternative
    # type: "combined", name : "dual_mm_yy_alternative_hijri", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م - شوال 1446 هـ - أبريل ٢٠٢٤ م", # Ramadan 1445 AH - March 2024 CE - Shawwal 1446 AH - April 2024 CE
    
    # variable: date_patterns.dual_mm_yy.hijri.alternative_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_hijri_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م - (شوال 1446 هـ - أبريل ٢٠٢٤ م)", # Ramadan 1445 AH - March 2024 CE - (Shawwal 1446 AH - April 2024 CE)
    "محرم ١٤٤٠ هـ - يناير ٢٠٢٣ م - (صفر 1445 هـ - فبراير ٢٠٢٤ م)", # Muharram 1440 AH - January 2023 CE - (Safar 1445 AH - February 2024 CE)
    
    # variable: date_patterns.dual_mm_yy.hijri.alternative_double_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_hijri_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "(رمضان ١٤٤٥ هـ - مارس ٢٠٢٤ م) - (شوال 1446 هـ - أبريل ٢٠٢٤ م)", # (Ramadan 1445 AH - March 2024 CE) - (Shawwal 1446 AH - April 2024 CE)
    "(محرم ١٤٤٠ هـ - يناير ٢٠٢٣ م) - (صفر 1445 هـ - فبراير ٢٠٢٤ م)", # (Muharram 1440 AH - January 2023 CE) - (Safar 1445 AH - February 2024 CE)
]

month_year_examples_gregorian = [
    # variable: date_patterns.mm_yy.gregorian.combined 
    # type: "combined", name : "mm_yy_gregorian", format: [MM-YYYY-ERA], calendar: GREGORIAN  
    "12/2023 م",        # December 2023 CE
    "يناير 2024 م",     # January 2024 CE
    "يناير 2024",       # January 2024
    "01/2020 ميلادي",   # January 2020 CE
    "مارس 2022 م",      # March 2022 CE
    "06/2025 ميلادية",  # June 2025 CE
    "أبريل 2023 ميلادي", # April 2023 CE
    "09/2021 م.",       # September 2021 CE
    "March 2024 CE",    # March 2024 CE
    "January 2023 AD",  # January 2023 AD
    
    # variable: date_patterns.cs_mm_yy.gregorian.mixed
    # type: "combined", name : "single_mixed_mm_yy_gregorian", format: [MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: GREGORIAN 
    "من يناير 2020 م إلى فبراير 2024 م",   # From January 2020 CE to February 2024 CE
    "من مارس 2020 م إلى أبريل 2022 م",     # From March 2020 CE to April 2022 CE
    "من مايو 2020 إلى يونيو 2022 م",       # From May 2020 to June 2022 CE
    "من يوليو 2020 إلى أغسطس 2022",       # From July 2020 to August 2022
    "سبتمبر 2021 م - أكتوبر 2022 م",      # September 2021 CE - October 2022 CE
    "نوفمبر 2023 م / ديسمبر 2024 م",      # November 2023 CE / December 2024 CE
    "من يناير 2022 م إلى فبراير 2023 م",   # From January 2022 CE to February 2023 CE
    "مارس 2020 م / أبريل 2024 م",         # March 2020 CE / April 2024 CE
    "مايو ٢٠٢٠ م - يونيو ٢٠٢٢ م",        # May 2020 CE - June 2022 CE
    "July 2020 CE / August 2022 CE",       # July 2020 CE / August 2022 CE
    "from March 2020 CE to April 2022 CE", # From March 2020 CE to April 2022 CE
    
    # variable: date_patterns.cs_mm_yy.gregorian.mixed_parenthetical
    # type: "combined", name : "single_mixed_mm_yy_gregorian_parenthetical", format: [MM-YYYY-ERA]-([MM-YYYY-ERA]), calendar: GREGORIAN
    "من يناير 2020 م إلى (فبراير 2024 م)", # From January 2020 CE to (February 2024 CE)
    "مارس 2022 م - (أبريل 2023 م)",       # March 2022 CE - (April 2023 CE)
    "من مايو 2020 م إلى (يونيو 2021 م)",   # From May 2020 CE to (June 2021 CE)
    "يوليو 2021 م - (أغسطس 2022 م)",      # July 2021 CE - (August 2022 CE)
    "from March 2020 CE to (April 2022 CE)", # From March 2020 CE to (April 2022 CE)
    
    # variable: date_patterns.cs_mm_yy.gregorian.alternative
    # type: "combined", name : "single_alternative_mm_yy_gregorian_hijri", format: [MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: GREGORIAN-HIJRI  
    "يناير 2023 م/محرم 1440 هـ",          # January 2023 CE/Muharram 1440 AH
    "مارس ٢٠٢٤ م - رمضان ١٤٤٥ هـ",       # March 2024 CE - Ramadan 1445 AH
    "من أبريل 2023 م إلى شعبان 1440 هـ",  # From April 2023 CE to Sha'ban 1440 AH
    "فبراير 2024 م إلى رجب 1442 هـ",     # February 2024 CE to Rajab 1442 AH
    "March 2024 CE - Ramadan 1445 AH",     # March 2024 CE - Ramadan 1445 AH
    
    # variable: date_patterns.mm_yy.gregorian.alternative_parenthetical
    # type: "combined", name : "single_alternative_mm_yy_gregorian_hijri_parenthetical", format: [MM-YYYY-ERA]-([MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "يناير 2023 م/(محرم 1440 هـ)",        # January 2023 CE/(Muharram 1440 AH)
    "مارس ٢٠٢٤ م - (رمضان ١٤٤٥ هـ)",     # March 2024 CE - (Ramadan 1445 AH)
    "من أبريل 2023 م إلى (شعبان 1440 هـ)", # From April 2023 CE to (Sha'ban 1440 AH)
    "فبراير 2024 م - (رجب 1442 هـ)",     # February 2024 CE - (Rajab 1442 AH)
    "March 2024 CE - (Ramadan 1445 AH)",   # March 2024 CE - (Ramadan 1445 AH)
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed
    # type: "combined", name : "dual_mm_yy_gregorian", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: GREGORIAN
    "from January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE", # From January 2023 CE to February 2024 CE - March 2025 CE - April 2026 CE
    "from March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE", # From March 2020 CE to April 2022 CE - May 2023 CE - June 2024 CE
    "يناير 2024 م - فبراير 2025 م - مارس 2026 م - أبريل 2027 م", # January 2024 CE - February 2025 CE - March 2026 CE - April 2027 CE
    "مايو 2023 م - يونيو 2024 م - يوليو 2025 م - أغسطس 2026 م", # May 2023 CE - June 2024 CE - July 2025 CE - August 2026 CE
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed_parenthetical
    # type: "combined", name : "dual_mm_yy_gregorian_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN
    "from January 2023 CE to February 2024 CE - (March 2025 CE - April 2026 CE)", # From January 2023 CE to February 2024 CE - (March 2025 CE - April 2026 CE)
    "from March 2020 CE to April 2022 CE - (May 2023 CE - June 2024 CE)", # From March 2020 CE to April 2022 CE - (May 2023 CE - June 2024 CE)
    "يناير 2024 م - فبراير 2025 م - (مارس 2026 م - أبريل 2027 م)", # January 2024 CE - February 2025 CE - (March 2026 CE - April 2027 CE)
    "مايو 2023 م - يونيو 2024 م - (يوليو 2025 م - أغسطس 2026 م)", # May 2023 CE - June 2024 CE - (July 2025 CE - August 2026 CE)
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed_double_parenthetical
    # type: "combined", name : "dual_mm_yy_gregorian_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN
    "from (January 2023 CE to February 2024 CE) - (March 2025 CE - April 2026 CE)", # From (January 2023 CE to February 2024 CE) - (March 2025 CE - April 2026 CE)
    "from (March 2020 CE to April 2022 CE) - (May 2023 CE - June 2024 CE)", # From (March 2020 CE to April 2022 CE) - (May 2023 CE - June 2024 CE)
    "(يناير 2024 م - فبراير 2025 م) - (مارس 2026 م - أبريل 2027 م)", # (January 2024 CE - February 2025 CE) - (March 2026 CE - April 2027 CE)
    "(مايو 2023 م - يونيو 2024 م) - (يوليو 2025 م - أغسطس 2026 م)", # (May 2023 CE - June 2024 CE) - (July 2025 CE - August 2026 CE)
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed_alternative
    # type: "combined", name : "dual_mm_yy_alternative_gregorian", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: GREGORIAN-HIJRI
    "يناير 2023 م - فبراير 2024 م - محرم 1445 هـ - صفر 1446 هـ", # January 2023 CE - February 2024 CE - Muharram 1445 AH - Safar 1446 AH
    "مارس 2020 م - أبريل 2022 م - رجب 1440 هـ - شعبان 1445 هـ", # March 2020 CE - April 2022 CE - Rajab 1440 AH - Sha'ban 1445 AH
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed_alternative_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_gregorian_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "يناير 2023 م - فبراير 2024 م - (محرم 1445 هـ - صفر 1446 هـ)", # January 2023 CE - February 2024 CE - (Muharram 1445 AH - Safar 1446 AH)
    "مارس 2020 م - أبريل 2022 م - (رجب 1440 هـ - شعبان 1445 هـ)", # March 2020 CE - April 2022 CE - (Rajab 1440 AH - Sha'ban 1445 AH)
    
    # variable: date_patterns.dual_mm_yy.gregorian.mixed_alternative_double_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_gregorian_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(يناير 2023 م - فبراير 2024 م) - (محرم 1445 هـ - صفر 1446 هـ)", # (January 2023 CE - February 2024 CE) - (Muharram 1445 AH - Safar 1446 AH)
    "(مارس 2020 م - أبريل 2022 م) - (رجب 1440 هـ - شعبان 1445 هـ)", # (March 2020 CE - April 2022 CE) - (Rajab 1440 AH - Sha'ban 1445 AH)
    
    # variable: date_patterns.dual_mm_yy.gregorian.alternative
    # type: "combined", name : "dual_mm_yy_alternative_gregorian", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA]-[MM-YYYY-ERA], calendar: GREGORIAN-HIJRI
    "يناير 2023 م - محرم 1445 هـ - فبراير 2024 م - صفر 1446 هـ", # January 2023 CE - Muharram 1445 AH - February 2024 CE - Safar 1446 AH
    "مارس 2020 م - رجب 1440 هـ - أبريل 2022 م - شعبان 1445 هـ", # March 2020 CE - Rajab 1440 AH - April 2022 CE - Sha'ban 1445 AH
    
    # variable: date_patterns.dual_mm_yy.gregorian.alternative_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_gregorian_parenthetical", format: [MM-YYYY-ERA]-[MM-YYYY-ERA]-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "يناير 2023 م - محرم 1445 هـ - (فبراير 2024 م - صفر 1446 هـ)", # January 2023 CE - Muharram 1445 AH - (February 2024 CE - Safar 1446 AH)
    "مارس 2020 م - رجب 1440 هـ - (أبريل 2022 م - شعبان 1445 هـ)", # March 2020 CE - Rajab 1440 AH - (April 2022 CE - Sha'ban 1445 AH)
    
    # variable: date_patterns.dual_mm_yy.gregorian.alternative_double_parenthetical
    # type: "combined", name : "dual_mm_yy_alternative_gregorian_double_parenthetical", format: ([MM-YYYY-ERA]-[MM-YYYY-ERA])-([MM-YYYY-ERA]-[MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(يناير 2023 م - محرم 1445 هـ) - (فبراير 2024 م - صفر 1446 هـ)", # (January 2023 CE - Muharram 1445 AH) - (February 2024 CE - Safar 1446 AH)
    "(مارس 2020 م - رجب 1440 هـ) - (أبريل 2022 م - شعبان 1445 هـ)", # (March 2020 CE - Rajab 1440 AH) - (April 2022 CE - Sha'ban 1445 AH)
]

day_month_year_examples_hijri = [
    # variable: date_patterns.dd_mm_yy.hijri.combined
    # type: "combined", name : "dd_mm_yy_hijri", format: [DD-MM-YYYY-ERA], calendar: HIJRI  
    "15/03/1445 هـ",      # 15th Rabi al-Awwal 1445 AH
    "01/محرم/1446 هجري", # 1st Muharram 1446 AH
    "27/رمضان/1445 هـ",   # 27th Ramadan 1445 AH (Laylat al-Qadr)
    "10/ذو الحجة/1444 ه", # 10th Dhul Hijjah 1444 AH (Eid al-Adha)
    "25/12/1443 هجرية",  # 25th Dhul Hijjah 1443 AH
    "09/ربيع الأول/1445 هـ.", # 9th Rabi al-Awwal 1445 AH
    "21/شعبان/1446 هـ",   # 21st Sha'ban 1446 AH
    "05/جمادى الآخرة/1444 هـ", # 5th Jumada al-Akhirah 1444 AH
    "12/رجب/1445 هجري",   # 12th Rajab 1445 AH
    "03/شوال/1443 ه",     # 3rd Shawwal 1443 AH (Eid al-Fitr)
    
    # variable: date_patterns.cs_dd_mm_yy.hijri.mixed
    # type: "combined", name : "single_mixed_dd_mm_yy_hijri", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: HIJRI 
    "من 15/03/1445 هـ إلى 01/04/1446 هـ", # From 15th Rabi al-Awwal 1445 AH to 1st Rabi al-Akhir 1446 AH
    "15/محرم/1440 هـ - 10/صفر/1445 هـ", # 15th Muharram 1440 AH - 10th Safar 1445 AH
    "27/رمضان/1445 هـ / 01/شوال/1446 هـ", # 27th Ramadan 1445 AH / 1st Shawwal 1446 AH
    "من 10/ذو الحجة/1444 هـ إلى 25/محرم/1445 هـ", # From 10th Dhul Hijjah 1444 AH to 25th Muharram 1445 AH
    "25/12/1443 هـ / 01/01/1445 هـ", # 25th Dhul Hijjah 1443 AH / 1st Muharram 1445 AH
    "09/ربيع الأول/1445 هـ - 15/جمادى الآخرة/1446 هـ", # 9th Rabi al-Awwal 1445 AH - 15th Jumada al-Akhirah 1446 AH
    "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ", # From 15th Muharram 1445 AH to 20th Safar 1445 AH
    "من 1 رمضان 1400 هـ إلى 10 شوال 1400 هـ", # From 1st Ramadan 1400 AH to 10th Shawwal 1400 AH
    "21/شعبان/1446 هـ - 05/رمضان/1446 هـ", # 21st Sha'ban 1446 AH - 5th Ramadan 1446 AH
    "12/رجب/1445 هـ / 03/شعبان/1445 هـ", # 12th Rajab 1445 AH / 3rd Sha'ban 1445 AH
    "من ١٥ محرم ١٤٤٥ هـ إلى ٢٠ صفر ١٤٤٥ هـ", # From 15th Muharram 1445 AH to 20th Safar 1445 AH
    
    # variable: date_patterns.cs_dd_mm_yy.hijri.mixed_parenthetical
    # type: "combined", name : "single_mixed_dd_mm_yy_hijri_parenthetical", format: [DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]), calendar: HIJRI
    "من 15/03/1445 هـ إلى (01/04/1446 هـ)", # From 15th Rabi al-Awwal 1445 AH to (1st Rabi al-Akhir 1446 AH)
    "15/محرم/1440 هـ - (10/صفر/1445 هـ)", # 15th Muharram 1440 AH - (10th Safar 1445 AH)
    "من 10/ذو الحجة/1444 هـ إلى (25/محرم/1445 هـ)", # From 10th Dhul Hijjah 1444 AH to (25th Muharram 1445 AH)
    "27/رمضان/1445 هـ - (01/شوال/1446 هـ)", # 27th Ramadan 1445 AH - (1st Shawwal 1446 AH)
    "من 15 محرم 1445 هـ إلى (20 صفر 1445 هـ)", # From 15th Muharram 1445 AH to (20th Safar 1445 AH)
    
    # variable: date_patterns.cs_dd_mm_yy.hijri.alternative
    # type: "combined", name : "single_alternative_dd_mm_yy_hijri_gregorian", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN  
    "15/محرم/1440 هـ/20/يناير/2023 م", # 15th Muharram 1440 AH/20th January 2023 CE
    "27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م", # 27th Ramadan 1445 AH - 15th March 2024 CE
    "من 10/ذو الحجة/1444 هـ إلى 25/ديسمبر/2023 م", # From 10th Dhul Hijjah 1444 AH to 25th December 2023 CE
    "01/شوال/1442 هـ إلى 10/أبريل/2024 م", # 1st Shawwal 1442 AH to 10th April 2024 CE
    "15/رجب/1445 هـ - 20/February/2024 CE", # 15th Rajab 1445 AH - 20th February 2024 CE
    
    # variable: date_patterns.dd_mm_yy.hijri.alternative_parenthetical
    # type: "combined", name : "single_alternative_dd_mm_yy_hijri_gregorian_parenthetical", format: [DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "15/محرم/1440 هـ/(20/يناير/2023 م)", # 15th Muharram 1440 AH/(20th January 2023 CE)
    "27/رمضان/١٤٤٥ هـ - (15/مارس/٢٠٢٤ م)", # 27th Ramadan 1445 AH - (15th March 2024 CE)
    "من 10/ذو الحجة/1444 هـ إلى (25/ديسمبر/2023 م)", # From 10th Dhul Hijjah 1444 AH to (25th December 2023 CE)
    "15/رجب/1445 هـ - (20/February/2024 CE)", # 15th Rajab 1445 AH - (20th February 2024 CE)
    "01/شوال/1442 هـ - (10/أبريل/2024 م)", # 1st Shawwal 1442 AH - (10th April 2024 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed
    # type: "combined", name : "dual_dd_mm_yy_hijri", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: HIJRI
    "من 15/محرم/1440 هـ إلى 10/صفر/1441 هـ - 25/رجب/1446 هـ - 01/شعبان/1447 هـ", # From 15th Muharram 1440 AH to 10th Safar 1441 AH - 25th Rajab 1446 AH - 1st Sha'ban 1447 AH
    "من 27/رمضان/1442 هـ إلى 15/شوال/1444 هـ - 10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ", # From 27th Ramadan 1442 AH to 15th Shawwal 1444 AH - 10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH
    "من 09/ربيع الأول/1440 هـ إلى 15/ربيع الآخر/1445 هـ - 20/جمادى الأولى/1446 هـ - 05/جمادى الآخرة/1447 هـ", # From 9th Rabi al-Awwal 1440 AH to 15th Rabi al-Akhir 1445 AH - 20th Jumada al-Ula 1446 AH - 5th Jumada al-Akhirah 1447 AH
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_hijri_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI
    "من 15/محرم/1440 هـ إلى 10/صفر/1441 هـ - (25/رجب/1446 هـ - 01/شعبان/1447 هـ)", # From 15th Muharram 1440 AH to 10th Safar 1441 AH - (25th Rajab 1446 AH - 1st Sha'ban 1447 AH)
    "من 27/رمضان/1442 هـ إلى 15/شوال/1444 هـ - (10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ)", # From 27th Ramadan 1442 AH to 15th Shawwal 1444 AH - (10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_hijri_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI
    "من (15/محرم/1440 هـ إلى 10/صفر/1441 هـ) - (25/رجب/1446 هـ - 01/شعبان/1447 هـ)", # From (15th Muharram 1440 AH to 10th Safar 1441 AH) - (25th Rajab 1446 AH - 1st Sha'ban 1447 AH)
    "من (27/رمضان/1442 هـ إلى 15/شوال/1444 هـ) - (10/ذو القعدة/1445 هـ - 25/ذو الحجة/1446 هـ)", # From (27th Ramadan 1442 AH to 15th Shawwal 1444 AH) - (10th Dhul Qi'dah 1445 AH - 25th Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed_alternative
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "من 27/رمضان/1445 هـ إلى 01/شوال/1446 هـ - 15/مارس/٢٠٢٤ م - 10/أبريل/٢٠٢٥ م", # From 27th Ramadan 1445 AH to 1st Shawwal 1446 AH - 15th March 2024 CE - 10th April 2025 CE
    "من 15/محرم/1440 هـ إلى 10/صفر/1445 هـ - 20/يناير/٢٠٢٣ م - 25/فبراير/٢٠٢٤ م", # From 15th Muharram 1440 AH to 10th Safar 1445 AH - 20th January 2023 CE - 25th February 2024 CE
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed_alternative_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من 27/رمضان/1445 هـ إلى 01/شوال/1446 هـ - (15/مارس/٢٠٢٤ م - 10/أبريل/٢٠٢٥ م)", # From 27th Ramadan 1445 AH to 1st Shawwal 1446 AH - (15th March 2024 CE - 10th April 2025 CE)
    "من 15/محرم/1440 هـ إلى 10/صفر/1445 هـ - (20/يناير/٢٠٢٣ م - 25/فبراير/٢٠٢٤ م)", # From 15th Muharram 1440 AH to 10th Safar 1445 AH - (20th January 2023 CE - 25th February 2024 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.mixed_alternative_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من (27/رمضان/1445 هـ إلى 01/شوال/1446 هـ) - (15/مارس/٢٠٢٤ م - 10/أبريل/٢٠٢٥ م)", # From (27th Ramadan 1445 AH to 1st Shawwal 1446 AH) - (15th March 2024 CE - 10th April 2025 CE)
    "من (15/محرم/1440 هـ إلى 10/صفر/1445 هـ) - (20/يناير/٢٠٢٣ م - 25/فبراير/٢٠٢٤ م)", # From (15th Muharram 1440 AH to 10th Safar 1445 AH) - (20th January 2023 CE - 25th February 2024 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.alternative
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م - 01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م", # 27th Ramadan 1445 AH - 15th March 2024 CE - 1st Shawwal 1446 AH - 10th April 2024 CE
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.alternative_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م - (01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م)", # 27th Ramadan 1445 AH - 15th March 2024 CE - (1st Shawwal 1446 AH - 10th April 2024 CE)
    "15/محرم/١٤٤٠ هـ - 20/يناير/٢٠٢٣ م - (10/صفر/1445 هـ - 25/فبراير/٢٠٢٤ م)", # 15th Muharram 1440 AH - 20th January 2023 CE - (10th Safar 1445 AH - 25th February 2024 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.hijri.alternative_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_hijri_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "(27/رمضان/١٤٤٥ هـ - 15/مارس/٢٠٢٤ م) - (01/شوال/1446 هـ - 10/أبريل/٢٠٢٤ م)", # (27th Ramadan 1445 AH - 15th March 2024 CE) - (1st Shawwal 1446 AH - 10th April 2024 CE)
    "(15/محرم/١٤٤٠ هـ - 20/يناير/٢٠٢٣ م) - (10/صفر/1445 هـ - 25/فبراير/٢٠٢٤ م)", # (15th Muharram 1440 AH - 20th January 2023 CE) - (10th Safar 1445 AH - 25th February 2024 CE)
]

day_month_year_examples_gregorian = [
    # variable: date_patterns.dd_mm_yy.gregorian.combined
    # type: "combined", name : "dd_mm_yy_gregorian", format: [DD-MM-YYYY-ERA], calendar: GREGORIAN  
    "15/03/2023 م",       # 15th March 2023 CE
    "25/December/2024 CE", # 25th December 2024 CE
    "01/يناير/2022 ميلادي", # 1st January 2022 CE
    "14/فبراير/2025 م",   # 14th February 2025 CE
    "31/12/2021 ميلادية", # 31st December 2021 CE
    "04/July/2023 AD",     # 4th July 2023 CE
    "22/نوفمبر/2024 م",   # 22nd November 2024 CE
    "08/أغسطس/2022 ميلادي", # 8th August 2022 CE
    "17/September/2025 CE", # 17th September 2025 CE
    "29/مايو/2023 م.",    # 29th May 2023 CE
    
    # variable: date_patterns.cs_dd_mm_yy.gregorian.mixed
    # type: "combined", name : "single_mixed_dd_mm_yy_gregorian", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: GREGORIAN
    "من 15/03/2023 م إلى 01/04/2024 م", # From 15th March 2023 CE to 1st April 2024 CE
    "15/يناير/2022 م - 10/فبراير/2023 م", # 15th January 2022 CE - 10th February 2023 CE
    "27/ديسمبر/2024 م / 01/يناير/2025 م", # 27th December 2024 CE / 1st January 2025 CE
    "من 10/مارس/2021 م إلى 25/أبريل/2022 م", # From 10th March 2021 CE to 25th April 2022 CE
    "25/12/2021 م / 01/01/2022 م", # 25th December 2021 CE / 1st January 2022 CE
    "14/February/2023 CE - 20/March/2024 CE", # 14th February 2023 CE - 20th March 2024 CE
    "من 22/نوفمبر/2024 م إلى 08/ديسمبر/2024 م", # From 22nd November 2024 CE to 8th December 2024 CE
    "17/September/2025 CE / 29/October/2025 CE", # 17th September 2025 CE / 29th October 2025 CE
    "من 04/يوليو/2023 م إلى 15/أغسطس/2023 م", # From 4th July 2023 CE to 15th August 2023 CE
    "31/مايو/2022 م - 12/يونيو/2022 م", # 31st May 2022 CE - 12th June 2022 CE
    "من ١٥ مارس ٢٠٢٣ م إلى ٢٠ أبريل ٢٠٢٤ م", # From 15th March 2023 CE to 20th April 2024 CE
    
    # variable: date_patterns.cs_dd_mm_yy.gregorian.mixed_parenthetical
    # type: "combined", name : "single_mixed_dd_mm_yy_gregorian_parenthetical", format: [DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]), calendar: GREGORIAN
    "من 15/03/2023 م إلى (01/04/2024 م)", # From 15th March 2023 CE to (1st April 2024 CE)
    "15/يناير/2022 م - (10/فبراير/2023 م)", # 15th January 2022 CE - (10th February 2023 CE)
    "من 10/مارس/2021 م إلى (25/أبريل/2022 م)", # From 10th March 2021 CE to (25th April 2022 CE)
    "27/ديسمبر/2024 م - (01/يناير/2025 م)", # 27th December 2024 CE - (1st January 2025 CE)
    "14/February/2023 CE - (20/March/2024 CE)", # 14th February 2023 CE - (20th March 2024 CE)
    "من 22 نوفمبر 2024 م إلى (08 ديسمبر 2024 م)", # From 22nd November 2024 CE to (8th December 2024 CE)
    
    # variable: date_patterns.cs_dd_mm_yy.gregorian.alternative
    # type: "combined", name : "single_alternative_dd_mm_yy_gregorian_hijri", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: GREGORIAN-HIJRI  
    "20/يناير/2023 م/15/محرم/1440 هـ", # 20th January 2023 CE/15th Muharram 1440 AH
    "15/مارس/٢٠٢٤ م - 27/رمضان/١٤٤٥ هـ", # 15th March 2024 CE - 27th Ramadan 1445 AH
    "من 25/ديسمبر/2023 م إلى 10/ذو الحجة/1444 هـ", # From 25th December 2023 CE to 10th Dhul Hijjah 1444 AH
    "10/أبريل/2024 م إلى 01/شوال/1442 هـ", # 10th April 2024 CE to 1st Shawwal 1442 AH
    "20/February/2024 CE - 15/رجب/1445 هـ", # 20th February 2024 CE - 15th Rajab 1445 AH
    "31/December/2025 CE / 25/ذو الحجة/1446 هـ", # 31st December 2025 CE / 25th Dhul Hijjah 1446 AH
    
    # variable: date_patterns.dd_mm_yy.gregorian.alternative_parenthetical
    # type: "combined", name : "single_alternative_dd_mm_yy_gregorian_hijri_parenthetical", format: [DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "20/يناير/2023 م/(15/محرم/1440 هـ)", # 20th January 2023 CE/(15th Muharram 1440 AH)
    "15/مارس/٢٠٢٤ م - (27/رمضان/١٤٤٥ هـ)", # 15th March 2024 CE - (27th Ramadan 1445 AH)
    "من 25/ديسمبر/2023 م إلى (10/ذو الحجة/1444 هـ)", # From 25th December 2023 CE to (10th Dhul Hijjah 1444 AH)
    "20/February/2024 CE - (15/رجب/1445 هـ)", # 20th February 2024 CE - (15th Rajab 1445 AH)
    "10/أبريل/2024 م - (01/شوال/1442 هـ)", # 10th April 2024 CE - (1st Shawwal 1442 AH)
    "31/December/2025 CE - (25/ذو الحجة/1446 هـ)", # 31st December 2025 CE - (25th Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed
    # type: "combined", name : "dual_dd_mm_yy_gregorian", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: GREGORIAN
    "from 15/January/2023 CE to 10/February/2024 CE - 25/March/2025 CE - 01/April/2026 CE", # From 15th January 2023 CE to 10th February 2024 CE - 25th March 2025 CE - 1st April 2026 CE
    "from 20/March/2020 CE to 15/April/2022 CE - 10/May/2023 CE - 25/June/2024 CE", # From 20th March 2020 CE to 15th April 2022 CE - 10th May 2023 CE - 25th June 2024 CE
    "15/يناير/2024 م - 10/فبراير/2025 م - 25/مارس/2026 م - 01/أبريل/2027 م", # 15th January 2024 CE - 10th February 2025 CE - 25th March 2026 CE - 1st April 2027 CE
    "22/مايو/2023 م - 08/يونيو/2024 م - 17/يوليو/2025 م - 29/أغسطس/2026 م", # 22nd May 2023 CE - 8th June 2024 CE - 17th July 2025 CE - 29th August 2026 CE
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_gregorian_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN
    "from 15/January/2023 CE to 10/February/2024 CE - (25/March/2025 CE - 01/April/2026 CE)", # From 15th January 2023 CE to 10th February 2024 CE - (25th March 2025 CE - 1st April 2026 CE)
    "from 20/March/2020 CE to 15/April/2022 CE - (10/May/2023 CE - 25/June/2024 CE)", # From 20th March 2020 CE to 15th April 2022 CE - (10th May 2023 CE - 25th June 2024 CE)
    "15/يناير/2024 م - 10/فبراير/2025 م - (25/مارس/2026 م - 01/أبريل/2027 م)", # 15th January 2024 CE - 10th February 2025 CE - (25th March 2026 CE - 1st April 2027 CE)
    "22/مايو/2023 م - 08/يونيو/2024 م - (17/يوليو/2025 م - 29/أغسطس/2026 م)", # 22nd May 2023 CE - 8th June 2024 CE - (17th July 2025 CE - 29th August 2026 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_gregorian_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN
    "from (15/January/2023 CE to 10/February/2024 CE) - (25/March/2025 CE - 01/April/2026 CE)", # From (15th January 2023 CE to 10th February 2024 CE) - (25th March 2025 CE - 1st April 2026 CE)
    "from (20/March/2020 CE to 15/April/2022 CE) - (10/May/2023 CE - 25/June/2024 CE)", # From (20th March 2020 CE to 15th April 2022 CE) - (10th May 2023 CE - 25th June 2024 CE)
    "(15/يناير/2024 م - 10/فبراير/2025 م) - (25/مارس/2026 م - 01/أبريل/2027 م)", # (15th January 2024 CE - 10th February 2025 CE) - (25th March 2026 CE - 1st April 2027 CE)
    "(22/مايو/2023 م - 08/يونيو/2024 م) - (17/يوليو/2025 م - 29/أغسطس/2026 م)", # (22nd May 2023 CE - 8th June 2024 CE) - (17th July 2025 CE - 29th August 2026 CE)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: GREGORIAN-HIJRI
    "15/يناير/2023 م - 10/فبراير/2024 م - 20/محرم/1445 هـ - 25/صفر/1446 هـ", # 15th January 2023 CE - 10th February 2024 CE - 20th Muharram 1445 AH - 25th Safar 1446 AH
    "20/مارس/2020 م - 15/أبريل/2022 م - 27/رجب/1440 هـ - 01/شعبان/1445 هـ", # 20th March 2020 CE - 15th April 2022 CE - 27th Rajab 1440 AH - 1st Sha'ban 1445 AH
    "25/December/2023 CE - 31/January/2024 CE - 15/ذو الحجة/1444 هـ - 20/محرم/1445 هـ", # 25th December 2023 CE - 31st January 2024 CE - 15th Dhul Hijjah 1444 AH - 20th Muharram 1445 AH
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "15/يناير/2023 م - 10/فبراير/2024 م - (20/محرم/1445 هـ - 25/صفر/1446 هـ)", # 15th January 2023 CE - 10th February 2024 CE - (20th Muharram 1445 AH - 25th Safar 1446 AH)
    "20/مارس/2020 م - 15/أبريل/2022 م - (27/رجب/1440 هـ - 01/شعبان/1445 هـ)", # 20th March 2020 CE - 15th April 2022 CE - (27th Rajab 1440 AH - 1st Sha'ban 1445 AH)
    "25/December/2023 CE - 31/January/2024 CE - (15/ذو الحجة/1444 هـ - 20/محرم/1445 هـ)", # 25th December 2023 CE - 31st January 2024 CE - (15th Dhul Hijjah 1444 AH - 20th Muharram 1445 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.mixed_alternative_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(15/يناير/2023 م - 10/فبراير/2024 م) - (20/محرم/1445 هـ - 25/صفر/1446 هـ)", # (15th January 2023 CE - 10th February 2024 CE) - (20th Muharram 1445 AH - 25th Safar 1446 AH)
    "(20/مارس/2020 م - 15/أبريل/2022 م) - (27/رجب/1440 هـ - 01/شعبان/1445 هـ)", # (20th March 2020 CE - 15th April 2022 CE) - (27th Rajab 1440 AH - 1st Sha'ban 1445 AH)
    "(25/December/2023 CE - 31/January/2024 CE) - (15/ذو الحجة/1444 هـ - 20/محرم/1445 هـ)", # (25th December 2023 CE - 31st January 2024 CE) - (15th Dhul Hijjah 1444 AH - 20th Muharram 1445 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.alternative
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA], calendar: GREGORIAN-HIJRI
    "15/يناير/2023 م - 20/محرم/1445 هـ - 10/فبراير/2024 م - 25/صفر/1446 هـ", # 15th January 2023 CE - 20th Muharram 1445 AH - 10th February 2024 CE - 25th Safar 1446 AH
    "20/مارس/2020 م - 27/رجب/1440 هـ - 15/أبريل/2022 م - 01/شعبان/1445 هـ", # 20th March 2020 CE - 27th Rajab 1440 AH - 15th April 2022 CE - 1st Sha'ban 1445 AH
    "25/December/2023 CE - 15/ذو الحجة/1444 هـ - 31/January/2024 CE - 20/محرم/1445 هـ", # 25th December 2023 CE - 15th Dhul Hijjah 1444 AH - 31st January 2024 CE - 20th Muharram 1445 AH
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.alternative_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian_parenthetical", format: [DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "15/يناير/2023 م - 20/محرم/1445 هـ - (10/فبراير/2024 م - 25/صفر/1446 هـ)", # 15th January 2023 CE - 20th Muharram 1445 AH - (10th February 2024 CE - 25th Safar 1446 AH)
    "20/مارس/2020 م - 27/رجب/1440 هـ - (15/أبريل/2022 م - 01/شعبان/1445 هـ)", # 20th March 2020 CE - 27th Rajab 1440 AH - (15th April 2022 CE - 1st Sha'ban 1445 AH)
    "25/December/2023 CE - 15/ذو الحجة/1444 هـ - (31/January/2024 CE - 20/محرم/1445 هـ)", # 25th December 2023 CE - 15th Dhul Hijjah 1444 AH - (31st January 2024 CE - 20th Muharram 1445 AH)
    
    # variable: date_patterns.dual_dd_mm_yy.gregorian.alternative_double_parenthetical
    # type: "combined", name : "dual_dd_mm_yy_alternative_gregorian_double_parenthetical", format: ([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA])-([DD-MM-YYYY-ERA]-[DD-MM-YYYY-ERA]), calendar: GREGORIAN-HIJRI
    "(15/يناير/2023 م - 20/محرم/1445 هـ) - (10/فبراير/2024 م - 25/صفر/1446 هـ)", # (15th January 2023 CE - 20th Muharram 1445 AH) - (10th February 2024 CE - 25th Safar 1446 AH)
    "(20/مارس/2020 م - 27/رجب/1440 هـ) - (15/أبريل/2022 م - 01/شعبان/1445 هـ)", # (20th March 2020 CE - 27th Rajab 1440 AH) - (15th April 2022 CE - 1st Sha'ban 1445 AH)
    "(25/December/2023 CE - 15/ذو الحجة/1444 هـ) - (31/January/2024 CE - 20/محرم/1445 هـ)", # (25th December 2023 CE - 15th Dhul Hijjah 1444 AH) - (31st January 2024 CE - 20th Muharram 1445 AH)
]

natural_language_examples_hijri = [
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # variable: date_patterns.natural_language.hijri.combined
    # type: "combined", name : "natural_language_hijri", format: [WD-MM-YYYY-ERA], calendar: HIJRI
    "الجمعة 15 محرم 1445 هـ",    # Friday 15th Muharram 1445 AH
    "الأحد 01 رمضان 1446 هجري", # Sunday 1st Ramadan 1446 AH
    "الاثنين 27 رجب 1444 هـ",   # Monday 27th Rajab 1444 AH
    "الثلاثاء 10 ذو الحجة 1445 ه", # Tuesday 10th Dhul Hijjah 1445 AH
    "السبت 25 شعبان 1443 هجرية", # Saturday 25th Sha'ban 1443 AH
    "الخميس 14 ربيع الآخر 1447 هـ.", # Thursday 14th Rabi al-Thani 1447 AH
    "الأربعاء 03 شوال 1445 هـ", # Wednesday 3rd Shawwal 1445 AH
    "الجمعة 21 جمادى الأولى 1446 هجري", # Friday 21st Jumada al-Ula 1446 AH
    "الاثنين 08 جمادى الآخرة 1444 هـ", # Monday 8th Jumada al-Akhirah 1444 AH
    "السبت 12 ذو القعدة 1447 ه", # Saturday 12th Dhul Qi'dah 1447 AH
    "الثلاثاء ٢٧ رمضان ١٤٤٥ هـ", # Tuesday 27th Ramadan 1445 AH
    "الأحد ١٠ محرم ١٤٤٦ هجرية", # Sunday 10th Muharram 1446 AH
    
    # variable: date_patterns.cs_natural_language.hijri.mixed
    # type: "combined", name : "single_mixed_cs_natural_language_hijri", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: HIJRI
    "من الجمعة 10 صفر 1445 هـ إلى الثلاثاء 20 صفر 1445 هـ", # From Friday 10th Safar 1445 AH to Tuesday 20th Safar 1445 AH
    "من الأحد 15 محرم 1445 هـ إلى الاثنين 20 صفر 1445 هـ", # From Sunday 15th Muharram 1445 AH to Monday 20th Safar 1445 AH
    "الجمعة 27 رمضان 1444 هـ - الأحد 01 شوال 1444 هـ", # Friday 27th Ramadan 1444 AH - Sunday 1st Shawwal 1444 AH
    "من الثلاثاء 10 ذو الحجة 1445 هـ إلى السبت 25 محرم 1446 هـ", # From Tuesday 10th Dhul Hijjah 1445 AH to Saturday 25th Muharram 1446 AH
    "الاثنين 21 شعبان 1443 هجري / الخميس 14 رمضان 1443 هجري", # Monday 21st Sha'ban 1443 AH / Thursday 14th Ramadan 1443 AH
    "من الأربعاء 03 شوال 1445 هـ إلى الجمعة 21 شوال 1445 هـ", # From Wednesday 3rd Shawwal 1445 AH to Friday 21st Shawwal 1445 AH
    "السبت 12 ذو القعدة 1447 هـ - الاثنين 08 ذو الحجة 1447 هـ", # Saturday 12th Dhul Qi'dah 1447 AH - Monday 8th Dhul Hijjah 1447 AH
    "من الخميس 14 ربيع الأول 1446 هـ إلى الأحد 25 ربيع الآخر 1446 هـ", # From Thursday 14th Rabi al-Awwal 1446 AH to Sunday 25th Rabi al-Thani 1446 AH
    "الثلاثاء 27 جمادى الأولى 1444 هـ / الجمعة 15 جمادى الآخرة 1444 هـ", # Tuesday 27th Jumada al-Ula 1444 AH / Friday 15th Jumada al-Akhirah 1444 AH
    "من الأحد ١٠ محرم ١٤٤٦ هجري إلى الثلاثاء ٢٧ رمضان ١٤٤٥ هـ", # From Sunday 10th Muharram 1446 AH to Tuesday 27th Ramadan 1445 AH
    "الاثنين 05 رجب 1445 هـ - الأربعاء 18 شعبان 1445 هـ", # Monday 5th Rajab 1445 AH - Wednesday 18th Sha'ban 1445 AH
    
    # variable: date_patterns.cs_natural_language.hijri.mixed_parenthetical
    # type: "combined", name : "single_mixed_cs_natural_language_hijri_parenthetical", format: [WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]), calendar: HIJRI
    "من الجمعة 10 صفر 1445 هـ إلى (الثلاثاء 20 صفر 1445 هـ)", # From Friday 10th Safar 1445 AH to (Tuesday 20th Safar 1445 AH)
    "الأحد 15 محرم 1445 هـ - (الاثنين 20 صفر 1445 هـ)", # Sunday 15th Muharram 1445 AH - (Monday 20th Safar 1445 AH)
    "من الثلاثاء 10 ذو الحجة 1445 هـ إلى (السبت 25 محرم 1446 هـ)", # From Tuesday 10th Dhul Hijjah 1445 AH to (Saturday 25th Muharram 1446 AH)
    "الجمعة 27 رمضان 1444 هـ - (الأحد 01 شوال 1444 هـ)", # Friday 27th Ramadan 1444 AH - (Sunday 1st Shawwal 1444 AH)
    "من الأربعاء 03 شوال 1445 هـ إلى (الجمعة 21 شوال 1445 هـ)", # From Wednesday 3rd Shawwal 1445 AH to (Friday 21st Shawwal 1445 AH)
    "الاثنين 21 شعبان 1443 هجري - (الخميس 14 رمضان 1443 هجري)", # Monday 21st Sha'ban 1443 AH - (Thursday 14th Ramadan 1443 AH)
    
    # variable: date_patterns.cs_natural_language.hijri.alternative
    # type: "combined", name : "single_alternative_cs_natural_language_hijri_gregorian", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN  
    "الجمعة 15 محرم 1440 هـ/السبت 20 يناير 2023 م", # Friday 15th Muharram 1440 AH/Saturday 20th January 2023 CE
    "الأحد 27 رمضان ١٤٤٥ هـ - الاثنين 15 مارس ٢٠٢٤ م", # Sunday 27th Ramadan 1445 AH - Monday 15th March 2024 CE
    "من الثلاثاء 10 ذو الحجة 1444 هـ إلى الأربعاء 25 ديسمبر 2023 م", # From Tuesday 10th Dhul Hijjah 1444 AH to Wednesday 25th December 2023 CE
    "الخميس 01 شوال 1442 هـ إلى الجمعة 10 أبريل 2024 م", # Thursday 1st Shawwal 1442 AH to Friday 10th April 2024 CE
    "السبت 15 رجب 1445 هـ - Sunday 20 February 2024 CE", # Saturday 15th Rajab 1445 AH - Sunday 20th February 2024 CE
    "الاثنين 03 شعبان 1446 هجري / Tuesday 25 March 2025 CE", # Monday 3rd Sha'ban 1446 AH / Tuesday 25th March 2025 CE
    
    # variable: date_patterns.natural_language.hijri.alternative_parenthetical
    # type: "combined", name : "single_alternative_cs_natural_language_hijri_gregorian_parenthetical", format: [WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "الجمعة 15 محرم 1440 هـ/(السبت 20 يناير 2023 م)", # Friday 15th Muharram 1440 AH/(Saturday 20th January 2023 CE)
    "الأحد 27 رمضان ١٤٤٥ هـ - (الاثنين 15 مارس ٢٠٢٤ م)", # Sunday 27th Ramadan 1445 AH - (Monday 15th March 2024 CE)
    "من الثلاثاء 10 ذو الحجة 1444 هـ إلى (الأربعاء 25 ديسمبر 2023 م)", # From Tuesday 10th Dhul Hijjah 1444 AH to (Wednesday 25th December 2023 CE)
    "السبت 15 رجب 1445 هـ - (Sunday 20 February 2024 CE)", # Saturday 15th Rajab 1445 AH - (Sunday 20th February 2024 CE)
    "الخميس 01 شوال 1442 هـ - (الجمعة 10 أبريل 2024 م)", # Thursday 1st Shawwal 1442 AH - (Friday 10th April 2024 CE)
    "الاثنين 03 شعبان 1446 هجري - (Tuesday 25 March 2025 CE)", # Monday 3rd Sha'ban 1446 AH - (Tuesday 25th March 2025 CE)
    
    # variable: date_patterns.dual_natural_language.hijri.mixed
    # type: "combined", name : "dual_cs_natural_language_hijri", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: HIJRI
    "من الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ - الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ", # From Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH - Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH
    "من الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ - الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ", # From Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH - Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH
    "من الأحد 09 ربيع الأول 1440 هـ إلى الاثنين 15 ربيع الآخر 1445 هـ - الثلاثاء 20 جمادى الأولى 1446 هـ - الأربعاء 05 جمادى الآخرة 1447 هـ", # From Sunday 9th Rabi al-Awwal 1440 AH to Monday 15th Rabi al-Thani 1445 AH - Tuesday 20th Jumada al-Ula 1446 AH - Wednesday 5th Jumada al-Akhirah 1447 AH
    
    # variable: date_patterns.dual_natural_language.hijri.mixed_parenthetical
    # type: "combined", name : "dual_cs_natural_language_hijri_parenthetical", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI
    "من الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ - (الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ)", # From Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH - (Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH)
    "من الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ - (الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ)", # From Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH - (Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_natural_language.hijri.mixed_double_parenthetical
    # type: "combined", name : "dual_cs_natural_language_hijri_double_parenthetical", format: ([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA])-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI
    "من (الجمعة 15 محرم 1440 هـ إلى السبت 10 صفر 1441 هـ) - (الأحد 25 رجب 1446 هـ - الاثنين 01 شعبان 1447 هـ)", # From (Friday 15th Muharram 1440 AH to Saturday 10th Safar 1441 AH) - (Sunday 25th Rajab 1446 AH - Monday 1st Sha'ban 1447 AH)
    "من (الثلاثاء 27 رمضان 1442 هـ إلى الأربعاء 15 شوال 1444 هـ) - (الخميس 10 ذو القعدة 1445 هـ - الجمعة 25 ذو الحجة 1446 هـ)", # From (Tuesday 27th Ramadan 1442 AH to Wednesday 15th Shawwal 1444 AH) - (Thursday 10th Dhul Qi'dah 1445 AH - Friday 25th Dhul Hijjah 1446 AH)
    
    # variable: date_patterns.dual_natural_language.hijri.mixed_alternative
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "من الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ - الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م", # From Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH - Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE
    "من الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ - السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م", # From Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH - Saturday 20th January 2023 CE - Sunday 25th February 2024 CE
    
    # variable: date_patterns.dual_natural_language.hijri.mixed_alternative_parenthetical
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri_parenthetical", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ - (الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م)", # From Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH - (Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE)
    "من الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ - (السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م)", # From Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH - (Saturday 20th January 2023 CE - Sunday 25th February 2024 CE)
    
    # variable: date_patterns.dual_natural_language.hijri.mixed_alternative_double_parenthetical
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri_double_parenthetical", format: ([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA])-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "من (الأحد 27 رمضان 1445 هـ إلى الاثنين 01 شوال 1446 هـ) - (الثلاثاء 15 مارس ٢٠٢٤ م - الأربعاء 10 أبريل ٢٠٢٥ م)", # From (Sunday 27th Ramadan 1445 AH to Monday 1st Shawwal 1446 AH) - (Tuesday 15th March 2024 CE - Wednesday 10th April 2025 CE)
    "من (الخميس 15 محرم 1440 هـ إلى الجمعة 10 صفر 1445 هـ) - (السبت 20 يناير ٢٠٢٣ م - الأحد 25 فبراير ٢٠٢٤ م)", # From (Thursday 15th Muharram 1440 AH to Friday 10th Safar 1445 AH) - (Saturday 20th January 2023 CE - Sunday 25th February 2024 CE)
    
    # variable: date_patterns.dual_natural_language.hijri.alternative
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: HIJRI-GREGORIAN
    "الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م - الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م", # Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE - Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE
    
    # variable: date_patterns.dual_natural_language.hijri.alternative_parenthetical
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri_parenthetical", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م - (الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م)", # Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE - (Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE)
    "الخميس 15 محرم ١٤٤٠ هـ - السبت 20 يناير ٢٠٢٣ م - (الجمعة 10 صفر 1445 هـ - الأحد 25 فبراير ٢٠٢٤ م)", # Thursday 15th Muharram 1440 AH - Saturday 20th January 2023 CE - (Friday 10th Safar 1445 AH - Sunday 25th February 2024 CE)
    
    # variable: date_patterns.dual_natural_language.hijri.alternative_double_parenthetical
    # type: "combined", name : "dual_cs_natural_language_alternative_hijri_double_parenthetical", format: ([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA])-([WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA]), calendar: HIJRI-GREGORIAN
    "(الأحد 27 رمضان ١٤٤٥ هـ - الثلاثاء 15 مارس ٢٠٢٤ م) - (الاثنين 01 شوال 1446 هـ - الأربعاء 10 أبريل ٢٠٢٤ م)", # (Sunday 27th Ramadan 1445 AH - Tuesday 15th March 2024 CE) - (Monday 1st Shawwal 1446 AH - Wednesday 10th April 2024 CE)
    "(الخميس 15 محرم ١٤٤٠ هـ - السبت 20 يناير ٢٠٢٣ م) - (الجمعة 10 صفر 1445 هـ - الأحد 25 فبراير ٢٠٢٤ م)", # (Thursday 15th Muharram 1440 AH - Saturday 20th January 2023 CE) - (Friday 10th Safar 1445 AH - Sunday 25th February 2024 CE)
]

natural_language_examples_gregorian = [
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # variable: date_patterns.natural_language.gregorian.combined
    # type: "combined", name : "natural_language_gregorian", format: [WD-MM-YYYY-ERA], calendar: GREGORIAN 
    "الجمعة 15 يناير 2023 ميلاديًا",  # Friday 15th January 2023 CE
    "الأحد 25 ديسمبر 2024 م",        # Sunday 25th December 2024 CE
    "Monday 04 July 2023 CE",       # Monday 4th July 2023 CE
    "الثلاثاء 14 فبراير 2025 ميلادي", # Tuesday 14th February 2025 CE
    "Saturday 31 December 2022 AD", # Saturday 31st December 2022 CE
    "الخميس 01 مارس 2024 ميلادية",   # Thursday 1st March 2024 CE
    "الأربعاء 22 نوفمبر 2024 م",     # Wednesday 22nd November 2024 CE
    "Sunday 08 أغسطس 2022 CE",      # Sunday 8th August 2022 CE
    "الاثنين 17 سبتمبر 2025 ميلادي", # Monday 17th September 2025 CE
    "Friday 29 مايو 2023 AD",       # Friday 29th May 2023 CE
    "السبت ١٥ يناير ٢٠٢٣ م",        # Saturday 15th January 2023 CE
    "الثلاثاء ٢٥ ديسمبر ٢٠٢٤ ميلادية", # Tuesday 25th December 2024 CE
    
    # variable: date_patterns.cs_natural_language.gregorian.mixed
    # type: "combined", name : "single_mixed_cs_natural_language_gregorian", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: GREGORIAN 
    "من الجمعة 01 مارس 2023 م إلى الاثنين 10 أبريل 2023 م", # From Friday 1st March 2023 CE to Monday 10th April 2023 CE
    "من الأحد 10 يناير 2024 م إلى الاثنين 20 ديسمبر 2024 م", # From Sunday 10th January 2024 CE to Monday 20th December 2024 CE
    "من الجمعة 01 مارس 2023 م إلى الأحد 19 نوفمبر 2023 م", # From Friday 1st March 2023 CE to Sunday 19th November 2023 CE
    "الثلاثاء 15 يناير 2022 م - الأربعاء 10 فبراير 2023 م", # Tuesday 15th January 2022 CE - Wednesday 10th February 2023 CE
    "الخميس 27 ديسمبر 2024 م / الجمعة 01 يناير 2025 م", # Thursday 27th December 2024 CE / Friday 1st January 2025 CE
    "من السبت 10 مارس 2021 م إلى الأحد 25 أبريل 2022 م", # From Saturday 10th March 2021 CE to Sunday 25th April 2022 CE
    "الاثنين 25 ديسمبر 2021 م / الثلاثاء 01 يناير 2022 م", # Monday 25th December 2021 CE / Tuesday 1st January 2022 CE
    "Wednesday 14 February 2023 CE - Thursday 20 March 2024 CE", # Wednesday 14th February 2023 CE - Thursday 20th March 2024 CE
    "من الجمعة 22 نوفمبر 2024 م إلى السبت 08 ديسمبر 2024 م", # From Friday 22nd November 2024 CE to Saturday 8th December 2024 CE
    "Sunday 17 September 2025 CE / Monday 29 October 2025 CE", # Sunday 17th September 2025 CE / Monday 29th October 2025 CE
    "من الثلاثاء 04 يوليو 2023 م إلى الأربعاء 15 أغسطس 2023 م", # From Tuesday 4th July 2023 CE to Wednesday 15th August 2023 CE
    "الجمعة ٠١ مارس ٢٠٢٣ م - الاثنين ١٠ أبريل ٢٠٢٣ م", # From Friday 1st March 2023 CE to Monday 10th April 2023 CE
    "الثلاثاء ١٥ يناير ٢٠٢٢ م - الأربعاء ١٠ فبراير ٢٠٢٣ م", # Tuesday 15th January 2022 CE - Wednesday 10th February 2023 CE
    "الخميس ٢٧ ديسمبر ٢٠٢٤ م / الجمعة ٠١ يناير ٢٠٢٥ م", # Thursday 27th December 2024 CE / Friday 1st January 2025 CE
    "من الأحد ١٠ يناير ٢٠٢٤ م إلى الاثنين ٢٠ ديسمبر ٢٠٢٤ م", # From Sunday 10th January 2024 CE to Monday 20th December 2024 CE
    "الاثنين ٢٥ ديسمبر ٢٠٢١ م / الثلاثاء ٠١ يناير ٢٠٢٢ م", # Monday 25th December 2021 CE / Tuesday 1st January 2022 CE
    "من السبت ١٠ مارس ٢٠٢١ م إلى الأحد ٢٥ أبريل ٢٠٢٢ م", # From Saturday 10th March 2021 CE to Sunday 25th April 2022 CE
    "الجمعة ٢٢ نوفمبر ٢٠٢٤ م إلى السبت ٠٨ ديسمبر ٢٠٢٤ م", # From Friday 22nd November 2024 CE to Saturday 8th December 2024 CE
    "من الثلاثاء ٠٤ يوليو ٢٠٢٣ م إلى الأربعاء ١٥ أغسطس ٢٠٢٣ م", # From Tuesday 4th July 2023 CE to Wednesday 15th August 2023 CE
    "Sunday 17 September 2025 CE / Monday 29 October 2025 CE", # Sunday 17th September 2025 CE / Monday 29th October 2025 CE
    
    # variable: date_patterns.cs_natural_language.gregorian.mixed_parenthetical
    # type: "combined", name : "single_mixed_cs_natural_language_gregorian_parenthetical", format: [WD-MM-YYYY-ERA]-([WD-MM-YYYY-ERA]), calendar: GREGORIAN 
    "من الجمعة 01 مارس 2023 م إلى (الاثنين 10 أبريل 2023 م)", # From Friday 1st March 2023 CE to (Monday 10th April 2023 CE)
    "من الأحد 10 يناير 2024 م إلى (الاثنين 20 ديسمبر 2024 م)", # From Sunday 10th January 2024 CE to (Monday 20th December 2024 CE)
    "الثلاثاء 15 يناير 2022 م - (الأربعاء 10 فبراير 2023 م)", # Tuesday 15th January 2022 CE - (Wednesday 10th February 2023 CE)
    "الخميس 27 ديسمبر 2024 م / (الجمعة 01 يناير 2025 م)", # Thursday 27th December 2024 CE / (Friday 1st January 2025 CE)
    "من السبت 10 مارس 2021 م إلى (الأحد 25 أبريل 2022 م)", # From Saturday 10th March 2021 CE to (Sunday 25th April 2022 CE)
    "الاثنين 25 ديسمبر 2021 م / (الثلاثاء 01 يناير 2022 م)", # Monday 25th December 2021 CE / (Tuesday 1st January 2022 CE)
    "Wednesday 14 February 2023 CE - (Thursday 20 March 2024 CE)", # Wednesday 14th February 2023 CE - (Thursday 20th March 2024 CE)
    "من الجمعة 22 نوفمبر 2024 م إلى (السبت 08 ديسمبر 2024 م)", # From Friday 22nd November 2024 CE to (Saturday 8th December 2024 CE)
    "Sunday 17 September 2025 CE / (Monday 29 October 2025 CE)", # Sunday 17th September 2025 CE / (Monday 29th October 2025 CE)
    "من الثلاثاء 04 يوليو 2023 م إلى (الأربعاء 15 أغسطس 2023 م)", # From Tuesday 4th July 2023 CE to (Wednesday 15th August 2023 CE)
    "الجمعة ٠١ مارس ٢٠٢٣ م - (الاثنين ١٠ أبريل ٢٠٢٣ م)", # From Friday 1st March 2023 CE to (Monday 10th April 2023 CE)
    "الثلاثاء ١٥ يناير ٢٠٢٢ م - (الأربعاء ١٠ فبراير ٢٠٢٣ م)", # Tuesday 15th January 2022 CE - (Wednesday 10th February 2023 CE)
    "الخميس ٢٧ ديسمبر ٢٠٢٤ م / (الجمعة ٠١ يناير ٢٠٢٥ م)", # Thursday 27th December 2024 CE / (Friday 1st January 2025 CE)
    "من الأحد ١٠ يناير ٢٠٢٤ م إلى (الاثنين ٢٠ ديسمبر ٢٠٢٤ م)", # From Sunday 10th January 2024 CE to (Monday 20th December 2024 CE)
    "الاثنين ٢٥ ديسمبر ٢٠٢١ م / (الثلاثاء ٠١ يناير ٢٠٢٢ م)", # Monday 25th December 2021 CE / (Tuesday 1st January 2022 CE)
    "من السبت ١٠ مارس ٢٠٢١ م إلى (الأحد ٢٥ أبريل ٢٠٢٢ م)", # From Saturday 10th March 2021 CE to (Sunday 25th April 2022 CE)
    "الجمعة ٢٢ نوفمبر ٢٠٢٤ م إلى (السبت ٠٨ ديسمبر ٢٠٢٤ م)", # From Friday 22nd November 2024 CE to (Saturday 8th December 2024 CE)
    "من الثلاثاء ٠٤ يوليو ٢٠٢٣ م إلى (الأربعاء ١٥ أغسطس ٢٠٢٣ م)", # From Tuesday 4th July 2023 CE to (Wednesday 15th August 2023 CE)
    "Sunday 17 September 2025 CE / (Monday 29 October 2025 CE)", # Sunday 17th September 2025 CE / (Monday 29th October 2025 CE)
    
    # variable: date_patterns.cs_natural_language.gregorian.alternative
    # type: "combined", name : "single_alternative_cs_natural_language_gregorian_hijri", format: [WD-MM-YYYY-ERA]-[WD-MM-YYYY-ERA], calendar: GREGORIAN-HIJRI  
    "الجمعة 15 يناير 2023 م/السبت 10 محرم 1445 هـ", # Friday 15th January 2023 CE/Saturday 10th Muharram 1445 AH
    "الأحد 25 ديسمبر 2024 م - الاثنين 12 جمادى الأولى 1446 هـ", # Sunday 25th December 2024 CE - Monday 12th Jumada al-Ula 1446 AH
    "من الثلاثاء 04 يوليو 2023 م إلى الأربعاء 20 ذو الحجة 1444 هـ", # From Tuesday 4th July 2023 CE to Wednesday 20th Dhul Hijjah 1444 AH
    "الخميس 14 فبراير 2025 م إلى الجمعة 22 ربيع الآخر 1446 هـ", # Thursday 14th February 2025 CE to Friday 22nd Rabi al-Thani 1446 AH
    "Saturday 31 December 2022 AD - Sunday 10 ربيع الأول 1444 هـ", # Saturday 31st December 2022 CE - Sunday 10th Rabi al-Awwal 1444 AH
    "من الخميس 01 مارس 2024 م إلى الجمعة 15 شعبان 1445 هـ", # From Thursday 1st March 2024 CE to Friday 15th Sha'ban 1445 AH
    "الأربعاء 22 نوفمبر 2024 م / الخميس 30 رمضان 1445 هـ", # Wednesday 22nd November 2024 CE / Thursday 30th Ramadan 1445 AH
    "Sunday 08 أغسطس 2022 CE - Monday 16 ذو القعدة 1443 هـ", # Sunday 8th August 2022 CE - Monday 16th Dhul Qi'dah 1443 AH
    "من الاثنين 17 سبتمبر 2025 م إلى الثلاثاء 25 صفر 1447 هـ", # From Monday 17th September 2025 CE to Tuesday 25th Safar 1447 AH
    "Friday 29 مايو 2023 AD / Saturday 07 شوال 1444 هـ", # Friday 29th May 2023 CE / Saturday 7th Shawwal 1444 AH
    "الجمعة ١٥ يناير ٢٠٢٣ م/السبت ١٠ محرم ١٤٤٥ هـ", # Friday 15th January 2023 CE/Saturday 10th Muharram 1445 AH
    "الأحد ٢٥ ديسمبر ٢٠٢٤ م - الاثنين ١٢ جمادى الأولى ١٤٤٦ هـ", # Sunday 25th December 2024 CE - Monday 12th Jumada al-Ula 1446 AH
    "من الثلاثاء ٠٤ يوليو ٢٠٢٣ م إلى الأربعاء ٢٠ ذو الحجة ١٤٤٤ هـ", # From Tuesday 4th July 2023 CE to Wednesday 20th Dhul Hijjah 1444 AH
    "الخميس ١٤ فبراير ٢٠٢٥ م إلى الجمعة ٢٢ ربيع الآخر ١٤٤٦ هـ", # Thursday 14th February 2025 CE to Friday 22nd Rabi al-Thani 1446 AH
    "Saturday 31 December 2022 AD - Sunday 10 ربيع الأول 1444 هـ", # Saturday 31st December 2022 CE - Sunday 10th Rabi al-Awwal 1444 AH
    "من الخميس ٠١ مارس ٢٠٢٤ م إلى الجمعة ١٥ شعبان ١٤٤٥ هـ", # From Thursday 1st March 2024 CE to Friday 15th Sha'ban 1445 AH
    "الأربعاء ٢٢ نوفمبر ٢٠٢٤ م / الخميس ٣٠ رمضان ١٤٤٥ هـ", # Wednesday 22nd November 2024 CE / Thursday 30th Ramadan 1445 AH
    "Sunday 08 أغسطس 2022 CE - Monday 16 ذو القعدة 1443 هـ", # Sunday 8th August 2022 CE - Monday 16th Dhul Qi'dah 1443 AH
    "من الاثنين ١٧ سبتمبر ٢٠٢٥ م إلى الثلاثاء ٢٥ صفر ١٤٤٧ هـ", # From Monday 17th September 2025 CE to Tuesday 25th Safar 1447 AH
    "Friday 29 مايو 2023 AD / Saturday 07 شوال 1444 هـ", # Friday 29th May 2023 CE / Saturday 7th Shawwal 1444 AH
]





examples_ = [
    "الجمعة 15 يناير 2023 م إلى الجمعة 15 محرم 1445 هـ",
    "الأحد 1 فبراير 2024 م إلى الجمعة 20 رجب 1445 هـ",
    "الاثنين 30 ديسمبر 2022 م إلى الاثنين 6 جمادى الثانية 1444 هـ",
    "الأربعاء 15/03/2023 م إلى الاثنين 15/03/1445 هـ",
    "الثلاثاء 01/01/2024 م إلى الثلاثاء 19/06/1445 هـ",

    "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
    "من 01 رمضان 1444 هـ إلى 10 رمضان 1444 هـ",
    "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
    "من 01 مارس 2022 م إلى 15 أبريل 2022 م",
    "من 15 محرم 1445 إلى 20 صفر 1445",
    "من 10 يناير 2024 إلى 20 ديسمبر 2024",
    "من الأحد - 15 محرم 1445 هـ إلى الثلاثاء - 20 صفر 1445 هـ",
    "من الأحد - 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
    "من الأحد - 10 يناير 2024 م إلى الأربعاء - 20 ديسمبر 2024 م",
    "من الأحد - 15 محرم 1445 هـ إلى الاثنين - 20 صفر 1445 هـ",
    "من الأحد - 10 يناير 2024 م إلى الاثنين - 20 ديسمبر 2024 م",
    "من 1440 هـ إلى 1445 هـ",
    "1441 هـ إلى 1443 هـ",
    "عام 1430 هـ إلى 1440 هـ",
    "من 2020 م إلى 2024 م",
    "2021 م حتى 2023 م",
    "بين عامي 2019 م و 2022 م",
    "من 1402 هـ.ش إلى 1405 هـ.ش",
    "1400 هـ.ش حتى 1403 هـ.ش",
    "من 1440 هـ إلى 1445 هـ",
    "1442 هـ إلى 1444",
    "من 2020 م إلى 2024 م",
    "2021 م إلى 2023",
    "من 1402 هـ.ش إلى 1405 هـ.ش",
    "1403 هـ.ش إلى 1406",
    "من محرم 1440 هـ إلى صفر 1445 هـ",
    "رجب 1435 هـ حتى شعبان 1440 هـ",
    "من يناير 2020 م إلى ديسمبر 2024 م",
    "مارس 2022 م حتى أكتوبر 2023 م",
    "من فروردین 1402 هـ.ش إلى خرداد 1405 هـ.ش",
    "مرداد 1399 هـ.ش حتى فروردین 1403 هـ.ش",
    "من محرم 1440 هـ إلى صفر 1445 هـ",
    "ربيع الأول 1435 هـ إلى رجب 1440",
    "من يناير 2020 م إلى ديسمبر 2024 م",
    "مارس 2022 م إلى نوفمبر 2024",
    "من فروردین 1402 هـ.ش إلى خرداد 1405 هـ.ش",
    "تیر 1399 هـ.ش إلى اسفند 1403",
    "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
    "10 رجب 1430 هـ حتى 25 شعبان 1442 هـ",
    "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
    "1 مارس 2020 م حتى 15 أكتوبر 2021 م" 
    "من 10 فروردین 1402 هـ.ش إلى 20 خرداد 1405 هـ.ش",
    "5 اسفند 1398 هـ.ش حتى 1 فروردین 1403 هـ.ش",
    "من 15 محرم 1445 هـ إلى 20 صفر 1445 هـ",
    "1 رمضان 1440 هـ حتى 10 شوال 1440",
    "من 10 يناير 2024 م إلى 20 ديسمبر 2024 م",
    "5 فبراير 2021 م حتى 18 مايو 2022",
    "من 10 فروردین 1402 هـ.ش إلى 20 خرداد 1405 هـ.ش",
    "1 دی 1399 هـ.ش حتى 15 بهمن 1403",
    "من الأحد - 15 محرم 1445 هـ إلى الخميس - 20 صفر 1445 هـ",
    "السبت 5 رجب 1432 هـ حتى الثلاثاء 10 شعبان 1432 هـ",
    "من الأحد - 10 يناير 2024 م إلى الخميس - 20 ديسمبر 2024 م",
    "الثلاثاء 5 مارس 2023 م حتى الجمعة 10 أبريل 2023",
    "من شنبه - 10 فروردین 1402 هـ.ش إلى پنج‌شنبه - 20 خرداد 1405 هـ.ش",
    "سه‌شنبه 1 اسفند 1399 هـ.ش حتى جمعه 10 فروردین 1400 هـ.ش",
    "من الأحد - 15 محرم 1445 هـ إلى الخميس - 20 صفر 1445 هـ",
    "الثلاثاء - 10 رمضان 1435 هـ حتى الجمعة 20 شوال 1435",
    "من الأحد - 10 يناير 2024 م إلى الخميس - 20 ديسمبر 2024 م",
    "الاثنين - 5 فبراير 2021 م حتى الخميس 18 مايو 2022",
    "من شنبه - 10 فروردین 1402 هـ.ش إلى پنج‌شنبه - 20 خرداد 1405 هـ.ش",
    "جمعه - 1 آذر 1397 هـ.ش حتى دوشنبه 12 دی 1400 هـ.ش",
    "(1440 - 1445) (2019 - 2024)",
    "[1441–1443] [2020–2022]",
    "(1440 هـ - 1445 هـ) (2019 م - 2024 م)",
    "[1442هـ–1444هـ] [2021م–2023م]",
    "(2020 م - 2024 م) (1441 هـ - 1445 هـ)",
    "[2022م–2023م] [1443هـ–1444هـ]",
    "(2020 - 2024) (1441 - 1445)",
    "[2022–2023] [1443–1444]",
    "(1440 هـ / 2023 م) (1441 هـ / 2024 م)",
    "[1442هـ/2021م][1443هـ/2022م]",
    "(2023 م / 1444 هـ) (2024 م / 1445 هـ)",
    "[2022م/1443هـ][2023م/1444هـ]",
    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 - ديسمبر 2023)",
    "[01/1441 - 02/1445] [01/2020 - 12/2023]",
    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 م - يوليو 2024 م)",
    "[جمادى الأولى 1438 هـ إلى رمضان 1440 هـ] [فبراير 2017 م إلى يونيو 2019 م]",
    "(يناير 2020 م - ديسمبر 2024 م) (محرم 1441 هـ - ربيع 1447 هـ)",
    "[01/2020 - 12/2024] [01/1441 - 04/1447]",
    "(يناير 2020 م - ديسمبر 2024 م) (جمادى الثانية 1441 هـ - ذو القعدة 1446 هـ)",
    "[مارس 2018 م إلى يونيو 2019 م] [رجب 1439 هـ إلى رمضان 1440 هـ]",
    "(محرم 1440 هـ - صفر 1445 هـ) (يناير 2019 - ديسمبر 2023)",
    "[1/1440 - 2/1445] [1/2019 - 12/2023]",
    "(جمادى الأولى 1435 هـ - شعبان 1440 هـ) (مارس 2014 م - مايو 2019 م)",
    "[صفر 1442 هـ إلى ربيع الثاني 1444 هـ] [أكتوبر 2020 م إلى نوفمبر 2022 م]",
    "(يناير 2020 م - ديسمبر 2024 م) (محرم 1441 هـ - ربيع 1447 هـ)",
    "[1/2020 - 12/2024] [1/1441 - 4/1447]",
    "(يناير 2020 م - ديسمبر 2024 م) (جمادى الأولى 1441 هـ - ذو الحجة 1446 هـ)",
    "[مارس 2018 م إلى يونيو 2019 م] [جمادى الآخرة 1439 هـ إلى رمضان 1440 هـ]",
    "(12/1440 هـ / 01/2023 م) (01/1441 هـ / 02/2023 م)",
    "[جمادى الأولى 1442 هـ / يناير 2021 م] [رجب 1443 هـ / مارس 2022 م]",
    "(يناير 2023 م / محرم 1445 هـ) (فبراير 2023 م / صفر 1445 هـ)",
    "[مارس 2022 م / رجب 1443 هـ] [إبريل 2022 م / شعبان 1443 هـ]",
    "(15/03/1445 هـ / 15/03/2023 م) (16/03/1445 هـ / 16/03/2023 م)",
    "[01/01/1400 هـ / 01/01/1980 م] [02/01/1400 هـ / 02/01/1980 م]",
    "(15/03/2023 م / 15/03/1445 هـ) (16/03/2023 م / 16/03/1445 هـ)",
    "[01/01/1980 م / 01/01/1400 هـ] [02/01/1980 م / 02/01/1400 هـ]",
    "(الجمعة 15 محرم 1445 هـ / 15 يناير 2023 م) (السبت 16 محرم 1445 هـ / 16 يناير 2023 م)",
    "(الجمعة 15 يناير 2023 م / 15 محرم 1445 هـ) (السبت 16 يناير 2023 م / 16 محرم 1445 هـ)",
]

text = "من 1440 هـ إلى 2023 م. في عام 2020 م، حدث شيء مهم. حوالي 1445 هـ كان عامًا مميزًا."
text = "في سنة 1445 هجرية الموافق 2023 ميلادية"
text = "من القرن الثالث الهجري حتى الخامس"
text = "حوالي 1440 هـ إلى 1445 هـ"
text = "بعد سنة 2020 م وقبل 1442 هجري"
text = "القرن الحادي عشر الهجري (السابع عشر الميلادي)"
text = "1445/2023 هـ/م"
text = "من 1440 هـ إلى 2023 م"
text = "سنة 1445 هـ (2023 م) كانت سنة مهمة"
text = "١٤٢٣هـ/٢٠٠٢م"
text = "١٤٣٠ هـ - ٢٠٠٩ م"
text = "١٤١١هـ"
text = "٢٠٠٠م"
text = "١٤١٩هـ - ١٩٩٩م"
text = "(١٤١٦ هـ=١٩٩٦ م) - (١٤٢٢ هـ=٢٠٠٢ م)"     
text = "١٤١٠ - ١٩٩٠"
text = "١٤١١هـ/١٩٩٠م"
text = "١٤٤٠ هـ - ٢٠١٩ م (الأولى لدار ابن حزم)"
text = "العدد الرابع، ربيع ثاني ١٣٩٣ هـ، مايو ١٩٧٣ م"  
text = "العدد الخامس والخمسون والسادس والخمسون، رجب- ذو الحجة ١٤٠٢هـ/١٩٨١"
text = "العدد الثاني غرة ذي الحجة عام ١٣٩٨هـ/١٩٧٨م"
text = "العدد الثاني غرة ذي الحجة عام ١٣٩٨ هـ/١٩٧٨ م"
text = "العدد الثالث، ذو الحجة ١٣٩٥هـ/ ديسمبر ١٩٧٥م"
text = "العدد الأول، رجب ١٣٩٤هـ/١٩٧٤م"
text = "١٤١٧ هـ -١٩٩٦ م"
text = "١٤٢٣ هـ/٢٠٠٢ م"
text = "العدد الحادي عشر بعد المائة، ١٤٢١هـ/٢٠٠٠م"
text = "العدد الثاني والستون - ربيع الآخر - جمادى الآخرة ١٤٠٤هـ/١٩٨٤م"
text = "(١٣٨٩ - ١٤٠٤ هـ) (١٩٦٩ - ١٩٨٤ م)"
text = "العدد الأول، رجب ١٣٩٢هـ/ أغسطس ١٩٧٢م"
text = "صفر، ربيع الأول ١٤٠٢هـ/١٩٨١م"
text = "١٤١٧هـ، ١٩٩٦م"
text = "١٤١١هـ١٩٩١م"
text = "١٤١١ - ١٩٩١"
text = "١٤٢٤هـ-٢٠٠٣م"
text = "١٤٢٠هـ١٩٩٩م"
text = "(١٤١١ - ١٤١٢ هـ) = (١٩٩٠ - ١٩٩٢ م)"
text = "١٣٨١ - ١٣٨٢ هـ = ١٩٦١ - ١٩٦٢ م"
text = "١٤٠٤هـ/١٩٨٤م"
text = "١٣٠٤ - ١٣٠٥ هـ"
text = "١٤٢٤هـ/٢٠٠٣م"
text = "١٤٢٤هـ / ٢٠٠٣م"
text = "العددان - مائة وثلاثة - مائة وأربعة - ١٤١٦/١٤١٧هـ"
text = "بالمطبعة الكبرى الأميرية، ببولاق مصر ١٣١٦ - ١٣١٨ هـ"
text = "ذو الحجة ١٣٩٧هـ نوفمبر - تشرين ثاني ١٩٧٧ م"
text = "٧٢) رجب-ذو الحجة ١٤٠٦هـ."     
text = "العدد الأول، جمادى الأخرة ١٣٩٧هـ مايو - يونية ١٩٧٧ م"    
text = "(١٣٨٨ هـ = ١٩٦٨ م) - (١٣٨٩ هـ = ١٩٦٩ م)"
text = "(١٤٢٩ هـ - ١٤٣٢ هـ)"
text = "١٤٢٠هـ =٢٠٠٠م"
text = "العدد الثاني غرة ذي الحجة عام ١٣٩٨هـ"
text = "من ١٤٢٣ - ١٤٢٩ هـ (ينظر التفصيل بأول كل جزء)"
text = "العدد الأول، رجب ١٣٩٤هـ"
text = "ولد في 10 رمضان 1420 هـ وتوفي في 20 شوال 1435 هـ"
text = "الحدث وقع في 15 يناير 2020 م الموافق 19 جمادى الأولى 1441 هـ"
text = "بين عامي 2010 م – 2015 م حصلت تغييرات كثيرة"
text = "الوثيقة مؤرخة في سنة 1435 هـ"
text = "تخرج عام 2020 ميلادية بعد دراسة دامت خمس سنوات"
text = "أحداث الثورة بدأت في أواخر صفر 1400 هـ واستمرت حتى رمضان 1401 هـ"
text = "في منتصف شوال سنة 1340 هجري"
text = "الفترة: من 2005 م إلى 2015 م",
text = "أظهر تقرير للأمم المتحدةاليوم الجمعة (11 يوليو/ تموز 2025)، "
text = "منذ مايو/أيار 2014 لعقوبات من الأمم المتحدة،"
text = "في يوليو 11, 2025"
text = " يصدر المرسوم الرئاسي رقم (102) لعام 2025 القاضي بزيادة 200% إلى الرواتب والأجور "
text = " 11-7-2025 أو 11.07.2025"
text = "بعض الجرائد قد تدمج بين التقويمين الميلادي والهجري، مثل:11 يوليو 2025 (3 ذو الحجة 1446)"
text = "دمشق 23 و ذو الحجة 1446 هـ 19 حزيران 2025 م."
text = "دمشق 23 و ذو الحجة 1446 هـ - الموافق 19 حزيران 2025 م."
text = "الاحد  | ١٨ محرم ١٤٤٧ هـ 🗓️"
text = "الاثنين - 19 مُحرَّم 1447 هـ - 14 تموز 2025 م"