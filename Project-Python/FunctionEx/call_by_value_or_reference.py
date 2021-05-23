"""
Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”. In the event that you pass arguments like whole numbers,
strings or tuples to a function, the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function. 
Whereas passing mutable objects can be considered as call by reference because when their values are changed inside the function, then it will also be 
reflected outside the function.
"""
# Note: In python everything is a call by reference, but we can modify only mutable objects

# Immutable object: int , bool, string, tuple, frozentset
a = 10

def change(a):
    a = 11
    return
  
print(a)
change(a)
print(a)


# Mutable object: list, dict, set
a = [1,2,3]
def change(a):
    a.append(4)
    return
  
print(a)
change(a)
print(a)
