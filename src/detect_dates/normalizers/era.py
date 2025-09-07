
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize date components for different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing components like year, month, day, era, and weekday.
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

from detect_dates.keywords import era_keywords, era_standard_keywords


from typing import Optional, Tuple, Set
import logging

logger = logging.getLogger(__name__)

def get_era_info(era: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Extract calendar type, language and normalized era from input era text.

    Parameters
    ----------
    era : str
        Era text in any supported language/script (e.g. 'هـ', 'AH', 'CE')

    Returns
    -------
    Tuple[Optional[str], Optional[str], Optional[str]]
        - detected_calendar: Calendar system ('gregorian', 'hijri', 'Jalali') or None
        - detected_language: Language code ('ar', 'en') or None 
        - normalized_era: Standard era code ('AH', 'CE', 'SH' etc) or None

    Examples
    --------
    >>> get_era_info('هـ')
    ('hijri', 'ar', 'AH')
    
    >>> get_era_info('CE') 
    ('gregorian', 'en', 'CE')
    """
    if not isinstance(era, str) or not era.strip():
        logger.error(f"Invalid input type '{type(era)}'. Expected non-empty string.")
        return None, None, None

    # Search in era keywords list
    search_era = era.lower().strip()
    for era_config in era_keywords:
        if search_era in [k.lower() for k in era_config['keywords']]:
            return (
                era_config['calendar'],
                era_config['language'].split('_')[0], # Extract base language
                era_config['era']
            )
            
    logger.warning(f"Era '{era}' not found in keyword configurations")
    return None, None, None

def normalize_era(
    era: str,
    to_lang: Optional[str] = None,
    to_calendar: Optional[str] = None
) -> Optional[str]:
    """
    Normalize era text to standard form in specified language and calendar system.

    Parameters
    ----------
    era : str
        Era text to normalize (e.g. 'هـ', 'AH', 'CE')
    to_lang : str, optional
        Target language code ('ar', 'en')
    to_calendar : str, optional
        Target calendar system ('gregorian', 'hijri', 'Jalali')

    Returns
    -------
    str or None
        Normalized era text in target language/calendar, or None if conversion fails

    Examples
    --------
    >>> normalize_era('هـ', to_lang='en')
    'AH'
    
    >>> normalize_era('CE', to_lang='ar')
    'م'
    """
    # Get info about input era
    detected_calendar, detected_lang, normalized = get_era_info(era)
    if not normalized:
        return None

    # Use detected values if not specified
    target_lang = to_lang or detected_lang
    target_calendar = to_calendar or detected_calendar

    if target_lang not in ['ar', 'en']:
        logger.error(f"Unsupported target language: {target_lang}")
        return None

    if target_calendar not in ['gregorian', 'hijri', 'Jalali']:
        logger.error(f"Unsupported target calendar: {target_calendar}")
        return None

    # Get normalized form for target language
    try:
        if target_lang == 'ar':
            key = f"{normalized.lower()}_ar"
        else:
            key = f"{normalized.lower()}_en"
            
        return era_standard_keywords.get(key)
    except Exception as e:
        logger.error(f"Error normalizing era: {e}")
        return None

def get_calendar(era: str) -> Optional[str]:
    """
    Get the calendar system(s) associated with an era.

    Parameters
    ----------
    era : str
        Era text to check (e.g. 'هـ', 'AH', 'CE')

    Returns
    -------
    str or None
        Set of calendar system names ('gregorian', 'hijri', 'Jalali')

    Examples
    --------
    >>> get_calendar('CE')
    'gregorian'
    
    >>> get_calendar('هـ')
    'hijri'
    """
    calendar, _, _ = get_era_info(era)
    if calendar:
        return calendar
    return None

if __name__ == "__main__":
    # Example usage
    print(get_era_info('هـ'))
    print(normalize_era('CE', to_lang='ar'))
    print(get_calendar('AH'))