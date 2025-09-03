
"""
Month keyword search utility.

Created on Thu Jul 24 20:01:16 2025

@author: m.lotfi
@description: Utility functions for searching month names within keyword dictionaries.
"""
from typing import Union, Tuple, Dict, Optional


def search_in_keywords(search_month: str, keywords: Dict[str, list]) -> Tuple[Optional[str], Optional[int]]:
    """
    Search for a month name in all keyword lists within a dictionary.

    This function performs a case-insensitive search across all lists in the keywords
    dictionary and returns the first match found along with its position.

    Parameters
    ----------
    search_month : str
        The month name to search for (will be normalized to lowercase and stripped)
    keywords : Dict[str, list]
        Dictionary where keys are category names and values are lists of month names

    Returns
    -------
    Tuple[Optional[str], Optional[int]]
        A tuple containing:
        - matching_key: The dictionary key where the month was found, or None if not found
        - index: The position of the month in the matched list, or None if not found

    Examples
    --------
    >>> keywords = {
    ...     'english': ['January', 'February', 'March'],
    ...     'spanish': ['Enero', 'Febrero', 'Marzo']
    ... }
    >>> search_in_keywords('january', keywords)
    ('english', 0)
    >>> search_in_keywords('marzo', keywords)
    ('spanish', 2)
    >>> search_in_keywords('nonexistent', keywords)
    (None, None)
    """
    # Normalize the search term once for efficiency
    normalized_search = search_month.lower().strip()
    
    for key, value in keywords.items():
        # Create normalized version of the current list for comparison
        search_list = [mon.lower().strip() for mon in value]

        if normalized_search in search_list:
            # Find the index of the matching month
            idx = search_list.index(normalized_search)
            return key, idx

    # Return None values if no match is found
    return None, None