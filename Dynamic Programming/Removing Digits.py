n=int(input())
d=[10**18]*(n+1)
d[0]=0
for i in range(n+1):
    for j in set(map(int,str(i))):
        d[i]=min(d[i],d[i-j]+1)
print(d[n])
