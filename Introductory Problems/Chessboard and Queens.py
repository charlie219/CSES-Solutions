def n_queens(x,a):
    global ans
    if(x==n):
        ans+=1
        return 1
    r=x+1
    for c in range(1,n+1):
        if((c not in C) and ((r+c) not in dig1) and ((r-c) not in dig2) and grid[r-1][c-1]=='.'):
            C[c]=0
            dig1[r+c]=0;dig2[r-c]=0
            #print("-->",dig1,dig2,C,r,c)
            n_queens(x+1,a+[c])
            del dig1[r+c];del C[c]
            del dig2[r-c]
ans=0
grid=[input() for i in range(8)]
dig1={};dig2={};C={}
n=8
n_queens(0,[])
print(ans)
