# print matrix and perform the addition between two matrix.
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print("first matrix")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
b=[[9,8,7],
   [6,5,4],
   [3,2,1]]
print("second matrix ")
for i in range(3):
    for j in range(3):
        print(b[i][j],end=" ")
    print()
print("Addition of Matrixs")
for i in range(3):
    for j in range(3):
        print(a[i][j]+b[i][j],end=" ")
    print()
