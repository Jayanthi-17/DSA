nums=list(map(int,input("Enter the values: ").split()))
key=nums[0]
for i in range(0,len(nums)):
    if nums[i]>key:
        key=nums[i]
print(f'Largest number in an array:  "{key}"')