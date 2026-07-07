"""write a program that takes list and a target number . Use a loop to determine if the target element exist in list."""


nums=list(map(int,input("Enter the values of list: ").split()))
target=int(input("Enter the target number: "))

for i in range(len(nums)):
    if nums[i]==target:
        print(f"The number {target} is present at index {i}")
        break
else:
        print(f"The number {target} is not present in the list")


def does_target_exists(lst,target):
     for i in range(len(nums)):
          if nums[i]==target:
               return True
     return False
print(does_target_exists(nums,target))
          