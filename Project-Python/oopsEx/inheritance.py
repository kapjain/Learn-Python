"""
Inheritance: Inheritance enable us to define a class that takes all the functionality from parent class and allows us to add more

Method Resolution Order (MRO) : It's the order in which method should be inherited in the presence of multiple inheritance. You can view the MRO by using
                                 __mro__ attribute.

print( Dog.__mro__ ) or print(help(Dog))
(<class 'Dog'>, 
<class 'NonMarineMammal'>, 
<class 'NonWingedMammal'>, 
<class 'Mammal'>, 
<class 'Animal'>, 
<class 'object'>)

Here is how MRO is calculated in Python:  
    1. A method in the derived calls is always called before the method of the base class. In our example, Dog class is called before NonMarineMammal or 
    NoneWingedMammal. These two classes are called before Mammal which is called before Animal, and Animal class is called before object.
    2. If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), method of NonMarineMammal is invoked first because it appears first.

"""


print("************************************Example 1*************************************")
#class DerivedClassName(modname.BaseClassName):
class Parent:# define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)


class Child(Parent):# define child class
    def __init__(self):
        print ("Calling child constructor")
        
    def childMethod(self):
        print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method




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
p = Parent1() # if attribute are same in both the class, then we need to call attribute from that class object itself
p.myMethod()
#print(p.a) object of parent class can not access attribute of child class



print("************************************Example 3*************************************")
print("example of multiple inheritance")

class First(object):
    def __init__(self):
        pass
    def add(self):
        print("First")
class Second(object):
    def __init__(self):
        pass
    def add(self):
        print("second")
class Third(Second,First):
    def __init__(self):
        pass

o = Third(); # left-to-right ordering
o.add() # the class which is appear first, method will call for that class only in case of same method in multiple inheritance

print(isinstance(o,First))





print("************************************very good example of inheritance *************************************")
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