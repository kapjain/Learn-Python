""" 
sorted(iterable[, key][, reverse]):  The sorted() method returns a sorted list from the given iterable. The sorted() method sorts
the elements of a given iterable in a specific order - Ascending or Descending.


sorted() Parameters
    1. iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator 
    2. reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
    3. key (Optional) - function that serves as a key for the sort comparison

Return : sorted list

ord(' ') #32
ord('a') #97
ord('A') # 65

Note: sorting work on ascii value base
"""

l = ['e', 'a', 'u', 'o', 'i']
print(sorted(l)) # ['a', 'e', 'i', 'o', 'u']

s = 'Hi This is Kapil'
print(sorted(s)) # [' ', ' ', ' ', 'H', 'K', 'T', 'a', 'h', 'i', 'i', 'i', 'i', 'l', 'p', 's', 's']

t = ('e', 'a', 'u', 'o', 'i')
print(sorted(t)) # ['a', 'e', 'i', 'o', 'u']

t = {'e', 'a', 'u', 'o', 'i'}
print("reverse=False : ",sorted(t, reverse=False)) # reverse=False :  ['a', 'e', 'i', 'o', 'u']

t = {'e', 'a', 'u', 'o', 'i'}
print("reverse=True : ",sorted(t, reverse=True)) # reverse=True :  ['u', 'o', 'i', 'e', 'a']

d = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(d, reverse=True)) # ['u', 'o', 'i', 'e', 'a']

fs = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(fs, reverse=True)) # ['u', 'o', 'i', 'e', 'a']


"""
How to sort using your own function with key parameter?
If you want your own implementation for sorting, sorted() also accepts a key function as an optional parameter.
Based on the results of the key function, you can sort the given iterable.

sorted(iterable, key=len)
"""
# Builtin function
t = ['abc','ghjsd', 'a']
print(sorted(t, key=len))

# Example 1
s = [
('Kapil',101,'8871337193'),
('Vishant',100,'887133723'),
('Sachin',103,'9871337193'),
]
def getroll(item):
    return item[2]
print(sorted(s,key = getroll ))
    
# Example 2
k = [
('Kapil',101),
('Vishant',100,'887133723'),
('Sachin',103,'9871337193'),
]
def getroll(item):
    return item[1]
print(sorted(k,key = getroll ))

# Example 3
k = [
('Kapil',101),
('Vishant',100,'887133723'),
('Sachin',103,'9871337193'),
]

def getroll(item):
    return item[2]
print(sorted(k,key = getroll)) # IndexError: tuple index out of range

# Example 4
s = [
('Kapil','101','8871337193'),
('Vishant',100,'887133723'),
('Sachin',103,'9871337193'),
]
def getroll(item):
    return item[1]
print(sorted(s,key = getroll )) # TypeError: '<' not supported between instances of 'int' and 'str'
