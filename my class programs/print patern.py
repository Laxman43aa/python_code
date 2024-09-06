#   1
#   2 4
#   3 6 9
#   4 8 12 16
#   5 10 15 20 25
#   6 12 18 24 30 36  print this patern in python.
row=6
for i in range(1,row+1,1):
    for j in range(1,i+1,1):
        s=i*j
        print(s,end=' ')
    print()