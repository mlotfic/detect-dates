
"""
Comprehensive examples for the date parsing library.
Demonstrates various use cases and functionality.
"""

from date_parsing_lib import (
    ParsedDate, DateAlternative, DateRange, DateRangeAlternative,
    Era, CalendarSystem, DatePrecision,
    create_simple_date, create_partial_date
)


def demo_basic_dates():
    """Demonstrate basic ParsedDate functionality."""
    print("=" * 50)
    print("BASIC PARSED DATES")
    print("=" * 50)
    
    # Complete modern date
    modern_date = ParsedDate(
        day=15,
        month=3,
        year=2024,
        era=Era.CE,
        calendar=CalendarSystem.GREGORIAN,
        precision=DatePrecision.EXACT,
        confidence=1.0,
        raw_text="March 15, 2024"
    )
    
    print(f"Modern date: {modern_date.to_readable_format()}")
    print(f"ISO format: {modern_date.to_iso_format()}")
    print(f"Custom format: {modern_date.strftime('%B %e, %Y %E')}")
    print(f"Is complete: {modern_date.is_complete()}")
    print()
    
    # Historical date with BCE
    historical_date = ParsedDate(
        day=15,
        month="March",  # Month as string
        year=44,
        era=Era.BCE,
        calendar=CalendarSystem.Jalali,
        precision=DatePrecision.EXACT,
        raw_text="Ides of March, 44 BCE"
    )
    
    print(f"Historical date: {historical_date.to_readable_format()}")
    print(f"Year with era: {historical_date.get_year_with_era()}")
    print(f"Custom format: {historical_date.strftime('%B %e, %Y %E (%S calendar)')}")
    print()
    
    # Partial date (year and month only)
    partial_date = create_partial_date(
        year=1066,
        month="October",
        era=Era.AD
    )
    
    print(f"Partial date: {partial_date.to_readable_format()}")
    print(f"ISO format: {partial_date.to_iso_format()}")
    print(f"Is partial: {partial_date.is_partial()}")
    print()
    
    # Very incomplete date (year only)
    year_only = ParsedDate(
        year=1969,
        era=Era.CE,
        precision=DatePrecision.YEAR,
        raw_text="sometime in 1969"
    )
    
    print(f"Year only: {year_only.to_readable_format()}")
    print(f"Custom format: {year_only.strftime('Year %Y %E (precision: %P)')}")
    print()


def demo_date_alternatives():
    """Demonstrate DateAlternative for multiple calendar systems."""
    print("=" * 50)
    print("DATE ALTERNATIVES (Multiple Calendar Systems)")
    print("=" * 50)
    
    # Gregorian/Islamic calendar alternative
    gregorian_date = ParsedDate(
        day=1,
        month=1,
        year=2024,
        era=Era.CE,
        calendar=CalendarSystem.GREGORIAN
    )
    
    islamic_date = ParsedDate(
        day=19,
        month=6,
        year=1445,
        era=Era.AH,
        calendar=CalendarSystem.ISLAMIC
    )
    
    dual_calendar = DateAlternative(
        primary=gregorian_date,
        alternative=islamic_date
    )
    
    print(f"Dual calendar date: {dual_calendar.to_combined_format()}")
    print(f"With custom separator: {dual_calendar.to_combined_format(' = ')}")
    print(f"Primary only: {dual_calendar.get_primary_readable()}")
    print(f"Alternative only: {dual_calendar.get_alternative_readable()}")
    print()
    
    # Jalali/Gregorian historical date
    Jalali_date = ParsedDate(
        day=3,
        month="October",
        year=1582,
        era=Era.AD,
        calendar=CalendarSystem.Jalali
    )
    
    gregorian_date = ParsedDate(
        day=13,
        month="October",
        year=1582,
        era=Era.AD,
        calendar=CalendarSystem.GREGORIAN
    )
    
    calendar_switch = DateAlternative(
        primary=Jalali_date,
        alternative=gregorian_date
    )
    
    print(f"Calendar switch date: {calendar_switch.to_combined_format(' (Jalali) / ')}")
    print("(This represents the same day in two different calendar systems)")
    print()


