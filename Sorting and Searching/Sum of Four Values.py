from collections import defaultdict as dc 
t=lambda:map(int,input().split())
n,x=t()
a=list(t())
d=dc(list)
for i in range(n):
    for j in range(i+1,n):
        d[a[i]+a[j]]+=[i,j]
for i in range(n-1):
    for j in range(i+1,n):
        s=a[i]+a[j]
        if x-s not in d:
            continue
        p=d[x-s]
        if p[0]!=i and p[0]!=j and p[1]!=i and p[1]!=j:
            print(i+1,j+1,p[0]+1,p[1]+1)
            exit()
print("IMPOSSIBLE")
