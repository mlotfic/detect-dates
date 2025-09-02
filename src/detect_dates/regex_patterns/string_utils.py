from typing import Literal, List, Dict, Any, Optional
# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================

def sort_strings_by_word_char_count(strings: List[str]) -> List[str]:
    """
    Sort a list of strings by word count (ascending), then by character count (ascending).
    Converts to lowercase, removes extra spaces, and removes duplicates before sorting.

    Args:
        strings (list): List of strings to sort

    Returns:
        list: Sorted list with duplicates removed, normalized to lowercase with extra spaces removed
    """
    if not strings:
        return []

    # Normalize strings: convert to lowercase and remove extra spaces
    normalized_strings = []
    for s in strings:
        # Normalize: lowercase, strip, collapse inner spaces
        normalized = ' '.join(s.lower().strip().split())
        normalized_strings.append(normalized)


    # Remove duplicates by converting to set, then back to list
    unique_strings = list(set(normalized_strings))

    # Sort by word count first, then by character count
    sorted_strings = sorted(unique_strings, key=lambda s: (-len(s.split()), -len(s)))

    return sorted_strings


# Example usage
if __name__ == "__main__":
    # Test with sample data including extra spaces and mixed case
    test_strings = [
        "Hello   World",
        "A",
        "This is a longer sentence with many words",
        "HELLO  world",  # duplicate after normalization
        "Short    Text",
        "a",  # duplicate after normalization
        "Medium   Length TEXT here",
        "X    Y    Z",
        "  Single  ",
        "  hello world  "  # duplicate after normalization
    ]

    result = sort_strings_by_word_char_count(test_strings)

    print("Original list:")
    for s in test_strings:
        print(f"'{s}' - Words: {len(s.split())}, Chars: {len(s)}")

    print("\nSorted result (duplicates removed):")
    for s in result:
        print(f"'{s}' - Words: {len(s.split())}, Chars: {len(s)}")

    Hijri_keywords = ["هـ","هــ","هـــ","ه","سنة هجرية","هجري","هجرية","السنة الهجرية","بالهجري","بالهجرية","للهجرة","AH","After Hijra"]
    sorted_hijri_keywords = sort_strings_by_word_char_count(Hijri_keywords)
    print("\nSorted Hijri keywords:")
    for s in sorted_hijri_keywords:
       print(f"'{s}' - Words: {len(s.split())}, Chars: {len(s)}")