"""
List comprehension is a short and simple way to create a new list using a single line of code.
SYNTAX: new_list = [expression for item in iterable if condition]
"""
# nums=list(map(int,input("Enter the values of list: ").split()))
# new_list=[i for i in nums if i% 2 ==0]
# print(new_list)

"""
Given a list of marks use list comprehension to create new list that contains only the marks that are above 75
"""

marks=list(map(int,input("Enter the values of list: ").split()))
new_list=[i for i in marks if i>=75 ]
print(new_list)