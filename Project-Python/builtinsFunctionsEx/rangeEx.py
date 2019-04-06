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
# empty range
print(list(range(0))) #[]

# using range(stop)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# using range(start, stop)
print(list(range(1, 10)))


"""
Note: We've converted the range to a Python list, as range() returns a generator-like object that only prints the output on demand
However, the range object returned by the range constructor can also be accessed by its index. It supports both positive and negative indices.
You can access the range object by index as:

rangeObject[index]                                                                                                                        """

r = range(10,-1,-1)
print(r[0]) #10
print(r[1]) #9

print(list(range(2, 14, 2))) # [2, 4, 6, 8, 10, 12]


start = 2
stop = -14
step = -2

print(list(range(4, -14, -2))) # [4, 3, 2, 0, -2, -4, -6, -8, -10, -12]

# value constraint not met
print(list(range(2, 14, -2))) # []

print(list(range(14, 2, -2))) # [14, 12, 10, 8, 6, 4]
