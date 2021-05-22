class JustCounter:
    __secretCount = 0 # Private Variable
    _temp = 0 # not a private Variable can call directly outside the class
    
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

#print (counter.__secretCount) AttributeError: 'JustCounter' object has no attribute '__secretCount'

print (counter._temp) #0

print (counter._JustCounter__secretCount)# 2 object._className__attrName. 



counter.__secretCount = 100 # this will create a instance variable __secretCount for counter object
print (counter.__secretCount)# then will be able to call directly



class Base:
    def __init__(self):
        self.__a = 3
    
    def print_a(self):
        print(self.__a) # 'Child' object has no attribute '_Base__a'

class Child(Base):
    def __init__(self):
        self.__a = 1
    

o = Child()
o.print_a()
