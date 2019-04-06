#map(function, sequence1[,sequence2]..) return a list
a = list(map(lambda x: x*x, [1,2,3]))
print(a)

a = list(map(lambda x: x*x, (1,2,3)))
print(a)

a = list(map(lambda x: x*x, range(1,11)))
print(a)

a = list(map(lambda x: x*2, "hello"))
print(a)

n = list(map(lambda a,b: a+b if b else a+10, [1,2,3,4,5], [1,2,3]))
print(n) #[2, 4, 6]

try:
    a = list(map(None, [1,2,3])) #TypeError: 'NoneType' object is not callable
    print(a)
except Exception as e:
    print(e)