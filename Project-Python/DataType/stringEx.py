"""
The str() method returns the "informal" or nicely printable representation of a given object.

str(object='')
str(byte_or_buffer=b'', encoding='utf-8', errors='strict')

str() Parameters: The str() method mainly takes three parameters which are same for both constructs:

object - object whose informal representation is to be returned
encoding - Defaults of UTF-8. Encoding of the given object
errors - response when decoding fails. 

Ex: str(b'hi',encoding = 'utf-8', errors = 'ignore')

There are six types of error response:

strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable unicode from the result
replace - replaces the unencodable unicode to a question mark ?
xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \uNNNN espace sequence instead of unencodable unicode
namereplace - inserts a \N{...} escape sequence instead of unencodable unicode

Note: If encoding and errors parameter is provided, the first parameter (object) should be a bytes-like-object (bytes or bytearray).
    If the object is bytes or bytearray, str() method internally calls bytes.decode(encoding, errors). 


# bytes run this code in interpitter
#b = bytes('pythön', encoding='utf-8')
#print(str(b, encoding='ascii', errors='ignore')) output : pythn

character 'ö'
b = bytes('pyth\xf6n', encoding='utf-8')
#print(str(b, encoding='ascii', errors='strict'))

#UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 4: ordinal not in range(128)


1. Immutable
2. support slicing
3. can contain mutable object

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 
 'encode',
 
 'capitalize', 'casefold', 'upper', 'lower', 'swapcase', 'title', 'center', 'zfill', 'ljust', 'rjust', 'count', 'startswith', 'endswith',  
 'index', 'rindex', 'find', 'rfind',  'join', 'strip', 'rstrip', 'lstrip', 'split', 'rsplit', 'splitlines'
 'isalnum', 'isalpha',  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
  'expandtabs', 'replace', 'maketrans', 'translate', 'partition', 'rpartition']
   
   format - https://www.programiz.com/python-programming/methods/string/format
   format_map - https://www.programiz.com/python-programming/methods/string/format_map
"""

sr1 = '' # empty string
sr2 = str() # empty string

sr3 = 'i'# single element string

sr4 = 'kapil'

sr5 = " a + 2 * 3.14"


input("wait to press enter!")

l1 = '0123456789'
l2 = 'kapil'
print(l1 + l2)#0123456789kapil
print(l1*2)#01234567890123456789
print( '1' in l1 )# True
print(len(l1))#10
print(min(l1))#0 it doesn't works with mix list like int and str are in same list
print(max(l1))#9
print(min(l2))#a check according to dictionary sequence
print(max(l2))#p





#capitalize(): It returns a copy of the string with only its first character capitalized.
#The first letter of the string is converted to uppercase and the others are converted to lowercase.
s = 'kapil'
print(s.capitalize()) # 'Kapil'
s = 'Kapil'
print(s.capitalize()) # 'Kapil' If the first letter of the string is already capital then it do nothing



#casefold(): It returns a copy of the string with all small character .
s = 'Kapil'
print(s.casefold()) #'kapil'
s = 'kAPIL'
print(s.casefold()) # 'kapil'



#The method upper() returns a copy of the string in uppercase.
#The method lower() returns a copy of the string in lowercased.
s = 'Kapil'
print(s.upper()) # 'KAPIL'
print(s.lower()) # 'kapil' # Uppercase letters are converted to lowercase. The other characters are left unchanged.

# swapcase(): it return a copy of string with changing the case of all character upper to lower ans vice versa
s = 'Kapil'
print(s.swapcase()) # 'kAPIL'



#title() - it return a string which contain the first letter of each word is capital and rest are small or anything
s = 'Hi this is python'
print(s.title())  # Hi This Is Python



# center(width[,fillchar]) The method center() returns centered in a string of length width. Padding is done using the specified fillchar. Default filler is a space.
s = 'kapil'
print(s.center(10,'@')) # '@@kapil@@@' filling start from left, left right left right so on
print(s.center(10)) # '  kapil   '
print("abcdef".center(0)) # 'abcdef' The entire string is printed when the argument passed to center() is less than the length of the string.
print('*', "abcdef".center(7), '*', sep='') #  Padding is done towards the right-hand-side first when the final string is of even length.

#zfill(width) The zfill() method pads string on the left with zeros to fill width.
s = 'kapil'
print(s.zfill(20)) # '000000000000000kapil'



