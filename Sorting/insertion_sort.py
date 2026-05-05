arr=list(map(int,input("Enter the values to be sorted: ").split()))
def Insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while arr[j]>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(Insertion_sort(arr))