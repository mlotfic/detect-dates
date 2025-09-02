#!/usr/bin/env python3
"""
Created on Sun Jun 22 21:38:10 2025

@author: m.lotfi

@description: This module provides calendar conversion utilities and functions to get calendar variants.
"""

if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # Import path helper to ensure modules directory is in sys.path
    # ===================================================================================
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

# Import necessary modules
from detect_dates.keywords import numeric_words_keywords
from detect_dates.regex_patterns import get_numeric_words_pattern

numeric_words_pattern_ar = get_numeric_words_pattern(numeric_words_keywords)