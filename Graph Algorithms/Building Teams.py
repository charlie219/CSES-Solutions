from collections import defaultdict as y,deque as dq
import sys
F=lambda:map(int,input().split())
n,m=F()
g=y(list)
for i in range(m):
    a,b=F()
    g[a]+=[b]
    g[b]+=[a]
v=[0]*(n+1)
c=[0]*(n+1)
for i in range(1,n+1):
    if v[i]:
        continue
    q=dq([[i,0]])
    v[i]=1
    while q:
        x,y=q.popleft()
        for j in g[x]:
            if v[j]:
                if c[j]==c[x]:
                    print("IMPOSSIBLE")
                    sys.exit()
            if not v[j]:
                v[j]=1
                c[j]=y^1
                q+=[[j,y^1]]
p=[i if i==1 else 2 for i in c[1:]]
print(*p)
