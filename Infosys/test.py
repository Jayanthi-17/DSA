arr = list(map(int,input("Enter the values of array: ").split()))


def rev(left,right):
   if left>=right:
      return
   arr[left],arr[right]=arr[right],arr[left]
   rev(left+1,right-1)
rev(0,len(arr)-1)
print(arr)