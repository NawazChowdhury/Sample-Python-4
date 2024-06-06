
import time

from datetime import date
 
def days_between_dates(dt1, dt2):
    date_format = "%d/%m/%Y"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    return int(delta / 86400)

last_date=input("Enter Date")

today = date.today()
 
dt1 = last_date
dt2 = today.strftime("%d/%m/%Y")
print(days_between_dates(dt1, dt2))