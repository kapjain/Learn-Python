a = bytearray('hi', 'utf-8')
print(id(a)) # 56912320

a[0]=99 # pass an ASCII value of character #
print(a) #  bytearray(b'ci')

print(id(a)) # 56912320 


import io
s = 'kapil'
sio = io.StringIO(s)
print(sio.getvalue()) # kapil

sio.seek(3)
sio.write('there')

print(sio.getvalue()) # kapthere



import array
s = 'kapil'
a = array.array('u',s)
print(a)
a[0] = 'y'
print(a)

# a = array.array(s) TypeError: array() argument 1 must be a unicode character, not str