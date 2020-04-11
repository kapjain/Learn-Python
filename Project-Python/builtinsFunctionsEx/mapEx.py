# map(func, *iterables): Make an iterator that computes the function using arguments from each of the iterables.  Stops when the shortest
# iterable is exhausted.
# return : a map object

a = map(lambda x: x*x, [1,2,3])
print(list(a)) # [1,4,9]

n = map(lambda a,b: a+b if b else a+10, [1,2,3,4,5], [1,2,3])
print(list(n)) #[2, 4, 6] Executed till second list, since that got exasted first

# a = map(None, [1,2,3])) TypeError: 'NoneType' object is not callable
