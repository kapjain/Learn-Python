print ("Pattern C")
for e in range (11,0,-1):
    print ((11-e) * ' ' + e * '*')

print ("Pattern D")
for g in range (11,0,-1):
    print  (g * ' ' + (11-g) * '*')



print ("Pattern E")
for e in range (1,10,1):
    print ( e * '*')

print ("Pattern F")
for e in range (10,0,-1):
    print ( e * '*')

print(10 * '**')
print ('')


for i in range(6):
    for j in range(i+1):
        print('*',end='')
    print()

n = 10
for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)
  
n = 10  
print("diamond shape")
for i in range(1,10):
    print(" "*(n-i)+ "*" * (2*(i-1) + 1))
for i in reversed(range(1,10)):
    print(" "*(n-i)+ "*" * (2*(i-1) + 1)) 