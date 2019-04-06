print('Hello')
num=123

order=len(str(num))
sum=0

while (num>0):
    r=num%10
    num=num//10
    sum=sum + r ** order
if num == sum :
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

print("1. pull and merge test")
print("2. merge test")
print("3. rebase test")
