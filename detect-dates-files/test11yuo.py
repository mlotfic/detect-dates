





# ===============================
# Composite Pattern Class
# ===============================

@dataclass
class CompositeNumericPatterns(PatternValidator):
    """
    Combines all basic numeric patterns into a unified structure.

    This class serves as a container for all the individual pattern classes,
    providing a single entry point for accessing all date pattern functionality.

    Attributes:
        base_patterns (BasePatterns): Base patterns from external module
        month_patterns (MonthPatterns): Month name patterns
        era_patterns (EraPatterns): Era indicator patterns
        indicator_patterns (IndicatorPatterns): Date indicator patterns
        numeric_patterns (NumericPatterns): Basic numeric patterns
        century_patterns (CenturyPatterns): Century-specific patterns
        year_patterns (YearPatterns): Year-specific patterns
        month_year_patterns (MonthYearPatterns): Month-year combinations
        day_month_year_patterns (DayMonthYearPatterns): Complete date patterns
        natural_language_patterns (NaturalLanguagePatterns): Weekday + date patterns
    """
    base_patterns: BasePatterns
    month_patterns: MonthPatterns
    era_patterns: EraPatterns
    indicator_patterns: IndicatorPatterns
    numeric_patterns: NumericPatterns

    def __post_init__(self):
        """Initialize all composite patterns after dataclass creation."""

        # Build all pattern hierarchies
        self.century_patterns = CenturyPatterns(
            numeric_patterns=self.numeric_patterns,
            indicator_patterns=self.indicator_patterns,
            era_patterns=self.era_patterns,
            base_patterns=self.base_patterns
        )

        self.year_patterns = YearPatterns(
            numeric_patterns=self.numeric_patterns,
            indicator_patterns=self.indicator_patterns,
            era_patterns=self.era_patterns
        )

        self.month_year_patterns = MonthYearPatterns(
            numeric_patterns=self.numeric_patterns,
            year_patterns=self.year_patterns,
            month_patterns=self.month_patterns,
            era_patterns=self.era_patterns,
            indicator_patterns=self.indicator_patterns
        )

        self.day_month_year_patterns = DayMonthYearPatterns(
            numeric_patterns=self.numeric_patterns,
            year_patterns=self.year_patterns,
            month_patterns=self.month_patterns,
            era_patterns=self.era_patterns,
            indicator_patterns=self.indicator_patterns,
            month_year_patterns=self.month_year_patterns
        )

        self.natural_language_patterns = NaturalLanguagePatterns(
            base_patterns=self.base_patterns,
            era_patterns=self.era_patterns,
            indicator_patterns=self.indicator_patterns,
            day_month_year_patterns=self.day_month_year_patterns
        )

        # Validate all patterns
        self._validate_patterns()

    def get_all_patterns(self) -> Dict[str, Any]:
        """
        Get all patterns organized by category and calendar system.

        Returns:
            Dict[str, Any]: Dictionary containing all pattern categories
        """
        return {
            'century': self.century_patterns,
            'year': self.year_patterns,
            'month_year': self.month_year_patterns,
            'day_month_year': self.day_month_year_patterns,
            'natural_language': self.natural_language_patterns
        }

    def get_calendar_patterns(self, calendar: str) -> Dict[str, Dict[str, str]]:
        """
        Get all patterns for a specific calendar system.

        Args:
            calendar (str): Calendar system ('hijri', 'gregorian', or 'julian')

        Returns:
            Dict[str, Dict[str, str]]: All patterns for the specified calendar

        Raises:
            ValueError: If calendar system is not supported
        """
        if calendar not in ['hijri', 'gregorian', 'julian']:
            raise ValueError(f"Unsupported calendar system: {calendar}")

        return {
            'century': getattr(self.century_patterns, calendar),
            'year': getattr(self.year_patterns, calendar),
            'month_year': getattr(self.month_year_patterns, calendar),
            'day_month_year': getattr(self.day_month_year_patterns, calendar),
            'natural_language': getattr(self.natural_language_patterns, calendar)
        }

    def compile_pattern(self, pattern: str) -> re.Pattern:
        """
        Compile a regex pattern with standard flags.

        Args:
            pattern (str): Regex pattern string to compile

        Returns:
            re.Pattern: Compiled regex pattern

        Raises:
            ValueError: If pattern compilation fails
        """
        try:
            return re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)
        except re.error as e:
            raise ValueError(f"Failed to compile pattern '{pattern}': {e}")


