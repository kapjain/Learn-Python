# len(iterable): returns the number of items (length) of an object.
# a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)

l = [1,2,3,4]
print(len(l)) # 
class Session:
    def __init__(self, number = 0):
        self.number = number
    def __len__(self):
        return self.number
    
# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))

#print(len(1)) TypeError: object of type 'int' has no len()
