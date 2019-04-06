org_nbr = 123
rev_nbr = 0
while(org_nbr>0):
    rev_nbr  = rev_nbr * 10 + (org_nbr % 10)
    org_nbr = org_nbr // 10
print(rev_nbr)

org_nbr = input("enter a nbr : ")
print(org_nbr[::-1])
print(reversed(org_nbr))