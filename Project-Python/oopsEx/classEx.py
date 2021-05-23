"""
Class/Static Variables:  Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class.
They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable.


Instance/Non-static Variables:  Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.
Unlike class variables, instance variables are defined within methods. 

All variables which are assigned a value in the class declaration are class variables. And variables that are assigned values inside methods are instance variables.
At the class level, variables are referred to as class variables, whereas variables at the instance level are called instance variables.

Note:  This differentiation allows us to use class variables to initialize objects with a specific value assigned to variables, and use different variables for each object 
with instance variables.
Making use of class- and instance-specific variables can ensure that our code adheres to the DRY principle to reduce repetition within code.
"""

print("Example 0: Basic understanding of class")
class Student:
    pass

#obj_name = Class_name(argument)
std_1 = Student()
std_2 = Student()

std_1.fname = 'Neel' # self.fname =  fname both are same
std_1.lname = 'Verma'
std_1.age = 25
std_1.email = 'neel.verma@school.com'

std_2.fname = 'Luis'
std_2.lname = 'wong'
std_2.age = 25
std_2.email = 'Luis.wong@school.com'

print(std_1.email) #neel.verma@school.com
print(std_2.email) #Luis.wong@school.com


# self is the instance of the current object
class Student1:
    def __init__(self,fname,lname,age):
        self.fname =  fname
        self.lname = lname
        self.age = age
        self.email = fname + '.' + lname + '@school.com'
        
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

std_1 = Student1("Neel","Verma",25)
std_2 = Student1("Luis","wong",23)
std_1.fname
std_1.lname
print(std_1.fullname())  #Neel Verma
print(std_2.fullname())  #Luis wong




print(" Example 1: Basic calling of class variable, instance variable and methods of class")
class Car:
    cc = 100 # Class Variable
    def __init__(self,modelname,yearm,price):
        self.modelname = modelname #instance variables
        self.yearm = yearm
        self.price = price
    
    def price_inc(self):
        return self.price*1.15
    def temp_f(self):
        return 10
honda = Car('City',2017,1000000)
tata = Car('Bolt',2016,800000)


# Note 1: class variable can call by class name or object(instance) of the class
print(honda.cc)  # 100
print(tata.cc) # 100
print(Car.cc) # 100 if you change the value of Car.cc it show in all instances but if you change tata.cc it will not effect other

tata.cc=150

print(honda.cc) # 100
print(tata.cc) # 150
print(Car.cc) # 100

honda.cc = 110

print(honda.cc) # 110
print(tata.cc) # 150
print(Car.cc) # 100

Car.cc = 160

bmw = Car('S3',2016,8020000)
print(honda.cc) # 110
print(tata.cc) # 150
print(Car.cc) # 160
print(bmw.cc) # 160

# Note 2: instance variable can not call by class name. they only called by instance of the class
print(honda.modelname) # City
#print(Car.modelname) AttributeError: type object 'Car' has no attribute 'modelname'


# Note 3: methods of the class can not be called by class name, they only called by class instances(object)
print(honda.price_inc()) #1150000.0

#print(Car.price_inc()) #TypeError: price_inc() missing 1 required positional argument: 'self'

print(Car.price_inc(honda)) #1150000.0


# Note 4:  we can refer the method of the class by  class name but can not call
print(honda.price_inc) # <bound method Car.price_inc of <__main__.Car object at 0x02E1F030>>
print(Car.price_inc) # <function Car.price_inc at 0x02E1C9C0>




print("Example 2: calling class variable inside the method of class can only done by class.class_variable")
class Cv:
    counter = 0
    def __init__(self):
        self.counter = self.counter + 5
        print(self.counter) # 5 instance variable
        print(Cv.counter) # 0 class variable

o1= Cv()
# note: if there is already a instance vairable with same name as class variable name, then we can not access class variable using self.
# We can access it using class name.


print("Example 3: __init__() is not mandatory but if you define in class then all the parameter are required parameter in constructor 
      __init__ except self ")
      
class Shark1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#s = Shark() # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'



print("Example 4: assigning a method of class to a local variable(method object) ")
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
xf = x.f # xf is an method object 
print(xf) #<bound method MyClass.f of <__main__.MyClass object at 0x018E68F0>>
print(xf()) # 'hello world'



print("Example 5: defining method of class outside the class body")
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
#     def f(self, x, y):
#         return min(x, x+y)
    def g(self):
        return 'hello world'

    h = g
#     def h(self):
#         return 'hello world'
o = C()
print(o.h()) # hello world
print(o.g()) # hello world
print(o.f(1,2)) # 1

print(f1(o,1,2)) #1
#print(f1(1,2)) TypeError: f1() missing 1 required positional argument: 'y'

print(f1(1,2,3)) #2 works as normal function




print("Example 6: setting value and getting value and automatic constructor call")
class Kapil:
    def setData(self,name, age):
        self.name=name
        self.age=age
    def getData(self):
        print ("name :",self.name)
        print ("age :",self.age)
    def __init__(self):
        print ("hello kapil")
k = Kapil() #hello kapil
k.setData('kapil',22)
k.getData()
# name : kapil
# age : 22






print("Example 7: basic class contents")
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    '''Common base class for all 
    employees , WILL CONSIDER AS MULTILINE COMMENT'''
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Mani", 5000)
print ("Employee.__doc__:", Employee.__doc__)#Class documentation string or none, if undefined.
# Employee.__doc__: Common base class for all employees

print ("Employee.__name__:", Employee.__name__)# Class Name
#Employee.__name__: Employee

print ("Employee.__module__:", Employee.__module__)#Module name in which the class is defined. This attribute is "__main__" in interactive mode. 
#Employee.__module__: __main__

print ("Employee.__bases__:", Employee.__bases__)#A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
#Employee.__bases__: (<class 'object'>,)

print ("Employee.__dict__:", Employee.__dict__ ) # all class variables, all methods of class
#Employee.__dict__: {'__module__': '__main__', '__doc__': 'Common base class for all employees', 'empCount': 2, '__init__': <function Employee.__init__ at 0x03AACA08>,
# 'displayCount': <function Employee.displayCount at 0x03AAC9C0>, 'displayEmployee': <function Employee.displayEmployee at 0x03AAC978>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}

