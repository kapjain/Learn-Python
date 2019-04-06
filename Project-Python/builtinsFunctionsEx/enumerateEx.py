'''
Using enumerate(sequence object) function you can iterate through the sequence and retrieve the index position and its corresponding value at the same time.
'''

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))




grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)
  
  

for i,v in enumerate(['h','j','k']):
    print(i,v)

l = [7,8,9]
for i,v in enumerate(l):
    print(i,v)