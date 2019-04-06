"""
The bytearray() method returns a bytearray object which is an array of the given bytes.
The syntax of bytearray() method is:
bytearray([source[, encoding[, errors]]])

The bytearray() method returns a bytearray object which is a mutable (can be modified) sequence of integers in the range 0 <=x < 256.

bytearray() Parameters

The bytearray() takes three optional parameters:

source (Optional) - source to initialize the array of bytes.
encoding (Optional) - if source is a string, the encoding of the string.
errors (Optional) - if source is a string, the action to take when the encoding conversion fails

The source parameter can be used to initialize the byte array in the following ways:


String :    Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
Integer :   Creates an array of provided size, all initialized to null
Object :    Read-only buffer of the object will be used to initialize the byte array
Iterable :  Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
No source (arguments):     Creates an array of size 0.

['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
  '__subclasshook__', 
  
  'append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index', 'insert',
 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'pop', 
 'remove', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
  'swapcase', 'title', 'translate', 'upper', 'zfill']

"""

a = bytearray(b'hi')
print(type(a)) # <class 'bytearray'>

#Example 1: Convert string to bytes

strg = 'hi'
barr = strg.encode('utf-8')
print(barr)# output: b'hi'

string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8') #mandatory to pass encoding


print(arr)# output bytearray(b'Python is interesting.')


#Example 2: Create a byte of given integer size
size = 5
arr = bytearray(size)
print(arr) #output: bytearray(b'\x00\x00\x00\x00\x00')


#Example 4: Convert iterable list to bytes
rList = [1, 2, 3, 4, 5]
arr = bytearray(rList)
print(arr)# output: bytearray(b'\x01\x02\x03\x04\x05')


#Example 5: create an empty bytes
b = bytearray()
print(b)# bytearray(b'')


l = ['k','z']
# bytearray(l)  TypeError: an integer is required





a = bytearray('hi', 'utf-8')
print(id(a)) # 56912320

a[0]=99 # pass an ASCII value of character #
print(a) #  bytearray(b'ci')

print(id(a)) # 56912320 



