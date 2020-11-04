n=int(input())
d=[0]*(n+1)
d[0]=1
for i in range(n+1):
    for j in range(1,7):
        if(i>=j):
            d[i]=(d[i]+d[i-j])%(10**9+7)
print(d[n])
