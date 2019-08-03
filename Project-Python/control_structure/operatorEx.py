input("press enter to exit")

a = 21
b = 10
c = 0

c = a + b#31
print ("Line 1 - Value of c is ", c)

c = a - b#11
print ("Line 2 - Value of c is ", c)

c = a * b#210
print ("Line 3 - Value of c is ", c) 

c = a / b#2.1
print ("Line 4 - Value of c is ", c) 

c = a % b#1
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b#8 
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b#2
print ("Line 7 - Value of c is ", c)


a = 5
b = 20
if ( a == b ):
    print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")

if ( a != b ):#<> this available in 2.7 but not available in 3.6
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")


if ( a < b ):
    print ("Line 4 - a is less than b") 
else:
    print ("Line 4 - a is not less than b")

if ( a > b ):
    print ("Line 5 - a is greater than b")
else:
    print ("Line 5 - a is not greater than b")


if ( a <= b ):
    print ("Line 6 - a is either less than or equal to  b")
else:
    print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
    print ("Line 7 - b is either greater than  or equal to b")
else:
    print ("Line 7 - b is neither greater than  nor equal to b")
    
a = 21
b = 10
c = 0

c += a
print ("Value of c is ", c )




a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

# left shift operator shift the bits towards left
c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

# Right shift operator shift the bits towards right
c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)

"""
The unary ~ (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is defined as -(x+1). 
It only applies to integral numbers.
https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations
~x = -x-1
"""
# 

a,b = 5,-4
print(~a)#-6
print(~b)# 3




    
a,b,c = 2,3,0
print(a and b)#3 if a is non zero then result will be the value of b
print(a and c)#0
print(c and b)#0 if First value is zero then result will be the value of first
print(c and c)#0

print(a or b)#2
print(a or c)#2
print(c or b)#3
print(c or a)#2


print(not a)# False
print(not c)# True
print(not False)# True
print(not True)# False



print(True and False) #False
print(True and True) #True
print(False and True)#False
print(False and False)# False

print(c and False)# 0
print(False and c)# False
print(False and a)# False
print(c and False)# 0 

print(False or c)#0
print(False or a)#2


    
#Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
a = 1
b = 5
c = [1,2,3]
d = [[1,2,3],4,5]


print(a in c)# True
print(b in c)# False
# print(a in b) TypeError: argument of type 'int' is not iterable

print(a not in c)# False
print(b not in c)# True

print(a in c in d)# True it work like a in c and c in d



a,b = 1,1

print(id(a))#1633277744
print(id(b))#1633277744

print(a is b)# True
print(a == b)# True

print(id(a) is id(b))# False
print(id(a) == id(b))# True

print(id(a) is not id(b))# True
print(id(a) != id(b))# False


x,y=20,50
big = x if x > y else y
print(big)#50
