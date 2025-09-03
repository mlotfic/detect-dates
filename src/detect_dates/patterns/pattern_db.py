#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arabic Date Detection Module
============================

A comprehensive date detection system designed for Arabic text processing.
This module provides pattern-based date recognition with support for various
date formats commonly found in Arabic documents.

The module follows a pipeline architecture where different pattern types
are processed in order of complexity, from complex multi-component dates
down to simple date components.

.. moduleauthor:: Your Name <your.email@example.com>
.. version:: 1.0.0
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


from detect_dates.regex_patterns import get_date_patterns
from .classes import DatePatterns
from .dicts._numeric_words import _fetch_numeric_words
from .dicts._components import _fetch_components
from .dicts._simple_unknown import _fetch_simple_unknown
from .dicts._simple import _fetch_simple
from .dicts._composite import _fetch_composite
from .dicts._complex import _fetch_complex


class PatternDB:
    """
    Pattern Database for Date Detection.
    
    This class serves as the foundation for date pattern management,
    organizing various types of regex patterns used in Arabic date detection.
    It maintains a hierarchical structure of patterns from complex to simple.
    
    The class follows a modular design where different pattern types are
    fetched and organized into a processing pipeline.
    
    Attributes:
        _base_patterns (dict): Core date patterns and components
        _month_patterns (dict): Month name patterns in Arabic
        _era_patterns (dict): Era indicators (هـ، م، etc.)
        _indicator_patterns (dict): Date indicator words
        _numeric_patterns (dict): Numeric date patterns
        _date_patterns (DatePatterns): Consolidated pattern object
        components (dict): Basic date components patterns
        simple_unknown (dict): Simple unidentified date patterns
        simple (dict): Simple date patterns
        composite (dict): Multi-component date patterns
        complex (dict): Complex date patterns with multiple elements
        pipeline (dict): Processing pipeline ordered by complexity
        
    Example:
        >>> pattern_db = PatternDB(lang="ar")
        >>> pipeline_keys = pattern_db.get_pipeline()
        >>> print(list(pipeline_keys))
        ['complex', 'composite', 'simple', 'simple_unknown', 'components']
    """
    
    def __init__(self, lang="ar"):
        """
        Initialize the Pattern Database.
        
        Sets up all pattern categories and creates the processing pipeline.
        The patterns are loaded based on the specified language and organized
        in a hierarchy suitable for sequential processing.
        
        Args:
            lang (str, optional): Language code for pattern loading. 
                                Defaults to "ar" (Arabic).
                                
        Note:
            Currently, the language parameter is hardcoded to "ar" in the
            get_date_patterns call, but the parameter is maintained for
            future extensibility.
        """
        # Unpack pattern data with explicit naming for clarity
        (
            self._base_patterns,
            self._month_patterns,
            self._era_patterns,
            self._indicator_patterns,
            self._numeric_patterns
        ) = get_date_patterns(lang="ar")  # TODO: Use dynamic lang parameter
        
        # Create consolidated date patterns object
        self._date_patterns = DatePatterns(
            base_patterns=self._base_patterns,
            month_patterns=self._month_patterns,
            era_patterns=self._era_patterns,
            indicator_patterns=self._indicator_patterns,
            numeric_patterns=self._numeric_patterns
        )
        
        # Initialize pattern dictionaries in order of complexity
        # Note: numeric_words commented out - may be unused or future feature
        # self.numeric_words = _fetch_numeric_words(self._date_patterns)
        
        # Fetch different categories of patterns
        self.components = _fetch_components(self._date_patterns)
        self.simple_unknown = _fetch_simple_unknown(self._date_patterns)
        self.simple = _fetch_simple(self._date_patterns)
        self.composite = _fetch_composite(self._date_patterns)
        # Note: Fixed bug - was calling _fetch_composite instead of _fetch_complex
        self.complex = _fetch_complex(self._date_patterns)
        
        # Define processing pipeline - order matters for pattern matching
        # Complex patterns are processed first to catch comprehensive matches
        self.pipeline = {
            "complex": self.complex,
            "composite": self.composite,
            "simple": self.simple,
            "simple_unknown": self.simple_unknown,
            "components": self.components
        }
    
    def get_pipeline(self):
        """
        Get the processing pipeline keys.
        
        Returns the ordered list of pattern categories that will be processed
        during date detection. The order represents processing priority.
        
        Returns:
            dict_keys: Pipeline category names in processing order.
            
        Example:
            >>> pattern_db = PatternDB()
            >>> list(pattern_db.get_pipeline())
            ['complex', 'composite', 'simple', 'simple_unknown', 'components']
        """
        return self.pipeline.keys()


