#To check whether the String is a Palindrome or not with recursion
S=input("Enter the text: ")     
def palin_strg(S,left,right):
    if left>=right:
        return True 
    if S[left]!=S[right]:
        return False
    return palin_strg(S,left+1,right-1)
print(palin_strg(S,0,len(S)-1))
    

# using while loop
S=input("Enter the text: ") 
left=0
right=len(S)-1
while left<right:
    if S[left]!=S[right]:
        print(False)
        break
    left+=1
    right-=1
else:
    print(True)
   
