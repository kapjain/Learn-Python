"""
a generator is a functionEx that returns an object (iterator) which we can iterate over (one value at a time).

Important:Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever
they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement
was last executed).

1. Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is 
that the __iter__() and __next__() methods are created automatically.

2. Another key feature is that the local variables and execution state are automatically saved between calls. This made the functionEx easier to write and much
 more clear than an approach using instance variables like self.index and self.data.

3. In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. In combination,
 these features make it easy to create iterators with no more effort than writing a regular functionEx.

https://www.youtube.com/watch?v=bD05uGo_sVI best youtube video

"""

#Note : You can assign iterator object to any no of time but can iterate over that only one time per object.


"""
Python Generator Expression:  
The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

difference between a list comprehension and a generator expression:

1. The major difference between a list comprehension and a generator expression is that while list comprehension produces the entire list, generator expression
produces one item at a time.
They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.


2. Memory Efficient
A normal functionEx to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence
is very large.
Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

"""


#***************************Example 1:************************************

def reverse(data):
    for index in range(len(data)-1, -1, -1): # so that it will also include 0
        yield data[index]


for char in reverse('golf'):
    print(char)

#or

r = reverse('hi')
print(next(r))
print(next(r))
# print(next(r)) StopIteration
print(r.next()) # AttributeError: 'generator' object has no attribute 'next'

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1)) #['f', 'l', 'o', 'g']

#***************************Example 2:************************************

def square_numbers(nums):
    result = []#A normal functionEx to return a sequence will create the entire sequence in memory before returning the result
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums) # [1,4,9,14,25]


def square_number(nums):
    for i in nums:
        yield (i*i)
my_num = square_number([1,2,3,4,5])
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
#print(next(my_num)) stopIteration

for num in my_num:
    print(num)


#***************************Example 3:************************************


import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
        print("And the next number is... %d!" %(random_number))

a = lottery()
print("a: ",a) # a:  <generator object lottery at 0x017BBA50>

b = lottery()
c = b 
d = b 

e = list(c)
f = list(d)
print("b: ",b) # b:  <generator object lottery at 0x017CE240>
print("c: ",c) # c:  <generator object lottery at 0x017CE240>
print("d: ",d) # d:  <generator object lottery at 0x017CE240>
print("e: ",e) # e:  [18, 25, 18, 15, 11, 29, 11]
print("f: ",f) #f:  []


input("wait here")
e = list(lottery())
f = list(lottery())

print("e: ",e)
print("f: ",f)
