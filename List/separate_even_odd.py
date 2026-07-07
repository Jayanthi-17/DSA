"""
Separate the list of intergers into two distinct lists: One containing all the even numbers and the other containing all the odd numbers.
"""
nums=list(map(int,input("Enter the values of list: ").split()))

def Separate_Even_Odd_List(nums):
    even_list=[]
    odd_list=[]
    for i in range(len(nums)):
        if nums[i]%2==0:
            even_list.append(nums[i])
        else:
            odd_list.append(nums[i])
    return even_list,odd_list
Even,odd=Separate_Even_Odd_List(nums)
print(f"Even list: {Even}")
print(f"Odd list: {odd}")