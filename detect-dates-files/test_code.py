#!/usr/bin/env python3
"""
Created on Thu Jun 26 00:03:56 2025

@author: m
"""
import re


# Import normalization functions - handle import errors gracefully
from modules.normalizers import normalize_month
from modules.normalizers import normalize_era
from modules.normalizers import normalize_weekday
from modules.normalizers import get_match_value

from modules.calendar_variants import get_calendar_variants_by_lang

match = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2023-12-25')
get_match_value(match, idxs=[1, 2])  # Returns '2023'

match_component = {
        "year": "2023",
        "month": "December",
        "day": "25",
        "era": "AD"
    }

result = get_calendar_variants_by_lang(match_component, lang = "en")
result = get_calendar_variants_by_lang(match_component, lang = "ar")

# Step 1: Get the pattern by name
#index = next((i for i, d in enumerate(COMPREHENSIVE_PATTERNS) if d.get("name") == "from_to_hijri_gregorian"), -1)

pattern = date_components_patterns_dict['patterns']
pattern = basic_date_pattern_dict['patterns']
len(pattern)

index = 0
p = pattern[index]
name = p['name']
examples = p['examples']
print("index =", index)
compiled = p['pattern']

match_component = p['date']

# Step 3: Test on example text
remaining_texts = examples


# remaining_text = remaining_texts[0]
for j, remaining_text in enumerate(remaining_texts):
    print("######","example # ", j, " #################")
    # Step 4: Use finditer (returns iterator)
    matches = list(compiled.finditer(remaining_text))

    result_en = get_calendar_variants_by_lang(match_component, lang = "en")
    result_ar = get_calendar_variants_by_lang(match_component, lang = "ar")

    # Step 5: Get the first match safely
    if matches:
        print("text :", remaining_text)
        match = matches[0]
        # Total number of captured groups (excluding group 0)
        print("Groups len:", len(match.groups()))
        # Print each named group individually
        for i in range(0, len(match.groups())+1):
            print(f"Group {i} - ", match.group(i))


# # Example usage and test cases:
# # ===================================================================================
# from calendar_variants.get_century_from_year import get_century_from_year
# # Century calculation examples:
# get_century_from_year(2023) → (21, "21st")
# get_century_from_year(1) → (1, "1st")
# get_century_from_year(100) → (1, "1st")
# get_century_from_year(101) → (2, "2nd")
# get_century_from_year("1445") → (15, "15th")  # Islamic calendar year
# get_century_from_year(None) → (None, None)

# # Ordinal suffix examples:
# get_ordinal_suffix(1) → "1st"
# get_ordinal_suffix(22) → "22nd"
# get_ordinal_suffix(13) → "13th"  # Special case
# get_ordinal_suffix(101) → "101st"

# # Date normalization examples:
# normalize_date_output({"year": "2023", "month": "January"})
# → {"year": "2023", "month": "January", "century": 21, "calendar": "gregorian"}

# normalize_date_output({"era": "هـ", "year": "1445", "month": "رمضان"}, lang="ar")
# → {"era": "AH", "year": "1445", "month": "Ramadan", "century": 15, "calendar": "islamic"}

# normalize_date_output({"era": "", "year": "1449", "month": "1"}, lang="ar")
# → {"era": "AH", "year": "1445", "month": "Ramadan", "century": 15, "calendar": "islamic"}

# print("=== Test 1: Specific date ===")
#     input_date = {
#         'calendar': 'gregorian',
#         'day': 1,
#         'month': 1,
#         'year': 2024
#     }
#     result = get_calendar_variants(input_date)
#     print_results(result, "January 1, 2024")

#     print("\n=== Test 2: All dates in a month ===")
#     input_date = {
#         'calendar': 'gregorian',
#         'month': 1,
#         'year': 2024
#     }
#     result = get_calendar_variants(input_date)
#     print_results(result, "All dates in January 2024")

#     print("\n=== Test 3: All 15th days in a year ===")
#     input_date = {
#         'calendar': 'gregorian',
#         'day': 15,
#         'year': 2024
#     }
#     result = get_calendar_variants(input_date)
#     print_results(result, "All 15th days in 2024")

#     print("\n=== Test 4: All dates in a year ===")
#     input_date = {
#         'calendar': 'gregorian',
#         'year': 2024
#     }
#     result = get_calendar_variants(input_date)
#     print_results(result, "All dates in 2024")



# # # ===================================================================================
# # # VALIDATION AND TESTING
# # # ===================================================================================

# # def validate_patterns(COMPREHENSIVE_PATTERNS):
# #     """Validate all patterns compile correctly and match their examples."""
# #     import re

# #     print("Validating comprehensive date patterns...")
# #     print("=" * 60)

# #     for i, pattern_config in enumerate(COMPREHENSIVE_PATTERNS):
# #         pattern_name = pattern_config["name"]
# #         pattern_regex = pattern_config["pattern"]
# #         example = pattern_config["example"]

