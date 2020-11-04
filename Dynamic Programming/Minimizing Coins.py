F=lambda: map(int,input().split())
n,x=F()
a=list(F())
d=[10**9]*(x+1)
d[0]=0
for i in a:
    for j in range(i,x+1):
        d[j]=min(d[j],d[j-i]+1)
if d[x]==10**9:
    d[x]=-1
print(d[x])
