"""
1. Immutable
2. does not support slicing and subscription
3. element must be immutable

Frozenset: Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable 
lists, frozensets are immutable sets.

Frozen set is just an immutable version of a Python set object. While, elements of a set can be modified at any time, elements of frozen set remains the same after creation.

Due to this, frozen sets can be used as key in Dictionary or as element of another set. But like sets, it is not ordered (the elements can be set at any index).

['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',
 
  'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
"""


fs1 = frozenset() # empty frozen set
# fs = {} this will not create empty frozen set it will create empty dictionary

fs2 = frozenset({1})# single element frozen set

fs3 = frozenset({1,2,3,4})

fs4 = frozenset({1, 'a', 'kapil', 3.14})

# fs5 = frozenset({1, 2, [1,2,3]}) TypeError: unhashable type: 'list', element must be immutable


#frozenset([iterable]): optional. an object that could be a sequence (string, frozensets) or collection (frozenset, dictionary) or iterator object
# empty frozenset
print(frozenset()) #frozenset({})

# string
l = frozenset('aeiou')
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# tuple
l = frozenset(('a', 'e', 'i', 'o', 'u'))
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# list
l = frozenset(['a', 'e', 'i', 'o', 'u'])
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# set
l = frozenset({'a', 'e', 'i', 'o', 'u'})
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# frozenset
l = frozenset(frozenset({'a', 'e', 'i', 'o', 'u'}))
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# dictionary
l = frozenset({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l)#frozenset({'i', 'u', 'o', 'e', 'a'}

# range
l = frozenset(range(10))
print(l)# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# l = frozenset(range(10), [1,2,3]) TypeError: frozenset() takes at most 1 argument (2 given)


input("wait to press enter!")