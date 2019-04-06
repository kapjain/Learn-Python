def isAlphabet(x): 
    return x.isalpha() or x =='-'
    
    
# Utility functions 
    


def reverse(string):
    str_list = string.split()
    
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
    
if __name__ == '__main__':
    s = "We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
    print(reverse(s))
    
    
def main():
    s = "Python is Interactive and fast"
    str_lst = s.split()

    max_len = 0
    for i in str_lst:
        if max_len<len(i):
            max_len = len(i)
            
    str_req = max_len+2
    print('*'*str_req)
    for word in str_lst:
        wrd_len = len(word)
        spc_req = max_len - wrd_len
        l_spc_req = spc_req//2
        r_spc_req = l_spc_req
        if spc_req%2==1:
            r_spc_req += 1
        print('*'  + ' '*l_spc_req + word+ ' '*r_spc_req + '*')
    print('*'*str_req)

if __name__ == '__main__':
    main()


s = 'acxyqknstuva'

def remove_consequative(string):
    idx = 0
    str_len = len(string)
    new_str = ''
    while(idx<str_len-1):
        if ord(string[idx])+1 == ord(string[idx+1]):
            while(idx<str_len-1):
                if ord(string[idx])+1 == ord(string[idx+1]):
                idx += 1
                
        else:
            new_str = new_str + ch
            idx = idx + 1
    return new_str
    
s = 'this is kapil jain here'

def rev(s):
    str_lst = s.split()
    new_str_lst = []
    for sr in str_lst:
        new_str_lst.append(sr[::-1])
    return (' '.join(new_str_lst))


def isAlphabet(x): 
    return x.isalpha() or x =='-'
    
    
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
    
if __name__ == '__main__':
    #s = "We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
    s = "email-id"
    print(reverse(s))