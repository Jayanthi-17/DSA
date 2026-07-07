"""Given two lists of equal length.write a python code using loop to create a new list where each element  is the sum of the corresponding elements from both original lists.
"""
lst1=list(map(int,input("Enter the values of list1: ").split()))
lst2=list(map(int,input("Enter the values of list2: ").split()))
def Sum_of_two_lists(lst1,lst2):
    new_list=[]
    for i in range(len(lst1)):
        total=lst1[i]+lst2[i]
        new_list.append(total)
    return new_list
result=Sum_of_two_lists(lst1,lst2)
print(result)

