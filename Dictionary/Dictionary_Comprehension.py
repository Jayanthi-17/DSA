""" Using a Dictionary compreshension, create a new dictionary where keys are numbers from 1 to 10 and values are their cubes 
"""
print()
cubes={i:i**3 for i in range(1,11)}
print(cubes)

print()
""" Filter Pssing Marks: Create a dictionary of subjects and there respective marks, use dictionary comprehension to generate a new dictionary that has subjects where the students scored more than 40 """
Marks={
    "Hin": 85,
    "Eng":91,
    "Maths":96,
    "Telugu":58,
    "Sci":85,
    "Soc":75, 
    "Geo":12,
    "Bio":29,
    "Comp":40
}

Marks= {sub:marks for sub,marks in Marks.items() if marks > 40}
print(Marks)
print()
""" You have two separate lists(): one containing subject names and another containing corresponding marks. Create a Dictionary that combines lists using Dictionary comprehension,mapping each subject to its marks.
"""
"""
What is zip()?

Definition (One line):

zip() combines two or more iterables (lists, tuples, etc.) element by element.

Think of it like a zipper on a bag—it joins two sides together.
"""

l1=["Hin","Tel","Eng", "Math", "Sci"]
l2=[71,62,83,42,96] 
new_dict=dict(zip(l1,l2))
print(new_dict) 
print()
#or
nw_dict={sub: mark for sub,mark in zip(l1,l2)}
print(nw_dict)