                                        """
A positive integer is called an Armstrong number of order n if

abcd... = a**n + b**n + c**n + d**n + ...
"""
num = 1634
#num = input("enter any number: ")
# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum1 = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum1 += digit ** order
    temp //= 10

# display the result
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")