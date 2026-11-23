"""Take an Email as input. Validate the input that contains atleast one "@" and atleast one . print valid or invalid"""

Email=input("Enter your Email: ")
if Email.count("@")==1 and "." in Email:
    print("Valid Mail")
else:
    print("Invalid Mail")
    
