#ascending order
nums=[58,74,9,6,5,2,4,5,6,7,8,9]
def sel_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    print(nums)
sel_sort(nums)

#descending order
nums=[58,74,9,6,5,2,4,5,6,7,8,9]
def sel_sort(nums):
    n=len(nums)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if nums[j]>nums[max_index]:
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
    print(nums)
sel_sort(nums)