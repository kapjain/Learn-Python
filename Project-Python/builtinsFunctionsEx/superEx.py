"""
 The super() builtin returns a proxy object that allows you to refer parent class by 'super'.

In Python, super() built-in has two major use cases:

    Allows us to avoid using base class explicitly
    Working with Multiple Inheritance


Dog has four legs.
Dog is a warm-blooded animal.

Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.

Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.
"""
class Mammal1(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
    
class Dog1(Mammal1):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
    
#d1 = Dog1()

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
    
d = Dog()
print('')
#bat = NonMarineMammal('Bat') 