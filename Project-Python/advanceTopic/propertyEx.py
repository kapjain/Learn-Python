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




# detail explanation
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

o = Celsius()
print(o.temperature)
o.temperature = 30
print(o.temperature)


""""""
#Let us assume that you decide to make a class that could store the temperature in degree Celsius. It would also implement a method to convert the 
#temperature into degree Fahrenheit. One way of doing this is as follows.

class Celsius3:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius3()
man.temperature = 37
print(man.temperature)
print(man.to_fahrenheit())


# Now, let's further assume that our class got popular among clients and they started using it in their programs. They did all kinds of assignments to the object.
# One fateful day, a trusted client came to us and suggested that temperatures cannot go below -273 degree Celsius (students of thermodynamics might argue that it's
# actually -273.15), also called the absolute zero. He further asked us to implement this value constraint. Being a company that strive for customer satisfaction, 
#we happily heeded the suggestion and released version 1.01 (an upgrade of our existing class).

class Celsius1:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


#We can see above that new methods get_temperature() and set_temperature() were defined and furthermore, temperature was replaced with _temperature. 
#An underscore (_) at the beginning is used to denote private variables in Python.

#c = Celsius1(-277)
#ValueError: Temperature below -273 is not possible

c = Celsius1(37)
c.get_temperature() # 37
c.set_temperature(10)

# c.set_temperature(-300) Traceback (most recent call last): ValueError: Temperature below -273 is not possible

#This update successfully implemented the new restriction. We are no longer allowed to set temperature below -273.
#The big problem with the above update is that, all the clients who implemented our previous class in their program have to modify their code from obj.temperature 
#to obj.get_temperature() and all assignments like obj.temperature = val to obj.set_temperature(val).
#This refactoring can cause headaches to the clients with hundreds of thousands of lines of codes.


"""All in all, our new update was not backward compatible. This is where property comes to rescue."""

class Celsius2:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
    temperature = property(get_temperature, set_temperature)

c = Celsius2()
c.temperature
#Getting value
#0


c.temperature = 37
#Setting value

c.to_fahrenheit()
#Getting value
#98.60000000000001


#By using property, we can see that, we modified our class and implemented the value constraint without any change required to the client code. Thus our implementation 
#was backward compatible and everybody is happy. Finally note that, the actual temperature value is stored in the private variable _temperature. The attribute temperature 
#is a property object which provides interface to this private variable.

o = """
Digging Deeper into Property

In Python, property() is a built-in function that creates and returns a property object. The signature of this function is

property(fget=None, fset=None, fdel=None, doc=None)

where, fget is function to get value of the attribute, fset is function to set value of the attribute, fdel is function to delete the attribute and doc is a string (like a comment). As seen from the implementation, these function arguments are optional. So, a property object can simply be created as follows.

>>> property()
<property object at 0x0000000003239B38>

A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel at a later point. This means, the line

temperature = property(get_temperature,set_temperature)

could have been broken down as

# make empty property
temperature = property()
# assign fget
temperature = temperature.getter(get_temperature)
# assign fset
temperature = temperature.setter(set_temperature)

These two pieces of codes are equivalent.


We can further go on and not define names get_temperature and set_temperature as they are unnecessary and pollute the class namespace. For this, we reuse
 the name temperature while defining our getter and setter functions. This is how it can be done.
"""

