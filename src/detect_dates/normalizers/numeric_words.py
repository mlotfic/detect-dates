#!/usr/bin/env python3
"""
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.
"""

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
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

# Import necessary modules
from detect_dates.keywords import numeric_words_keywords
from detect_dates.regex_patterns import get_numeric_words_pattern

numeric_words_pattern_ar = get_numeric_words_pattern(numeric_words_keywords)