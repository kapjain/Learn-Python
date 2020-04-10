"""
1. Mutable
2. support slicing
3. can contain mutable object
4. can contain duplicate element
5. can contain multiple type of element

List: list is a sequential collection of heterogeneous element and mutable data structure.
its index start from 0 to n-1 or -n to -1
list operation are creation, accessing, modification, append, Concatenate , delete, pop, push, searching, count, sorting, indexing,slicing

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
   '__subclasshook__']

'append',  'insert', 'extend', 'pop', 'remove', 'clear', 'index', 'count', 'copy',  'reverse', 'sort'
"""
# Empty List
l = []
l1 = list()

# Single Element List
l2 = [1,] or [1]

# Multiple element list
l3 = [1, 2, 3, 4, 5] # same type of element
l4 = [1,'hello', "Hi jone", 3.14, [1,2,3], {1,2,3} ] # different type of element with mutable object


#list([iterable]): optional. an object that could be a sequence (string, tuples) or collection (set, dictionary) or iterator object

# Data type Conversion into list
# string
l = list('aeiou')
print(l)#['i', 'u', 'o', 'e', 'a']

# tuple
l = list(('a', 'e', 'i', 'o', 'u'))
print(l)#['i', 'u', 'o', 'e', 'a']

# list
l = list(['a', 'e', 'i', 'o', 'u'])
print(l)#['i', 'u', 'o', 'e', 'a']

# set
l = list({'a', 'e', 'i', 'o', 'u'})
print(l)#['i', 'u', 'o', 'e', 'a']

# frozen set
l = list(frozenset({'a', 'e', 'i', 'o', 'u'}))
print(l)#['i', 'u', 'o', 'e', 'a']

# dictionary
l = list({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l)#['i', 'u', 'o', 'e', 'a'] Note: Keys in the dictionary are used as elements of the returned list

# range
l = list(range(10))
print(l)# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# l = list(range(10), [1,2,3]) TypeError: list() takes at most 1 argument (2 given)

input("wait to press enter!")
#Accessing value from the list
#list[start index: end index: step value]
#start index is inclusive while end index is exclusive
# Note: if the step value is positive, it will move forward 0 to end and if the step value is negative, it will move backward end to 0
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[3])  # 3
print(l[-3])  # 7

print(l[1:5])  # [1, 2, 3, 4]
print(l[5:6])  # [5]
print(l[5:5])  # [] -->
print(l[6:4])  # [] --> when step is positive and start index is greater than(>) end index result will be []

print(l[5:])  # [5, 6, 7, 8, 9]
print(l[:3])  # [0, 1, 2]
print(l[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l[-1:5])  # [] -->
print(l[1:-5])  # [1, 2, 3, 4]
print(l[-1:-5])  # [] -->
print(l[-5:-1])  # [5, 6, 7, 8]

print(l[-2:])  # [8, 9]
print(l[:-2])  # [0, 1, 2, 3, 4, 5, 6, 7]

print(l[1:7:1])  # [1, 2, 3, 4, 5, 6]
print(l[1:7:2])  # [1, 3, 5]
print(l[1:2:2])  # [1]
print(l[1:1:2])  # [] -->


print(l[1:7:])  # [1, 2, 3, 4, 5, 6]
print(l[1::2])  # [1, 3, 5, 7, 9]
print(l[:5:2])  # [0, 2, 4]
print(l[::2])  # [0, 2, 4, 6, 8]
print(l[::])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l[-9:-6:1])  # [1, 2, 3]

print(l[1:7:-1])  # [] --> when step is negative and start index is less than(<) end index result will be []
print(l[7:1:-1])  # [7, 6, 5, 4, 3, 2]
print(l[:1:-1])  # [9, 8, 7, 6, 5, 4, 3, 2]
print(l[3::-1])  # [3, 2, 1, 0]
print(l[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(l[-1:-7:-1])  # [9, 8, 7, 6, 5, 4]
print(l[-7:-1:-1])  # [] -->


# Asignment
a = []
a[0]=10 # IndexError: list assignment index out of range

# updating value in the list
l3[0] = 10
l3[1] = (-1,-2,-3,-4)
print(l3)#[10,(-1,-2,-3,-4),3,4,5]
l3[0:] = "end"
print(l3)#['e', 'n', 'd']
#basic operations
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = ['hi','this','is','kapil']

#basic operation

print(l1 + l2)#[1,2,3,4,5,6,7,8,9,10]
print(l1*2)#[1,2,3,4,5,1,2,3,4,5]
print( 1 in l1 )# True
print(len(l1))#5
print(min(l1))#1 it doesn't works with mix list like int and str are in same list
print(max(l1))#5
print(min(l3))#hi check according to dictionary sequence
print(max(l3))#this


#append(object): The append() method appends a passed obj into the existing list.
#return: None
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l.append(10)
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l.append([1,2,3])
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3]]

