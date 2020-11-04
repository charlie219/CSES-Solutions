from sys import stdin, stdout

def input():
    return stdin.readline().rstrip()
from collections import deque
n,m=[int(i) for i in input().split()]
a=[list(input()) for i in range(n)]
R=[0,0,-1,1]
C=[1,-1,0,0]
s=[(X, Y) for X in range(n) for Y in range(m) if a[X][Y] == 'A']
q=deque(s)
t=''
d={}
while(q):
    x,y=q.popleft()
    if a[x][y]=='B':
        while([(x,y)]!=s):
            r,c=d[(x,y)]
            if x-r:
                t+='D' if x-r==1 else 'U'
            if y-c:
                t+='R' if y-c==1 else 'L'
            x,y=r,c
        break
    a[x][y]='#'
    for i in range(4):
        r=x+R[i]
        c=y+C[i]
        if 0<=r<n and 0<=c<m and a[r][c]!='#':
            d[(r,c)]=[x,y]
            q+=[[r,c]]
if len(t)==0:
    print('NO')
else:
    print('YES')
    print(len(t))
    print(t[::-1])
    