def demo_date_ranges():
    """Demonstrate DateRange functionality."""
    print("=" * 50)
    print("DATE RANGES")
    print("=" * 50)
    
    # Exact date range
    start_date = create_simple_date(20, 3, 2024, Era.CE)
    end_date = create_simple_date(25, 3, 2024, Era.CE)
    
    exact_range = DateRange(
        start_date=start_date,
        end_date=end_date,
        range_type="exact"
    )
    
    print(f"Exact range: {exact_range.to_readable_format()}")
    print(f"Is single day: {exact_range.is_single_day()}")
    print(f"Duration estimate: {exact_range.get_duration_estimate()}")
    print()
    
    # Single day (same start and end)
    single_day = DateRange(
        start_date=start_date,
        end_date=start_date,
        range_type="exact"
    )
    
    print(f"Single day range: {single_day.to_readable_format()}")
    print(f"Is single day: {single_day.is_single_day()}")
    print()
    
    # Historical range with partial dates
    battle_start = ParsedDate(
        month="September",
        year=1066,
        era=Era.AD,
        precision=DatePrecision.MONTH
    )
    
    battle_end = ParsedDate(
        month="October",
        year=1066,
        era=Era.AD,
        precision=DatePrecision.MONTH
    )
    
    battle_range = DateRange(
        start_date=battle_start,
        end_date=battle_end,
        range_type="approximate"
    )
    
    print(f"Historical range: {battle_range.to_readable_format()}")
    print()
    
    # Seasonal range
    winter_start = ParsedDate(
        month="December",
        year=1776,
        era=Era.AD,
        precision=DatePrecision.SEASON
    )
    
    spring_end = ParsedDate(
        month="March",
        year=1777,
        era=Era.AD,
        precision=DatePrecision.SEASON
    )
    
    winter_range = DateRange(
        start_date=winter_start,
        end_date=spring_end,
        range_type="seasonal"
    )
    
    print(f"Seasonal range: {winter_range.to_readable_format()}")
    print()


def demo_date_range_alternatives():
    """Demonstrate DateRangeAlternative for ranges in multiple calendars."""
    print("=" * 50)
    print("DATE RANGE ALTERNATIVES")
    print("=" * 50)
    
    # Islamic calendar range
    islamic_start = ParsedDate(
        year=1411,
        era=Era.AH,
        calendar=CalendarSystem.ISLAMIC,
        precision=DatePrecision.YEAR
    )
    
    islamic_end = ParsedDate(
        year=1412,
        era=Era.AH,
        calendar=CalendarSystem.ISLAMIC,
        precision=DatePrecision.YEAR
    )
    
    islamic_range = DateRange(
        start_date=islamic_start,
        end_date=islamic_end,
        range_type="approximate"
    )
    
    # Corresponding Gregorian range
    gregorian_start = ParsedDate(
        year=1990,
        era=Era.CE,
        calendar=CalendarSystem.GREGORIAN,
        precision=DatePrecision.YEAR
    )
    
    gregorian_end = ParsedDate(
        year=1992,
        era=Era.CE,
        calendar=CalendarSystem.GREGORIAN,
        precision=DatePrecision.YEAR
    )
    
    gregorian_range = DateRange(
        start_date=gregorian_start,
        end_date=gregorian_end,
        range_type="approximate"
    )
    
    # Combine them
    dual_range = DateRangeAlternative(
        primary_range=islamic_range,
        alternative_range=gregorian_range,
        range_type="approximate"
    )
    
    print(f"Dual calendar range: {dual_range.to_combined_format()}")
    print(f"With equals sign: {dual_range.to_combined_format(' = ')}")
    print(f"Primary duration: {dual_range.get_primary_duration()}")
    print(f"Alternative duration: {dual_range.get_alternative_duration()}")
    print()


