"""
Given a list of numbers , use a loop to calculate and print their average. you can also len() to get the count of elements , but avoid using sum() for total.
"""
nums=list(map(int,input("Enter the values of list: ").split()))
def get_average(lst):
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
    return sum/len(nums)
print(get_average(nums))