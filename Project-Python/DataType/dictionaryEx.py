"""
[
1. Mutable
2. Does not support slicing
3. value can contain mutable object but key must be immutable
4. Value can be duplicate but Key must be unique otherwise it take only the last value of the key
5. it can contain different types of data


'__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
  '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
  
    'fromkeys', 'get',  'keys',  'values', 'items', 'pop', 'popitem', 'clear', 'copy',  'setdefault', 'update']
"""

d1 = {}#empty dictionary
d2 = dict()#empty dictionary
d3 = {'a' : 1,}#single element dictionary
d4 = {'a' : 1, 'b' : 2, 'c' : 3}
d5 = {'a' : 1, 1 : 2, 2.5 : 2}
d6 = {'a' : {1,2,3}, 'b' : 2, 'c' : 3} #value can contain mutable object but key must be immutable
#d7 = {[1,2,3] : 1, 'b' : 2, 'c' : 3} TypeError: unhashable type: 'list'
#d7 = {{1,2,3} : 1, 'b' : 2, 'c' : 3} TypeError: unhashable type: 'set'
d7 = {frozenset({1,2,3}) : 1, 'b' : 2, 'c' : 3}

d4 = {'a' : 1, 'a' : 2, 'c' : 3}
print(d4) #{'a': 2, 'c': 3} Key must be unique otherwise it take only the last value of the key


# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

# Note: **kwarg let you take arbitrary number of keyword arguments.
#A keyword argument is an argument preceded by an identifier (eg. name=). Hence, the keyword argument of the form kwarg=value is passed to the dict()
# constructor to create dictionaries.


numbers = dict(x=5, y=0)
print('numbers = ',numbers)
print(type(numbers))

empty = dict()
print('empty = ',empty)
print(type(empty))  # <class 'dict'>
# keyword argument is not passed

numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)  # {'x': 5, 'y': -5}

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)  # {'x': 5, 'y': -5, 'z': 8}

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)  # {'x': 1, 'y': 2, 'z': 3}

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)
#dict([('a',1,3),(2,'b',2)]) ValueError: dictionary update sequence element 
#0 has length 3; 2 is required. Every index should have 2 values pair

#accessing value and updating value
d = {'name': 'john','code':6734, 'dept': 'sales'}
print(d['name']) #'john'
d['name'] = 'Kapil'
print(d['name']) # 'Kapil'


# Basic operation
d1 = {'name': 'john','code':6734, 'dept': 'sales'}
d2 = {'a':1, 'b':2, 'c':3}

#print(d1*4) TypeError: unsupported operand type(s) for *: 'dict' and 'int'
#d = d1 + d2 TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# 'code' always perform these functionEx on keys
print(1 in d2) # False
print('a' in d2) # True
print(len(d1)) # 3
print(min(d2)) # 'a'  
print(max(d1)) #'name'




# fromkeys(iterable, value=None): The method fromkeys() creates a new dictionary with keys from seq and value set to value.
# return: it return a dictionary with given defult value like {1: 'Null', 2: 'Null', 3: 'Null'} 
d1 = {'name': 'john','code':6734, 'dept': 'sales'}
seq = ('name', 'age', 'sex')

print(dict.fromkeys(seq)) # {'name': None, 'age': None, 'sex': None}
print(dict.fromkeys(seq,10))  # {'name': 10, 'age': 10, 'sex': 10}
print(dict.fromkeys(seq,(1,2,3)))  # {'name': (1, 2, 3), 'age': (1, 2, 3), 'sex': (1, 2, 3)}
print(dict.fromkeys(range(1,3)))  # {1: None, 2: None}
print(dict.fromkeys(d1))  # {'name': None, 'code': None, 'dept': None}

# print(dict.fromkeys(1)) TypeError: 'int' object is not iterable
# print(dict.fromkeys([1,2,3],1,2)) TypeError: fromkeys expected at most 2 arguments, got 3



# get(key, default=None): 
# return: The method get() returns a value for the given key. If key is not available then returns default value.
d = {'Name': 'Zara', 'Age': 27}
print(d.get('Name')) #'Zara'
print(d.get('Sex')) # None
print(d.get('Sex','Not available')) #'Not available'
# d.get()  TypeError: get expected at least 1 arguments, got 0
# d.get('sex','M','F') TypeError: get expected at most 2 arguments, got 3


# dict.setdefault(key, default = None) The method setdefault() is similar to get(), but will set dict[key] = default if key is not already in dict.

d = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  d.setdefault('Age', None)) # Value : 7
print ("Value : %s" %  d.setdefault('Sex', None)) # Value : None
print ("Value : %s" %  d.setdefault('Mobile', '783684')) # value: 783684
print (d) # {'Name': 'Zara', 'Sex': None, 'Age': 7,'Mobile':'783684'}





#keys() and values() and  items()
#keys() : The method keys() returns a list of all the available keys in the dictionary.
#values(): The method values() returns a list of all the values available in a given dictionary.
#items(): The method items() returns a list of dict's (key, value) tuple pairs

d = {'Name': 'Zara', 'Age': 27}
print(type(d.keys())) # <class 'dict_keys'>
print(d.keys()) # dict_keys(['Name', 'Age'])

print(d.values()) # dict_values(['Zara', 27])
print(d.items()) # dict_items([('Name', 'Zara'), ('Age', 27)])
# d.keys(f) f is not defined


#pop (key, optional value) : key must be there

d = {'Name': 'Zara', 'Age': 27}
# d.pop() TypeError: pop expected at least 1 arguments, got 0
# d.pop('N') KeyError: 'N'
print(d.pop('N','not available')) # 'not available'

print(d.pop('Name')) #'Zara'
print(d) # {'Age': 27}


# popitem(), remove item from dictionary from the last
d = {'Name': 'Zara', 'Age': 27}
d.popitem() #('Age', 27)
print(d) # {'Name': 'Zara'}

d.popitem() #('Name', 'Zara')
print(d) #{}

# d.popitem() KeyError: 'popitem(): dictionary is empty'



# clear() it deletre all the items from the dictionary
d = {'Name': 'Zara', 'Age': 27}
d.clear()
print(d) # {}

d = {'Name': 'Zara', 'Age': 27}
del d # but del delete the dictionary with all items




# copy() The method copy() returns a shallow copy of the dictionary.

d = {'Name': 'Zara', 'Age': 27}

d1 = d.copy()
print(d1) # {'Name': 'Zara', 'Age': 27}
d1['sex'] = 'male'
print(d) # {'Name': 'Zara', 'Age': 27}
print(d1) # {'Name': 'Zara', 'Age': 27, 'sex': 'male'}




# dict.update(dict2) The method update() adds dictionary dict2's key-values pairs in to dict. This functionEx does not return anything.

d = {'Name': 'Zara', 'Age': 7}
d2 = {'Sex': 'female','dob':1993 }

d.update(d2)
print ("updated dict : ", d)# updated dict : {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}



