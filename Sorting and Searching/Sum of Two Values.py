from collections import defaultdict
n,x=map(int,input().split())
a=[int(i) for i in input().split()]
d=defaultdict(list)
for i in range(n):
    d[a[i]]+=[i+1]
b=[]
for i in d.keys():
    if x-i==i:
        if len(d[i])>1:
            b=[d[i][0],d[i][1]]
        continue
    if x-i in d:
        b=[d[i][0],d[x-i][0]]
        break
if b==[]:
    print("IMPOSSIBLE")
else:
    print(*b)
