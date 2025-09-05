from typing import Optional
from dataclasses import dataclass

@dataclass
class DateMeta:
    """
    Metadata container for date parsing context and quality information.

    Stores additional information about how a date was parsed, including
    the original text, language detection, precision level, confidence scoring,
    and validation flags. Used for debugging, quality assessment, and
    post-processing decisions.

    Parameters
    ----------
    text : str, optional
        Original text that was parsed to create this date
    lang : str, optional
        Language of the original text (ISO 639-1 code like 'en', 'ar')
    precision : str, optional
        Precision level indicator ('day', 'month', 'year', 'century')
    confidence : float, optional
        Parsing confidence score between 0.0 and 1.0
    created_at : str, optional
        Timestamp when the date was parsed
    created_by : str, optional
        System or module that created this date
    is_calendar_date : bool, default False
        Whether the date has calendar-level information (year + era)
    is_complete_date : bool, default False
        Whether the date has complete day-level precision
    valid_date : bool, default False
        Whether the date passed all validation checks
    role_in_text : str, optional
        Role this date plays in the source text (e.g., 'birth_date', 'event_date')
    related_to : str, optional
        What entity or concept this date relates to

    Examples
    --------
    >>> meta = DateMeta(
    ...     text="15 March 2023",
    ...     lang="en",
    ...     precision="day",
    ...     confidence=0.95,
    ...     is_complete_date=True
    ... )
    """
    text: Optional[str] = None
    lang: Optional[str] = None
    precision: Optional[str] = None
    confidence: Optional[float] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    is_calendar_date: bool = False
    is_complete_date: bool = False
    valid_date: bool = False
    role_in_text: Optional[str] = None
    related_to: Optional[str] = None

