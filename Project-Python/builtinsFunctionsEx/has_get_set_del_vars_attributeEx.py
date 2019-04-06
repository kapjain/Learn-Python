"""
The getattr(object, name[, default]) method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

The hasattr(object, name) method returns true if an object has the given named attribute and false if it does not.

The setattr(object, name, value) method sets the value of given attribute of an object.

The delattr(object, name) deletes an attribute from the object (if the object allows it).

The vars(object) function returns the __dict__ attribute of the given object if the object has __dict__ attribute.
"""

class kapil:
    
    __name = 'kapil'
    age = 25
k = kapil()
print(globals())

input('wait here')
print(vars(k))
print(getattr(k,'name'))
print(getattr(k,'sex','male'))
#print(getattr(k,'caste')) #AttributeError: 'kapil' object has no attribute 'caste'

print(hasattr(k,'name'))
print(hasattr(k,'caste'))

setattr(k, 'name', 'jain')
print(k.name)

setattr(k, 'sex', 'male')# we have setted attribute sex for k object only
print(k.sex)



class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z') #the attribute z is removed from the Coordinate class using delattr(Coordinate, 'z'). not for only one object it is deleted for all other object too

print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)

# Raises Error
#print('z = ',point1.z)

point2 = Coordinate() 

print('z = ',point2.z)


#The vars() function returns the __dict__ attribute of the given object if the object has __dict__ attribute.
#It return the value when we set either through object or init method,otherwise it will give blank dictionary
class Foo:
    def __init__(self, a = 5, b = 10):
        self.a = a
        self.b = b
  
InstanceOfFoo = Foo()
print(vars(InstanceOfFoo))