# ===============================
# Usage Examples and Testing
# ===============================

def create_example_patterns() -> CompositeNumericPatterns:
    """
    Create example patterns for demonstration purposes.

    Note: In real usage, these patterns would be provided from
    external configuration or pattern definition files.

    Returns:
        CompositeNumericPatterns: Configured pattern instance
    """

    # Example base patterns (these would come from external sources)
    base_patterns = BasePatterns(
        weekday=r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|الإثنين|الثلاثاء|الأربعاء|الخميس|الجمعة|السبت|الأحد)",
        numeric_words=r"(?:st|nd|rd|th|م|ام|ین|وم)"
    )

    # Example month patterns
    month_patterns = MonthPatterns(
        hijri=r"(?:محرم|صفر|ربيع الأول|ربيع الآخر|جمادى الأولى|جمادى الآخرة|رجب|شعبان|رمضان|شوال|ذو القعدة|ذو الحجة)",
        gregorian=r"(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)",
        julian=r"(?:فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)"
    )

    # Example era patterns
    era_patterns = EraPatterns(
        hijri=r"(?:هـ|ه\.ش|AH|A\.H\.)",
        gregorian=r"(?:AD|A\.D\.|CE|C\.E\.|BC|B\.C\.|BCE|B\.C\.E\.)",
        julian=r"(?:ش\.ه|ش\.خ|SH)"
    )

    # Example indicator patterns
    indicator_patterns = IndicatorPatterns(
        day=r"(?:day|روز|يوم|یوم)",
        month=r"(?:month|ماه|شهر)",
        year=r"(?:year|سال|عام)",
        century=r"(?:century|قرن|القرن)",
        separator=r"[/\-\s،,]",
        range_connector=r"(?:to|until|till|-|تا|إلى|الى)",
        range_starter=r"(?:from|since|منذ|من|از)"
    )

    # Example numeric patterns (using defaults)
    numeric_patterns = NumericPatterns(
        year=r"(\d{1,4})",
        month=r"(\d{1,2})",
        day=r"(\d{1,2})",
        century=r"(\d{1,2})"
    )

    # Create and return composite patterns
    return CompositeNumericPatterns(
        base_patterns=base_patterns,
        month_patterns=month_patterns,
        era_patterns=era_patterns,
        indicator_patterns=indicator_patterns,
        numeric_patterns=numeric_patterns
    )


# ===============================
# Main Functionality
# ===============================

if __name__ == "__main__":
    """
    Example usage and testing of the date pattern recognition module.
    """

    try:
        # Create example patterns
        patterns = create_example_patterns()

        # Test pattern compilation
        hijri_patterns = patterns.get_calendar_patterns('hijri')
        print("✓ Hijri patterns loaded successfully")

        gregorian_patterns = patterns.get_calendar_patterns('gregorian')
        print("✓ Gregorian patterns loaded successfully")

        julian_patterns = patterns.get_calendar_patterns('julian')
        print("✓ julian patterns loaded successfully")

        # Example pattern usage
        test_text = "Monday 15 December 2024"
        gregorian_natural = patterns.natural_language_patterns.gregorian['combined']
        compiled_pattern = patterns.compile_pattern(gregorian_natural)

        match = compiled_pattern.search(test_text)
        if match:
            print(f"✓ Successfully matched: '{test_text}'")
        else:
            print(f"✗ Failed to match: '{test_text}'")

    except Exception as e:
        print(f"✗ Error during testing: {e}")


# ===============================
# Module Exports
# ===============================

__all__ = [
    'BasePatterns',
    'MonthPatterns',
    'EraPatterns',
    'IndicatorPatterns',
    'NumericPatterns',
    'CenturyPatterns',
    'YearPatterns',
    'MonthYearPatterns',
    'DayMonthYearPatterns',
    'NaturalLanguagePatterns',
    'CompositeNumericPatterns',
    'PatternValidator',
    'create_example_patterns'
                                                                                                                                                                                                                                                       