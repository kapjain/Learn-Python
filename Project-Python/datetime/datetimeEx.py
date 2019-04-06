import datetime

print("------------------------------Working with date year month and day--------------------------")
d = datetime.date(2016,7,16) # datetime.date(2016, 7, 16) date(YYYY, M, D) don't put 0 like date(2016,07,16) it will through Syntax error invalid token
print(d) # 2016-07-16

tday = datetime.date.today() # datetime.date(2017, 12, 17)
print(tday) # 2017-12-17
print(tday.day) # 17
print(tday.month) # 12
print(tday.year) # 2017

print(tday.weekday())
print(tday.isoweekday())

# weekday() Monday - 0 , Tuesday - 1, Wednesday - 2, Thursday - 3, Friday - 4, Saturday - 5, Sunday - 6
# _isoweekday() Monday - 1, Tuesday - 2, Wednesday - 3, Thursday - 4, Friday - 5, Saturday - 6, Sunday - 7

#timedelta(     [days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
tdelta = datetime.timedelta(days = 7) #time difference between two dates 
tdelta = datetime.timedelta(seconds = 86400)
print(tday + tdelta) # date after 7 days 2017-12-24 2017-12-18
print(tday - tdelta) # date before 7 days 2017-12-10 2017-12-16

bday = datetime.date(1993,12,29)

till_days = bday - tday #datetime.timedelta(-8754)
print(till_days) # -8754 days, 0:00:00
print(till_days.days) # -8754
print(till_days.total_seconds()) # -756345600.0

print(till_days.max) # 999999999 days, 23:59:59.999999
print(till_days.min) # -999999999 days, 0:00:00
print(till_days.seconds) #0
print(till_days.microseconds) #0
print(till_days.resolution) # 0:00:00.000001


print("------------------------Working with time hour minute and seconds-------------------------------")

t = datetime.time(12,59,10,10520)  # date(hour, Minute, seconds, microseconds)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

print("-------------------------Working with date and time together------------------------")

dt = datetime.datetime(2017,11,30,13,4,45,10903) # datetime(YYYY,M,D,hour, Minute, seconds, microseconds)
print("date and time : "+str(dt)) # date and time : 2017-11-30 13:04:45.010903
print(dt.time()) # 13:04:45.010903
print(dt.date()) # 2017-11-30

print(dt.day) # 30
print(dt.month) # 11
print(dt.year) # 2017

print(dt.hour) # 13
print(dt.minute) # 4
print(dt.second) # 45

tdelta = datetime.timedelta(hours = 7) #time difference between two dates

print(dt + tdelta) # date time after 7 hour
print(dt - tdelta) # date time before 7 hour



print("-------------------------Working with time zone------------------------")
dt_today = datetime.datetime.today() # 2017-12-17 16:15:13.508845 current machine date and time
dt_now = datetime.datetime.now() # 2017-12-17 16:15:13.508844 current machine date and time
dt_utcnow = datetime.datetime.utcnow() # 2017-12-17 10:45:13.508844 current UTC date and time

print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz

dt = datetime.datetime(2017,11,9,13,26,16, tzinfo = pytz.UTC) # 2017-11-09 13:26:16+00:00

print(dt)

dt_now = datetime.datetime.now(tz = pytz.UTC) # 2017-12-17 10:48:52.611104+00:00 current UTC date and time with timezone related
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC) # 2017-12-17 10:48:52.611104+00:00
print(dt_utcnow)