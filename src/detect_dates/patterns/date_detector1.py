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
    get_date_unknown_calender_patterns,
    get_date_basic_patterns,
    get_date_components_patterns,
    get_date_mixed_patterns,
    get_date_complex,
)


# Unpack pattern data with explicit naming
(
    base_patterns,
    month_patterns,
    era_patterns,
    indicator_patterns,
    numeric_patterns
) = get_date_patterns(lang="ar")

#
date_patterns = DatePatterns(
    base_patterns       = base_patterns,
    month_patterns      = month_patterns,
    era_patterns        = era_patterns,
    indicator_patterns  = indicator_patterns,
    numeric_patterns    = numeric_patterns
)

print(f"   ✓ Arabic patterns loaded: {date_patterns}")

# Demonstrate pattern hierarchy access
print("\n2. Exploring pattern hierarchy...")
all_patterns = date_patterns.get_all_patterns()

for complexity, patterns in all_patterns.items():
    print(f"   {complexity.capitalize()} level: {len(patterns)} pattern types")

# Demonstrate specific pattern access
print("\n3. Accessing specific patterns...")


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
        self.date_unknown_calender = get_date_unknown_calender_patterns(
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
            "unknown_calender"  : self.date_unknown_calender,
        }

    def get_pipeline(self):
        return self.pipeline.keys()

    def match(self, text):
        detection = []
        remaining_text = text
        matched_positions = set()  # Track character positions that have been matched

        for key, value in self.pipeline.items():
            metadata = value["metadata"]
            for patterns_info in reversed(value["patterns"]):
                compiled = patterns_info['pattern']
                # Find matches in the remaining text
                matches = list(compiled.finditer(remaining_text))

                if matches:
                    # Filter out matches that overlap with previously matched positions
                    non_overlapping_matches = []
                    for match in matches:
                        match_positions = set(range(match.start(), match.end()))
                        if not match_positions.intersection(matched_positions):
                            non_overlapping_matches.append(match)
                            matched_positions.update(match_positions)

                    if non_overlapping_matches:
                        print("text :", remaining_text)
                        print("pattern name :", patterns_info['name'])

                        detection.append({
                            "metadata": metadata,
                            "pattern_name": patterns_info['name'],
                            "matches": non_overlapping_matches
                        })

                        # Remove matched text by replacing with spaces to preserve positions
                        for match in sorted(non_overlapping_matches, key=lambda m: m.start(), reverse=True):
                            start, end = match.start(), match.end()
                            remaining_text = remaining_text[:start] + ' ' * (end - start) + remaining_text[end:]

        return detection

    def match_with_details(self, text):
        """Enhanced match method that provides more detailed information"""
        detection = []
        for pipeline_key, value in self.pipeline.items():
            metadata = value["metadata"]
            for patterns_info in value["patterns"]:
                compiled = patterns_info['pattern']
                matches = list(compiled.finditer(text))
                if matches:
                    match_details = []
                    for match in matches:
                        match_details.append({
                            "text": match.group(),
                            "start": match.start(),
                            "end": match.end(),
                            "groups": match.groups(),
                            "groupdict": match.groupdict()
                        })

                    detection.append({
                        "pipeline": pipeline_key,
                        "metadata": metadata,
                        "pattern_name": patterns_info['name'],
                        "match_count": len(matches),
                        "match_details": match_details
                    })
        return detection

    def find_all_dates(self, text, verbose=False):
        """Find all dates in text with optional verbose output"""
        all_detections = self.match(text)

        if verbose:
            print(f"\nAnalyzing text: '{text}'")
            print(f"Found {len(all_detections)} pattern matches:")
            for i, detection in enumerate(all_detections, 1):
                print(f"  {i}. Pattern: {detection['pattern_name']}")
                print(f"     Pipeline: {detection.get('pipeline', 'N/A')}")
                print(f"     Matches: {len(detection['matches'])}")
                for match in detection['matches']:
                    print(f"     Text: '{match.group()}' at position {match.start()}-{match.end()}")
                print()

        return all_detections


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
    ]

    print("Testing DateDetector:")
    print("=" * 50)

    for text in test_texts:
        detections = detector.find_all_dates(text, verbose=True)
       print("-" * 50)