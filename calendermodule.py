#calender module
'''import calendar
year=2026
month=4
print(calendar.month(year,month)) '''

#year
'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input("enter the year:"))
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year:"))
b=int(input("enter the month:"))
print(calendar.month(a,b))'''

#date & Time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"today time is-{b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"day is {b.tm_mday}-{b.tm_yday}_{b.tm_isdst}")'''

import random
import time
for i in range(10):
    a=random.randint(100,999)
    print(a)
    time.sleep(2)
