from _functools import reduce

#reduce(function, sequences[, initial]) return a single value
a = reduce(lambda x,y: x*y, [1,2,3])
print(a)

a = reduce(lambda x,y: x*y, (1,2,3))
print(a)

a = reduce(lambda x,y: x*y, range(0,10))
print(a)

a = reduce(lambda x,y: x*y, range(1,10),10)
print(a)

#a = reduce(None, range(1,10),10) #TypeError: 'NoneType' object is not callable
print(a)