import sys
def input():
    return sys.stdin.readline().rstrip()
from collections import defaultdict as y,deque as dq
F=lambda:map(int,input().split())
n,m=F()
g=y(list)
t={}
for i in range(m):
    a,b=F()
    g[a]+=[b]
    g[b]+=[a]
v=[0]*(n+1)
q=dq([1])
while q:
    x=q.popleft()
    if x==n:
        p=[n]
        x=n
        while x!=1:
            x=t[x]
            p.append(x)
        print(len(p))
        print(*p[::-1])
        sys.exit()
    for j in g[x]:
        if v[j]:
            continue
        t[j]=x
        v[j]=1
        q.append(j)
            
print('IMPOSSIBLE')
