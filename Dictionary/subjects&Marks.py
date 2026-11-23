"""
Create a dictionary of 6 subjects a nd their respective marks .Print the subject with the highest marks and lowest marks using max() and min() functions alongside with lambda
"""

Marks={
    "Hin": 85,
    "Eng":91,
    "Maths":96,
    "Telugu":58,
    "Sci":85,
    "Soc":75
}
ans=dict(sorted(Marks.items(),key=lambda x:x[1] ))
print(f"Highest Marks= {ans[list(ans)[-1]]}")
print(f"Lowest Marks= {ans[list(ans)[0]]}")

#or
Highest=max(Marks.values())
Lowest=min(Marks.values())
print(f"Highest Marks={Highest}")
print(f"Lowest Marks={Lowest}") 

#Best
Highest=max(Marks,key = lambda x: Marks[x])
Lowest=min(Marks,key = lambda x: Marks[x])
print(f"Highest Marks : {Highest}-> {Marks[Highest]}")
print(f"Lowest Marks : {Lowest}-> {Marks[Lowest]}") 