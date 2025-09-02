#!/usr/bin/env python3
"""
Created on Thu Jul 24 20:01:16 2025

@author: m.lotfi

@description:

"""
from typing import Union, Tuple, Dict, Optional


def search_in_keywords(search_month: str, keywords: dict) -> Tuple[Optional[str], Optional[int]]:
    """
    Search for month in all keyword lists.

    Args:
        search_month (str): Normalized month name to search for

    Returns:
        tuple: (matching_key, index) or (None, None) if not found
    """
    for key, value in keywords.items():
        search_list = [mon.lower().strip() for mon in value]

        if search_month in search_list:
            idx = search_list.index(search_month)
            return key, idx

   return None, None