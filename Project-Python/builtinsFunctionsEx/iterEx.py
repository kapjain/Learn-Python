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
