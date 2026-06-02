#Bruteforce method- time complexity : O(NlogN), SC: o(1)
nums=list(map(int,input("Enter the values: ").split()))
n=len(nums)
nums.sort()
print(nums[n-2])

#Efficient method- time complexity : O(N+N), SC: o(1)
largest=float('-inf')
second_largest=float('-inf')
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
for i in range(0,n):
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
print(second_largest)

#Efficient method- time complexity : O(N), SC: o(1)
largest=second_largest=float('-inf')
second_largest=float('-inf')
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        second_largest=largest
        largest=nums[i]
    elif nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
print(second_largest)

    


          