"""
Inheritance: Inheritance enable us to define a class that takes all the functionality from parent class and allows us to add more

Method Resolution Order (MRO) : It's the order in which method should be inherited in the presence of multiple inheritance. You can view the MRO by using
                                 __mro__ attribute.

print(Fourth.__mro__) or print(help(Fourth))
(
<class '__main__.Fourth'>, 
<class '__main__.Third'>, 
<class '__main__.Second'>, 
<class '__main__.First'>, 
<class '__main__.Zeroth'>, 
<class '__main__.Number'>, 
<class 'object'>
)

Here is how MRO is calculated in Python:  
    1. A method in the derived calls is always called before the method of the base class. 
    In our example, Third class is called before First or Second. These two classes are called before Zeroth which is called before Number, and Number class is called before object.
    2. the class which is appear first, method will get called for that class only in case of same method.
    If there are multiple parents like Third(First, Second), method of First class is invoked first because it appears first.

"""

print("************************************Importent to understand MRO*************************************")
## Example of Hybrid Inheritance
class Number(object):
    def __init__(self):
        pass

    def add(self):
        print("Number")


class Zeroth(Number): # Single Inheritance   Number->Zeroth
    def __init__(self):
        pass

    def add(self):
        print("Zeroth")


class First(Zeroth): # Multilevel Inheritance   Number->Zeroth->First
    def __init__(self):
        pass

    def add(self):
        print("First")


class Second(First): # Heirarchical Inheritance   First -> Second, Third
    def __init__(self):
        pass

    def add(self):
        print("second")


class Third(First):
    def __init__(self):
        pass

    def add(self):
        print("Third")


class Fourth(Third, Second, ): # Multiple Inheritance   Third,Second->Fourth
    def __init__(self):
        pass

    def add(self):
        print("Fourth")


obj = Fourth();
obj.add()  # Fourth
print(Fourth.__mro__)
"""
(
<class '__main__.Fourth'>, 
<class '__main__.Third'>, 
<class '__main__.Second'>, 
<class '__main__.First'>, 
<class '__main__.Zeroth'>, 
<class '__main__.Number'>, 
<class 'object'>
)
"""


print("************************************Example 1*************************************")
#class DerivedClassName(modname.BaseClassName):
class Parent:# define parent class
    def parentMethod(self):
        print ('Calling parent method')

class Child(Parent):# define child class
    def childMethod(self):
        print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)


print("************************************Example 2*************************************")
input("wait for input")
class Parent1:
    def myMethod(self):
        print ('Calling parent method')

class Child1(Parent1):
    a = 0
    def myMethod(self):
        print ('Calling child method')

c = Child1()          # instance of child
c.myMethod()  #Calling child method
p = Parent1() # if there are same attribute in both parent and child class, if we want to call parent class method then we need to create object of parent class
p.myMethod()
# Note: object of parent class can not access attribute of child class
#print(p.a) 


print("************************************very good example of class with inheritance *************************************")
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

class Developer(Employee):
    
    def __init__(self,first,last,sal,prog_lang):
        super().__init__(first,last,sal)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, sal, employees = None):
        super().__init__(first,last,sal)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('--->',emp.fullname())
        
emp1 = Employee('Aakash','Tiwari',80000)
emp2 = Employee('Sachin','Arya',60000)


mng1 = Manager('Rajesh','Arya',100000,[emp1])

print(mng1.fullname())

mng1.add_employee(emp2)

mng1.print_employees()
