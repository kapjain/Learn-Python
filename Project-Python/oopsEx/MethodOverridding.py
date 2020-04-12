"""
Method overriddinging: When a method present in parent class is also available in child class is called as method overriding.

"""
class Parent:
    def method(self):
        print("Original Method")

class Child(Parent):
    def method(self):
        print("Overrided Method")
        
obj = Child()
obj.method() # Overrided Method
