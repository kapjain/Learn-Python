
from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self,sal):# Note 1 : all child class should implement this method
        pass

#emp1 = Employee()  Note 2 :  can not create object of abstract class
#TypeError: Can't instantiate abstract class Employee with abstract methods calculate_salary

class Developer(Employee):

    def calculate_salary(self, sal):
        final_sal = sal * 1.10
        return final_sal

emp1 = Developer()

print(emp1.calculate_salary(10000)) #11000.0
