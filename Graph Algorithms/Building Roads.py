from collections import defaultdict as y
F=lambda:map(int,input().split())
n,m=F()
g=y(list)
for i in range(m):
    a,b=F()
    g[a]+=[b]
    g[b]+=[a]
v=[0]*(n+1)
c=0
t=[]
for i in range(1,n+1):
    if not v[i]:
        c+=1
        t+=[i]
        s=[i]
        v[i]=1
        while s:
            x=s.pop()
            for j in g[x]:
                if not v[j]:
                    s+=[j]
                    v[j]=1
print(c-1)
a,b=0,1
while b<c:
    print(t[a],t[b])
    a,b=b,b+1


