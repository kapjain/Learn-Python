"""
Must to know:
1. Operator precedence and their associativity: 
Operators in the same box group execute left to right (except for exponentiation, which groups from right to left).

(expressions...), [expressions...], : Binding or tuple display, list display, dictionary display, set display
{key: value...}, {expressions...} 
x[index], x[index:index],           : Subscription, slicing, call, attribute reference
x(arguments...), x.attribute 
await x                             : Await expression
**                                  : Exponentiation 
+x, -x, ~x                          : Positive, negative, bitwise NOT
*, @, /, //, %                      : Multiplication, matrix multiplication, division, floor division, remainder
+, -                                : Addition and subtraction
<<, >>                              : Shifts
&                                   : Bitwise AND
^                                   : Bitwise XOR
|                                   : Bitwise OR
in, not in, is, is not, <,          : Comparisons, including membership tests and identity tests
<=, >, >=, !=, == 
not x                               : Boolean NOT
and                                 : Boolean AND
or                                  : Boolean OR
if – else                           : Conditional expression
lambda                              : Lambda expression

Note: a. x < y < z neither means (x < y) < z nor x < (y < z). x < y < z is equivalent to x < y and y < z, and is evaluates 
from left-to-right.
b. Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is evaluated
before the left-hand side.
+=, -=, *=, /+, //+, %= **=

2. Division operator in Python:
Python 2.7: The / (division) and // (floor division) operators yield the quotient of their arguments. The numeric arguments are 
            first converted to a common type. Plain or long integer division yields an integer of the same type; the result is that
            of mathematical division with the ‘floor’ function applied to the result. Division by zero raises the ZeroDivisionError 
            exception.
print(3/2) # 1
print(3//2) # 1

When devident or divisor is float then result will be in float only.
print(3.0/2) # 1.5
print(3/2.0) # 1.5
print(3.0/2.0) # 1.5

Python 3.5: The / (division) and // (floor division) operators yield the quotient of their arguments. The numeric arguments are 
            first converted to a common type. Division of integers yields a float, while floor division of integers results in an 
            integer; the result is that of mathematical division with the ‘floor’ function applied to the result. Division by zero
            raises the ZeroDivisionError exception.
print(3/2) # 1.5
print(3//2) # 1

When devident or divisor is float then result will be in float only.
print(3/2.0) # 1.5
print(3//2.0) # 1.0


3. Not equal operator:
print( 2 <> 3 ) # True
print( 2 <> 3 ) # SyntaxError: invalid syntax in python 3.7


4. Shift Operator:
 Left shift(<<) operator shift the bits towards left.
 Right shift(>>) operator shift the bits towards right.
 print(10<<2) # 40
 steps: a. convert decimal into binary number (10 - 00001010)
        b. append or prepend the zero's in binary number (00101000)
        c. convert new number into decimal(00101000 - 40)


5. Unary ~ operator:
The unary ~ (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is defined as -(x+1). 
It only applies to integral numbers. (https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations)
~x = -x-1
print(~5) #-6
print(~(-4)) # 3


6. 'and' operator:
a. if the both the operands are non-zero, non empty list or(tuple, set, dictionary,string, frozenset, bytes , butearray) Then result
will be the value of second operand.
print([1,2,3] and (1,2,3,4)) # (1,2,3,4)

b. if first operand or both are zero , or empty list or(tuple, set, dictionary,string, frozenset, bytes , butearray) Then result will be
the value of first operand.
print([] and (1,2,3,4)) # []
print([] and ()) # []

c. if second operand is zero, or empty list or(tuple, set, dictionary,string, frozenset, bytes , butearray) Then result will be
the value of second operand.
print((1,2,3,4) and []) # []


7. 'or' operator:
a. if the first or both the operands are non-zero, non empty list or(tuple, set, dictionary,string, frozenset, bytes , butearray) Then result
will be the value of first operand.
print((1,2,3,4) or []) # (1,2,3,4)
print([1,2,3] or (1,2,3,4)) # [1,2,3]

b. if first operand or both are zero , or empty list or(tuple, set, dictionary,string, frozenset, bytes , butearray) Then result will be
the value of second operand.
print([] or (1,2,3,4)) # (1,2,3,4)
print([] or ()) # ()

"""


## Arithmetic Operators:
a,b = 3,2
print("a + b: ", a + b) # 5
print("a - b: ", a - b) # 1
print("a * b: ", a * b) # 6
print("a / b: ", a / b) # 1.5
print("a // b: ", a / b) # 1
print("a % b: ", a % b) # 1
print("a ** b: ", a ** b) # 9


## Comparison (Relational) Operators:
a, b = 5, 20
if ( a == b ):
    print ("a is equal to b")
else:
    print ("a is not equal to b")

if ( a != b ): # not equal <> this available in 2.7 but not available in 3.6
    print ("a is not equal to b")
else:
    print ("a is equal to b")

if ( a < b ):
    print ("a is less than b") 
else:
    print ("a is not less than b")

if ( a > b ):
    print ("a is greater than b")
else:
    print ("a is not greater than b")

if ( a <= b ):
    print ("a is either less than or equal to  b")
else:
    print ("a is neither less than nor equal to  b")

if ( b >= a ):
    print ("b is either greater than  or equal to b")
else:
    print ("b is neither greater than  nor equal to b")

    
## Assignment Operators:
a = 21
b = 10
c = 0
c += a
print ("c += a: ", c ) # 31


## Bitwise Operators:
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 

print ("a & b:", a & b) # 12 = 0000 1100
print ("a | b:", a | b) # 61 = 0011 1101
print ("a ^ b:", a ^ b) # 49 = 0011 0001
print (" ~a :", ~a ) # -61 = 1100 0011
print ("a << 2:", a << 2) # 240 = 1111 0000
print ("a >> 2:", a << 2) # 15 = 0000 1111


## Logical Operators
"""
Note: Here operands can be anything like a integer, float, bool, complex, string, list, tuple, dictionary, set, frozenset, range, bytes, bytearray
"""
print(2 and 3) # 3 if a and b both are non zero then result will be the value of b in and operator
print(3 and 2) # 2
print(2 and 0) # 0
print(0 and 2) # 0
print(0 and 0) # 0

print(2 or 3) # 2 if a and b both are non zero then result will be the value of a in or operator
print(3 or 2) # 3
print(2 or 0) # 2
print(0 or 2) # 2
print(0 or 0) # 0

print(not 3)# False
print(not 0)# True



print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True


print(2 and True)# True
print(True and 2)# 2
print(2 and False)# False
print(False and 2)# False
print(False and False)# False
print(False and 0)# False
print(0 and False)# 0

print(2 or True)# 2
print(True or 2)# True
print(2 or False)# 2
print(False or 2)# 2
print(False or False)# False
print(False or 0)# 0
print(0 and False)# False

    
## Membership Operators:
a, b, c, d = 1, 5, [1,2,3], [[1,2,3],4,5]
print(a in c)# True
print(b in c)# False
# print(a in b) TypeError: argument of type 'int' is not iterable
print(a not in c)# False
print(b not in c)# True
print(a in c in d)# True it work like a in c and c in d


## Identity Operators:
a,b = 1,1
print(id(a))#1633277744 return the memory address of object
print(id(b))#1633277744

print(a is b)# True
print(a == b)# True

print(id(a) is id(b))# False
print(id(a) == id(b))# True

print(id(a) is not id(b))# True
print(id(a) != id(b))# False


## Ternary Operator:
x,y=20,50
big = x if x > y else y
print(big)#50
