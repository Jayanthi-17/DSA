# reverse an array with recursion
nums=[5,8,9,6,7,4,8,9,3,2,15,3]
def rev_arr(nums,L,R):
    if L>=R:
        return
    nums[L],nums[R]=nums[R],nums[L]
    rev_arr(nums,L+1,R-1)
rev_arr(nums,0,len(nums)-1)
print(nums)


#without recursion 
nums=[5,8,9,6,7,4,8,9,3,2,15,3]
L=0
R=len(nums)-1
while L<R:
    nums[L],nums[R]=nums[R],nums[L]
    L+=1
    R-=1
print(nums)

