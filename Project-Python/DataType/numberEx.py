"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__',
 '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__',
  '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
   '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
    '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
    'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
"""

# int , float and complex
"#Note 1. We can use the type() function to know which class a variable or a value belongs to and isinstance() #function to check if it belongs to a particular class."


a = 5


print(type(a)) # Output: <class 'int'>
print(type(5.0)) # Output: <class 'float'>
c = 5 + 3j
print(c + 3) # Output: (8+3j)
print(isinstance(c, complex)) # Output: True




"#Note 2. While integers can be of any length, a floating point number is accurate only up to 15 decimal places (the 16th place is inaccurate)."


"""
Number System        Prefix
Binary             '0b' or '0B'
Octal              '0o' or '0O'
Hexadecimal        '0x' or '0X'
"""



print(0b1101011) # Output: 107
print(0xFB + 0b10) # Output: 253 (251 + 2)
print(0o15) # Output: 13


"Note 3. : System will convert all values into decimal then add and then return the result in integer"



#Type Conversion : We can convert one type of number into another. This is also known as coercion
#Operations like addition, subtraction coerce integer to float implicitly (automatically), if one of the operand is float.

print(1 + 2.0)# 3.0
from decimal import Decimal
#We can see above that 1 (integer) is coerced into 1.0 (float) for addition and the result is also a floating point number. We can also use built-in functions like int(), float() and complex() to convert between types explicitly. These function can even convert from strings.

print(int(2.3)) # 2
print(int(-2.8)) # -2
print(float(5)) # 5.0
print(complex('3+5j')) # (3+5j)
Decimal(1.234) # Decimal('1.2339999999999999857891452847979962825775146484375')



"# note 4. : When converting from float to integer, the number gets truncated (integer that is closer to zero)."




#Python Decimal : Python built-in class float performs some calculations that might amaze us. We all know that the sum of 1.1 and 2.2 is 3.3, but Python seems to disagree.
print((1.1 + 2.2) == 3.3) # output False

"""

What is going on?
It turns out that floating-point numbers are implemented in computer hardware as binary fractions, as computer only understands binary (0 and 1). Due to this reason,
 most of the decimal fractions we know, cannot be accurately stored in our computer.
Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and we can only approximate it.
Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011... and our computer only stores a finite number of it.
This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error in Python.

When to use Decimal instead of float?

We generally use Decimal in the following cases.

    When we are making financial applications that need exact decimal representation.
    When we want to control the level of precision required.
    When we want to implement the notion of significant decimal places.
    When we want the operations to be carried out like we did at school

Important Note: Decimal support all operations with int like Decimal + int but does not support anything for float. It will throw error for float
TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
"""

print(1.1 + 2.2) # output  3.3000000000000003

import decimal
#To overcome this issue, we can use decimal module that comes with Python. While floating point numbers have precision up to 15 decimal places, the decimal module has user settable precision.
print(0.1) # Output: 0.1
print(decimal.Decimal(0.1)) # Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')


"This module is used when we want to carry out decimal calculations like we learned in school."
#It also preserves significance. We know 25.50 kg is more accurate than 25.5 kg as it has two significant decimal places compared to one."


from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))




"""Python Fractions

Python provides operations involving fractional numbers through its fractions module.

A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.

We can create Fraction objects in various ways."""

import fractions

# Output: 3/2
print(fractions.Fraction(1.5))

# Output: 5
print(fractions.Fraction(5))

# Output: 1/3
print(fractions.Fraction(1,3))


#While creating Fraction from float, we might get some unusual results. This is due to the imperfect binary floating point number representation as discussed in the previous section.

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))



from fractions import Fraction as F

# Output: 2/3
print(F(1,3) + F(1,3))

# Output: 6/5
print(1 / F(5,6))

# Output: False
print(F(-3,10) > 0)

# Output: True
print(F(-3,10) < 0)




"Python Mathematics"

import math

# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))


"Python Randam"
import random

# Output: 16
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())