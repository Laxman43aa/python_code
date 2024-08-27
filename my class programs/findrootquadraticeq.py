import math
D=("as a variable to store values qe ")
a=int(input("enter the a of quadratic equation "))
b=int(input("enter the b of quadratic equation "))
c=int(input("enter the c of quadratic equation "))
x=float
y=float
D= b * b - 4 * a * c 
sqrt_val=math.sqrt(D)
print(D)
if(D<0):
    print("no roots and root is imagenary ")

if(D==0):
    print("root is equal ")
    x=-b/(2.0*a)
    print("equal = ",x)

if(D>0):
    print("root is distinct")
    x=(-b+(sqrt_val))/(2.0*a)
    y=(-b-(sqrt_val))/(2.0*a)
    print("Distinct = ",x)
    print("Distinct = ",y)
    print(" roots are real number ")
    
    
    
