I=[0,0,1,-1];M=['R','L','D','U']
J=[1,-1,0,0]
def dfs(m,x,y):
    global ans
    if(x==n-1 and y==0):
        if(m==n*n-1):
            ans+=1
        return 1

    for i in range(4):
        r=x+I[i]
        c=y+J[i]
        if(0<=r<n and 0<=c<n and not visited[r][c]):
            visited[r][c]=1
            dfs(m+1,r,c)
            visited[r][c]=0
    return 1
s=input()
n=7
visited=[[0]*n for i in range(n)]
visited[0][0]=1
ans=0
dfs(0,0,0)
print(ans)
