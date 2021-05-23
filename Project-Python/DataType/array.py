"""

array(typecode [, initializer]) -> array                                                                    
                                                                                                            
Return a new array whose items are restricted by typecode, and                                              
initialized from the optional initializer value, which must be a list,                                      
string or iterable over elements of the appropriate type.                                                   
                                                                                                            
Arrays represent basic values and behave very much like lists, except                                       
the type of objects stored in them is constrained. The type is specified                                    
at object creation time by using a type code, which is a single character.                                  
The following type codes are defined:                                                                       
                                                                                                            
    Type code   C Type             Minimum size in bytes                                                    
    'b'         signed integer     1                                                                        
    'B'         unsigned integer   1                                                                        
    'u'         Unicode character  2 (see note)                                                             
    'h'         signed integer     2                                                                        
    'H'         unsigned integer   2                                                                        
    'i'         signed integer     2                                                                        
    'I'         unsigned integer   2                                                                        
    'l'         signed integer     4                                                                        
    'L'         unsigned integer   4                                                                        
    'q'         signed integer     8 (see note)                                                             
    'Q'         unsigned integer   8 (see note)                                                             
    'f'         floating point     4                                                                        
    'd'         floating point     8                                                                        
                                                                                                            
NOTE: The 'u' typecode corresponds to Python's unicode character. On                                        
narrow builds this is 2-bytes on wide builds this is 4-bytes.                                               
                                                                                                            
NOTE: The 'q' and 'Q' type codes are only available if the platform                                         
C compiler used to build Python supports 'long long', or, on Windows,                                       
'__int64'.                                                                                                  
                                                                                                            
Methods:                                                                                                    
                                                                                                            
append() -- append a new item to the end of the array                                                       
buffer_info() -- return information giving the current memory info                                          
byteswap() -- byteswap all the items of the array                                                           
count() -- return number of occurrences of an object                                                        
extend() -- extend array by appending multiple elements from an iterable                                    
fromfile() -- read items from a file object                                                                 
fromlist() -- append items from the list                                                                    
frombytes() -- append items from the string                                                                 
index() -- return index of first occurrence of an object                                                    
insert() -- insert a new item into the array at a provided position                                         
pop() -- remove and return item (default last)                                                              
remove() -- remove first occurrence of an object                                                            
reverse() -- reverse the order of the items in the array                                                    
tofile() -- write all items to a file object                                                                
tolist() -- return the array converted to an ordinary list                                                  
tobytes() -- return the array converted to a string                                                         

['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 


'append','insert', 'extend', 'pop', 'remove', 'count', 'index', 'reverse',
'typecode', 'buffer_info', 'byteswap', 'itemsize', 
'frombytes', 'fromfile', 'fromlist', 'fromstring', 'fromunicode', 
'tobytes', 'tofile', 'tolist', 'tostring', 'tounicode']
"""

import array

foo = array.array('u','apple and juice')
foo[0]='S'
foo[-4:]=array.array('u','milk') # TypeError: can only assign array (not "str") to array slice
print(''.join(foo)) # Spple and jmice

foo[6:]=array.array('u','milk') # Spple milk

