import datetime

def date_difference(date1,date2):
    return date1-date2

def future_date(date1, add_days):
    return date1+add_days
add_days = datetime.timedelta(days=42)
date1 = datetime.datetime(2020,12,5)
date2 = datetime.datetime(2019,10,3)

print(date_difference(date1, date2))
print(future_date(date1, add_days))
