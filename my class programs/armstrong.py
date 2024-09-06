#write a program in python to check number is armstrong or not.
a=int(input("enter the number"))
b=a
l=0
while(a>0):
    c=a%10
    l=c*c*c+l
    a=a//10
if(b==l):
    print("number is armstrong")
else:
    print("number is not armstrong")