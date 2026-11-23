"""
Create a dictionary mapping five countries to their capital cities. Iterate through this dictionary using items() method and print each pair in format: country -> Capital 
"""
Country_Capital = {
    "India": "New Delhi",
    "Germany":"Berlin",
    "Japan":"Tokyo",
    "Brazil":"Brasilia",
    "France":"Paris"
}
for i,j in Country_Capital.items():
    print(f"{i}->{j}")