""" Given two lists merge them into single new list without modifying the originals"""
lst1=list(map(int,input("Enter the values of list1: ").split()))
lst2=list(map(int,input("Enter the values of list2: ").split()))
new_list=lst1+lst2
print(new_list)