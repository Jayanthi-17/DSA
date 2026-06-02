nums=list(map(int,input("Enter the values: ").split()))
def is_sorted(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(is_sorted(nums))