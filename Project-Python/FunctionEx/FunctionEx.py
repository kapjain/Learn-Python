"""
First class objects in a language are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. 
A programming language is said to support first-class functions if it treats functions as first-class objects. Python supports the concept of First Class functions.


## Function defination:
def function_name (argument1, argument2..):
    statments
    return (statement)
    
## Function Calling
variable_name = function_name(argument_values)
"""

## Function Without argument
# function which return the value
def hello_world():
    return "Hello World"

output = hello_world()
print(output) # Hello World

# function which does not return any value
def print_name():
    print("Hello Kapil")

print_name()

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


# 1. Functions are objects: Various different names can be bound to the same function object.
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")


# 2. Functions can be passed as arguments to other functions:
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


# 3. Functions can return another function:
def create_adder(x):
    def adder(y):
        return x+y
    return adder
  
add_15 = create_adder(15)
print (add_15(10))

print (create_adder(20)(10))



## Nested Function
def func(x,y):
    print(x,y)

func1 = lambda x: lambda y: func(x,y)

def func2(x):
    def new_func(y):
        return func(x,y)
    return new_func
    
func1(2)(3)
func2(2)(3)


"""
In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and 
the lambda keyword is used to create anonymous functions. It has the following syntax:

lambda arguments: expression
1. This function can have any number of arguments but only one expression, which is evaluated and returned.
2. One is free to use lambda functions wherever function objects are required.

Without using Lambda : Here, both of them returns the cube of a given number. But, while using def, we needed to define a function with a name cube 
and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the return keyword.

Using Lambda : Lambda definition does not include a “return” statement, it always contains an expression which is returned. We can also put a lambda 
definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.
"""

# Python code to illustrate cube of a number  
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 
  
g = lambda x: x*x*x 
print(g(7)) 
  
print(cube(5)) 


# Python code to illustrate 
# map() with lambda() 
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 


# Python code to illustrate 
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
