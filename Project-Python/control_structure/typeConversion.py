'''
repr(x)
    

Converts object x to an expression string.

set(s)
    

Converts s to a set.

dict(d)
    

Creates a dictionary. d must be a sequence of (key,value) tuples.

frozenset(s)
    

Converts s to a frozen set.

chr(x)
    

Converts an integer to a character.

unichr(x)
    

Converts an integer to a Unicode character.

ord(x)
    

Converts a single character to its integer value.


'''



"""_int(x [,base])
Converts x to an integer. base specifies the base if x is a string.
_int() argument must be a string, a bytes-like object or a number, not 'list'
"""

a = '12'
print("a: " +a)
b =int(a)
print("b:" +str(b))


"""float(x) -> floating point number
Convert a string or number to a floating point number, if possible."""

a = (12.5)#its not an tuple this will consider as float
b =float(a)
print("b:" +str(b))

"""
complex(real [,imag])
complex(real, image) first argument must be a string or a number, not 'list'
complex() second argument must be a number, second arg can't be a string, not 'list'
complex() can't take second arg if first is a string"""

a = 2.5
b = 2 
c =complex(a,b)
print(c)

"""str(x) Converts object x to a string representation.
x can be anything"""

a=('kap',2+3j)
b=str(a)
print(b)

"""tuple(s)-> Converts s to a tuple.
if you convert dictionary to tuple it remove the values of dictionary
object should _iterable
"""

a={'kap':2+3j, 'kap1':2}
b=tuple(a)
print(b)

"""list(s)-> Converts s to a list.
if you convert dictionary to list it remove the values of dictionary
object should _iterable
"""

a={'kap':2+3j}
b=list(a)
print(b)

"""eval(str)
Evaluates a string and returns an object.
eval() arg 1 must be a string, bytes or code object"""
a='1+2+3'
c={'kap':2+3j, 'kap1':2}
b=eval(a,c)
print(b)

"""oct(x)->0o11
Converts an integer to an octal string."""

a = 9
b = oct(a)
print(b)

"""hex(x)->0x9
Converts an integer to an octal string."""

a = 9
b = hex(a)
print(b)