# #         try:
# #             # Compile the pattern
# #             compiled_pattern = re.compile(pattern_regex, re.IGNORECASE | re.UNICODE)

# #             # Test against example
# #             match = compiled_pattern.search(example)

# #             if match:
# #                 print(f"✅ [{i+1:2d}] {pattern_name}")
# #                 print(f"    Example: {example}")
# #                 print(f"    Match: {match.group(0)}")
# #                 if match.groupdict():
# #                     print(f"    Groups: {match.groupdict()}")
# #                 print()
# #             else:
# #                 print(f"❌ [{i+1:2d}] {pattern_name} - FAILED TO MATCH EXAMPLE")
# #                 print(f"    Example: {example}")
# #                 print(f"    Pattern: {pattern_regex}")
# #                 print()

# #         except re.error as e:
# #             print(f"💥 [{i+1:2d}] {pattern_name} - REGEX COMPILATION ERROR")
# #             print(f"    Error: {e}")
# #             print(f"    Pattern: {pattern_regex}")
# #             print()

# #     print("Validation complete!")

# # # ===================================================================================
# # # USAGE EXAMPLES
# # # ===================================================================================

# # if __name__ == "__main__":
# #     # Run validation
# #     validate_patterns(COMPREHENSIVE_PATTERNS)

# #     # Example usage
# #     test_texts = [
# '''
        "من 1440 هـ إلى 2023 م في فترة مهمة من التاريخ",
        "حدث ذلك في 1445 هـ (2023 م) تقريباً",
        "القرن الثالث الهجري كان عصراً ذهبياً",
        "الجمعة 15 محرم 1445 هـ موافق 1 أغسطس 2023 م",
        "سنة 1402 هـ.ش كانت سنة مميزة",
        "حوالي 2020 م بدأت جائحة كورونا"
#         '''
# #     ]

# #     print("\n" + "=" * 60)
# #     print("TESTING WITH SAMPLE TEXTS")
# #     print("=" * 60)

# #     import re

# #     for text in test_texts:
# #         print(f"\nTesting: {text}")
# #         print("-" * 40)

# #         matches_found = []

# #         # Test each pattern against the text
# #         for pattern_config in COMPREHENSIVE_PATTERNS:
# #             try:
# #                 compiled_pattern = re.compile(pattern_config["pattern"], re.IGNORECASE | re.UNICODE)
# #                 matches = list(compiled_pattern.finditer(text))

# #                 for match in matches:
# #                     matches_found.append({
# #                         "pattern": pattern_config["name"],
# #                         "match": match.group(0),
# #                         "groups": match.groupdict(),
# #                         "priority": pattern_config["priority"],
# #                         "match_type": pattern_config["match_type"],
# #                         "calendars": pattern_config["calendars"]
# #                     })
# #             except:
# #                 continue

# #         # Sort by priority and display
# #         matches_found.sort(key=lambda x: x["priority"])

# #         if matches_found:
# #             for match_info in matches_found[:3]:  # Show top 3 matches
# #                 print(f"  Pattern: {match_info['pattern']}")
# #                 print(f"  Match: '{match_info['match']}'")
# #                 print(f"  Groups: {match_info['groups']}")
# #                 print(f"  Priority: {match_info['priority']}")
# #                 print(f"  Match Type: {match_info['match_type']}")
# #                 print(f"  Calendars: {', '.join(match_info['calendars'])}")
# #                 print("-" * 40)
# #         else:
# #             print("  No matches found for this text.")

# # index = 15
# # text : 15/03/1445 هـ
# # Groups len: 10
# # Group 0 -  15/03/1445 هـ
# # Group 1 -  15
# # Group 2 -  03
# # Group 3 -  1445 هـ
# # Group 4 -  1445
# # Group 5 -  هـ
# # Group 6 -  None
# # Group 7 -  None
# # Group 8 -  None
# # Group 9 -  None
# # Group 10 -  None


# #     # All unnamed group values as tuple
# #     print("Groups:", match.groups())

# #     # Named group dictionary
# #     print("GroupDict:", match.groupdict())

# #     # Print each named group individually
# #     for i, (name, value) in enumerate(match.groupdict().items(), start=0):
# #         print(f"Group Name {i} - {name}: {value}")

# # else:
# #     print("No match found.")

# # ###   ======================================================================
# # re.compile(r'(القرن\s+)?(\d(1, 2))\s*(قبل\s*هجري\s*قمري|بعد\s*هجري\s*قمري|السنة\s*الهجرية|قبل\s*الهجرة|بعد\s*الهجره|قبل\s*الهجره|بعد\s*الهجرة|سنة\s*هجرية|هجري\s*قمري|بعد\s*هجري|بعد\s*هجرت|قبل\s*هجرت|قبل\s*هجري|قبل\s*هـ\.ش|قبل\s*هـــ|قبل\s*هــ|ق\s*هـــ|قبل\s*هـ|قبل\s*ه|ق\s*هــ|ق\s*هـ|ق\s*ه|بالهجرية|بالهجري|للهجرة|هجرية|هجره|هجري|هـــ|هجری|هــ|هـ|ه)',
# #            re.IGNORECASE|re.UNICODE)

