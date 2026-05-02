'''You are given a string "number" representing a positive integer and a character digit . Return the resulting string after removing the exactly one occurance of digit from number such that the value of resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in the number.
'''

n=str(input("Enter the number: "))
d=str(input("Enter the digit: "))
ans=[]

for i in range(len(n)):
    if n[i]==d:
        t= n[:i]+n[i+1:]
        ans.append(int(t))
print(str(max(ans)))