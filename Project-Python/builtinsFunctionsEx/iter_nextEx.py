Please refer "https://github.com/ncjain/Learn-Python/blob/master/Project-Python/advanceTopic/iterater.py" for iter method

"""
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator
The iter() functionEx (which in turn calls the __iter__() method) returns an iterator object from them.
"""
s = 'abc'
it = iter(s)
print(it) #<iterator object at 0x00A1DB50>
next(it) #'a'
next(it) #'b'
it.__next__() #'c'
#next(it) # Traceback (most recent call last):  File "<stdin>", line 1, in <module>     next(it) StopIteration



# iter() with sentinel parameter
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        processLine(line)
#When you run the program, it will open the mydata.txt file in reading mode.
#Then, the iter(fp.readline, '') in the for loop calls readline (which reads each line in the text file) until the sentinel character,
#'' (empty string), is reached.


## next(iterator, default):
#iterator - next() retrieves next item from the iterator
#default (optional) - this value is returned if the iterator is exhausted (there is no next item)

# Return Value from next()
#The next() function returns the next item from the iterator.
#If the iterator is exhausted, it returns the default value passed as an argument.
#If the default parameter is omitted and the iterator is exhausted, it raises StopIteration exception.

random = [5, 9, 'cat']
random_iterator = iter(random)
print(random_iterator)
# Output: 5
print(next(random_iterator))

# Output: 9
print(next(random_iterator))

# Output: 'cat'
print(next(random_iterator))

# Output: None
print(next(random_iterator, None))

# This will raise Error since iterator is exhausted
print(next(random_iterator))
