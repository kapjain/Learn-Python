s = 'f'
c = 0
with open("file1.txt","r") as f:
    for line in f:
        c += line.count(s)
    print(c)