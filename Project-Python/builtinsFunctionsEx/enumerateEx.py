grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery)) # <class 'enumerate'>
print(enumerateGrocery) # <enumerate object at 0x019C6868>
print(list(enumerateGrocery)) # [(0, 'bread'), (1, 'milk'), (2, 'butter')]
print(list(enumerateGrocery)) # [] Note can not iterate twise on a iterable object


# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery)) # [(10, 'bread'), (11, 'milk'), (12, 'butter')]


for item in enumerate(grocery):
    print(item)
#(0, 'bread')
#(1, 'milk')
#(2, 'butter')


for count, item in enumerate([10,11,12]):
    print(count, item)
# 0 10
# 1 11
# 2 12
