"""

1. Mutable
2. does not support slicing and subscription
3. element must be immutable
4. does not allow duplicate
5. can contain different type of data


A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
However, the set itself is mutable. We can add or remove items from it.
Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.


The set() constructor constructs a Python set from the given iterable and returns it.

set() Parameters: set() takes a single optional parameter:
    iterable (Optional) - a sequence (string, tuple, etc.) or collection (set, dictionary, etc.) or an iterator object to be converted into a set

Return value from set(): set() returns:
    an empty set if no parameters are passed and a set constructed from the given iterable parameter

Note: Empty sets cannot be created using {}, use set()
Note: It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, 
    like list, set or dictionary, as its element


['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
 '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', 
 '__str__', '__sub__', '__subclasshook__', '__xor__',
 
 'add', 'update', 'pop', 'remove', 'discard','clear', 'copy', 
 'isdisjoint',  'issubset',  'issuperset',
 'union', 'intersection','intersection_update' ,'difference', 'difference_update',  'symmetric_difference', 'symmetric_difference_update']
 
"""


s1 = set()# empty set
# s = {} this will not create empty set it will create empty dictionary

s2 = {1}# single element set

s3 = {1,2,3,4}

s4 = {1, 'a', 'kapil', 3.14}

# s5 = {1, 2, [1,2,3]} TypeError: unhashable type: 'list', element must be immutable


#set([iterable]): optional. an object that could be a sequence (string, sets) or collection (set, dictionary) or iterator object
# empty set
print(set()) #{}

# string
l = set('aeiou')
print(l)#{'i', 'u', 'o', 'e', 'a'}

# tuple
l = set(('a', 'e', 'i', 'o', 'u'))
print(l)#{'i', 'u', 'o', 'e', 'a'}

# list
l = set(['a', 'e', 'i', 'o', 'u'])
print(l)#{'i', 'u', 'o', 'e', 'a'}

# set
l = set({'a', 'e', 'i', 'o', 'u'})
print(l)#{'i', 'u', 'o', 'e', 'a'}

# frozen set
l = set(frozenset({'a', 'e', 'i', 'o', 'u'}))
print(l)#{'i', 'u', 'o', 'e', 'a'}

