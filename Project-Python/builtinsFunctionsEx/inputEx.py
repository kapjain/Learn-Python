""""
input([prompt]): The input() method reads a line from input, converts into a string and returns it.
    prompt (Optional) - a string that is written to standard output (usually screen) without trailing newline
    
Return value from input() :The input() method reads a line from input (usually user), converts the line into a string by removing the trailing newline, and returns it.
                If EOF is read, it raises an EOFError exception.


Note: input() :interprets and evaluates the input which means that if user enters integer,an integer will be returned ,if user enters string,"
string is returned.

raw_input():raw_input() takes exactly what user typed and passes it back as string .It doesn’t interprets the user input.Even an integer 
value of 10 is entered or a list is entered its type will be of string only.

The difference is that raw_input() does not exist in Python 3.x, while input() does. Actually, the old raw_input() has been renamed to input(),
 and the old input() is gone, but can easily be simulated by using eval(input()).

In python 3.X, whatever you will give, system will always return value as string.
"""


inputString = input()

print('The inputted string is:', inputString)

inputString = input('Enter a string:')

print('The inputted string is:', inputString)