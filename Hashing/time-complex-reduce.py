# proof that hasing reduces the complexity of a program
#constraints: 1)1<=n[i]<=10, 2) n can have 10**8 elements 3) m can have 10**8 elements
n=[1,2,6,4,8,6,7,9,2,4,7,5,9,6,8,7,9,3,9]
m=[85,74,6,2,4,1,3,5,9]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<0 or num>10:
        print(0)
    else:
        print(hash_list[num])