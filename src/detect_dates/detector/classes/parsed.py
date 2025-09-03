from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Union

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

@dataclass
class ParsedDate:
    """
    Base class representing a date entity with flexible precision and optional components.

    This class serves as the foundation for date representation, allowing for partial
    dates where some components (day, month, year) may be missing. It supports
    multiple calendar systems and includes metadata for parsing confidence.

    Attributes:
        weekday (Optional[str]): Day of the week (e.g., "Monday", "Mon")
        day (Optional[int]): Day of the month (1-31)
        month (Optional[Union[int, str]]): Month as number (1-12) or name ("January", "Jan")
        year (Optional[int]): Full year (e.g., 2023, 1066, -44 for 45 BCE)
        century (Optional[Union[int, str]]): Century number or description ("21st", "first")
        era (Optional[str]): Era designation (BCE, CE, AD, BC, etc.)
        calendar (Optional[str]): Calendar system used ('gregorian', 'hijri', 'julian')
        raw_text (Optional[str]): Original text that was parsed to create this date
        lang (Optional[str]): Language of the original text (ISO 639-1 code)
        precision (Optional[str]): Indicates the precision level of this date
        confidence (Optional[float]): Confidence score (0.0-1.0) for parsed accuracy
        metadata (Optional[Dict[str, Any]]): Additional parsing information

    Example:
        Creating a complete date::

            date = ParsedDate(
                day=15, month=3, year=2023,
                era='CE', calendar='gregorian',
                confidence=1.0
            )

        Creating a partial date::

            partial = ParsedDate(
                month="March", year=2023,
                precision='month', confidence=0.8
            )

    Note:
        This class is designed to be flexible and handle real-world date parsing
        scenarios where information may be incomplete or ambiguous.
    """
    match: Optional[re.Match] = None
    raw_text: Optional[str] = None
    raw_values: Optional[Dict[str, Any]] = field(default_factory=dict)
    weekday: Optional[str] = None
    day: Optional[int] = None
    month: Optional[Union[int, str]] = None
    year: Optional[int] = None
    century: Optional[Union[int, str]] = None
    era: Optional[str] = None
    calendar: Optional[str] = None
    raw_text: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)