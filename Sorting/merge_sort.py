arr=list(map(int,input("Enter the elements of array: ").split()))
def Merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=Merge_sort(left_half)
    right_half=Merge_sort(right_half)
    def Merge_array(left,right):
        result=[]
        i,j=0,0
        n,m=len(left),len(right)
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i<n:
            while i<n:
                result.append(left[i])
                i+=1
        if j<m:
            while j<m:
                result.append(right[j])
                j+=1
        return result
    return Merge_array(left_half,right_half)
print(Merge_sort(arr))
    

def Merge_Sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=Merge_Sort(left_arr)
    right=Merge_Sort(right_arr)
    def Merge_array(left,right):
        result=[]
        i,j=0,0
        n,m=len(left),len(right)
        while i<n and j<m:
            if left[i]>right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i<n:
            while i<n:
                result.append(left[i])
                i+=1
        if j<m:
            while j<m:
                result.append(right[j])
                j+=1
        return result
    return Merge_array(left,right)
print(Merge_Sort(arr))