def demo_advanced_formatting():
    """Demonstrate advanced formatting capabilities."""
    print("=" * 50)
    print("ADVANCED FORMATTING")
    print("=" * 50)
    
    # Complete date with all components
    full_date = ParsedDate(
        weekday="Friday",
        day=29,
        month=8,
        year=2025,
        century=21,
        era=Era.CE,
        calendar=CalendarSystem.GREGORIAN,
        precision=DatePrecision.EXACT,
        confidence=1.0,
        raw_text="Friday, August 29, 2025"
    )
    
    print("Various format strings:")
    print(f"ISO format:        {full_date.strftime('%Y-%m-%d')}")
    print(f"US format:         {full_date.strftime('%m/%d/%Y')}")
    print(f"European format:   {full_date.strftime('%d.%m.%Y')}")
    print(f"Long format:       {full_date.strftime('%A, %B %e, %Y')}")
    print(f"With era:          {full_date.strftime('%B %e, %Y %E')}")
    print(f"With calendar:     {full_date.strftime('%Y-%m-%d (%S)')}")
    print(f"With precision:    {full_date.strftime('%Y-%m-%d [%P]')}")
    print(f"Century format:    {full_date.strftime('%C century')}")
    print()
    
    # Partial date formatting
    partial = ParsedDate(
        month="March",
        year=2024
    )
    
    print("Partial date formatting:")
    print(f"Available parts:   {partial.strftime('%B %Y')}")
    print(f"With missing day:  {partial.strftime('%Y-%m-%d')}")
    print(f"Question marks:    {partial.strftime('%e %B %Y')}")
    print()


def demo_factory_functions():
    """Demonstrate factory functions for easy date creation."""
    print("=" * 50)
    print("FACTORY FUNCTIONS")
    print("=" * 50)
    
    # Simple date creation
    simple = create_simple_date(4, 7, 1776, Era.AD)
    print(f"Simple date: {simple.to_readable_format()}")
    print(f"Confidence: {simple.confidence}")
    print(f"Precision: {simple.precision.value}")
    print()
    
    # Partial date creation with various combinations
    year_month = create_partial_date(year=1969, month="July")
    print(f"Year + Month: {year_month.to_readable_format()}")
    
    year_only = create_partial_date(year=2001)
    print(f"Year only: {year_only.to_readable_format()}")
    
    month_day = create_partial_date(month=12, day=25)
    print(f"Month + Day: {month_day.strftime('%B %e (year unknown)')}")
    print()


def demo_real_world_examples():
    """Demonstrate real-world historical date examples."""
    print("=" * 50)
    print("REAL-WORLD HISTORICAL EXAMPLES")
    print("=" * 50)
    
    # Battle of Hastings
    hastings = create_simple_date(14, 10, 1066, Era.AD)
    print(f"Battle of Hastings: {hastings.to_readable_format()}")
    
    # Moon landing (exact date and time precision)
    moon_landing = ParsedDate(
        day=20,
        month=7,
        year=1969,
        era=Era.CE,
        precision=DatePrecision.DAY,
        raw_text="July 20, 1969",
        metadata={"time": "20:17 UTC", "mission": "Apollo 11"}
    )
    print(f"Moon Landing: {moon_landing.to_readable_format()}")
    
    # Fall of Constantinople (dual calendar)
    Jalali_fall = ParsedDate(day=29, month=5, year=1453, era=Era.AD, calendar=CalendarSystem.Jalali)
    gregorian_fall = ParsedDate(day=7, month=6, year=1453, era=Era.AD, calendar=CalendarSystem.GREGORIAN)
    
    constantinople_fall = DateAlternative(
        primary=Jalali_fall,
        alternative=gregorian_fall
    )
    print(f"Fall of Constantinople: {constantinople_fall.to_combined_format(' (Jalali) / ')}(Gregorian)")
    
    # Approximate historical period
    renaissance_start = create_partial_date(year=1400, era=Era.AD)
    renaissance_end = create_partial_date(year=1600, era=Era.AD)
    
    renaissance = DateRange(
        start_date=renaissance_start,
        end_date=renaissance_end,
        range_type="approximate"
    )
    print(f"Renaissance Period: {renaissance.to_readable_format()}")
    
    # Islamic/Gregorian calendar example
    islamic_conquest = ParsedDate(year=638, era=Era.AD, calendar=CalendarSystem.Jalali)
    islamic_hijri = ParsedDate(year=17, era=Era.AH, calendar=CalendarSystem.ISLAMIC)
    
    conquest_dual = DateAlternative(primary=islamic_conquest, alternative=islamic_hijri)
    print(f"Islamic Conquest of Jerusalem: {conquest_dual.to_combined_format()}")
    print()


def main():
    """Run all demonstration functions."""
    demo_basic_dates()
    demo_date_alternatives()
    demo_date_ranges()
    demo_date_range_alternatives()
    demo_advanced_formatting()
    demo_factory_functions()
    demo_real_world_examples()
    
    print("=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()