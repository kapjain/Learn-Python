print("******************example 1*************")
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
my_num1 = [x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
my_num2 = (x**2 for x in my_list) 



print(list(my_num2)) # you can convert generator object to list but you will lose the advantage in tern of performance
print(list(my_num2))
for num in my_num2:
    print(num)
print("******************example 2*************")
sum(i*i for i in range(10))                 # sum of squares 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product 260


print("******************example 3*************")
from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

print("******************example 4*************")


# unique_words = set(word  for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)


print("******************example 5*************")
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']









#List comprehension


a_list = [1, '4', 9, 'a', 0, 4]
squared_ints = [ e**2 for e in a_list if type(e) == type(1) ]
print (squared_ints)
print(type(squared_ints))


# Nested list comprehension
l = [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]
print(type(l))


#Set comprehension
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
s = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
print(type(s))


#Dictionary comprehension
mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}

mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
print (mcase_frequency)
print(type(mcase_frequency))

# Tuple comprehension
t = *(x for x in range(10)),
print (t)
print(type(t))
