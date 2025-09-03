#!/usr/bin/env python3
"""
Regex match value extraction utilities.

This module provides a function to extract date component values from regex match objects.
It handles both single and multiple group indices, returning the first non-empty value found.

Created on Fri Jul 25 23:01:21 2025
@author: m.lotfi
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
    print("This module is not intended to be run directly. Import it in your code.")
    setup_src_path()
import re
from typing import Optional, Union, List


def get_match_value(
    match: Optional[re.Match], 
    idx: Optional[Union[int, str, List[Union[int, str]]]] = None
) -> Optional[Union[int, str]]:
    """
    Extract component values from a regex match object.
    
    This function provides flexible access to regex capture groups by supporting
    single indices, string indices (converted to int), or lists of indices to try
    in sequence. Returns the first non-empty match found.
    
    Parameters
    ----------
    match : Optional[re.Match]
        A regex match object from re.search/re.match, or None if no match found
    idx : Optional[Union[int, str, List[Union[int, str]]]], optional
        Group index specification:
        - int: Single group index (1-based, 0 is full match)
        - str: String convertible to int group index
        - list: Multiple indices to try in order, returns first non-empty match
        
    Returns
    -------
    Optional[Union[int, str]]
        The first non-empty captured group value found, or None if:
        - No match object provided
        - No valid index provided  
        - Index out of bounds
        - All specified groups are empty
        
    Examples
    --------
    >>> import re
    >>> match = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2023-12-25')
    >>> get_match_value(match, 1)        # Single index
    '2023'
    >>> get_match_value(match, [1, 2])   # List of indices, returns first non-empty
    '2023'  
    >>> get_match_value(match, "1")      # String index
    '2023'
    >>> get_match_value(match, [10, 2])  # Invalid first index, fallback to second
    '12'
    >>> get_match_value(None, 1)         # No match object
    None
    """
    
    # Early return for None match (no regex match found)
    if match is None:
        return None
    
    # Early return for None index specification
    if idx is None:
        return None
    
    # Handle single index (int or str that converts to int)
    if isinstance(idx, (int, str)):
        try:
            # Convert string to int if needed, preserve int as-is
            group_idx = int(idx) if isinstance(idx, str) else idx
            
            # Validate index bounds: group 0 is full match, groups start at 1
            # Upper bound check against actual number of capturing groups
            if group_idx < 0 or group_idx > len(match.groups()):
                return None
                
            # Extract group value and return only if non-empty
            group_value = match.group(group_idx)
            return group_value if group_value else None
            
        except (ValueError, IndexError):
            # Handle string conversion errors or unexpected index errors
            return None
    
    # Handle list of indices - try each in sequence until non-empty match found
    elif isinstance(idx, list):
        for single_idx in idx:
            # Recursively call for each index in the list
            group_value = get_match_value(match, single_idx)
            if group_value:  # Return first non-empty group value found
                return group_value
        # No non-empty values found in any of the specified groups
        return None
    
    else:
        # Unsupported index type
        return None


def main():
    """
    Test function demonstrating get_match_value functionality.
    
    Runs various test cases to validate the function behavior with
    different input types and edge cases.
    """
    # Setup test data
    test_string = "2023-12-25"
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.search(pattern, test_string)
    
    print("Test string:", test_string)
    print("Pattern:", pattern)
    print("Match groups:", match.groups() if match else "No match")
    print()
    
    # Test single index access
    print("=== Single Index Tests ===")
    print("get_match_value(match, 1):", get_match_value(match, 1))    # Year: '2023'
    print("get_match_value(match, 2):", get_match_value(match, 2))    # Month: '12'  
    print("get_match_value(match, '3'):", get_match_value(match, '3')) # Day: '25'
    print()
    
    # Test list of indices (fallback behavior)
    print("=== List Index Tests ===")
    print("get_match_value(match, [1, 2]):", get_match_value(match, [1, 2]))  # First valid: '2023'
    print("get_match_value(match, [5, 2]):", get_match_value(match, [5, 2]))  # Fallback to second: '12'
    print("get_match_value(match, [10, 20]):", get_match_value(match, [10, 20])) # Both invalid: None
    print()
    
    # Test edge cases and error conditions
    print("=== Edge Case Tests ===")
    print("get_match_value(None, 1):", get_match_value(None, 1))      # No match object: None
    print("get_match_value(match, None):", get_match_value(match, None)) # No index: None
    print("get_match_value(match, 10):", get_match_value(match, 10))  # Index out of bounds: None
    print("get_match_value(match, []):", get_match_value(match, []))  # Empty list: None
    print("get_match_value(match, 'invalid'):", get_match_value(match, 'invalid')) # Invalid string: None


# Example usage and tests
if __name__ == "__main__":
    main()