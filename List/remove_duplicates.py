"""
Given a list, remove all the duplicate  elements while preserving the original order of the unique items
"""
nums=list(map(int,input("Enter the values of list: ").split()))
new_list=[]
def remove_duplicates(nums):
    n=len(nums)
    for i in range(n):
        if nums[i] not in new_list:
            new_list.append(nums[i])
    return new_list

result=remove_duplicates(nums)
print(result)