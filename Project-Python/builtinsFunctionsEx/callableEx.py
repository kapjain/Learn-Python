"""
The callable(object) method returns True if the object passed appears callable. If not, it returns False.
It important to remember that, even if the callable() is True, call to the object may still fail.

However, if the callable() returns False, call to the object will certainly fail.
"""
b =3
print(callable(b))

b ='abc'
print(callable(b))

b =[1,2,3]
print(callable(b))


b =(1,2,3)
print(callable(b))

b = lambda x: x*x
print(callable(b))

def add(a,b):
    return a + b

print(callable(add))

#The instance of Foo class appears to be callable (and is callable in this case).
class Foo:
    def __call__(self):
        print('Print Something')
    def __call1__(self):#only first fuction will get call
        print('Print Something1')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()

#The instance of Foo class appears to be callable but it's not callable
class Foo1:
    def printLine(self):
        print('Print Something')

print(callable(Foo1))

InstanceOfFoo1 = Foo1()
# Raises an Error
# 'Foo1' object is not callable
#InstanceOfFoo1()


