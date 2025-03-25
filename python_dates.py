from datetime import date, timedelta

import delta

today = date.today()
print(today.day)

f_date = today.strftime("%d/%m/%Y")
print(f_date)

expiry_date = today + timedelta(days = 30)
print(expiry_date)

#2005,01,16
#1998,12,25

date1 = date(2005,1,16)
date2 = date(1998,12,25)
difference = date1 - date2
print(difference.days)