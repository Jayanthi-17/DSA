"""
Prrint the largest element in the list without using in-built max()
"""
nums=list(map(int,input("Enter the values of list: ").split()))
max=nums[0]
for i in range(len(nums)):
    if nums[i]>max:
        max=nums[i]
print(max)
