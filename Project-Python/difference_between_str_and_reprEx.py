"""
repr(object) : The repr() method returns a printable representation of the given object.

    Return a string containing a printable representation of an object. For many types, this functionEx makes an attempt to return a string that would yield 
    an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the 
    type of the object together with additional information often including the name and address of the object. A class can control what this functionEx returns 
    for its instances by defining a __repr__() method.

class str(object=''):
class str(object=b'', encoding='utf-8', errors='strict')

Return a string version of object. If object is not provided, returns the empty string. Otherwise, the behavior of str() depends on whether encoding or
errors is given, as follows.

If neither encoding nor errors is given, str(object) returns object.__str__(), which is the “informal” or nicely printable string representation of object.
For string objects, this is the string itself. If object does not have a __str__() method, then str() falls back to returning repr(object).

If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray). In this case, if object is a bytes 
(or bytearray) object, then str(bytes, encoding, errors) is equivalent to bytes.decode(encoding, errors). Otherwise, the bytes object underlying the buffer
object is obtained before calling bytes.decode(). See Binary Sequence Types — bytes, bytearray, memoryview and Buffer Protocol for information on buffer objects.
Passing a bytes object to str() without the encoding or errors arguments falls under the first case of returning the informal string representation 
(see also the -b command-line option to Python). For example:
>>> str(b'Zoot!')
"""

import datetime
import pytz
a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print('str(a): {}'.format(str(a))) # str(a): 2017-12-03 17:54:08.716043+00:00
print('str(a): {}'.format(str(b))) # str(a): 2017-12-03 17:54:08.716043+00:00

print

print('repr(a): {}'.format(repr(a))) # repr(a): datetime.datetime(2017, 12, 3, 17, 54, 8, 716043, tzinfo=<UTC>)
print('repr(a): {}'.format(repr(b))) # repr(a): '2017-12-03 17:54:08.716043+00:00'

print 






string = "hi \nwelcome to python \nworld"

print(repr(string)) #output:'hi \nwelcome to python \nworld'

print(str(string))

#hi 
#welcome to python 
#world


"""
Return value from repr() : The repr() method returns a printable representational string of the given object.

It returns a string that would yield an object with the same value when passed to eval().

eval(repr(obj)) = obj (approximation that holds true for most of built-in types)
"""

string = "hi \nwelcome to python \nworld"
print(repr(string)) #'hi \nwelcome to python \nworld'
print(eval(repr(string))) # 'hi \nwelcome to python \nworld'




b = bytes('pyth\xf6n', encoding='utf-8')
#print(str(b, encoding='ascii', errors='strict'))

#UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 4: ordinal not in range(128)