F=lambda: map(int,input().split())
n,x=F()
a=list(F())
c=[0]*(x+1)
c[0]=1
for i in a:
    for j in range(i,x+1):
        c[j]+=c[j-i]
        c[j]%=10**9+7
print(c[x])
