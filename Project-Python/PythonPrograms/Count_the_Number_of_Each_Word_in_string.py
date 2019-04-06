s = str(input("enter any string : "))
s = s.casefold()
line = s.split()
nl=[]
for word in line:
    if word not in nl:
        print("Word %s comes %d times."%(word, line.count(word)))
        nl.append(word)


s = str(input("enter any string : "))
s = s.casefold()
