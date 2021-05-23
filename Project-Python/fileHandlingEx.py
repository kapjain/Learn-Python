"""
Open file: open()
Close file: close()
Read file: read(), readline(), readlines()
Write file: write(), writelines()
tell()
seek()
"""

with open("D:\My Data\Study material\django.txt","r") as fh : print(sum(1 for line in fh for character in line if character.isupper()))

a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

print("Example 1 ************************************************")
try :
    f = open("file1.txt", "r")
    print(f.read(10))
    f.close()
except Exception as e:
    print(e)

print("Example 2 ************************************************")
try :
    f = open("file1.txt", "r")
    print(f.read(-10)) #When size is omitted or negative, the entire contents of the file will be read and returned
    f.close()
except Exception as e:
    print(e)
       
print("Example 3 ************************************************")
try :
    f = open("file1.txt", "r")
    print(f.read())
    print(f.read()) # If the end of the file has been reached, f.read() will return an empty string ('').
    f.close()
except Exception as e:
    print(e)

print("Example 4 ************************************************")

try :
    f = open("file1.txt", "r")
    for line in f:
        print(line)
    f.close()
except Exception as e:
    print(e)

print("Example 5 ************************************************")

try :
    f = open("file1.txt", "r")
    print(f.readline()) #f.readline() reads a single line from the file
    print(f.readline())
    f.close()
except Exception as e:
    print(e)
    
print("Example 6 ************************************************")

try :
    f = open("file1.txt", "r")
    print(f.readlines()) # If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    f.close()
except Exception as e:
    print(e)
    
print("Example 7 ************************************************")

try :
    f = open("file1.txt", "r")
    print(list(f)) # If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    f.close()
except Exception as e:
    print(e)
    

print("Example 8 ************************************************")
try :
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt","w")
    s = f1.read()
    print(s)
    f2.write(s)
    f1.close()
    f2.close()
except Exception as e:
    print(e)


print("Example other ************************************************")  
try :
    f = open("file1.txt", "r")
    l = list(map(lambda s: s.strip(), f.readlines())) 
    print(l)
    f.close()
except Exception as e:
    print(e)

try :
    f=open('file2.txt','w')
    for o in l:
        f.writelines(o + '\n')
    f.close()
except Exception as e:
    print(e)
    
print("Example EOL added ************************************************") 
with open("file1.txt",'w') as f:
    f.write("hi\n")
    f.write("kapil")
    
print("Example append ************************************************")    
with open("file1.txt",'a') as f:
    f.write("hi\n")
    f.write("kapil\n")
    
print("Example of tell and seek ************************************************")    
with open("file1.txt",'r') as f:
    print(f.tell())
    f.seek(2,0)
    print(f.tell())
print("Example of full path tested in interpitter ************************************************")     
with open("D:\Personal Data\Study material\python.txt","r") as f:
    for line in f:
        print(line)


print("Example of full path tested in interpitter ************************************************")     
with open("C:\\normal.txt","r") as f:
    for line in f:
        print(line)
        
#pip install python-docx        
from docx import Document
document = Document()

with open('D:\\My Data\\file1.txt', 'r') as textfile:
    for line in textfile.readlines():
        document.add_paragraph(line)

document.save('file21.docx')
