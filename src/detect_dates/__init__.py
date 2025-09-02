ar_date_module/
├── regex_patterns/
│   ├── get_pattern.py                # All get_*_pattern functions (era, month, day, year, etc.)
│   ├── keywords_to_regex.py          # Helper for building regex from keywords
│   └── ... (other regex-related files)
│
├── extractors/
│   ├── get_base_pattern_by_lang.py   # Logic for selecting base patterns
│   ├── get_calendar_variants.py      # Calendar variant extraction logic
│   └── ... (other parsing/extraction logic)
│
├── normalizers/
│   ├── normalize_era.py
│   ├── normalize_month.py
│   ├── normalize_numeric_words.py
│   ├── normalize_separators.py
│   ├── calendar_yr_to_yr_cal.py      # Calendar conversion routines
│   └── ... (other normalization/conversion logic)
│
├── utils/
│   ├── __init__.py
│   └── ... (general helpers, validation, fuzzy matching, etc.)
│
├── tests/
│   ├── test_code.py
│   ├── test_text.py
│   └── ... (all test files)
│
├── main.py
├── cli.py
├── README.md
── ...