# Packing and Unpacking Arguments in Python: We use two operators * (for tuples) and ** (for dictionaries).

a = ("MNNIT Allahabad", 5000, "Engineering") # Packing
(college, student, type_ofcollege) = a       # Unpacking

"""
Background 
Consider a situation where we have a function that receives four arguments. We want to make a call to this function and we have a list of size 4 with us that has all arguments for the function. If we simply pass a list to the function, the call doesn’t work. 
"""

def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(my_list) # TypeError: fun() takes exactly 4 arguments (1 given)


#Unpacking 
#We can use * to unpack the list so that all elements of it can be passed as different parameters.

def fun(a, b, c, d):
    print(a, b, c, d)
 
my_list = [1, 2, 3, 4]
fun(*my_list)

def result(x, y):
    return x * y
z = (10, 100)
print (result(*z))


# Note: We need to keep in mind that the no. of arguments must be the same as the length of the list that we are unpacking for the arguments.

args = [0, 1, 4, 9]
def func(a, b, c):
    return a + b + c
func(*args) # func() takes 3 positional arguments but 4 were given


# Packing : When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments in a tuple. 

def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# ** is used for dictionaries 

def fun(a, b, c):
    print(a, b, c)
d = {'a':2, 'b':4, 'c':10} # dictionary keys must be string
fun(**d)

def fun(a, b, c):
    print(a, b, c)
d = {'a':2, 'b':4, 1:10}
fun(**d)  # TypeError: fun() keywords must be strings


def test(a, *args, **kwargs):
	print(kwargs)

test(1,2,{"c":12})
test(1,2,**{"c":12})


_, b, *x, _ = ("I ", "love ", "Geeks ", "for ", "Geeks ", 3000) 
  
# print details 
print(b)
print(x)
print(_)

a, b, *x, a = ("I ", "love ", "Geeks ", "for ", "Geeks ", 3000) 
  
# print details 
print(b)
print(x)
print(_)

a, b, *_, c = ("I ", "love ", "Geeks ", "for ", "Geeks ", 3000) 
  
# print details 
print(a)
print(b) 
print(c)
print(_)

#If we used * with a variable then all those would get into that variable as a list.

def arithmetic_operations(arr: list):
  MAX = max(arr)
  MIN = min(arr)
  SUM = sum(arr)
  AVG = SUM/len(arr)
    
  return (SUM, AVG, MAX, MIN)

arr = [5, 8, 9, 12, 50, 3, 1]
# for all data
sum_arr, avg_arr, max_arr, min_arr = arithmetic_operations(arr)
print("CASE 1 ", sum_arr, avg_arr, max_arr, min_arr)

#for only avg and max
_, avg_arr, max_arr, _ = arithmetic_operations(arr)
print("CASE 2 ", avg_arr, max_arr)

# for only sum and min
sum_arr, *_, min_arr = arithmetic_operations(arr)
print("CASE 3 ", sum_arr, min_arr,_)
