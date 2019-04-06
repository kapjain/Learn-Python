#template.format(p0, p1, ..., k0=v0, k1=v1, ...)
a = int(input("Enter value of a  :"))
b = int(input("enter value of b :"))

print(format("Welcome", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.2f"))
c=a+b

print ("sum=%s,a=%s"%(c,a))
print ("sum={} a={} ,b= {} ".format(c,a,b))
print ('sum:', c)

fname = "Joe"
lname = "Who"
age = "24"
print ("{} {} is {} years ".format(fname, lname, age))

print ("{0} {1} is {2} years".format(fname, lname, age))


s = 'Hello World!'
print (s + "TEST")

a = 10
x= 'word a'
y= "This is a sentence."
z = """This is a paragraph. It is
made up of multiple lines and sentences."""
w='''hjklkjhg'''

print(w)

print (a)
print ("\b")
print(x)
print(y)
print(z)

temp = """the str.rjust() method of string objects, which right-justifies a string in a field of a given width by padding it with spaces on the left. 
There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long,
 they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative,
  which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

There is another method, str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs:"""

a = 3
print(repr(a).ljust(9))
#output'3        '
print(repr(a).rjust(9))
#output'        3'
print(repr(a).center(9))
#output'    3    '

a=12345
repr(a).rjust(2)
# output'12345'



print('12'.zfill(5))
#output '00012'
print('-3.14'.zfill(7))
#output '-003.14'
print('3.14159265359'.zfill(5))
#output '3.14159265359'

#Basic usage of the str.format()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#output: We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
#output: spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))
#output: eggs and spam

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
#output: This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
#output: The story of Bill, Manfred, and Georg.



#'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:

contents = 'eels'
print('My hovercraft is full of {!s}.'.format(contents))
# output: My hovercraft is full of eels.
print('My hovercraft is full of {!r}.'.format(contents))
# output: My hovercraft is full of 'eels'.


import math
print('The value of PI is approximately {0:5.3f}.'.format(math.pi))
#output:The value of PI is approximately 3.142.

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide

#{0:10} or {0:10s} string

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

#Jack       ==>       4098
#Dcab       ==>       7678
#Sjoerd     ==>       4127



print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))