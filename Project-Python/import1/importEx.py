#6. refer importEx2 for remaining
from .import21 import add # if the both files are in same directory 

#7. from import1.import21 import add
add(10,2)


#from .. import add #doubts

#from logs.loggingEx import subtract
#subtract(10,2)

# 8. from other directory
from loggingEx.loggingEx import add
add(10,2)


input("press enter to exit")