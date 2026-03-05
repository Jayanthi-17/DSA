#To print the factorial of a number
n=int(input("Enter the factoaial number: "))
def Fact(res,i,n):
    if i>n:
        print(res)
        return
    Fact(res*i,i+1,n)
Fact(1,1,n)


