nums=list(map(int,input("Enter the values of array: ").split()))
def quickSort(nums,low,high):
    if low<high:
        p_ind=partition(nums,low,high)
        quickSort(nums,low,p_ind-1)
        quickSort(nums,p_ind+1,high)
def partition(nums,low,high):
    pivot=nums[low]
    i,j=low,high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
quickSort(nums,0,len(nums)-1)
print(nums)