#str.ljust(width[, fillchar]): The method ljust() returns the string left justified in a string of length width. Padding is done using the specified 
#fillchar (default is a space). The original string is returned if width is less than len(s).
#str.rjust(width[, fillchar]):  The rjust() method returns the string right justified in a string of length width. Padding is done using the specified
#fillchar (default is a space). The original string is returned if width is less than len(s).
s = "this is string example....wow!!!"

print (s.ljust(50, '*')) #this is string example....wow!!!******************
print (s.rjust(50, '*')) #******************this is string example....wow!!!



#count(sub,start = 0,end = len(string)) The count() method returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
s = "hello all this is the python language of the world"
print(s.count('h')) # 5
print(s.count('the')) #2
# print("xyyzxyzxzxyy".count('xyy', 0, 100)) An error will not occur if the end value is greater than the length of the string itself.
print("xyyzxyzxzxyy".count('xyy', 0, 12)) # 2



#The startswith() method checks whether the string starts with str, optionally restricting the matching with the given indices start and end.
#It returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.

s = "this is string example....wow!!!"
print (s.startswith( 'this' )) #True
print (s.startswith( 'string', 8 ))#True
print (s.startswith( 'this', 2, 4 ))#False


suffix='!!'
print (s.endswith(suffix))#True
print (s.endswith(suffix,20))#True
suffix='exam'
print (s.endswith(suffix))#False
print (s.endswith(suffix, 0, 19))#True




#The index() method determines if the string str occurs in string or in a substring of string, if the starting index beg and ending index end are given.
# This method is same as find(), but raises an exception if sub is not found.

#The rindex() method returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting
# the search to string[beg:end].

#str.rindex(str, beg = 0 end = len(string))

#str.index(str, beg = 0 end = len(string))

str1 = "this is string example....wow!!!"
str2 = "exam";

print (str1.index(str2)) #15
print (str1.index(str2, 10)) #15
print (str1.index(str2, 40)) # ValueError: substring not found

str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rindex(str2)) # 5
print (str1.rindex(str2,10)) # ValueError: substring not found



#The find() method determines if the string str occurs in string, or in a substring of string if the starting index beg and ending index end are given.

#The rfind() method returns the last index where the substring str is found, or -1 if no such index exists, optionally restricting the search to string[beg:end].
#str.rfind(str, beg = 0 end = len(string))
#str.find(str, beg = 0 end = len(string))


str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rfind(str2)) # 5

print (str1.rfind(str2, 0, 10)) # 5
print (str1.rfind(str2, 10, 0)) # -1

print (str1.find(str2)) # 2
print (str1.find(str2, 0, 10)) # 2
print (str1.find(str2, 10, 0)) # -1



#str.join(sequence): The join() method returns a string in which the string elements of sequence have been joined by str separator.
s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq )) #a-b-c

seq = [1,2,3]
s = ','
#s.join(seq) TypeError: sequence item 0: expected str instance, int found



#str.strip([chars]): The strip() method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string 
#(default whitespace characters \t \n also).

#str.lstrip([chars]): The lstrip() method returns a copy of the string in which all chars have been stripped from the beginning of the string 


#str.rstrip([chars]): The rstrip() method returns a copy of the string in which all chars have been stripped from the end of the string 


s = "*****this is sing example....wow!!!*****"
print (s.strip( '*' ))# this is sing example....wow!!!

s = "     this is sing example....wow!!!     "
print (s.rstrip())#'      this is sing example....wow!!!'

s = "*****this is sing example....wow!!!*****"
print (s.rstrip('*')) #*****this is sing example....wow!!!

     
s = "     this is sing example....wow!!!"
print (s.lstrip())# this is sing example....wow!!!

s = "*****this is sing example....wow!!!*****"
print (s.lstrip('*'))#this is sing example....wow!!!*****




# b.replace(old,new,count): Return a copy of b with all occurrences of subsection old replaced by new. If the optional argument count is given, only the first count occurrence are replaced.

s = 'hi this is python. It is very good languange'
print(s.replace('is','are',2)) #hi thare are python. It is very good languange
print(s.replace('is','are')) # hi thare are python. It are very good languange




# str.split(sep="", maxsplit = string.count(str)): The split() method returns a list of all the words in the string, using str as the separator
# (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.

# str. rsplit([sep=''[, maxsplit]]): Returns a list of the words in the string, separated by the delimiter string (starting from right). 
#maxsplit: Optional. Number of splits to do; default is -1 which splits all the items.

