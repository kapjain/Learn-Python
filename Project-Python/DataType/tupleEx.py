"""

1. Immutable
2. support slicing
3. can contain mutable object 
4. can contain duplicate element
5. can contain multiple type of element

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 
  'count', 'index']
"""


t1 = ()#empty tuple
t2 = tuple()#empty tuple
t3 = (1,)#single element tuple
t4 = (1, 2, 3, 4)
t5 = (1,'hello',"Hi jone",3.14,(1,2,3))
t6 = (1,2,[1,2,3]) # can container mutable object

#tuple([iterable]): optional. an object that could be a sequence (string, tuples) or collection (set, dictionary) or iterator object
# empty tuple
print(tuple()) #()

# string
l = tuple('aeiou')
print(l)#('i', 'u', 'o', 'e', 'a')

# tuple
l = tuple(('a', 'e', 'i', 'o', 'u'))
print(l)#('i', 'u', 'o', 'e', 'a')

# list
l = tuple(['a', 'e', 'i', 'o', 'u'])
print(l)#('i', 'u', 'o', 'e', 'a')

# set
l = tuple({'a', 'e', 'i', 'o', 'u'})
print(l)#('i', 'u', 'o', 'e', 'a')

# frozen set
l = tuple(frozenset({'a', 'e', 'i', 'o', 'u'}))
print(l)#('i', 'u', 'o', 'e', 'a')

# dictionary
l = tuple({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l)#('i', 'u', 'o', 'e', 'a') Note: Keys in the dictionary are used as elements of the returned tuple

# range
l = tuple(range(10))
print(l)# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# l = tuple(range(10), [1,2,3]) TypeError: tuple() takes at most 1 argument (2 given)



#count(object or value) count the no of times value are there
l = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1,10)
print(l.count(10))#2
print(l.count(12))#0
#print(l.count(10,2)) TypeError: count() takes exactly one argument (2 given)
#print(l.count()) TypeError: count() takes exactly one argument (0 given)



# index(value, start index, end index), note: return the lowest index
l = (1,2,3,4,5,1)
print(l.index(1))#0
print(l.index(2,0,4))#

#print(l.index(6))ValueError: 6 is not in list
#print(l.index()) TypeError: index() takes at least 1 argument (0 given)
#print(l.index(1,10,20)) ValueError: 1 is not in list
print(l.index(1,2))  # 5
#print(l.index(5,0,4)) ValueError: 5 is not in list
print(l.index(1,0,4))  # 0
