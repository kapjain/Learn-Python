def isAlphabet(x): 
    return x.isalpha() or '-' in x
    
    
# Utility functions 
    


def reverse(string):
    str_list = string.split()
    print(str_list)
    idx = 0
    for strn in str_list:
        if isAlphabet(strn):
            str_list[idx] = strn[::-1]
        else:
            str_list[idx] = str_spcial(strn)
        idx = idx + 1
        
    return ' '.join(str_list)
    
def str_spcial(string):
    new_str = ''
    idx = 0
    start_idx = 0
    end_idx = 0
    for ch in string:
        alp_str = string[start_idx:]
        if start_idx == idx and isAlphabet(alp_str):
            new_str = new_str + alp_str[::-1]
            break

        if not isAlphabet(ch):
            end_idx = idx
            sub_str = string[start_idx:end_idx]
            new_str = new_str + sub_str[::-1] + ch
            start_idx = idx + 1

        idx += 1
    return new_str




def remove_consequative(string):
    idx = 0
    str_len = len(string)
    new_str = ''
    while(idx<str_len):
        if idx == str_len-1:
            new_str = new_str + string[idx]
            return new_str
        if ord(string[idx])+1 == ord(string[idx+1]):
            while(idx<str_len-1 and ord(string[idx])+1 == ord(string[idx+1])):
                idx += 1
                
        else:
            new_str = new_str + string[idx]
        idx = idx + 1    
    return new_str

if __name__ == '__main__':
    s = "We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
    #print(reverse(s))
    print(remove_consequative('acxyqkmnstuvaxyz'))
    