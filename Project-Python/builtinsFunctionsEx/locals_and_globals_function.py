"""
A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.

    Global symbol table
    Local symbol table

A Global symbol table stores all information related to the global scope of the program, and is accessed in Python using globals() method.

The global scope contains all functions, variables which are not associated to any class or function.

Likewise, Local symbol table stores all information related to the local scope of the program, and is accessed in Python using locals() method.

The local scope could be within a function, within a class, etc.
"""

print(locals())
#{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x030DA6F0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Kapil Jain\\git\\kapil\\TestPython\\builtinsFunctionsEx\\locals_and_globals_function.py', '__cached__': None}


def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsNotPresent())
print('localsPresent:', localsPresent())


def localsPresent1():
    present = True
    print(present)
    locals()['present'] = False;#Unlike, globals() dictionary which reflects the change to the actual global table, locals() dictionary may not change the information inside the locals table.
    print(present)

localsPresent1()

age = 23

globals()['age'] = 25
print('The age is:', age)



a,b,x,y = 1,15,3,4
def foo(x,y):
    global a
    a = 42
    x,y= y,x
    b=33
    b=17
    c=100
    print(a,b,x,y)
foo(17,4) # 42 17 4 17