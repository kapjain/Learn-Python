# When there are multiple classes or methods with same name, then system consider only the lasted class or method defination.

class Number(object):
    def __init__(self):
        pass

    def add(self):
        print("Number")


obj = Number();
obj.add()  # Number
print(Number.__mro__) # (<class '__main__.Number'>, <class 'object'>)


class Number(): # By defult all the class inherited by object class. The 'object' class is a parent of all the classes in Python
    def __init__(self):
        pass

    def add(self):
        print("Number 2")


obj = Number();
obj.add()  # Number 2
print(Number.__mro__) # (<class '__main__.Number'>, <class 'object'>)
