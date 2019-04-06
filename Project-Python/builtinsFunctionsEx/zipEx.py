"""
zip(*iterables): The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples. 

Parameter: The zip() function takes: iterables - can be built-in iterables (like: list, string, dict), or user-defined iterables (object that has __iter__ method).


Return Value from zip() : The zip() function returns an iterator of tuples based on the iterable object.

    1. If no parameters are passed, zip() returns an empty iterator
    2. If a single iterable is passed, zip() returns an iterator of 1-tuples. Meaning, the number of elements in each tuple is 1.
    3. If multiple iterables are passed, ith tuple contains ith Suppose, two iterables are passed; one iterable containing 3 and other containing 5 elements. Then,
     the returned iterator has 3 tuples. It's because iterator stops when shortest iterable is exhaused.


Note: #zip(*zippedList): The * operator can be used in conjuncton with zip() to unzip the list.
"""

#Example 1: How zip() works in Python?
result = zip()
resultList = list(result)
print(resultList)


numberList = [1, 2, 3]
strList = ['one', 'two', 'three']
result = zip(numberList, strList)
resultSet = set(result)
print(resultSet)  #{(3, 'three'), (1, 'one'), (2, 'two')}




#Example 2: Different Number of Elements in Iterables Passed to zip()
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
result = zip(numbersList, numbersTuple)
resultSet = set(result)
print(resultSet) # {(2, 'TWO'), (1, 'ONE'), (3, 'THREE')}


result = zip(numbersList, strList, numbersTuple)
resultSet = set(result)
print(resultSet) # {(1, 'one', 'ONE'), (2, 'two', 'TWO')}



#Example 3: Unzipping the Value Using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList) # [('x', 3), ('y', 4), ('z', 5)]

c, v =  zip(*resultList)# Note: #zip(*zippedList): The * operator can be used in conjuncton with zip() to unzip the list.
print('c =', c) # c = ('x', 'y', 'z')
print('v =', v) # v = (3, 4, 5)




a = list(zip(range(5),range(1,20,2)))
print(a) [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9)]

l1=[1,2]
l2=[1]
l3=zip(l1,l2)
print(l3) #  <zip object at 0x0358E440>

