"""
The sys module allows you to use stdin() and stdout(), as well as stderr(), but, most interestingly, we can utilize sys.argv(). To many, this is a confusing concept,
 but it is pretty simple and very useful once you learn it. The idea of sys.argv is to allow you to pass arguments through to Python from the command line.
"""
import sys


sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')