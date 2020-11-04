F=lambda:list(map(int,input().split()))
n,x=F()
d=[[0]*(x+1) for i in range(n+1)]
c=F();p=F()
for i in range(1,n+1):
    for j in range(1,x+1):
        a=d[i-1][j]
        if c[i-1]<=j:
            a=max(a,p[i-1]+d[i-1][j-c[i-1]])
        d[i][j]=a
print(d[-1][-1])
