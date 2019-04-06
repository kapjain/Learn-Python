"""
eval(expression, globals=None, locals=None): The eval is used to evaluate a single dynamically generated Python expression
            In simple terms, the eval() method runs the python code (which is passed as an argument) within the program.

eval() Parameters : The eval() takes three parameters:

    1. expression - this string as parsed and evaluated as a Python expression(Single expresion,otherwise will throw error invalid syntax)
    2. globals (optional) - a dictionary
    3. locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.


exec(object, globals, locals): The exec() method executes the dynamically created program, which is either a string or a code object.



Difference between eval() and exec():

1. eval accepts only a single expression, exec can take a code block that has Python statements: loops, try: except:, class and function/method definitions and so on.

2. eval returns the value of the given expression, whereas exec ignores the return value from its code, and always returns None (in Python 2 exec is a statement
 and cannot be used as an expression, so it really does not return anything)
 
3. 
"""

#example 1:
a = 5
eval('37 + a')   # 42 it is an expression
exec('37 + a')   # it is an expression statement; value is ignored (None is returned)




#example 2:
exec('a = 47')   # modify a global variable as a side effect
print(a) #47

#eval('a = 47')  # you cannot evaluate a statement
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<string>", line 1
#    a = 47
#      ^
#SyntaxError: invalid syntax

#eval('for i in range(3): print(i)') # Error 
#eval('print();print()') # Error 




#example 3:
"""

 
 
compile() Parameters

    source - a normal string, a byte string, or an AST object
    filename - file from which the code was read. If it wasn't read from a file, you can give a name yourself
    mode - Either exec or eval or single.
        eval - accepts only a single expression.
        exec - It can take a code block that has Python statements, class and functions and so on.
        single - if it consists of a single interactive statement
    flags (optional) and dont_inherit (optional) - controls which future statements affect the compilation of the source. Default Value: 0
    optimize (optional) - optimization level of the compiler. Default value -1.
"""



"""
The compile in 'exec' mode compiles any number of statements into a bytecode that implicitly always returns None, whereas in 'eval' mode it compiles a single
expression into bytecode that returns the value of that expression.
In the 'eval' mode (and thus with the eval function if a string is passed in), the compile raises an exception if the source code contains statements or anything 
else beyond a single expression
"""


# example 1
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')# works fine
exec(codeObejct)


# example 2
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'eval') # got error
eval(codeObejct)


# example 3
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'single') # got error because single mode support multiple line with;
exec(codeObejct)


# example 4
codeInString = 'a = 5;b=6;sum=a+b;print("sum =",sum);'
codeObejct = compile(codeInString, 'sumstring', 'single') # works fine
exec(codeObejct)

# example 5 mix
codeInString = 'a = 5;b=6;sum=a+b;print("sum =",sum);'
codeObejct = compile(codeInString, 'sumstring', 'exec') # works fine
eval(codeObejct)