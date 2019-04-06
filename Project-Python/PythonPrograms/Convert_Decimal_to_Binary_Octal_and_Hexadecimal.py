n = int(input("enter any number : "))
binary_nbr = ''
while(n>0):
    binary_nbr = binary_nbr + str(n % 2)
    n = n // 2

print(binary_nbr[::-1])

bn = str(input("enter any number : "))
l = len(bn)
print(l)
decimal = 0
for i in range(l):
    decimal = decimal * 2
    if bn[i] == '1':
        decimal += 1
print(decimal)