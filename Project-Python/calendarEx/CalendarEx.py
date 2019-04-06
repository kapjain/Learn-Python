# Python program to display calendar of given month of the year

# import module
import calendar as c

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(c.month(yy, mm))
print(c.isleap(2017))
print(c.isleap(2010))
print(c.leapdays(2012, 2017))