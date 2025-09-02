# [ ] ============================================================
standard_date_format = {
    "range" : {
            "higri": "{hijri_year} : {hijri_year_end} {hijri_era}",
            "gregorian": "{gregorian_year} : {gregorian_year_end} {gregorian_era}",
            "julian": "{julian_year} : {julian_year_end} {julian_era}",
            "higri_gregorian": "{hijri_year} : {hijri_year_end} {hijri_era} / {gregorian_year} : {gregorian_year_end} {gregorian_era}",
            "higri_julian": "{hijri_year} : {hijri_year_end} {hijri_era} / {julian_year} : {julian_year_end} {julian_era}",
            "gregorian_julian": "{gregorian_year} : {gregorian_year_end} {gregorian_era} / {julian_year} : {julian_year_end} {julian_era}"
        },
    "year" : {
            "higri": "{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_year} {gregorian_era}",
            "julian": "{julian_year} {julian_era}",
            "higri_gregorian": "{hijri_year} {hijri_era} / {gregorian_year} {gregorian_era}",
            "higri_julian": "{hijri_year} {hijri_era} / {julian_year} {julian_era}",
            "gregorian_julian": "{gregorian_year} {gregorian_era} / {julian_year} {julian_era}"
        },
    "month_year" : {
            "higri": "{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_month}-{gregorian_year} {gregorian_era}",
            "julian": "{julian_month}-{julian_year} {julian_era}",
            "higri_gregorian": "{hijri_month}-{hijri_year} {hijri_era} / {gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_julian": "{hijri_month}-{hijri_year} {hijri_era} / {julian_month}-{julian_year} {julian_era}",
            "gregorian_julian": "{gregorian_month}-{gregorian_year} {gregorian_era} / {julian_month}-{julian_year} {julian_era}"
        },
    "day_month_year" : {
            "higri": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "julian": "{julian_day}-{julian_month}-{julian_year} {julian_era}",
            "higri_gregorian": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_julian": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {julian_day}-{julian_month}-{julian_year} {julian_era}",
            "gregorian_julian": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {julian_day}-{julian_month}-{julian_year} {julian_era}"
        },
    "day_day_month_year" : {
            "higri": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "julian": "{week_day} - {julian_day}-{julian_month}-{julian_year} {julian_era}",
            "higri_gregorian": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_julian": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {week_day} - {julian_day}-{julian_month}-{julian_year} {julian_era}",
            "gregorian_julian": "{week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {week_day} - {julian_day}-{julian_month}-{julian_year} {julian_era}"
        },
    "century" : {
            "higri": "{hijri_century} {hijri_era}",
            "gregorian": "{gregorian_century} {gregorian_era}",
            "julian": "{julian_century} {julian_era}",
            "higri_gregorian": "{hijri_century} {hijri_era} / {gregorian_century} {gregorian_era}",
            "higri_julian": "{hijri_century} {hijri_era} / {julian_century} {julian_era}",
            "gregorian_julian": "{gregorian_century} {gregorian_era} / {julian_century} {julian_era}"
        }
}