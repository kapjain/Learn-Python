"""
First-class Function:  "A programming language is said to have first-class functions if it treats functions as first-class citizens."

First-class Citizen (Programming): "A first-class citizen (sometimes called first-class objects) in a programming language is an entity
which supports all the operations generally available to other entities. These operations typically include being passed as an argument,
returned from a function and assigned to a variable."


What is closure:
The technique by which some data ("Hello") gets attached to the code is called closure in Python.
This value in the enclosing scope is remembered even when the variable goes out of scope or the functionEx itself is removed from the
current namespace.

1. A functionEx defined inside another functionEx is called a nested functionEx. Nested functions can access variables of the 
enclosing scope.
2. In Python, these non-local variables are read only by default and we must declare them explicitly as non-local (using nonlocal 
keyword) in order to modify them.


When to use closures?
Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution 
to the problem.

Conditions for creating closure:

1. We must have a nested functionEx (inner_func inside a outer_func).
2. The nested inner_func must refer to a value defined in the enclosing outer_func.
3. The enclosing outer_func must return the nested inner_func.

"""

print("*********************Example 1 Just to understand****************")
def outer_func():
    message = 'Hi'
    
    def inner_func():
        print(message)
    
    return inner_func()
print(outer_func()) #output  : Hi and None


print("*********************Example 2 Just to understand****************")
def outer_func1():
    message = 'Hi'
    
    def inner_func1():
        print(message)
    
    return inner_func1
print(outer_func1()) #output  : <function outer_func1.<locals>.inner_func1 at 0x035CCB70>



print("*********************closure Example ****************")
def outer_func2():
    message = 'Hi'
    
    def inner_func2():
        print(message)
    
    return inner_func2
closure = outer_func2() # now closure is functionEx which is equal to inner_func2
print(closure) # <functionEx outer_func2.<locals>.inner_func2 at 0x02DADC90>
print(closure.__name__) #inner_func2
closure()#hi
print(outer_func2()) #<functionEx outer_func2.<locals>.inner_func2 at 0x0336DB70>

#This value in the enclosing scope is remembered even when the variable goes out of scope or the functionEx itself is removed from the current namespace.
del outer_func2
closure() # hi
# outer_func2() NameError: name 'outer_func2' is not defined


print("closure.__closure__[0].cell_contents : ",closure.__closure__[0].cell_contents)
#output: closure.__closure__[0].cell_contents :  Hi




input("Please wait here")
print("*********************Example 4****************")
def outer_func3(msg):
    message = msg
    
    def inner_func3():
        print(message)
    
    return inner_func3

hi_func = outer_func3('Hi')
hello_func = outer_func3('Hello')
hi_func()
hello_func()
#hello_func("hi") #TypeError: inner_func3() takes 0 positional arguments but 1 was given



print("*********************Example 5 Passing parameter in closure****************")
def outer_func4(msg):
    message = msg
    
    def inner_func4(msg2):# we can pass parameter in inner functionEx
        print(message,msg2)
    
    return inner_func4

hi_func = outer_func4('Hi')

hi_func('hello')


#
import logging
logging.basicConfig(filename = 'closure.log', level = logging.INFO)

def logger(func):
    def inner_logger(*args):
        logging.info("executing {} function with {} parameter".format(func.__name__,args))
        print(func(*args))
    return inner_logger

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,2) # 5
sub_logger(3,2) # 1