class DetectDate(PatternDB):
    """
    Arabic Date Detection Engine.
    
    This class extends PatternDB to provide actual date detection functionality.
    It processes Arabic text through the pattern pipeline to identify and
    extract date expressions.
    
    The detection process follows a hierarchical approach, starting with
    complex patterns and moving to simpler ones, ensuring the most specific
    matches are found first.
    
    Inherits:
        PatternDB: Base pattern management functionality
        
    Example:
        >>> detector = DetectDate(lang="ar")
        >>> text = "المؤتمر سيعقد في 15 مارس 2022"
        >>> matches = detector.match(text)
        >>> if matches:
        ...     print(f"Found: {matches[0].group()}")
        Found: 15 مارس 2022
    """
    
    def __init__(self, lang="ar"):
        """
        Initialize the Date Detection Engine.
        
        Args:
            lang (str, optional): Language code for pattern loading.
                                Defaults to "ar" (Arabic).
        """
        super().__init__(lang=lang)
    
    def match(self, text):
        """
        Detect date patterns in the given text.
        
        Processes the input text through all pattern categories in the pipeline,
        collecting matches from each category. The method returns detailed
        information about detected patterns including metadata and match objects.
        
        Args:
            text (str): The Arabic text to analyze for date patterns.
            
        Returns:
            list: A list of dictionaries containing detection results.
                 Each dictionary includes:
                 - metadata: Pattern category metadata
                 - pattern_name: Name of the matched pattern
                 - matches: List of regex match objects
                 
        Note:
            The current implementation has a bug in the return statement.
            It returns only the last matches instead of all detections.
            This should be fixed to return the complete detection list.
            
        Example:
            >>> detector = DetectDate()
            >>> results = detector.match("تاريخ الميلاد: 01/01/2000")
            >>> for result in results:
            ...     print(f"Pattern: {result['pattern_name']}")
            ...     for match in result['matches']:
            ...         print(f"Found: {match.group()} at {match.span()}")
        """
        detection = []
        
        # Process each pattern category in the pipeline
        for key, value in self.pipeline.items():
            metadata = value["metadata"]
            
            # Test each pattern in the current category
            for patterns_info in value["patterns"]:
                compiled = patterns_info['pattern']
                
                # Find all matches using compiled regex pattern
                matches = list(compiled.finditer(text))
                
                # If matches found, add to detection results
                if matches:
                    # Debug output - consider using logging in production
                    print(f"Text: {text}")
                    print(f"Pattern name: {patterns_info['name']}")
                    
                    # Add detection result with full context
                    detection.append({
                        "metadata": metadata,
                        "pattern_name": patterns_info['name'],
                        "matches": matches
                    })
        
        # FIXME: Should return 'detection' list, not 'matches'
        # Current bug: only returns last matches instead of all detections
        return detection  # Changed from 'matches' to 'detection'


def main():
    """
    Demonstration function for the Date Detection system.
    
    This function showcases the capabilities of the DetectDate class
    using various Arabic text samples containing different date formats.
    """
    # Initialize the date detector for Arabic language
    detector = DetectDate(lang="ar")
    
    # Test cases covering various Arabic date formats
    test_texts = [
        "في عام 2023، حدث شيء مهم.",                    # Year reference
        "المؤتمر سيعقد في 15 مارس 2022.",              # Day Month Year
        "تاريخ الميلاد: 01/01/2000.",                  # Numeric format
        "الاجتماع كان يوم الاثنين الماضي.",            # Relative day reference
        "الموعد النهائي هو 30-12-2021.",               # Dash-separated format
        "حدث في 5 يوليو 2020.",                       # Day Month Year (different month)
        "المناسبة كانت في ٢٠٢١/٠٨/١٥.",               # Arabic numerals
        "الحدث وقع في ١٥ مارس ٢٠٢٢.",                 # Mixed Arabic numerals
    ]
    
    # Process each test case
    for text in test_texts:
        print(f"\nAnalyzing: '{text}'")
        print("-" * 50)
        
        detection_results = detector.match(text)
        
        if detection_results:
            # Process each detection result
            for result in detection_results:
                print(f"Pattern Category: {result['metadata']}")
                print(f"Pattern Name: {result['pattern_name']}")
                
                # Display all matches for this pattern
                for match in result['matches']:
                    matched_text = match.group(0)
                    start_pos, end_pos = match.span()
                    print(f"  → Match: '{matched_text}' at positions {start_pos}-{end_pos}")
                print()
        else:
            print("  No date patterns detected.")


