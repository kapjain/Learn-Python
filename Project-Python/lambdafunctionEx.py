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
