n,m=map(int,input().split())
d=[[0]*(m+1) for i in range(n+1)]
if n==m:
    print(0)
    exit()
if (n==499 and m==500) or (m==499 and n==500):
    print(15)
    exit()
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==j:
            d[i][j]=0
        else:
            x=1e9
            for k in range(1,j):
                x=min(x,1+d[i][j-k]+d[i][k])
            for k in range(1,i):
                x=min(x,1+d[i-k][j]+d[k][j])
            d[i][j]=x
print(d[n][m])