l.append(range(11,15))
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3], range(11, 15)]

l.append(print("hi"))#hi
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3], range(11, 15), None]

l.append(2+3)
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3], range(11, 15), None, 5]

#l.append(object=3) TypeError: append() takes no keyword arguments
#l.append() TypeError: append() takes exactly one argument (0 given)
#l.append(1,2) TypeError: append() takes exactly one argument (2 given)

#insert(index, object)
# return: None
l = [1,2,3,4,5]
l.insert(0,0)
print(l)#[0, 1, 2, 3, 4, 5]

l.insert(-5,1.5)
print(l)#[0, 1.5, 1, 2, 3, 4, 5]

l.insert(4,range(6,8))
print(l)#[0, 1.5, 1, 2, range(6, 8), 3, 4, 5]

l.insert(5,3+4)
print(l)#[0, 1.5, 1, 2, range(6, 8), 7, 3, 4, 5]

l.insert(9, 10)
print(l)#[0, 1.5, 1, 2, range(6, 8), 7, 3, 4, 5, 10]

l.insert(20,12)# if the given index in not there and index value is positive then this will add the element at the last position
print(l)#[0, 1.5, 1, 2, range(6, 8), 7, 3, 4, 5, 10, 12]

l.insert(-20,233)# if the given index in not there and index value is negative then this will add the element at the first position
print(l)#[233,0, 1.5, 1, 2, range(6, 8), 7, 3, 4, 5, 10, 12]

l.insert(11,[1,2,3])
print(l)#[0, 1.5, 1, 2, range(6, 8), 7, 3, 4, 5, 10, 12, [1, 2, 3]]

# l.insert(2) TypeError: insert() takes exactly 2 arguments (1 given)
# l.insert() TypeError: insert() takes exactly 2 arguments (0 given)
# l.insert(index=0, object=1) TypeError: insert() takes no keyword arguments


#The extend(iterable) method appends the contents of seq or itratable object to list.
# return: None
l = [0, 1, 2,]
l.extend((10,11,12))
print(l)#[0, 1, 2, 10, 11, 12]

l.extend(range(13,16))
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15]

d = {'a' : 1, 'b' : 2}
l.extend(d)#dictionary
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15, 'a', 'b']

l.extend(d.values())
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15, 'a', 'b', 1, 2]

l.extend(d.items())
print(l)#[0, 1, 2,, 10, 11, 12, 13, 14, 15, 'a', 'b', 1, 2, ('a', 1), ('b', 2)]


l.extend({1,2})#set
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15, 'a', 'b', 1, 2, ('a', 1), ('b', 2), 'h', 1, 2]

l.extend('h')
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15, 'a', 'b', 1, 2, ('a', 1), ('b', 2), 1, 'h']

l.extend([]) # nothing chnaged
print(l)#[0, 1, 2, 10, 11, 12, 13, 14, 15, 'a', 'b', 1, 2, ('a', 1), ('b', 2), 1, 'h']

# l.extend(1) TypeError: 'int' object is not iterable
# l.extend(1,2,3) TypeError: extend() takes exactly one argument (3 given)
# l.extend() TypeError: extend() takes exactly one argument (0 given)
# l.extend([5,6],[7,8]) TypeError: extend() takes exactly one argument (2 given)
# l.extend(iterable="akp") TypeError: extend() takes no keyword arguments


# pop(index = -1), index is an optional parameter
# return: removed value
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l.pop()# it will remove the last element from the list and return the value of element
# 1
print(l)#[10, 9, 8, 7, 6, 5, 4, 3, 2]

l.pop(3)# if the index is given, it will remove the value of given index
print(l)#[10, 9, 8, 6, 5, 4, 3, 2]

