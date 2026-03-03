# stores the frequency of a number in Dictionary
nums=[5,8,4,7,9,6,9,6,7,5,9,6,2,4,2,5,3,6,1,7,9,9]
freq_map=dict()
for i in range (0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map[9])


# other easy method
nums=[5,8,4,7,9,6,9,6,7,5,9,6,2,4,2,5,3,6,1,7,9,9]
hash_map=dict()
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1 #in one line we can do using get very simple and efficient 
print(hash_map[6])