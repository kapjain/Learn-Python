## Type 1:

# List Comprehension:
[x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
list(x**2 for x in range(10)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tuple Comprehension or Generator expression
# Note: you can convert generator object to list but you will loose the advantage in term of performance
(x**2 for x in range(10)) # <generator object <genexpr> at 0x02A4C1B0>

# Set Comprehension
{x**2 for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
set(x**2 for x in range(10)) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Dictionary Comprehension
{x : x**2 for x in range(10)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



## Type 2: when only if condition is there then it should be at the end (value will be added if condition is true, otherwise it won't be added)
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
s = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }

[ e**2 for e in [1, '4', 9, 'a', 0, 4] if type(e) == type(1) ] # [1, 81, 0, 16]
[x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]



## Type 3: when if and else both are there then it should be at begining (value will be added always, but what value should be added it depend on the condition)
# [x for x in range(10) if x%2==0 else None]
[x if x%2==0 else None for x in range(10)] # [0, None, 2, None, 4, None, 6, None, 8, None]



## Type 4:
[(i,j) for i in range(3) for j in range(3)] # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
unique_words = {word  for line in "ab \ncd \n fe"  for word in line.split()}



## Type 5:
[(i,j) for i in range(1,11) for j in range(1, 11) if i*j % 5 == 0]
# [(1, 5), (1, 10), (2, 5), (2, 10), (3, 5), (3, 10), (4, 5), (4, 10), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 5), 
#(6, 10), (7, 5), (7, 10), (8, 5), (8, 10), (9, 5), (9, 10), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)


## Type 6: Nested list comprehension

l = [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]

    
#https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/



# Importent topic
t = *(x for x in range(10)), # tuple (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print (t)
print(type(t))

tuple(x**2 for x in range(10))

[[word for word in line] for line in "ab cd fe".split()] # [['a', 'b'], ['c', 'd'], ['f', 'e']]
[word for line in "ab cd fe".split() for word in line] # ['a', 'b', 'c', 'd', 'f', 'e']
