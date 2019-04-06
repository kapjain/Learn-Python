print("Example 7: basic class contents")
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    '''Common base class for all 
    employees '''
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Mani", 5000)
print ("Employee.__doc__:", Employee.__doc__)#Class documentation string or none, if undefined.
# Employee.__doc__: Common base class for all employees

print ("Employee.__name__:", Employee.__name__)# Class Name
#Employee.__name__: Employee

print ("Employee.__module__:", Employee.__module__)#Module name in which the class is defined. This attribute is "__main__" in interactive mode. 
#Employee.__module__: __main__

print ("Employee.__bases__:", Employee.__bases__)#A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
#Employee.__bases__: (<class 'object'>,)

print ("Employee.__dict__:", emp1.__dict__ ) # all class variables, all methods of class
#Employee.__dict__: {'__module__': '__main__', '__doc__': 'Common base class for all employees', 'empCount': 2, '__init__': <function Employee.__init__ at 0x03AACA08>,
# 'displayCount': <function Employee.displayCount at 0x03AAC9C0>, 'displayEmployee': <function Employee.displayEmployee at 0x03AAC978>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}

# n=18
# lst=[]
# while(n>0):
#     rem=n%2
#     n=n//2
#     lst.append(rem)
# 
# r=reversed(lst)
# 
# 
# print(list(r))
#  n=18
#r=''
#while(n>0):
#    rem=n%2
#    n=n//2
#    r=str(rem)+r


#  print(str(r))

# class cal:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         
#     def add (self):
#         return (self.a+self.b) 
# obj=cal(10,5)
# p=obj.add()
# print(p)
# obj.add()

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# 
# c=a+b
# print("addition of {} and {} is :{}".format(a,b,c))
# 
# d=a-b
# print("subtraction of {} and {} is :{}".format(a,b,d))
# 
# n=58743546
# if(n>1):
#     for i in range(2,n):
#         if(n%i==0):
#             print(n,"is not a prime")
#             break
#     else:
#         print(n,"is a prime numer")
# else:
#      print(n,"is not a prime number")  

# n=int(input("enter any number"))
# sum1=0
# for i in range(1,n):
#     if(n%i==0):
#         sum1=sum1+i
# if(sum1==n):
#     print("the number is a perfect number")
# else:
#     print("the number is not a perfect number ")  
# print('hello word')
# num=123
# order=len(str(num))
# sum=0
# while (num>0):
#     r=num%10
#     s=num//10
#     sum=sum + r ** order
# if num == sum :
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")    
    
    # import complex math module  
import cmath 
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (- b - cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   
                    