"""
slice(stop)
slice(start, stop, step)

The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).
The slice object is used to slice a given sequence (string, bytes, tuple, list or range) or any object which supports sequence protocol (implements __getitem__() and __len__() method).

slice() Parameters

slice() mainly takes three parameters which have the same meaning in both constructs:

    start - starting integer where the slicing of the object starts
    stop - integer until which the slicing takes place. The slicing stops at index stop - 1.
    step - integer value which determines the increment between each index for slicing
If a single parameter is passed, start and step are set to None.
"""

#Example 1: Create a slice object for slicing

# contains indices (0, 1, 2)
print(slice(3))

# contains indices (1, 3)
print(slice(1, 5, 2))




#Example 2: Get substring from a given string using slice object

pyString = 'Python'

# contains indices (0, 1, 2)
# i.e. P, y and t
sObject = slice(3)

print(pyString[sObject])

# contains indices (1, 3)
# i.e. y and h
sObject = slice(1, 5, 2)
print(pyString[sObject])



#Example 3: Get substring from a given string using negative index

pyString = 'Python'

# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)

print(pyString[sObject])


#Example 6: Get substring from a given string by extending indexing syntax

pyString = 'Python'

# contains indices (0, 1, 2)
# i.e. P, y and t
print(pyString[0:3])

# contains indices (1, 3)
# i.e. y and h
print(pyString[1:5:2])


l5 = list(range(10))

print(l5[1])#1
print(l5[-3])#7
print(l5[1:7:1])#[1,2,3,4,5,6]
print(l5[1:7:2])#[1,3,5]
print(l5[1:5])#[1,2,3,4]
print(l5[5:6])#[5]

print(l5[:])#[0,1,2,3,4,5,6,7,8,9]
print(l5[::])#[0,1,2,3,4,5,6,7,8,9]

print(l5[::1])#[0,1,2,3,4,5,6,7,8,9]
print(l5[3:])#[3,4,5,6,7,8,9]
print(l5[:6])#[0,1,2,3,4,5]


print(l5[-9:-6:1])#[1,2,3]
print(l5[-1:-5:-1])#[9,8,7,6]
print(l5[-1:-5:-2])#[9,7]

print(l5[9:0])#[]
print(l5[6:3:1])#[] if start index> end index result will be []
print(l5[::-1])#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0] Reverse