"""
# reversed(sequence): reversed() method returns the reversed iterator of the given sequence.
# Return: a reverse iterator

# Could be an object that supports sequence protocol (__len__() and __getitem__() methods) as tuple, string, list or range
# Could be an object that has implemented __reversed__()
"""
# for string
seqString = 'Python'
print(list(reversed(seqString))) #['n', 'o', 'h', 't', 'y', 'P']

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple))) #['n', 'o', 'h', 't', 'y', 'P']

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange))) #[8, 7, 6, 5]

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList))) #[5, 3, 4, 2, 1]



class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v))) # ['u', 'o', 'i', 'e', 'a']
