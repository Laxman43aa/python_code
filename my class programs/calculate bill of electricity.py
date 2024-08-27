bill=0
unit=int(input("enter the unit "))
totalbill=0
if (unit<=100):
    bill= unit*3
    print("bill = ",bill)
elif(unit<=150):
     bill=unit * 5
     print("bill = ",bill)
elif(unit>150):
    bill=unit*15
print("the total bill of units = ",bill)
    
