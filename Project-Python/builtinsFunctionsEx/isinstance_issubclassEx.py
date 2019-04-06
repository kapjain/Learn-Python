"""
isinstance(object, classinfo): The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

    object - object to be checked
    classinfo - class, type, or tuple of classes and types

    True if the object is an instance or subclass of a class, or any element of the tuple
    False otherwise

issubclass(object, classinfo): The isinstance() function checks if the object argument (first argument) is a subclass of classinfo class (second argument).

"""
class Foo:
    a = 5
  
fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)







class Polygon:
    def __init__(self,polygonType):
        print('Polygon is a ', polygonType)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))