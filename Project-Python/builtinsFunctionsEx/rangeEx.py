"""
The range() constructor returns an immutable sequence object of integers between the given start integer to the stop integer.

range() constructor has two forms of definition:
1. range(stop)
2. range(start, stop[, step])

range() Parameters:

1. start - integer starting from which the sequence of integers is to be returned
2. stop - integer before which the sequence of integers is to be returned. The range of integers end at stop - 1.
3. step (Optional) - integer value which determines the increment between each integer in the sequence

Return value from range(): range() returns an immutable sequence object of integers depending upon the definitions used:
1. range(stop):
    a. Returns a sequence of numbers starting from 0 to stop - 1
    b. Returns an empty sequence if stop is negative or 0.

2. range(start, stop[, step])

The return value is calculated by the following formula with the given constraints:

r[n] = start + step*n (for both positive and negative step)
where, n >=0 and r[n] < stop (for positive step)
where, n >= 0 and r[n] > stop (for negative step)

Note: 1. (If no step) Step defaults to 1. Returns a sequence of numbers starting from start and ending at stop - 1.
      2. (if step is zero) Raises a ValueError exception
      3. (if step is non-zero) Checks if the value constraint is met and returns a sequence according to the formula
        If it doesn't meet the value constraint, Empty sequence is returned.


"""
range() constructor has two forms of definition:
1. range(stop)
2. range(start, stop[, step])

['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 
 'count', 'index', 'start', 'step', 'stop']
"""




print(lrange(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9] # (If no step) Step defaults to 1
print(list(range(1,10,2))) # [1, 3, 5, 7, 9]
print(list(range(-10))) # [] Because stop value is negative
print(list(range(0))) # [] Because stop value is 0
print(list(range(-10,-20))) # [] When step value is positive, start value should be less than stop value, otherwise it will return []
print(list(range(-30,-20))) # [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21]
print(list(range(-30,-20,-1)) # [] When step value is negative, start value should be greater than stop value, otherwise it will return []
print(list(range(-10,-20,-1))) # [-10, -11, -12, -13, -14, -15, -16, -17, -18, -19]

print(range(1,10,0)) # ValueError: range() arg 3 must not be zero

Note: We've converted the range to a Python list, as range() returns a generator-like object that only prints the output on demand
However, the range object returned by the range constructor can also be accessed by its index. It supports both positive and negative indices.
You can access the range object by index as:

rangeObject[index]                                                                                                                        """

r = range(10,-1,-1)
print(r[0]) #10
print(r[1]) #9

# Like range(), but instead of returning a list, returns an object that generates the numbers in the range on demand. 
# For looping, this is slightly faster than range() and more memory efficient.
