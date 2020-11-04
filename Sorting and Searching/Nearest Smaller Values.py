T=input
n=int(T())
a=[int(i) for i in T().split()]
s=[-1]
for i in range(1,n):
    t=i-1
    while t>=0:
        if a[t]>=a[i]:
            t=s[t]
        else:
            break
    s+=[t]
print(*[i+1 for i in s])