# if the given index is not present in the list it will throw error
# l.pop(13) IndexError: pop index out of range
# l.pop(-10)IndexError: pop index out of range
# l.pop(index=2) TypeError: pop() takes no keyword arguments


# remove(object), object is mandatory parameter
# return: None
l = [10, 8, 6, 4, 2,[1,2,3],8,3]
l.remove(10)
print(l)#[8, 6, 4, 2,[1,2,3],8,3]

l.remove([1,2,3])
print(l)#[8, 6, 4, 2, 8 ,3]

l.remove(8) # If there the same value in the list, so it will remove whichaver value comes first(index 0,1,2,..n) 
# and remove only one object
print(l)#[6, 4, 2, 8 ,3]

l.remove(30) # if the given object is not present in the list. ValueError: list.remove(x): x not in list

#l.remove() TypeError: remove() takes exactly one argument (0 given)
#l.remove(10,8) TypeError: remove() takes exactly one argument (2 given)


#clear(), no argument
# return: None
l = [4, 5, 3, 9, 1, 10]
l.clear()
print(l)#[]
# l.clear(1) TypeError: clear() takes no arguments (1 given)

l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
del l[0]#10
print(l)#[9, 8, 7, 6, 5, 4, 3, 2, 1]

del l[5:7]#4,3
print(l)#[9, 8, 7, 6, 5, 2, 1]

del l #it delete whole list with structure
#print(l) NameError: name 'l' is not defined


#count(object or value) 
# return: count the no of times value are there
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,10]
print(l.count(10))#2
print(l.count(12))#0

#print(l.count(10,2)) TypeError: count() takes exactly one argument (2 given)
#print(l.count()) TypeError: count() takes exactly one argument (0 given)
# l.count(value=2) TypeError: count() takes no keyword arguments


# index(value, start index, end index), 
# return the lowest index
l = [1,2,3,4,5,1]
print(l.index(1))#0
print(l.index(2,0))#1
print(l.index(2,0,4))#1

#print(l.index(6)) ValueError: 6 is not in list
#print(l.index()) TypeError: index() takes at least 1 argument (0 given)
#print(l.index(1,10,20)) ValueError: 1 is not in list
#print(l.index(1,2)) ValueError: 1 is not in list
#print(l.index(5,0,4)) ValueError: 5 is not in list
print(l.index(1,0,4))#0


#reverse(), it reverse the list
# return: None
l = [1,2,3,4,5]
l.reverse()
print(l)#[5, 4, 3, 2, 1]

l1 = [1,'hi', 'dog','kapil jain', 3.4]
l1.reverse()
print(l1)#[3.4, 'kapil jain', 'dog', 'hi', 1]
#l.reverse(1) TypeError: reverse() takes no arguments (1 given)


#sort() no argument. it sort the list
# return : None
l = [1,2,3,4,5,1]
l.sort()
print(l)# [1, 1, 2, 3, 4, 5]

l1 = [1,'hi', 'dog','kapil jain', 3.4]
#l1.sort() TypeError: '<' not supported between instances of 'str' and 'int'


#copy()  Return a shallow copy of the list.
# return: copy of list
l = [1,2,[2,3]]
m = l.copy()
print(m)  # [1, 2, [2, 3]]
print(l)  # [1, 2, [2, 3]]
l[2][0]=5
print(m)  # [1, 2, [5, 3]]
print(l)  # [1, 2, [5, 3]]


# dictionary
l = list({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l)#['i', 'u', 'o', 'e', 'a'] Note: Keys in the dictionary are used as elements of the returned list

# point 1:
l = [1,2,3]
l.append({'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5})
print(l) #[1, 2, 3, {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}]

# point 2:
m = [1,2,3,{'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}]
print(m) #[1, 2, 3, {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}]


l = [1,2,3,4,5]
l[0:] = 'abc'
print(l) # ['a','b','c']

l = [1,2,3,4,5]
l[1:] = 'abc'
print(l) # [1, 'a','b','c']

l = [1,2]
l[1:] = 'abc'
print(l) # [1, 'a','b','c']


# Asignment
a = []
#a[0]=10 # IndexError: list assignment index out of range

l = []
if l:
    print("True")
else:
    print("False") # output False
    
    
l = [None]
if l:
    print("True") # Output True
else:
    print("False")
