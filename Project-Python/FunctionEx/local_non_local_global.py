# Example 1:
def f():
    print(s)
s = "I love Geeksforgeeks"
f() # I love Geeksforgeeks


# Example 2:
def f():
    s = "Me too."
    print(s)
s = "I love Geeksforgeeks"
f()
print(s)
#Me too.
#I love Geeksforgeeks


# Example 3:
def f():
    print(s) # UnboundLocalError: local variable 's' referenced before assignment
    s = "Me too."
    print(s)
s = "I love Geeksforgeeks"
f()
print(s)


# Example 4:
def f():
    global s
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)
s = "Python is great!"
f()
print(s)
# Python is great!
# Look for Geeksforgeeks Python Section.
# Look for Geeksforgeeks Python Section.


# Example 5:
a = 15
def change():
    a = a + 5 # UnboundLocalError: local variable 'a' referenced before assignment
    print(a)
change()


# Example 6:
x = 15
def change():
    global x
    x = x + 5 
    print("Value of x inside a function :", x)
change()
print("Value of x outside a function :", x)

# Example 7:
def add():
     x = 15
       
     def change():
         global x
         x = 20
     print("Before making changing: ", x)
     print("Making change")
     change()
     print("After making change: ", x)
  
add()
print("value of x",x)

Before making changing:  15
Making change
After making change:  15
value of x 20


# Example 8:
Code 1: Create a config.py file to store global variables:

x = 0
y = 0
z ="none"
Code 2: Create a modify.py file to modify global variables:

import config
config.x = 1
config.y = 2
config.z ="geeksforgeeks"

Code 3: Create a main.py file to modify global variables:

import config
import modify
print(config.x)
print(config.y)
print(config.z)



# Example 1:
a = 15
def outer_function():
    a = 5
    def inner_function():
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)


a = 15
def outer_function():
    global a
    a = 5
    def inner_function():
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)

a = 15
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)


a = 15
def outer_function():
    a = 5
    def inner_function():
        global a
        a = 10
        print("1. functionEx: ",a)
    inner_function()    
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)

# Note: at a time , you can use either nonlocal or global keyword. otherwise it will throw error
a = 15
def outer_function():
    global a
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)
