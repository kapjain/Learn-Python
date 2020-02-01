"""
## Function defination:
def function_name (argument1, argument2..):
    statments
    return (statement)
    
## Function Calling
variable_name = function_name(argument_values)
"""

## Function Without argument
def hello_world():
    return "Hello World"


# Required/Positional Arguments
# you need to pass all the argument which has given in the function defination_
def printme( str1 ):
    "This prints a passed string into this function"
    print (str1)

# Now you can call printme_ function
printme('kapil')



# Keyword Arguments

# Function definition is here
def printinfo( name, age, sex ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    print ("sex ", sex)
    return

# Now you can call printinfo_ function
printinfo( age = 50, name = "m",sex='f' )
# printinfo( "m",'k',age = 50 )#TypeError: printinfo() got multiple values for argument 'age'
# printinfo(  'f',age = 50, "m" ) #SyntaxError: positional argument follows keyword argument
printinfo(  'f', 50, sex="m" ) 



# Default Arguments

# Function definition is here Note:non-default argument follows default argument
def printinfo1( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return

# Now you can call printinfo_ function
printinfo1( age = 50, name = "m" )
printinfo1( name = "m")



# Variable-length Arguments

# Function definition is here
def printinfo2( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return

# Now you can call printinfo2 function
printinfo2( 10 )
printinfo2( 70, 60, 50 )


# *args: it take non-keyword argument as a tuple
def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum
print(add(10,20,30))
print(add(10,20,30,40))

# **kwargs: it take keyword argument as a dictionary

def intro(**kwargs):
    print(kwargs)
    for firstname,lastname in kwargs.items():
        print('{} {}'.format(firstname,lastname))
        print('%s %s'%(firstname,lastname))
intro(kapil='jain', umesh='pawar')


def intro1(*args, **kwargs):
    print(args)
    print(kwargs)
intro1(1,2 ,kapil='jain', umesh='pawar')
intro1()




#lambda Function
# lambda args: expresion
sum1 = lambda arg1, arg2: arg1 + arg2

map(lambda a: a*a,[1,2,3,4])

# Now you can call sum as a function
print ("Value of total : ", sum1( 10, 20 ))
print ("Value of total : ", sum1( 20, 20 ))

def a_void_function():
    a = 1
    b = 2
    c = a + b
    print(c)

x = a_void_function()
print(x) # None By default function return None


#Various different names can be bound to the same function object.
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")


#Functions can be passed as arguments to another function. If you have used functions like map, filter and reduce in Python, then you already know about this.
#Such function that take other functions as arguments are also called higher order functions. Here is an example of such a function.

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result
operate(inc,3) # 4
operate(dec,3) # 2

