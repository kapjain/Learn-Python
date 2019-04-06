"""
The @classmethod decorator, is a builtin function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows
your function definition.
A class method receives the class as implicit first argument, just like an instance method receives the instance


    1. A class method is a method which is bound to the class and not the object of the class.
    2. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    3. It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.

A staticmethod is a method that knows nothing about the class or instance it was called on. It just gets the arguments that were passed, no implicit first argument.
A staticmethod isn't useless - it's a way of putting a function into a class (because it logically belongs there), while indicating that it does not require access 
to the class


    1. A static method is also a method which is bound to the class and not the object of the class.
    2. A static method can't access or modify class state.
    3. It is present in a class because it makes sense for the method to be present in class.



Class method vs Static Method

    A class method takes cls as first parameter while a static method needs no specific parameters.
    A class method can access or modify class state while a static method can't access or modify it.
    We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

@classmethod
def fromtimestamp(cls,t):
    y,m,d,hh,mm,ss,weekday,jday,dst = _time.localtime(t)
    return cls(y,m,d)

@classmethod
def today(cls):
    t = _time.time()
    retun cls.fromtimestamp(t)
"""




class A(object):
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)  


""" """
print("Normal methods")
a=A()
a.foo('normal')#executing foo(<__main__.A object at 0x010D6670>,normal)

#A.foo() # TypeError: foo() missing 2 required positional arguments: 'self' and 'x'
#A.foo('normal') #TypeError: foo() missing 1 required positional argument: 'x'





"""note 2: With classmethods, the class of the object instance is implicitly passed as the first argument instead of self."""

print("\n\nClass methods")

a.class_foo(1) # executing class_foo(<class '__main__.A'>,1)

A.class_foo(2) #executing class_foo(<class '__main__.A'>,2)





"""Note 3: With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument. 
They behave like plain functions except that you can call them from an instance or the class:"""
a.static_foo(1) # executing static_foo(1)

A.static_foo('hi') # executing static_foo(hi)

#Staticmethods are used to group functions which have some logical connection with a class to the class.
#A staticmethod isn't useless - it's a way of putting a function into a class (because it logically belongs there), while indicating that it does not require access to the class




print("**************************Example 1: Python program to demonstrate use of class method and static method.*****************************")
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
     
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print (person1.age)#21
print (person2.age)#21
 
# print the result
print (Person.isAdult(22))#True





print("**************************Example 2: Python program to demonstrate use of class method and static method.*****************************")


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
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls,emp_string):
        first,last,sal = emp_string.split('-')
        return cls(first,last,sal) # Employee(first,last,sal) both are similar
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Aakash','Tiwari',80000)
emp2 = Employee('Sachin','Arya',60000)

print(emp1.fullname()) #Aakash Tiwari
print(emp2.fullname()) #Sachin Arya


Employee.set_raise_amt(1.10) # Employee.raise_amt = 1.10 both are same
print(Employee.raise_amt) # 1.1
print(emp1.raise_amt) # 1.1
print(emp2.raise_amt) # 1.1

emp1.set_raise_amt(1.12)
print(Employee.raise_amt) # 1.12
print(emp1.raise_amt) #1.12
print(emp2.raise_amt) #1.12

emp1.raise_amt = 1.5
print(Employee.raise_amt) # 1.12
print(emp1.raise_amt) #1.5
print(emp2.raise_amt) #1.12



emp_string_1 = 'kapil-jain-45000'

emp3 = Employee.from_string(emp_string_1)

print(emp3.fullname())# kapil jain
print(emp3.email) # kapil.jain@company.com


import datetime
#my_date = datetime.date(2017,12,29) True
my_date = datetime.date(2017,12,30) # False
print(Employee.is_workday(my_date))

input()


