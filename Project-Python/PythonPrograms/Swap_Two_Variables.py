a,b = 10,20

a,b = b,a
print("a :{}, b : {}".format(a,b))

#with using third variable

a,b = 30,40

c = a
a = b
b = c

print("a :{}, b : {}".format(a,b))

x , y = 10, 20
#Addition and Subtraction

x = x + y
y = x - y
x = x - y
print("x :{}, y : {}".format(x,y))
#Multiplication and Division
x , y = 10, 20
x = x * y
y = x / y
x = x / y
print("x :{}, y : {}".format(x,y))
input("wait ")
#XOR swap This algorithm works for integers only
x , y = 10, 20
x = x ^ y
y = x ^ y
x = x ^ y
print("x :{}, y : {}".format(x,y))