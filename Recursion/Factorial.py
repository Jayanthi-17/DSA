#To print the factorial of a number
# n=int(input("Enter the factoaial number: "))
# def Fact(res,i,n):
#     if i>n:
#         print(res)
#         return
#     Fact(res*i,i+1,n)
# Fact(1,1,n)

# age=int(input("enter a number: "))
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}')