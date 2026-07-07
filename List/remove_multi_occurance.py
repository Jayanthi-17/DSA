"""
Given a list of numbers (which may contain duplicates) , write a python script that takes an interger as input from the user and removes all occurances of that interger from the list.
"""
nums=list(map(int,input("Enter the values of list: ").split()))
#changes in new list
def remove_target_occurance(nums,target):
    new_list=[]
    for i in range(len(nums)):
        if nums[i]!=target:
            new_list.append(nums[i])
    return new_list
result=remove_target_occurance(nums,2)
print(result)

#changes in original
def remove_target_occurance(nums,target):
    while target in nums:
        nums.remove(target)
    return nums
result=remove_target_occurance(nums,2)
print(result)

        