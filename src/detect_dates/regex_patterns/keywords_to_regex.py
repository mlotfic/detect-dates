
#!/usr/bin/env python3
import re
from typing import List


from .string_utils import sort_strings_by_word_char_count

# ===================================================================================
# UTILITY FUNCTIONS
# ===================================================================================
def keywords_to_regex(keywords: List[str], escape: bool = True) -> str:
    """
    Convert a list of keywords to a regex pattern.
    Sorts by length (longest first) and handles spaces flexibly.
    """
    if not keywords:
        return ""

    keywords = list(set(keywords))
    # Sort by length (longest first) to avoid partial matches
    # sorted_keywords = sorted(keywords, key=len, reverse=True)
    sorted_keywords = sort_strings_by_word_char_count(keywords)

    if escape:
        # Escape regex special characters and make spaces flexible
        escaped_keywords = [re.escape(k).replace(r'\ ', r'\s*') for k in sorted_keywords if k.strip()]
        pattern = "|".join(escaped_keywords)
    else:
        pattern = "|".join([k for k in sorted_keywords if k.strip()])

    return rf"({pattern})"