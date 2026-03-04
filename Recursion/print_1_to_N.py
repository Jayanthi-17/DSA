# print 1 to N numbers using recursion 
#Head
def print_1_to_N (n):
    if n==0:
        return
    print_1_to_N(n-1)
    print(n)
print_1_to_N(10)

#Tail
def print_1_to_N (n,i=1):
    if i>n:
        return
    print(i)
    print_1_to_N(n,i+1)
print_1_to_N(10)