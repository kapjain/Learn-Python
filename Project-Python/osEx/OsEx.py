"""
The main purpose of the OS module is to interact with your operating system. The primary use I find for it is to create folders, remove folders, move folders, 
and sometimes change the working directory. You can also access the names of files within a file path by doing listdir().

Executing a shell command
os.system()    

Get the users environment 
os.environ()   

#Returns the current working directory.
os.getcwd()   

Return the real group id of the current process.
os.getgid()       

Return the current processs user id.
os.getuid()    

Returns the real process ID of the current process.
os.getpid()     

Set the current numeric umask and return the previous umask.
os.umask(mask)   

Return information identifying the current operating system.
os.uname()     

Change the root directory of the current process to path.
os.chroot(path)   

Return a list of the entries in the directory given by path.
os.listdir(path) 

Create a directory named path with numeric mode mode.
os.mkdir(path)    

Recursive directory creation function.
os.makedirs(path)  

Remove (delete) the file path.
os.remove(path)    

Remove directories recursively.
os.removedirs(path) 

Rename the file or directory src to dst.
os.rename(src, dst)  

Remove (delete) the directory path.
os.rmdir(path) 
"""
import os

curDir = os.getcwd()
print(curDir) # C:\Users\Kapil Jain\git\kapil\TestPython\osEx

print(os.listdir(os.getcwd()))
#os.mkdir('newDir') # system will create a directory in current working directory
#os.rename('newDir','newDir2')
#os.rmdir('newDir2')