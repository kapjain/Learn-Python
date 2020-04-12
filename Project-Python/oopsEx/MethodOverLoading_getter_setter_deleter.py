"""
Method overloading: When a class contain multiple methods with same name is called method overloading.

Note: Python does not support method overloading. If you will create multiple method with same name, python will overide the method,
the lastest method will get execute.

But we can achieve method overloading using property decorator.
"""
class MethodOverloading:
    def method(self):
        print("Original Method")

    def method(self):
        print("Overloaded Method")
        
obj = MethodOverloading()
obj.method() # Overloaded Method
class Employee:
    
    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
    
    @property
    def email(self):
        return "{}.{}@school.com".format(self.fname, self.lname)
    
    
    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
    
    
    @fullname.setter
    def fullname(self,fullname):
        fname, lname = fullname.split()
        self.fname = fname
        self.lname = lname
    
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.fname = None
        self.lname = None


emp1 = Employee("Kapil", "jain", 50000)
emp2 = Employee("Sachin", "Arya", 50000)

print(emp1.fullname)
emp1.fullname = 'Aakash Tiwari'
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)

print(emp2.email)
emp2.fullname = 'Rahul jain'
print(emp2.email)
