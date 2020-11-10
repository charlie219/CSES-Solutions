from collections import defaultdict as y
from heapq import heappush as push,heappop as pop
F=lambda: [int(i) for i in input().split()]
n,m=F()
g=y(dict)
ma=1e18
for i in range(m):
    a,b,c=F()
    if  b in g[a]:
        c=min(g[a][b],c)
    
    g[a][b]=c
d=[ma]*(n+1)
h=[]
d[1]=0
for i in range(1,n+1):
    push(h,[ma,i])
    
x=1
while h:
    u=pop(h)[1]
    boo=1
    for v in g[u].keys():
        if d[v]>d[u]+g[u][v]:
            b=0
            d[v]=d[u]+g[u][v]
            push(h,[d[v],v])
    if b:
        break
print(*d[1:])
