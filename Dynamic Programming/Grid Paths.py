n=int(input())
g=[input() for i in range(n)]
a=[[0]*n for i in range(n)]
a[0][0]=1
for i in range(n):
    for j in range(n):
        if i:  a[i][j]+=a[i-1][j]
        if j:  a[i][j]+=a[i][j-1]
        if(g[i][j]=='*'):   a[i][j]=0

print(a[-1][-1]%(10**9+7))
