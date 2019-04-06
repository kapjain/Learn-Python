"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', '__weakref__', 'i', 'r']
"""

class Employee:
    
    raise_amt = 1.05
    num_of_emps = 0
    
    def __init__(self,first,last,sal):
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
        
    def fullname(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.sal *= self.raise_amt
        
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    
    def __repr__(self):
        return "Employee({},{},{})".format(self.first, self.last, self.sal)
    
    
    def __add__(self,other): # operator overloading
        return (self.sal + other.sal)
    
    

emp1 = Employee('Aakash','Tiwari',80000)
emp2 = Employee('Sachin','Arya',60000)

#print(emp1) <__main__.Employee object at 0x031A6AF0> when __str__ or __repr__ were not defined




print(emp1) # Aakash Tiwari - Aakash.Tiwari@company.com

print(repr(emp1)) # Employee(Aakash,Tiwari,80000) when __repr__ define but __str__ not defined
print(str(emp1)) # Aakash Tiwari - Aakash.Tiwari@company.com when both are defined

print(emp1.__repr__()) # Employee(Aakash,Tiwari,80000) 
print(emp1.__str__()) # Aakash Tiwari - Aakash.Tiwari@company.com


print(emp1 + emp2) # 140000







input()
# __init__() is not mandatory but if you define in class then all the parameter are required parameter in constructor __init__ except self 
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "str class"

#s = Shark() # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
s = Shark('Luis','wong')

print(s) # str class if you remove __str__ it will print object