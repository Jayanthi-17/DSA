"""Write a function called square that takes a number and return its square,store the result and print it ."""
def square(num):
    return num**2
ans=square(5)
print(ans)

"""write a function called min_of_three that takes three numbers and returns the smallest without using any built in function."""
def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    return c
ans=min_of_three(5,-9,1)
print(ans)

"""Write a function called absolute_value that takes a number and returns its absolute value without using any built in function"""
def absolute_value(num):
    if num >0:
        return num
    return num*-1
ans=absolute_value(-5)
print(ans)