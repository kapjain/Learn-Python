# In python, Monkey patch refer to dynamic modification of a class or module at runtime.
class Myclass(object):
    def f(self):
        print("f()")

def monkey(self):
    print("monkey")

o1 = Myclass()
o1.f()

Myclass.f = monkey

o2 = Myclass()

o2.f()
o1.f()