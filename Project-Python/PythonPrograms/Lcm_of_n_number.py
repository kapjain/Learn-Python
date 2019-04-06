def nlcm(nbr_str):
    numbers = nbr_str.split(',')
    numbers = list(map(lambda x: x.strip(),numbers))
    lcm = int(max(numbers))
    while(True):
        if(numbers == list(filter(lambda x: lcm % int(x) == 0,numbers))):
            break
        lcm += 1
    return lcm

def nhcf(nbr_str):
    numbers = nbr_str.split(',')
    numbers = list(map(lambda x: x.strip(),numbers))
    maxhcf = int(min(numbers))
    min1 = 1
    while(min1<=maxhcf):
        if (numbers == list(filter(lambda x: int(x) % min1 == 0,numbers))):
            hcf = min1
        min1 += 1
    return hcf

nbr_str1 = input("enter the numbers seprated by comma's")
hcf = nhcf(nbr_str1)
print(hcf)

lcm = nlcm(nbr_str1)
print(lcm)