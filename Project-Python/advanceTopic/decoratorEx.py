"""
Python has an interesting feature called decorators to add functionality to an existing code.

A decorator takes in a function, adds some functionality and returns it.

We can see that the decorator function add some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper.
The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).
"""
print("*******************Example 1 without parameter******************")
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


ordinary() #I am ordinary

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty() # I got decorated I am ordinary


#In the example shown above, make_pretty() is a decorator. In the assignment step.
pretty = make_pretty(ordinary)
#The function ordinary() got decorated and the returned function was given the name pretty.

#Generally, we decorate a function and reassign it as,
ordinary = make_pretty(ordinary)


#This is a common construct and for this reason, Python has a syntax to simplify this.
# We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,

@make_pretty
def ordinary1():
    print("I am ordinary")
    




print("*******************Example 2 with parameter*********************")

#Decorating Functions with Parameters

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

divide(2,5) 
#I am going to divide 2 and 5
#0.4

divide(2,0)
#I am going to divide 2 and 0
#Whoops! cannot divide



print("*******************Example 3 comman for all decorator*************")

#we can make general decorators that work with any number of parameter. In Python, this magic is done as function(*args, **kwargs). In this way, args will be the tuple
# of positional arguments and kwargs will be the dictionary of keyword arguments. An example of such decorator will be.

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner




print("*******************Example 4 chaining************") 
# Chaining Decorators in Python : a function can be decorated multiple times with different (or same) decorators. 

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")


output = """
is equivalent to

def printer(msg):
    print(msg)
printer = star(percent(printer))

******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************

"""

print("*******************# Note the way is used to go, that will only use to come************")

@percent
@star
def printer1(msg):
    print(msg)
printer1("Hello")
output = """

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""


#class decorator
def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")

foo()


class decorator2:
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def foo1():
    print("inside foo()")

foo1()


def my_logger(orig_func):

    import logging
    logging.basicConfig(filename = '{}.log'.format(orig_func.__name__), level = logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info('Ran with args{}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper
    
def my_timer(orig_func):
    
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print("{} ran in {} sec".format(orig_func.__name__, t1 - t2))
        return result
    return wrapper