#Note: try-else and try-finally-else not possible
# try except
try:
    a = 1
    print(a)
except:
    print("error")

#try finally
try:
    a = 1
    print(a)
finally:
    print("error")

#try except else    
try:
    a = 1
    print(a)
except:
    print("error")
else: #The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception
    print("else")

#try except finally    
try:
    a = 1
    print(a)
except:
    print("error")
finally:
    print("else")


try :
    a = int(input("enter any no :"))
    b = 12
    c = b / a
    print (c)
except ZeroDivisionError as x:
    print (x)
else :#The code in the else-block executes if the code in the try: block does not raise an exception.
    print("else part")
finally :
    print ("finally part") 
    

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


def functionName( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception 
    return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("error in level argument",e.args[0])






#A try statement may have more than one except clause, to specify handlers for different exceptions
# An except clause may name multiple exceptions as a parenthesized tuple, for example:

except (RuntimeError, TypeError, NameError):
    pass


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


#User-defined Exceptions
#Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). Exceptions should typically be derived from the Exception class, either directly or indirectly.

class MultiplyByZeroError(ArithmeticError):#Note: user defined exceptions must derive from BaseException
    def __init__(self, arg):
        self.args = arg
try:
    a = int(input("enter value of a"))
    if (a*0==0):
            raise MultiplyByZeroError("Bad hostname")
except MultiplyByZeroError as e:
    print ("user defined exception"+ str(e))


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        

#Important
#Defining Clean-up Actions: A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in an except or else clause), it is re-raised after the finally clause has been executed. The finally clause is also executed “on the way out” when any other clause of the try statement is left via a break, continue or return statement. A more complicated example:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)


divide(2, 0)


divide("2", "1")
