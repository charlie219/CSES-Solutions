n=int(input())
a=[0]*n;c=1
if(1<n<=3):
    print("NO SOLUTION")
else:
    for i in range(1,n,2):
        a[i]=c
        c+=1
    for i in range(0,n,2):
        a[i]=c
        c+=1
    print(*a)
