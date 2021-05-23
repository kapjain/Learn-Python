# Note: In python everything is a call by reference, but we can modify only mutable objects
a = 10

def change(a):
    a = 11
    return
  
print(a)
change(a)
print(a)

a = [1,2,3]

def change(a):
    a.append(4)
    return
  
print(a)
change(a)
print(a)
