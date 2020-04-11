# filter(function or None, iterable) : return those item of sequence for which function is true. if function is None, return the items that are true
# return: a filter object

def filterVowels(alphabet):
    return True if alphabet in ['a', 'e', 'i', 'o', 'u'] else False

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o','j']
filteredVowels = filter(filterVowels, alphabets)
print(filteredVowels) # <filter object at 0x02DC7160>
print(type(filteredVowels)) # <class 'filter'>


a = list(filter(lambda d: d!='a','abcd'))
print(a) # ['b', 'c', 'd']


def d(x):
    return True if x !='a' else False
a = list(filter(d,'abcd'))
print(a) # ['b', 'c', 'd']


b = filter(None,'abcd ')
print(list(b)) # ['a', 'b', 'c', 'd', ' ']


b = filter(None,{None,1,2,3})
print(list(b)) # [1, 2, 3]


b = filter(None,{'a':10,'b':20})
print(list(b))
