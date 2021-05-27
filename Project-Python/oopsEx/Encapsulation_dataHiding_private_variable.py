"""
Encapsulation : It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods 
    directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. 
    Those types of variables are known as private variable. 

    A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc. 
The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, the sales section handles all
the sales-related activities and keeps records of all the sales. Now there may arise a situation when for some reason an official from the finance section 
needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section. He will first have 
to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales
section and the employees that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. In this example, 
the data of the sections like sales, finance, or accounts are hidden from any other section.

"""

# Example 1:
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


# Example 2:
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


Private variables:
# Example 3: Private variable can not be modify directly from outside the class
class Base:
    def __init__(self):
        self.__c = "GeeksforGeeks"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c) # Will raise error private member can not be accesible outside class

obj1 = Derived()

# Example 4: Private variable can be modify indirectly
class Base:
    def __init__(self):
        self.__name = "Vishant"

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling private member of base class: ")
        # print(self.__name) # Will raise error private member can not be accesible outside class

obj1 = Derived()

print(obj1.get_name()) # Vishant
print(obj1.set_name('Kapil')) # None
print(obj1.get_name()) # Kapil
