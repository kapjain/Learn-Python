"""
#timedelta(     [days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])

All arguments are optional and default to 0. Arguments may be ints, longs, or floats, and may be positive or negative.

Only days, seconds and microseconds are stored internally. Arguments are converted to those units:

    A millisecond is converted to 1000 microseconds.
    A minute is converted to 60 seconds.
    An hour is converted to 3600 seconds.
    A week is converted to 7 days.

and days, seconds and microseconds are then normalized so that the representation is unique, with

    0 <= microseconds < 1000000
    0 <= seconds < 3600*24 (the number of seconds in one day)
    -999999999 <= days <= 999999999

"""
import datetime


tday = datetime.date.today()

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