# dictionary
l = set({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l)#{'i', 'u', 'o', 'e', 'a'}

# range
l = set(range(10))
print(l)# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# l = set(range(10), [1,2,3]) TypeError: set() takes at most 1 argument (2 given)


#access element of set
# first way
s = {1, 2, 3}
print(list(s)[0]) # 1

# second way
for e in s:break # e is now an element from s
print(e) #1

# third way
next(iter(s))

i = iter(s)
print(next(i))#1
print(next(i))#2
print(next(i))#3



## Basic operation
s = {'i', 'u', 'o', 'e', 'a'}

# print(s*3) TypeError: unsupported operand type(s) for *: 'set' and 'int'
# print(s+s1) TypeError: unsupported operand type(s) for +: 'set' and 'set'
#min(s) TypeError: '<' not supported between instances of 'str' and 'int'
print(min(s1)) #1
print(max(s1)) #3
#print(s1[::]) TypeError: 'set' object is not subscriptable
print(1 in s1) # True
print(len(s1)) #3



# add(immutable object)
# return : None
s = {'i', 'u', 'o', 'e', 'a'}
s.add(1)
print(s) #{1, 'a', 'e', 'i', 'u', 'o'}
s.add((1,2,3))
print(s) #{1, 'a', (1, 2, 3), 'e', 'i', 'u', 'o'}
s.add(range(4))
print(s) # {range(0, 4), 1, 'a', (1, 2, 3), 'e', 'i', 'u', 'o'}
# s.add([1,2]) TypeError: unhashable type: 'list'
# s.add() TypeError: add() takes exactly one argument (0 given)


# update(iterable object) update a set with union of itself and other
# return : None
s = {'i', 'u', 'o', 'e', 'a'}
s.update([1,2,3])
print(s) #{'o', 1, 2, 3, 'e', 'a', 'i', 'u'}
s.update({'1':'a','2':'b'})
print(s) #{'o', 1, 2, 3, 'e', 'a', 'i', 'u', '1', '2'}
# s.update(3) TypeError: 'int' object is not iterable


# discard(value): remove an element from the set if it is there, other wise do nothing
# return : None
s = {'i', 'u', 'o', 'e', 'a'}
s.discard(1) #value not found remain unchanged
print(s) # {'i', 'u', 'o', 'e', 'a'}
s.discard('a')
print(s) # {'i', 'u', 'o', 'e'}
# s.discard('a','b') TypeError: discard() takes exactly one argument (2 given)
# s.discard() TypeError: discard() takes exactly one argument (0 given)


#remove(value), it remove a element from a set. it must be a meber other it will through Keyerror
# return : None
s = {'i', 'u', 'o', 'e', 'a'}
s.remove('a')
print(s) # {'u', 'o', 'i', 'e'}
#s.remove() TypeError: remove() takes exactly one argument (0 given)
#s.remove('a','b') TypeError: remove() takes exactly one argument (2 given)
#s.remove(1) KeyError: 1


#s.pop() it remove an arbitrary element from set and raise key error when set is empty
# return: value
s = {'i', 'u', 'o', 'e', 'a'}
s.pop()#'u'
s.pop()#'a'
s.pop()#'i'
s.pop()#'o'
s.pop()#'e'
print(s)# set()
#s.pop() KeyError: 'pop from an empty set'
#s.pop(1) TypeError: pop() takes no arguments (1 given)


#clear() remove all element from the set
# return: None
s = {'i', 'u', 'o', 'e', 'a'}
s.clear()
print(s)# set()
s.clear() # it will raise any error even if there is no element in the set
print(s) #set()


# copy(): D.copy() a shallow copy of D
# return: shalow copy of set
s = {'i', 'u', 'o', 'e', 'a'}
s1 = s.copy()
print(s) #{'u', 'e', 'a', 'o', 'i'}
print(s1) #{'e', 'o', 'i', 'a', 'u'}
s1.add(1)
print(s1) #{'u', 1, 'e', 'a', 'o', 'i'}
print(s1) #{'e', 'o', 'i', 'a', 'u'}


# isdisjoint(): Two sets are said to be disjoint sets if they have no common elements.
# return: True if two sets are disjoint sets. If not, it returns False.

A = {1, 5, 9, 0}
B = {2, 4, -5}
#The isdisjoint() method takes a single argument (a set).
#You can also pass an iterable (list, tuple, dictionary and string) to disjoint(). The isdisjoint() method will automatically convert iterables to 
#set and checks whether the sets are disjoint or not.
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
print('Are A and B disjoint?', A.isdisjoint(B)) # True
print('Are A and C disjoint?', A.isdisjoint(C))    # False
A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D ={1 : 'a', 2 : 'b'}
E ={'a' : 1, 'b' : 2}
print('Are A and B disjoint?', A.isdisjoint(B)) # False
print('Are A and C disjoint?', A.isdisjoint(C)) # False
print('Are A and D disjoint?', A.isdisjoint(D)) # True
print('Are A and E disjoint?', A.isdisjoint(E)) # False



# issubset():
# return: True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B)) # Returns True
# B is not subset of A
print(B.issubset(A)) # Returns False
print(A.issubset(C)) # Returns False
print(C.issubset(B)) # Returns True



# issuperset():
# return: True if a set has every elements of another set (passed as an argument). If not, it returns False.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
print(A.issuperset(B)) # Returns True
print(B.issuperset(A)) # Returns False
print(C.issuperset(B)) # Returns True



# union():
# return: a new set with distinct elements from all the sets.
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C= {1, 2, 3}

#we can use | operator for union
print('A U B =', A.union(B)) # A | B {2, 'a', 'd', 'c'}
print('B U C =', B.union(C)) # {1, 2, 3, 'd', 'c'}
print('A U B U C =', A.union(B, C)) # {1, 2, 3, 'a', 'd', 'c'}
print('A.union() = ', A.union()) # {'a', 'd', 'c'}



# intersection() method returns a new set with elements that are common to all sets.
A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}
#we can use & operator for intersection
print(B.intersection(A)) # {2, 5}
print(B.intersection(C)) # {2}
print(A.intersection(C)) # {2, 3}
print(C.intersection(A, B)) # {2}



# intersection_update() updates the set calling intersection_update() method with the intersection of sets.
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
result = A.intersection_update(B)
print('result =', result) # None
print('A =', A) # {2, 3, 4}
print('B =', B) # {2, 3, 4, 5, 6}



# difference: If A and B are two sets. The set difference of A and B is a set of elements that exists only in set A but not in B.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}
print(A.difference(B)) # Equivalent to A-B {'b', 'a', 'd'}
print(B.difference(A)) # Equivalent to B-A {'g', 'f'}



# difference_update() updates the set calling difference_update() method with the difference of sets.
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
result = A.difference_update(B)
print('A = ', A) # {'d', 'a'}
print('B = ', B) # {'c', 'g', 'f'}
print('result = ', result) # None



# symmetric_difference() :
# return: a new set which is the symmetric difference of two sets. 
#The symmetric difference of two sets A and B is the set of elements which are in either of the sets A or B but not in both.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}
print(A.symmetric_difference(B)) # A ^ B {'b', 'a', 'e'}
print(B.symmetric_difference(A)) # {'b', 'e', 'a'}
print(A.symmetric_difference(C)) # {'b', 'd', 'c', 'a'}
print(B.symmetric_difference(C)) # {'d', 'e', 'c'}


# symmetric_difference_update(): method updates the set calling the symmetric_difference_update() with the symmetric difference of sets.
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
result = A.symmetric_difference_update(B)
print('A = ', A) # {'a', 'e'}
print('B = ', B) # {'d', 'c', 'e'}
print('result = ', result) # None
