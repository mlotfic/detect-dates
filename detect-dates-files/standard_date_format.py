# [ ] ============================================================
standard_date_format = {
    "range" : {
            "higri": "{hijri_year} : {hijri_year_end} {hijri_era}",
            "gregorian": "{gregorian_year} : {gregorian_year_end} {gregorian_era}",
            "Jalali": "{Jalali_year} : {Jalali_year_end} {Jalali_era}",
            "higri_gregorian": "{hijri_year} : {hijri_year_end} {hijri_era} / {gregorian_year} : {gregorian_year_end} {gregorian_era}",
            "higri_Jalali": "{hijri_year} : {hijri_year_end} {hijri_era} / {Jalali_year} : {Jalali_year_end} {Jalali_era}",
            "gregorian_Jalali": "{gregorian_year} : {gregorian_year_end} {gregorian_era} / {Jalali_year} : {Jalali_year_end} {Jalali_era}"
        },
    "year" : {
            "higri": "{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_year} {gregorian_era}",
            "Jalali": "{Jalali_year} {Jalali_era}",
            "higri_gregorian": "{hijri_year} {hijri_era} / {gregorian_year} {gregorian_era}",
            "higri_Jalali": "{hijri_year} {hijri_era} / {Jalali_year} {Jalali_era}",
            "gregorian_Jalali": "{gregorian_year} {gregorian_era} / {Jalali_year} {Jalali_era}"
        },
    "month_year" : {
            "higri": "{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_month}-{gregorian_year} {gregorian_era}",
            "Jalali": "{Jalali_month}-{Jalali_year} {Jalali_era}",
            "higri_gregorian": "{hijri_month}-{hijri_year} {hijri_era} / {gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_Jalali": "{hijri_month}-{hijri_year} {hijri_era} / {Jalali_month}-{Jalali_year} {Jalali_era}",
            "gregorian_Jalali": "{gregorian_month}-{gregorian_year} {gregorian_era} / {Jalali_month}-{Jalali_year} {Jalali_era}"
        },
    "day_month_year" : {
            "higri": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "Jalali": "{Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}",
            "higri_gregorian": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_Jalali": "{hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}",
            "gregorian_Jalali": "{gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}"
        },
    "day_day_month_year" : {
            "higri": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era}",
            "gregorian": "{week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "Jalali": "{week_day} - {Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}",
            "higri_gregorian": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era}",
            "higri_Jalali": "{week_day} - {hijri_day}-{hijri_month}-{hijri_year} {hijri_era} / {week_day} - {Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}",
            "gregorian_Jalali": "{week_day} - {gregorian_day}-{gregorian_month}-{gregorian_year} {gregorian_era} / {week_day} - {Jalali_day}-{Jalali_month}-{Jalali_year} {Jalali_era}"
        },
    "century" : {
            "higri": "{hijri_century} {hijri_era}",
            "gregorian": "{gregorian_century} {gregorian_era}",
            "Jalali": "{Jalali_century} {Jalali_era}",
            "higri_gregorian": "{hijri_century} {hijri_era} / {gregorian_century} {gregorian_era}",
            "higri_Jalali": "{hijri_century} {hijri_era} / {Jalali_century} {Jalali_era}",
            "gregorian_Jalali": "{gregorian_century} {gregorian_era} / {Jalali_century} {Jalali_era}"
        }
}