# # # for i, d in enumerate(patterns):
# # #     print(i, d.get("name"))


# # # # Find index where name == "year_flexible"


# # # remaining_text = "من 1440 هـ إلى 2023 م. في عام 2020 م، حدث شيء مهم. حوالي 1445 هـ كان عامًا مميزًا. "

# # # Step 1: Get the pattern by name
# # index = next((i for i, d in enumerate(COMPREHENSIVE_PATTERNS) if d.get("name") == "from_to_hijri_gregorian"), -1)

# # index = 1
# # # Step 2: Compile the regex
# # compiled = re.compile(COMPREHENSIVE_PATTERNS[index]['pattern'], flags=re.IGNORECASE | re.UNICODE)

# # # Step 3: Test on example text
# # remaining_text = COMPREHENSIVE_PATTERNS[index]["example"]

# # # Step 4: Use finditer (returns iterator)
# # matches = list(compiled.finditer(remaining_text))

# # # Step 5: Get the first match safely
# # if matches:
# #     match = matches[0]

# #     # Total number of captured groups (excluding group 0)
# #     print("Groups len:", len(match.groups()))


# #     # Print each named group individually
# #     for i in range(0, len(match.groups())+1):
# #         print(f"Group {i} - ", match.group(i))

# #     # All unnamed group values as tuple
# #     print("Groups:", match.groups())

# #     # Named group dictionary
# #     print("GroupDict:", match.groupdict())

# #     # Print each named group individually
# #     for i, (name, value) in enumerate(match.groupdict().items(), start=0):
# #         print(f"Group Name {i} - {name}: {value}")
# # else:
# #     print("No match found.")

# # # for test in patterns:
# # #     print(test['pattern'])
# # #     print(test['name'], test["example"])
# # #     match = re.search(test["pattern"], test["example"])
# # #     if match:
# # #         # Safely extract groups with bounds checking
# # #         groups = match.groups()
# # #         max_groups = len(groups)
# # #         # Debug output (consider removing in production)
# # #         print(f"Pattern: {test.get('name', 'Unknown')}")
# # #         print(f"Full match: {match.group(0)}")
# # #         for i in range(1, max_groups + 1):  # Show up to 5 groups safely
# # #             try:
# # #                 group_val = match.group(i)
# # #                 print(f"Group {i}: {group_val}")
# # #             except IndexError:
# # #                 print(f"Group {i}: N/A")
# # #         print("---")




# # #     assert match is not None, f"[{test['name']}] Pattern failed to match: {test['example']}"
# # #     print(f"[{test['name']}] Passed ✔")
# # #     if match:
# # #         print(" -------------- ", )
# # #         pprint(match.groupdict(), indent = 4)

# # import re

# # compiled = re.compile(
# #     r'(?P<hijri_day>\d{1,2})\s*(?:\.|:|/|\\|–|—|\||\-)\s*'
# #     r'(?P<hijri_month>\d{1,2}|جمادى\s*الآخرة|جمادى\s*الأولى|ربيع\s*الآخر|ربيع\s*الأول|ذو\s*القعدة|ذو\s*الحجة|رمضان|شعبان|شوال|محرم|صفر|رجب)\s*'
# #     r'(?:\.|:|/|\\|–|—|\||\-)\s*'
# #     r'(?P<hijri_year>\d{1,4})\s*'
# #     r'(?P<hijri_era>بعد\s*هجري\s*قمري|قبل\s*هجري\s*قمري|السنة\s*الهجرية|بعد\s*الهجره|قبل\s*الهجرة|قبل\s*الهجره|بعد\s*الهجرة|سنة\s*هجرية|هجري\s*قمري|قبل\s*هـــ|قبل\s*هجرت|قبل\s*هجري|بعد\s*هجري|قبل\s*هـ\.ش|بعد\s*هجرت|قبل\s*هــ|قبل\s*هـ|ق\s*هـــ|قبل\s*ه|ق\s*هــ|ق\s*هـ|ق\s*ه|بالهجرية|بالهجري|الهجري|للهجرة|هجرية|هجري|هجری|هـــ|هجره|هــ|هـ|ه)?',
# #     flags=re.IGNORECASE | re.UNICODE
# # )

# # text = "15/03/1445 هـ"

# # match = pattern.search(text)
# # if match:
# #     print("GroupDict:", match.groupdict())
# # else:
# #     print("No match")
                                                                                                                                  