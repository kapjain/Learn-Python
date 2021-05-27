"""
Abstraction:  Data abstraction is the process of hiding certain details and showing only essential information to the user. 
              Abstraction can be achieved with either abstract classes or interfaces

Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on how to use the application.

    In Python, abstraction can be achieved using abstract classes and methods.
    No, the abstract class cannot be instantiated, i.e., we cannot create objects for the abstract class.
    An abstract class may or may not have all abstract methods. Some of them can be concrete methods

a. abstract class:
    An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes
    built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a 
    declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common 
    interface for different implementations of a component, we use an abstract class. 

    from abc import ABC, abstractmethod

    class Polygon(ABC):

        @abstractmethod
        def noofsides(self):
            pass
		
Why use Abstract Base Classes : 
    By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful 
    in situations where a third-party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large 
    code-base where keeping all classes in your mind is difficult or not possible. 

b. interface: It is used to provide total abstraction

Encapsulation vs Data Abstraction
	1. Encapsulation is data hiding(information hiding) while Abstraction is detail hiding(implementation hiding).
	2. While encapsulation groups together data and methods that act upon the data, data abstraction deals with exposing the interface to the user and hiding the details of implementation.
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self,sal):# Note 1 : all child class should implement this method
        pass
    
    def test(self):
        print("normal method")

#emp1 = Employee()  Note 2 :  can not create object of abstract class if it contain any abstract method. If there is no abstract method then we can create object.
#TypeError: Can't instantiate abstract class Employee with abstract methods calculate_salary

class Developer(Employee):

    def calculate_salary(self, sal):
        final_sal = sal * 1.10
        return final_sal

emp1 = Developer()

print(emp1.calculate_salary(10000)) #11000.0
