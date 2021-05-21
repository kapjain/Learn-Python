"""
Note: Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition
becomes false (with while), but not when the loop is terminated by a break statement.
"""

print("******************while loop*********************")
n = 1
while( n <= 10 ) :
    print("2 * {} = {}".format(n, 2*n))
    n += 1
#output: 2 * 1 = 2, 2 * 2 = 4 .. 2 * 10 = 20

print("******************for loop*********************")
for n in range(1,11) :
    print("2 * {} = {}".format(n, 2*n))
#output: 2 * 1 = 2, 2 * 2 = 4 .. 2 * 10 = 20

print("******************while else loop*********************")   
count = 0
while (count < 9):
    print ("""The count is:""", count)
    count = count + 1
else :
    print ("Good bye!") 
# else statement does not executed when loop terminated with break

print("******************for else loop*********************") 
List =[1,2,3,4,5]
for i in List:
        print (i)
        if i == 4:
            break
else:
    print("else statement")
# else statement does not executed when loop terminated with break

print("******************Nested loop*********************") 
for i in range(1,11):
    for j in range(1,11):
        print(i*j,",",end = '')
    print("")
    
print("******************continue statement*********************") 
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

print("******************break statement*********************") 
for i in range(10):
    if i == 5:
        break
    print(i)

print("******************Pass statement*********************") 
for i in range(10):
    pass



for index, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(index, value)
    

questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for question, answer in zip(questions, answers):
    print(question, answer)
    
    
d = { "geeks" : "for", "only" : "geeks" }
for key,value in d.items():
    print key,value

lis = [ 1 , 3, 5, 6, 2, 1, 3 ]
for i in set(lis) :
    print (i,end=" ")






