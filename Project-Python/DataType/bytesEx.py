"""
bytes([source[, encoding[, errors]]]): The bytes() method returns a immutable bytes object initialized with the given size and data.
The bytes() method returns a bytes object which is an immmutable (cannot be modified) sequence of integers in the range 0 <=x < 256.

bytes() Parameters: The bytes() takes three optional parameters:

source (Optional) -   source to initialize the array of bytes.
encoding (Optional) - if source is a string, the encoding of the string.
errors (Optional) -   if source is a string, the action to take when the encoding conversion fails (Read more: String encoding)

The source parameter can be used to initialize the byte array in the following ways:

String :    Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
Integer :   Creates an array of provided size, all initialized to null
Object  :   Read-only buffer of the object will be used to initialize the byte array
Iterable :  Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
No source (arguments) :    Creates an array of size 0

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
  
   'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 
   'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
   'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

a = b'hi'
print(type(a)) # <class 'bytes'>

#Example 1: Convert string to bytes

strg = 'hi'
#a = bytes(strg) #TypeError: string argument without an encoding

barr = strg.encode('utf-8')
print(barr)# output: b'hi'

string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)# output b'Python is interesting.'


#Example 2: Create a byte of given integer size
size = 5
arr = bytes(size)
print(arr) #output: b'\x00\x00\x00\x00\x00'


#Example 4: Convert iterable list to bytes
rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr)# output: b'\x01\x02\x03\x04\x05'


#Example 5: create an empty bytes
b = bytes()
print(b)# b''


l = ['k','z']
# bytes(l)  TypeError: 'str' object cannot be interpreted as an integer