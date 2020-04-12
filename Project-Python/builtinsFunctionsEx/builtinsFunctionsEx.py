# abs(number) :Return the absolute value(means return positive value) of a number. The argument may be an integer or a floating
# point number. If the argument is a complex number, its magnitude is returned.
print("******************************************abs() Example***********************************")
print(abs(-1)) # 1
print(abs(-2.3)) # 2.3
print(abs(-3+4j)) #return magnitude for 5.0
print(abs(0)) # 0
print(abs(True)) # 1
print(abs(False)) # 0
# abs(None) TypeError: bad operand type for abs(): 'NoneType'



# divmod(numerator, denominator) method takes two numbers 
# return: a pair of numbers (a tuple) consisting of their quotient and remainder. Return the tuple (x//y, x%y)
print("******************************************divmod() Example***********************************")

print(divmod(8, 3)) # (2, 2)
print(divmod(3, 8)) # (0, 3)
print(divmod(5, 5)) # (1, 0)

print(divmod(8.0, 3)) # (2.0, 2.0)
print(divmod(3, 8.0)) # (0.0, 3.0)
print(divmod(7.5, 2.5)) # (3.0, 0.0)
print(divmod(2.6, 0.5)) # (5.0, 0.10000000000000009)



# pow(base, exp, mod=None):  Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
print("******************************************pow() Example***********************************")
# positive x, positive y (x**y) 4
print(pow(2, 2)) 
# negative x, positive y 4
print(pow(-2, 2))
# positive x, negative y (x**-y) 0.25
print(pow(2, -2))
# negative x, negative y 0.25
print(pow(-2, -2))
print(pow(7, 2, 5)) # 4



#round(number[, ndigits]) : The round() method returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is
# provided, it rounds off the number to the nearest integer.
print("******************************************pow() Example***********************************")
print(round(10.9)) #11
print(round(10.5)) #10
print(round(10.4)) #10

print(round(12.33435,2)) #12.33
print(round(2.665, 2))# 2.67
print(round(2.664, 2))# 2.66
print(round(2.675, 2))# 2.67 # cannot be represented exactly as float
print(round(2.676, 2))# 2.68



# ascii(object) : The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII 
# characters in the string using \x, \u or \U escapes.
print("******************************************ascii() Example***********************************")
normalText = 'Python is interesting'
print(ascii(normalText)) # 'Python is interesting'

otherText = 'Pythön is interesting'
print(ascii(otherText)) # 'Pyth\xf6n is interesting'

randomList = ['Python', 'Pythön', 5]
print(ascii(randomList)) ['Python', 'Pyth\xf6n', 5]

print('Pyth\xf6n is interesting') # Pythön is interesting



# chr(ascii_value): 0 <= i <= 0x10ffff. valid range of the integer is from 0 through 1,114,111.
# return: a character (a string) from an integer (represents unicode code point of the character).
print("******************************************chr() Example***********************************")
print(chr(65))
#print(chr(1114112)) ValueError: chr() arg not in range(0x110000)
#print(chr(-1)) ValueError: chr() arg not in range(0x110000)



# ord(single_character): string length must be 1.
# returns: an integer representing Unicode code point for the given Unicode character(only character).
print("******************************************ord() Example***********************************")
print(ord('a'))
# print(ord('')) TypeError: ord() expected a character, but string of length 0 found
# print(ord('ab') TypeError: ord() expected a character, but string of length 2 found



# bin(integer or object): parameter must be integer
# return: the binary equivalent string of a given integer.
# If the parameter isn't an integer, it has to implement __index__() method to return an integer.
print("******************************************bin() Example***********************************")
print(bin(10)) # 0b1010
print(bin(0o31)) # 0b11001
print(bin(0xf)) # 0b1111
print(bin(10.3)) # TypeError: 'float' object cannot be interpreted as an integer

class Quantity:
    apple = 1
    orange = 2
    grapes = 12
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
print('The binary equivalent of quantity is:', bin(Quantity())) # 0b1111



# oct(integer or object): Return the octal representation of an integer
# return: its octal representation. 
# If the given number is not an int, it must implement __index__() method to return an integer.
print("******************************************oct() Example***********************************")
print(oct(10)) # 0o12
print(oct(0b101)) # 0o5
print(oct(0XA)) # 0o12

class Quantity:
    apple = 1
    orange = 2
    grapes = 12
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
print('The binary equivalent of quantity is:', oct(Quantity())) # 0o17



# hex(integer or object): Return the hexadecimal representation of an integer.
# return: hexadecimal string.
# If the given number isn't an int, it must implement __index__() method to return an integer.
print("******************************************hex() Example***********************************")
print(hex(435)) # 0x1b3
print(hex(0)) # 0x0
print(hex(-34)) # -0x22
print(type(hex(10))) # <class 'str'>

print(float.hex(2.5)) # 0x1.4000000000000p+1
print(float.hex(0.0)) # 0x0.0p+0
print(float.hex(10.5)) # 0x1.5000000000000p+3

class Quantity:
    apple = 1
    orange = 2
    grapes = 12
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
print('The binary equivalent of quantity is:', hex(Quantity())) # 0xf



