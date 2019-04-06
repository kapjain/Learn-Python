#filter(function or None, sequence) list tuple or string
#return those item of sequence for which function is true if function i None, return the items that are true
# if the sequence is tuple or string, return the same type or return list.

a = list(filter(lambda d: d!='a','abcd'))
print(a)


def d(x):
    return True if x !='a' else False

a = list(filter(d,'abcd'))
print(a)


b= list(filter(None,'abcd'))
print(b)



# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)