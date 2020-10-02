import datetime
from extensions import jalali
def convert_to_jalali(Greg_datetime):
    week_days = {
                 "Saturday":"شنبه",
                 "Sunday":"یکشنبه",
                 "Monday":"دوشنبه",
                "Tuesday":"سه شنبه",
                "Wednesday":"چهارشنبه",
                "Thursday":"پنجشنبه",
                "Friday":"جمعه"
                 }
    months = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر', 5: 'مرداد', 6: 'شهریور', 7: 'مهر', 8: 'آبان',
     9: 'آذر', 10: 'دی', 11: 'بهمن', 12: 'اسفند'}

    shamsi_date = jalali.Gregorian(Greg_datetime.year, Greg_datetime.month, Greg_datetime.day).persian_tuple()
    shamsi_datetime = "ساعت: {time} روز: {dow} {day}-{month}-{year}".format(year = shamsi_date[0],month =  months.get(shamsi_date[1]), day = shamsi_date[2], dow = week_days.get(Greg_datetime.strftime("%A")), time = Greg_datetime.strftime("%X"))
    return shamsi_datetime


