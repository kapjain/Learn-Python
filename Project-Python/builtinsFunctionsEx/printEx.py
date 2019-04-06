"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) :The print() function prints the given object to the standard output device (screen) or to the text stream file.

print() Parameters

    objects - object to the printed. * indicates that there may be more than one object
    sep - objects are separated by sep. Default value: ' '
    end - end is printed at last
    file - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
    flush - If True, the stream is forcibly flushed. Default value: False

Return Value from print() : It doesn't return any value; returns None.

"""

a = 5
print("a =", a, sep='00000', end='\n\n\n') # a =000005
print("a =", a, sep='0', end=' ') # a =05 stop
print("stop")


#Example 3: print() with file parameter:  In Python, you can print objects to the file by specifying the file parameter.


sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()