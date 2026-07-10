"""
Create a Dictionary for students including keys like name,age,city and marks(As a list of score) . Print each piece of info using its key
"""

Student={
    "Name":"John",
    "Age":32,
    "City": "Hyderabad",
    "Marks": [42,85,96,79,86]
}
for i in Student:
    print(f"{i} is {Student[i]}")