a = "hello" # created an "Hello" Object in the memory

print("address of %s: %d"%(a,id(a)))

a = "kapil" # created a new string object "Kapil"

print("address of %s: %d"%(a,id(a)))

#a[0]= 'e' # TypeError: 'str' object does not support item assignment

print("****************************************************")

t1 = (1,2,3)
print("address of %s: %d"%(t1,id(t1)))
t1 = t1 + (4,5,6)
print("address of %s: %d"%(t1,id(t1)))

print("****************************************************")
plist = [1,2,3,4,5]
print("address of %s: %d"%(plist,id(plist)))

plist = [0,1,2,3,4,5]
print("address of %s: %d"%(plist,id(plist)))

plist = plist + [1,2,3,4,5]
print("address of %s: %d"%(plist,id(plist)))

plist.extend([6,2,3,4,5])
print("address of %s: %d"%(plist,id(plist)))

plist[0] = 9
print("address of %s: %d"%(plist,id(plist)))

plist.append(11)
print("address of %s: %d"%(plist,id(plist)))

print("****************************************************")

t2 = (1,[1,2,3],'kapil')
print("address of %s: %d"%(t2,id(t2)))
t2[1][0]=5
print("address of %s: %d"%(t2,id(t2)))