print(' a b c '.split()) #['a', 'b', 'c']
print(' a b c '.split(None, 1)) #[' a ', 'bc']
print(' a b c '.split(None, 2)) #[' a', 'b', 'c']


print(' a b c '.rsplit()) #['a', 'b', 'c']
print(' a b c '.rsplit(None, 1)) #[' a b', 'c']
print(' a b c '.rsplit(None, 2)) #[' a', 'b', 'c']



#str.splitlines( num = string.count('\n')): The splitlines() method returns a list with all the lines in string, optionally including the line breaks (if num is supplied and is true).
#num − This is any number, if present then it would be assumed that line breaks need to be included in the lines.

s = "this is \nstring example....\nwow!!!"
print (s.splitlines( )) #['this is ', 'string example....', 'wow!!!']



s1 = '12345'
s2 = 'abcd'
s3 = 'abc123' 
s4 = 'Kapil'
s5 = 'jain'
s6 = 'AKSH'
s7 = '  '
s8 = 'Hi This Is Python'
#isalnum():
print(s1.isalnum()) #False
print(s3.isalnum()) #True

#isalpha():
print(s1.isalpha()) #False
print(s2.isalnum()) #True

#islower():
print(s4.islower()) #False
print(s5.islower()) #True

#isupper():
print(s4.isupper()) #False
print(s6.isupper()) #True

#isspace(): return true if all the caracter are white space
print(s4.isspace()) #False
print(s7.isspace()) #True

#istitle():
print(s4.istitle()) #False
print(s8.istitle()) #True


#str.isdecimal() (Only Decimal Numbers) return true if all character are decimal
print("34".isdecimal())  #True
print("\u00B2")#superscript 2
print("\u00B2".isdecimal())  #False

#str.isdigit() (Decimals, Subscripts, Superscripts) retrun true if all the character all digit

print("34".isdigit()) #True
print("\u00B2")
print("\u00B2".isdigit()) #True

#str.isnumeric() (Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators) return true if all character are numeric

print("34".isnumeric()) #True
print("\u00B2")
print("\u00B2".isnumeric()) #True

print("\u00BC")#Quarter numeric
print("\u00BC".isnumeric()) #True


#isprintable(): return true if all the character can be printed and does not contain char \n, \t
s = 'hi'
print(s.isprintable()) #True
True
s = 'hi\nk'
print(s.isprintable()) #False

#isidentifier- return true if the string is identifier mean any pythin keyword funfunctionExass

s = 'else'
print(s.isidentifier()) #True
s = 'None'
print(s.isidentifier()) #True



# str.expandtabs(tabsize = 8): The expandtabs() method returns a copy of the string in which the tab characters ie. '\t' are expanded using spaces, optionally using the given tabsize (default 8).
#tabsize − This specifies the number of characters to be replaced for a tab character '\t'.

s = "this is\tstring example....wow!!!"
#you can resize the tab size

print ("Original string: " + s)
print ("Defualt exapanded tab: " +  s.expandtabs())
print ("Double exapanded tab: " +  s.expandtabs(16))
#Original string: this is        string example....wow!!!
#Defualt exapanded tab: this is string example....wow!!!
#Double exapanded tab: this is         string example....wow!!!



#string.partition(separator): The partition() method splits the string at the first occurrence of the argument string and returns a tuple containing the part the
# before separator, argument string and the part after the separator.
#The partition() method takes a string parameter separator that separates the string at the first occurrence of it.


#1. the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string
#2. string itself and two empty strings if the separator parameter is not found

string = "Python is fun"

# 'is' separator is found
print(string.partition('is ')) #('Python ', 'is ', 'fun')

# 'not' separator is not found
print(string.partition('not ')) #('Python is fun', '', '')

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))#('Python ', 'is', " fun, isn't it")




"""
string.rpartition(separator): The rpartition() splits the string at the last occurrence of the argument string and returns a tuple containing the part the before 
separator, argument string and the part after the separator.

The rpartition() method takes a string parameter separator that separates the string at the last occurrence of it.

The rpartition method returns a 3-tuple containing:

    the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string
    two empy strings, followed by the string itself if the separator parameter is not found

"""

string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is ')) #('Python ', 'is ', 'fun')

# 'not' separator is not found
print(string.rpartition('not ')) #('', '', 'Python is fun')

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is')) #('Python is fun, ', 'is', "n't it")
