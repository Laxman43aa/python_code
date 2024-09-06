#write a program in python to check number is palindrom or not.
a=int(input("enter the number"))
b=a
l=0
while(a>0):
    c=a%10
    l=l*10+c
    a=a//10
if(b==l):
    print("number is palindrom")
else:
    print("number is not palindrom")