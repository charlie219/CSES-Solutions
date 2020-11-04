from heapq import heappop,heappush
g=[[0]*8 for i in range(8)]
x,y=map(int,input().split())
x-=1;y-=1
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
n=8
for k in range(n*n):
    h=[]
    g[y][x]=k+1
    for i in range(8):
        r=x+dx[i]
        c=y+dy[i]
        if 0<=r<n and 0<=c<n and not g[c][r]:
            t=0
            for j in range(8):
                R=r+dx[j]
                C=c+dy[j]
                if 0<=R<n and 0<=C<n and not g[C][R]:
                    t+=1
            heappush(h,(t,-i))
    if h:
        p,m=heappop(h)
        x+=dx[-m]
        y+=dy[-m]
    
for i in g:
    print(*i)
                    
