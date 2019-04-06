# import complex math module  
# import cmath  
# a = float(input('Enter a: '))  
# b = float(input('Enter b: '))  
# c = float(input('Enter c: '))  
#   
# # calculate the discriminant  
# d = (b**2) - (4*a*c)  
#   
# # find two solutions  
# sol1 = (-b-cmath.sqrt(d))/(2*a)  
# sol2 = (-b+cmath.sqrt(d))/(2*a)  
# print('The solution are {0} and {1}'.format(sol1,sol2))   
# from test.crashers.mutation_inside_cyclegc import lst
# from test.crashers.mutation_inside_cyclegc import lst

# import calendar  
# # Enter the month and year  
# yy = int(input("Enter year: "))  
# mm = int(input("Enter month: "))  
#   
# # display the calendar  
# print(calendar.month(yy,mm))  \

# # n1 = int(input("enter the first number"))
# # n2 = int(input("enter the second number"))
# # 
# # x = n1
# # y = n2
# # 
# # while(n1 != n2):
# #     if(n1>n2):
# #         n1 = n1 - n2
# #     else:
# #         n2 = n2 - n1
# # print("HCF is",n1)
# # hcf = n1
# # lcm = (x*y)/hcf
# # print("LCM is",lcm)            

# # dec = 140
# # # print(hex(dec),"in hexasecimal")
# 
# try:
#     a = 1
#     raise Exception
# except:
#     print("error")
# else:
#     print("else")


# print ("Pattern C")
# for e in range (11,0,-1):
#     print ((11-e) * ' ' + e * '*')


# def swapList(list): 
#       
#     start, *middle, end = list
#     list = [end, *middle, start] 
#       
#     return list
#       
# # Driver code 
# newList = [1,2,3,4,5,5,6,7] 
#   
# print(swapList(newList)) 
# def Reverse(lst):
#     lst.reverse()
#     return lst
# lst = [1,2,3,4]

# n = 10
# for i in range(1,n+1):
#     print('' * (n-1) + '*' * i )
#     
#     
n=10
for i in reversed(range(1,n+1)):
    print('' * (n-1) + '*' * i )
    
    