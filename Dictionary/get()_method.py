"""
Define a Dictionary with five subjects and their respectives marks .Utilize the get() method to try accessing a subject that is not in the dictionary , ensuring it prints "Not Available as default"
"""

Marks={
    "Hin": 85,
    "Eng":91,
    "Maths":96
}
print(Marks.get("Telugu","Not Available"))