# bool(object): The bool() method converts a value to Boolean (True or False)
# returns: False when yo don't pass any value
#    None
#    False
#    Zero of any numeric type. For example, 0, 0.0, 0j
#    Empty sequence. For example, (), [], ''.
#    Empty mapping. For example, {}
#    objects of Classes which has __bool__() or __len()__ method which returns 0 or False
print("******************************************bool() Example***********************************")
print(bool([])) # False
print(bool([0]))# [0] is True
print(bool(0.0))# False
print(bool(None))# False
print(bool(True))# True
print(bool('Easy string'))# True



# int(string_of_digit or int or float, base): 
# return: an integer object from any number or string.
# int(x=0, base=10) by default and base  Can be 0 (code literal) or 2-36.
# an integer object from the given number or string, treats default base as 10 and (No parameters) returns 0
"""
Convert a number or string to an integer, or return 0 if no arguments are given.  If x is a number, return x.__int__().  For floating point numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in the given base.  The literal can be preceded by '+' or '-' and be surrounded by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal.
"""
print("******************************************int() Example***********************************")
print(int(123)) # 123
print(int(123.23)) # 123
print(int('123')) # 123
print(int('1010', 2)) # 10
print(int('0b1010', 2)) # 10
print(int('12', 8)) # 10
print(int('0o12', 8)) # 10
print(int('A', 16)) # 10
print(int('0xA', 16)) # 10
# print(int('a')) ValueError: invalid literal for int() with base 10: 'a'
print(int('1')) # 1



# complex([real[, imag]]):The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.
# Note: The string passed to the complex() should be in the form real+imagj or real+imagJ otherwise value error
print("******************************************complex() Example***********************************")
print(complex(2, -3)) # (2-3j)
print(complex(1)) # (1+0j)
print(complex()) # 0j
print(complex('5-9j')) # (5-9j)
print(complex('-2')) # (-2+0j)
print(complex('j')) # 1j
# print(complex('a')) ValueError: complex() arg is a malformed string



# float(number or string): The float() method returns a floating point number from a number or a string.
# Must contain decimal numbers.Leading and trailing whitespaces are removed.Optional use of "+", "-" signs.Could contain NaN, Infinity, inf (lowercase or uppercase).
print("******************************************float() Example***********************************")
print(float(10)) # 10.0
print(float(11.22)) # 11.22
print(float("-13.33")) # -13.33
print(float("     -24.45\n")) # -24.45

# string float error
# print(float("abc")) ValueError: could not convert string to float: 'abc'

# print(float('0b10')) ValueError: could not convert string to float: '0b10'
print(float(0b10)) # 2.0
print(float(0o10)) # 8.0
print(float(0x10)) # 16.0



#The dir() method tries to return a list of valid attributes of the object.
print("******************************************dir() Example***********************************")
class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']
    

teacher = Person()
print(dir(teacher))
l = [1,2,3]
print(dir(l))
print(dir())#If object is not passed to the dir() method, it returns the list of names in the current local scope.



#The hash(object) method returns the hash value of an object if it has one.
#object-the object whose hash value is to be returned (integer, string, float)
print("******************************************hash() Example***********************************")

# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))


# help(object) The help() method calls the built-in Python help system.
# object (optional) - you want to generate the help of the given object

print("******************************************help() Example***********************************")
help(list)

# all(iterable) : Return True if all elements of the iterable are true (or if the iterable is empty).
print("******************************************all() Example***********************************")
l = [1,2,3]
m = [1,2,0]
n = [1, False]
o = []
p = [[],'',(),{},frozenset({}),set(),0,0.0,False,None,0+0j]
q = [[None],'',(),{},frozenset({}),set(),0,0.0,False,None,0+0j]
print(all(l)) # True
print(all(m)) # False
print(all(n)) # False
print(all(o)) # True because iterable is empty
print(all(p)) # False
print(all(q)) # False


# any(iteratable) : Return True if any element of the iterable is true. If the iterable is empty, return False.
print("******************************************any() Example***********************************")
l = [1,2,3]
m = [False,0]
n = [1, False]
o = []
p = [[],'',(),{},frozenset({}),set(),0,0.0,False,None,0+0j]
q = [[None],'',(),{},frozenset({}),set(),0,0.0,False,None,0+0j]
print(any(l)) # True
print(any(m)) # False 
print(any(n)) # True
print(any(o)) # False because iterable is empty
print(any(p)) # False
print(any(q)) # True




#The id() function returns identity (unique integer) of an object.
print("******************************************id() Example***********************************")
class Foo:
    b = 5

dummyFoo = Foo()
print('id of dummyFoo =',id(dummyFoo))

print('id of 5 =',id(5))

a = 5
print('id of a =',id(a))

b = a
print('id of b =',id(b))

c = 5.0
print('id of c =',id(c))



#object() This returns a featureless object which is a base for all classes.
print("******************************************object() Example***********************************")
test = object()

print(type(test))
print(dir(test)) #<class 'object'>
#['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']








#sum(iterable, start): The sum() function adds the items of an iterable and returns the sum.
print("******************************************sum() Example***********************************")

"""
The sum() function adds start and items of the given iterable from left to right.
sum() Parameters
1. iterable - iterable (list, tuple, dict etc) whose item's sum is to be found. Normally, items of the iterable should be numbers.
2. start (optional) - this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

Return Value from sum() : The sum() function returns the sum of start and items of the given iterable.

Note: If you need to add floating point numbers with exact precision then, you should use math.fsum(iterable) instead
If you need to concatenate items of the given iterable (items must be string), then you can use join() method.
''.join(sequence)
"""

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum) # 4.5

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum) # 14.5
