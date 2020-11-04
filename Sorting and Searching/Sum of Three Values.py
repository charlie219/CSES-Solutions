from collections import defaultdict as dc 
t=lambda:map(int,input().split())
n,x=t()
a=list(t())
d=dc(list)
for i in range(n):
    d[a[i]]+=[i+1]
for i in d:
    for j in d:
        a=b=0
        k=x-i-j
        if k not in d:
            continue
        
        if i==k:
            if len(d[i])==1:
                continue
            b=1
        if j==k:
            if len(d[j])==1:
                continue
            b=1
        if i==j:
            if len(d[i])==1 or (len(d[i])==2 and i==k):
                continue
            elif i==k:
                b=2
            a=1
                
        print(d[i][0],d[j][a],d[k][b])
        exit()
print("IMPOSSIBLE")
