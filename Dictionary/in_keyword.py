"""
Construct a Dictionary containing four product names and their prices . Prompt the user to enter a product name . Use the in keyword to check if it exists , if so display its price else print product not available
"""

Products={
    "TV":85000,
    "REMOTE":4000,
    "AC":96000,
    "MOBILE": 41000
}
ur_product=input("Enter the name of the product: ").upper()
for i in Products:
    if ur_product in Products:
        print(f"The price of {ur_product} is {Products[i]}")
        break
else:
    print("Product not found")