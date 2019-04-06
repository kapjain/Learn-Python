"""
__import__(name, globals=None, locals=None, fromlist=(), level=0):  The __import__() is an advanced function that is called by the import statement.

__import__() Parameters

    name - name of the module you want to import
    globals and locals - determines how to interpert name
    fromlist - objects or submodules that should be imported by name
    level - specifies whether to use absolute or relative imports

"""

mathematics = __import__('math', globals(), locals(), [], 0)

print(mathematics.fabs(-2.5))