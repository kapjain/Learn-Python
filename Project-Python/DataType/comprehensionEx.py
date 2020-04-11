## Type 1:

# List Comprehension:
[x**2 for x in range(10)]
list(x**2 for x in range(10))

# Tuple Comprehension or Generator expression
# Note: you can convert generator object to list but you will loose the advantage in term of performance
(x**2 for x in range(10))

# Set Comprehension
{x**2 for x in range(10)}
set(x**2 for x in range(10))

# Dictionary Comprehension
{x : x**2 for x in range(10)}

[2**i for i in range(13)]

from math import pi, sin
{x: sin(x*pi/180) for x in range(91)}

mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }



## Type 2:
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
s = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }

[ e**2 for e in [1, '4', 9, 'a', 0, 4] if type(e) == type(1) ]
[x for x in range(100) if x % 2 == 0]
[x for x in range(2, 50) if x not in noprimes]



## Type 3:
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
unique_words = {word  for line in "ab \ncd \n fe"  for word in line.split()}



## Type 4:
[i*j for i in range(1,11) for j in range(1, 11) if i*j % 2 == 0]



## Type 5: Nested list comprehension

l = [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]
words = 'The quick brown fox jumps over the lazy dog'.split()
print([[w.upper(), w.lower(), len(w)] for w in words])

    
#https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/



# Importent topic
t = *(x for x in range(10)),
print (t)
print(type(t))

tuple(x**2 for x in range(10))

