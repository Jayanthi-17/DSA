"""
*
* *
* * *
* * * *
* * *
* *
*
"""

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 
1 2 
1 
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

"""
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
for i in range(2,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()