"""
Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. 
but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the
iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. 
are iterables.

The iter() functionEx (which in turn calls the __iter__() method) returns an iterator from them.

"""
s = 'abc'
it = iter(s)
print(it) #<iterator object at 0x00A1DB50>
next(it) #'a'
next(it) #'b'
it.__next__() #'c'
#next(it) # Traceback (most recent call last):  File "<stdin>", line 1, in <module>     next(it) StopIteration

#A more elegant way of automatically iterating is by using the for loop. Using this, we can iterate over any object that can return 
# an iterator, for example list, string, file etc.
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("file1.txt"):
    print(line, end='')


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

# either normal or for
for char in rev:
    print(char)

#  or for
i = iter(rev)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) StopIteration



class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
print(next(print_num_iter))
