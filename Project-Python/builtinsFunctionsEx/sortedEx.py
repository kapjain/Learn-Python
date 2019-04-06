""" 
sorted(iterable[, key][, reverse]):  The sorted() method returns a sorted list from the given iterable. The sorted() method sorts the elements of a given iterable in a specific order - Ascending or Descending.


sorted() Parameters
    1. iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator 
    2. reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
    3. key (Optional) - function that serves as a key for the sort comparison

Return : sorted() method returns a sorted list from the given iterable.

ord(' ') #32
ord('a') #97
ord('A') # 65

Note: sorting work on ascii value base
"""

# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string 
pyString = 'Hi This is Kapil'
print(sorted(pyString)) # [' ', ' ', ' ', 'H', 'K', 'T', 'a', 'h', 'i', 'i', 'i', 'i', 'l', 'p', 's', 's']

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))


# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print("reverse=False : ",sorted(pySet, reverse=False)) # reverse=False :  ['a', 'e', 'i', 'o', 'u']

pySet = {'e', 'a', 'u', 'o', 'i'}
print("reverse=True : ",sorted(pySet, reverse=True)) # reverse=True :  ['u', 'o', 'i', 'e', 'a']

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(pyDict, reverse=True))

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(pyFSet, reverse=True))





"""
How to sort using your own function with key parameter?
If you want your own implementation for sorting, sorted() also accepts a key function as an optional parameter.
Based on the results of the key function, you can sort the given iterable.

sorted(iterable, key=len)
"""


# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList) #Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]