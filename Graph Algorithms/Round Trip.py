from collections import defaultdict as y
import sys
F=lambda:map(int,input().split())
n,m=F()
g=y(list)
for i in range(m):
    a,b=F()
    g[a]+=[b]
    g[b]+=[a]
v=[0]*(n+1)
t={}
for i in range(1,n+1):
    if v[i]:
        continue
    s=[i]
    v[i]=1
    while s:
        x=s.pop()
        for j in g[x]:
            if v[j]:
                print(j,x)
                a=[j,x]
                while x!=j:
                    x=t[x]
                    a+=[x]
                print(len(a))
                print(*a)
                sys.exit()
            else:
                t[j]=x
                v[j]=1
                s+=[j]
print("IMPOSSIBLE")