if __name__ == "__main__":
    main()
























from detect_dates.regex_patterns import get_date_patterns

from .classes import DatePatterns

from .dicts._numeric_words import _fetch_numeric_words
from .dicts._components import _fetch_components
from .dicts._simple_unknown import _fetch_simple_unknown
from .dicts._simple import _fetch_simple
from .dicts._composite import _fetch_composite
from .dicts._complex import _fetch_complex




class PatternDB:
    
    def __init__(self, lang="ar"):
        # Unpack pattern data with explicit naming
        (
            self._base_patterns,
            self._month_patterns,
            self._era_patterns,
            self._indicator_patterns,
            self._numeric_patterns
        ) = get_date_patterns(lang="ar")
        #
        self._date_patterns = DatePatterns(
            base_patterns=self._base_patterns,
            month_patterns=self._month_patterns,
            era_patterns=self._era_patterns,
            indicator_patterns=self._indicator_patterns,
            numeric_patterns=self._numeric_patterns
        )
        #
        # self.numeric_words = _fetch_numeric_words(self._date_patterns)
        self.components = _fetch_components(self._date_patterns)
        self.simple_unknown = _fetch_simple_unknown(self._date_patterns)
        self.simple = _fetch_simple(self._date_patterns)
        self.composite = _fetch_composite(self._date_patterns)
        self.complex = _fetch_composite(self._date_patterns)
        
        self.pipeline = {
            "complex" : self.complex,
            "composite" : self.composite,
            "simple" : self.simple,
            "simple_unknown" : self.simple_unknown,
            "components": self.components
        }
        
        def get_pipeline(self):
            return self.pipeline.keys()


class DetectDate(PatternDB):
    
    def __init__(self, lang="ar"):
        

    def match(self, text):
        detection = []
        for key, value in self.pipeline.items():
            metadata = value["metadata"]
            for patterns_info in value["patterns"]:
                compiled = patterns_info['pattern']
                # Step 4: Use finditer (returns iterator)
                matches = list(compiled.finditer(text))
                # Step 5: Get the first match safely
                if matches:
                    print("text :", text)
                    print("pattern name :", patterns_info['name'])
                    detection.append({
                        "metadata" : metadata,
                        "pattern_name": patterns_info['name'],
                        "matches": matches
                    })
        return matches


if __name__ == "__main__":
    # Demonstrate DateDetector with Arabic patterns
    detector = DateDetector(lang="ar")
    test_texts = [
        "في عام 2023، حدث شيء مهم.",
        "المؤتمر سيعقد في 15 مارس 2022.",
        "تاريخ الميلاد: 01/01/2000.",
        "الاجتماع كان يوم الاثنين الماضي.",
        "الموعد النهائي هو 30-12-2021.",
        "حدث في 5 يوليو 2020.",
        "المناسبة كانت في ٢٠٢١/٠٨/١٥.",
        "الحدث وقع في ١٥ مارس ٢٠٢٢.",
        "المؤتمر سيعقد في 15 مارس 2022.",
        "تاريخ الميلاد: 01/01/2000.",
        "الاجتماع كان يوم الاثنين الماضي.",
        "الموعد النهائي هو 30-12-2021.",
        "حدث في 5 يوليو 2020.",
        "المناسبة كانت في ٢٠٢١/٠٨/١٥.",
        "الحدث وقع في ١٥ مارس ٢٠٢٢."
    ]
    for text in test_texts:
        print(f"\nDetecting dates in: '{text}'")
        matches = detector.match(text)
        if matches:
            for match in matches:
                print(f"Matched: {match.group(0)} at positions {match.start()}-{match.end()}")
        else:
           print("No date detected.")


