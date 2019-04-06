"""
The super() builtin returns a proxy object that allows you to refer parent class by 'super'.

In Python, super() built-in has two major use cases:
1. Allows us to avoid using base class explicitly
2. Working with Multiple Inheritance
"""



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
