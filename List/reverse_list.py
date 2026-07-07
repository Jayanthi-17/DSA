"""
Reverse a list without using .reverse() or [::-1]
"""

nums=list(map(int,input("Enter the values of list: ").split()))

def reverse_list(nums):
    n=len(nums)
    for i in range(n//2):
        j=n-1-i
        nums[i],nums[j]=nums[j],nums[i]
    return nums
reverse_list(nums)
print(nums)

def reverse_list(nums):
    new_list=[]
    n=len(nums)
    for i in range(n-1,-1,-1):
        val=nums[i]
        new_list.append(val)
    return new_list
result=reverse_list(nums)
print(result)