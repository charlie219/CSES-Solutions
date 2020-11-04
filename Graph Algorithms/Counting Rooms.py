n,m=map(int,input().split())
a=[list(input()) for i in range(n)]
o=0
R=[0,0,-1,1]
C=[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if a[i][j]=='.':
            o+=1
            s=[(i,j)]
            while(s):
                x,y=s.pop()
                a[x][y]='#'
                for k in range(4):
                    r=x+R[k]
                    c=y+C[k]
                    if 0<=r<n and 0<=c<m and a[r][c]=='.':
                        s+=[(r,c)]
print(o)
                
