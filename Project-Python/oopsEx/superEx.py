# Please refer once you complete this. https://github.com/kapjain/Learn-Python/blob/master/Project-Python/oopsEx/inheritance.py
"""
The super() builtin returns a proxy object that allows you to refer parent class by 'super'.
Python 2: super(SubClass, self).__init__()
Python 3: super().__init__()

In Python, super() built-in has two major use cases:
1. Allows us to avoid using base class explicitly
2. Working with Multiple Inheritance
"""

# Example 1
## Initialized Parent class when creating object of child class
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)


# Example 2
## Python super() will always refer the immediate superclass.
# Python super() function not only can refer the __init()__ function but also can call all other function of the superclass.
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)

c = C()
c.sub_method(1)
"""
Initializing: class C
Initializing: class B
Initializing: class A
Printing from class C: 1
Printing from class B: 2
Printing from class A: 3
"""


# Example 3
## Super() method also follow MRO (Herachical Inheritance)
# Condition: all parent class method shuold have super.method_name, else it will call only one method

class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B:
    def __init__(self):
        print('Initializing: class B')

    def sub_method(self, b):
        print('Printing from class B:', b)


class C(A,B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


c = C()
c.sub_method(1)
print(C.__mro__)
"""
Initializing: class C
Initializing: class A
Printing from class C: 1
Printing from class A: 2
(
<class '__main__.C'>, 
<class '__main__.A'>, 
<class '__main__.B'>, 
<class 'object'>
)
"""

# Example 4
##  When there is no grand parent, it call whichever class appear first then next and so on..
# all parent class method shuold have super.method_name, else it will call only one method
class Second():
    def __init__(self):
        print("second")
        super().__init__()


class Third():
    def __init__(self):
        print("Third")
        super().__init__()


class Fourth(Third, Second, ):
    def __init__(self):
        print("Fourth")
        super().__init__()


obj = Fourth();
print(Fourth.__mro__)
"""
Fourth
Third
second
(
<class '__main__.Fourth'>, 
<class '__main__.Third'>, 
<class '__main__.Second'>, 
<class 'object'>
)
"""

# Example 5
## When there are grand parent, then it call whichever class appear first and complate its familiy then go to next class and so on..
class Zeroth():
    def __init__(self):
        print("Zeroth")
        super().__init__()


class First():
    def __init__(self):
        print("First")
        super().__init__()


class Second(Zeroth):
    def __init__(self):
        print("second")
        super().__init__()


class Third(First):
    def __init__(self):
        print("Third")
        super().__init__()


class Fourth(Third, Second, ):
    def __init__(self):
        print("Fourth")
        super().__init__()


obj = Fourth();
print(Fourth.__mro__)
"""
(
<class '__main__.Fourth'>, 
<class '__main__.Third'>, 
<class '__main__.First'>, 
<class '__main__.Second'>, 
<class '__main__.Zeroth'>, 
<class 'object'>
)
Fourth
Third
First
second
Zeroth
"""

# Example 6
## When there is same grand parent for all parent class, then it cover all sibling first then go to grand parent class.
class First():
    def __init__(self):
        print("First")
        super().__init__()


class Second(First):
    def __init__(self):
        print("second")
        super().__init__()


class Third(First):
    def __init__(self):
        print("Third")
        super().__init__()


class Fourth(Third, Second, ):
    def __init__(self):
        print("Fourth")
        super().__init__()


obj = Fourth();
print(Fourth.__mro__)
"""
Fourth
Third
second
First
(<class '__main__.Fourth'>, 
<class '__main__.Third'>, 
<class '__main__.Second'>, 
<class '__main__.First'>, 
<class 'object'>)
"""

# Example 7

class A:
    def sub_method(self, b):
        print('Printing from class A:', b)
        super().sub_method(b + 1)


class B:
    def sub_method(self, b):
        super().sub_method(b + 1) # AttributeError: 'super' object has no attribute 'sub_method'
        print('Printing from class B:', b)


class C(A,B):
    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)
        
c = C()
c.sub_method(1)

print("************************************Example 1*************************************")
class Mammal1(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
    
class Dog1(Mammal1):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
"""
Dog has four legs.
Dog is a warm-blooded animal.
"""
d1 = Dog1()




print("************************************Example 2*************************************")
class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.');

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')
    
d = Dog() # it will complete all parent class first then grand parents

print(help(Dog))
"""
Method resolution order:
Dog
NonMarineMammal
NonWingedMammal
Mammal
Animal
builtins.object
"""

"""
Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.
"""

bat = NonMarineMammal('Bat') 
""""
Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.
"""


class HttpResponseBase:
    """ 
    1. if we have same class variable in all the class (childs and parents), then system will take value from greatest child class.
    2. In parent class method, you can not call super().method().
    """
    status_code = 200
    def __init__(self, content_type=None, status=None, reason=None, charset=None):
        print("Z")
        print(self.status_code)
        super().__init__()  # Can not add * args or **kwargs or any variable, because object class doesn't accept any variable.
        
    def set_streaming_data(self):
        print("ab Z")
        #super().set_streaming_data() 

class HttpResponse(Z):
    def __init__(self, content=b'', *args, **kwargs):
        print("A")
        super().__init__(*args, **kwargs)
        print(self.status_code)

    def set_streaming_data(self):
        print("ab A")
        super().set_streaming_data()
        
class JsonResponse(HttpResponse):
    status_code = 300
    def __init__(self, data, *args, type=None, **kwargs):
        print("B")
        super().__init__(*args, **kwargs)

    def set_streaming_data(self):
        print("ab B")
        return super().set_streaming_data()
        
o = JsonResponse(data='b',content_type = 'z')
o.ab()
