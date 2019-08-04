"""
Points to remember:
1. syntax:
try:
    pass
except (RuntimeError, TypeError, NameError):
    pass
except ZeroDivisionError as e:
    print (e)
except NameError:
    pass
except:
    pass
else:
    pass
finally:
    pass

Note: 1. try-else is not possible
      2. It should follow this order try->except->else->finally.
      3. default except must be last except statement(only except without exception)
      4. It can have multiple except statement but only one except statement executed.
      5. Each except clause can have multiple exceptions
      6. It can have duplicate except clause but there is no use of duplicate clause
      7. the except block of code executed when try block throws any exception.
      7. The else block of code is executed only when there no exception occurs in try block.(When try block does not raise any exception).
      8. The finally block of code always executed whether we got exception or not.
      9. Exception() takes no keyword arguments.(Pass only positional argument)
"""

try :
    a = int(input("enter any no :"))
    b = 12
    c = b / a
    print (c)
except ZeroDivisionError as x:
    print (x)
else :
    print("else part")
finally :
    print ("finally part") 
 

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
    
 

## Manually raising an exception: raise IntanceOfBaseException(). It must be either a subclass or an instance of BaseException
def functionName( level ):
    if level <1:
        raise Exception("Invalid Level",level) # Exception() takes no keyword arguments.(Pass only positional argument)
    return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("error in level argument",e.args[0],e.args[1]) # error in level argument Invalid Level -10
    print(e) # ('Invalid Level', -10)
    print(type(e)) # <class 'Exception'>


    
## User-defined Exceptions: Exceptions should typically be derived from the Exception class, either directly or indirectly.
class MultiplyByZeroError(Exception):  # Note: user defined exceptions must derive from BaseException
    def __init__(self, *args):
        self.args = args
        # super().__init__(*args)

    def __str__(self):
        return str(self.args)
try:
    if 5 * 0 == 0:
        raise MultiplyByZeroError("Bad hostname", 5)
except MultiplyByZeroError as e:
    print(e) # ('Bad hostname', 5)
    print(type(e)) # <class '__main__.MultiplyByZeroError'>

    

## creating base exception for all errors:
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
        

#Defining Clean-up Actions: 
"""
A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When an exception 
has occurred in the try clause and has not been handled by an except clause (or it has occurred in an except or else clause), it 
is re-raised after the finally clause has been executed. The finally clause is also executed “on the way out” when any other clause
of the try statement is left via a break, continue or return statement. A more complicated example:
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
        raise Exception("Re-raise exception")
    finally:
        print("executing finally clause")

divide(2, 1)
"""
result is 2.0

Traceback (most recent call last):
executing finally clause

  File "C:/Users/Test/test.py", line 12, in <module>
    divide(2, 1)
  File "C:/Users/Test/test.py", line 8, in divide
    raise Exception("Re-raise exception")

Exception: Re-raise exception
Process finished with exit code 1
"""
divide(2, 0)
divide("2", "1")
