import re

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
from detect_dates.patterns.classes import DatePatterns
from detect_dates.patterns.dicts import (
    _fetch_numeric_words,
    _fetch_components,
    _fetch_simple_unknown,
    _fetch_simple,
    _fetch_composite,
    _fetch_complex
)


class DateDetector:
    def __init__(self, lang="ar"):
        # Unpack pattern data with explicit naming
        print(f"\n1. Loading {lang} language patterns...")

        # Unpack pattern data with explicit naming
        (
            base_patterns,
            month_patterns,
            era_patterns,
            indicator_patterns,
            numeric_patterns
        ) = get_date_patterns(lang="ar")
        #
        self.date_patterns = DatePatterns(
            base_patterns=base_patterns,
            month_patterns=month_patterns,
            era_patterns=era_patterns,
            indicator_patterns=indicator_patterns,
            numeric_patterns=numeric_patterns
        )
        self.date_unknown_calendar = get_date_unknown_calendar_patterns(
            self.date_patterns
        )
        self.date_basic_pattern_dict = get_date_basic_patterns(
            self.date_patterns
        )
        self.date_components_patterns_dict = get_date_components_patterns(
            self.date_patterns
        )
        self.date_mixed_patterns_dict = get_date_mixed_patterns(
            self.date_patterns
        )
        self.date_complex_dict = get_date_complex(
            self.date_patterns
        )
        self.pipeline = {
            "complex"           : self.date_complex_dict,
            "mixed"             : self.date_mixed_patterns_dict,
            "components"        : self.date_components_patterns_dict,
            "unknown_calendar"  : self.date_unknown_calendar,
        }

    def get_pipeline(self):
        return self.pipeline.keys()

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