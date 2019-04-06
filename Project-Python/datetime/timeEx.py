import time

# 1,2,3 argument: NULL
print("time() : ",time.time()) # time() :  1513501919.0781207
print("ctime() :  ",time.ctime()) # ctime() :   Sun Dec 17 14:41:59 2017 current Machine time
print("gmtime() : ",time.gmtime()) # current UTC time
# gmtime() :  time.struct_time(tm_year=2017, tm_mon=12, tm_mday=17, tm_hour=9, tm_min=11, tm_sec=59, tm_wday=6, tm_yday=351, tm_isdst=0)



# 4. strftime(format, tuple) : return time in given  formate
print("strftime() : ",time.strftime("%b %d %Y %H:%M:%S", time.gmtime())) #strftime() :  Dec 17 2017 09:16:10
# %a    weekday name.
# %b    month name
# %c    date and time
# %e    day of a month
# %m    month in digit.
# %n    new line character.
# %S    second
# %t    tab character

# 5 . seconds(tuple) return default formated time date
print("asctime() : ",time.asctime(time.gmtime())) #asctime() :  Sun Dec 17 09:18:51 2017 


# 6. sleep(seconds)  # this will ask you to wait for 10 seconds
print("ctime() :  ",time.ctime()) # ctime() :   Sun Dec 17 14:52:28 2017
time.sleep(1) 
print("ctime() :  ",time.ctime()) # ctime() :   Sun Dec 17 14:52:38 2017


# 7. mktime(tuple) you can pass either 9 item sequence or t = (2014, 2, 17, 17, 3, 38, 1, 48, 0) return seconds
print("mktime() : ",time.mktime(time.gmtime())) # mktime() :  1513482899.0


# 8. localtime(seconds): return 9 item sequence
print("localtime() : ",time.localtime(time.time()))
#localtime() :  time.struct_time(tm_year=2017, tm_mon=12, tm_mday=17, tm_hour=14, tm_min=58, tm_sec=13, tm_wday=6, tm_yday=351, tm_isdst=0)


# 9. strptime(string,format of that string): return 9 item sequence
print("strptime() : ",time.strptime("26 Jun 14", "%d %b %y"))
#strptime() :  time.struct_time(tm_year=2014, tm_mon=6, tm_mday=26, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=177, tm_isdst=-1)