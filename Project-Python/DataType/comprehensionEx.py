S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print (S)
print (V)
print (M)

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print (primes)


words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)


stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in stuff:
    print(i)
    
#https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/
