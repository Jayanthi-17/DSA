"""Given a 3x3 matrix as input, print its lower triangle . Replace all elements in the upper triangle (above the main diagonal) with *
"""

#upper row matrix 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
        if i>=j:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()

#lower row matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
        if i<=j:
            print(matrix[i][j],end=" ")
        else:
            print("*", end=" ")
    print()
print()

#diagonal matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()

#diagonal matrix 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()

#antidiagonal matrix 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
        if i+j==row-1:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()

matrix=[[1,2,3,9],[4,5,6,7],[7,8,9,8],[0,3,1,4]]
row=len(matrix)
column=len(matrix[0])
for i in range(0,row):
    for j in range(0,column):
            if (i==1 or i==2) and (j==1 or j==2):
                 print("*",end=" ")
            else:
                print(matrix[i][j],end=" ")
    print()
print()
            