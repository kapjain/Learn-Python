"""

When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the "argv" variable in the sys module. You can access this list by executing import sys. The length of the list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c command or -m module are not consumed by the Python interpreter’s option processing but left in sys.argv for the command or module to handle.

Note: when you run a python module in command prompt like:
python main.py 2 5
So system will assin value 2 in argv[1] (argv[1] = '2') and assin value 5 in argv[2] (argv[2] = '2') and so on.

Note: When you want to run a module as a command ,so either you need to go into path where the file is present or add the path while running command 
"""
import sys
def te(a,b):
    return a*b

if __name__ == '__main__':
    multiply  = te(int(sys.argv[1]),int(sys.argv[2]))
    print(multiply)