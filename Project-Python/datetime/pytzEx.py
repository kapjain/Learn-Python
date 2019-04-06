import datetime
import pytz

print("***************************************")
dt_utcnow = datetime.datetime.now(tz = pytz.UTC)

print(dt_utcnow)  # Universal Time Coordinated

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain')) # changing timezone 'Asia/Kolkata'

print(dt_mtn)



for i,tz in enumerate(pytz.all_timezones):
    print(i,tz)



print("***************** Complex example**********************")
dt_now = datetime.datetime.now()
print("current IST time: ",str(dt_now))

tz_ist = pytz.timezone('Asia/Kolkata')

dt_now = tz_ist.localize(dt_now)

print("current IST time: ",str(dt_now))


dt_us_east = dt_now.astimezone(pytz.timezone('US/Eastern'))
print("current US/Eastern time: ",str(dt_us_east))



print("***************************************")
dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)

print(dt_now.strftime("%B %d, %Y"))

dt_str = 'November 10, 2017'

dt = datetime.datetime.strptime(dt_str,"%B %d, %Y")
print(dt)

#strptime - string to datetime
#strftime - datetime to string