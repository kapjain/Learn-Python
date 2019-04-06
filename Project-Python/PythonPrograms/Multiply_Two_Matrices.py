X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
Y = [[10,11,12],  
      [13,14,15],  
      [16,17,18]]  
  
result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
  
# iterate through rows of X  
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
            
for r in result: 
    print(r)


matrix=[]
for i in range(1,4):
    row = []
    for j in range(1,4):
        value = int(input("enter value"))
        row.append(value)
    matrix.append(row)

for row in matrix:
    print(row)