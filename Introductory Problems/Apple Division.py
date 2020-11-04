n=int(input())
a=[int(i) for i in input().split()]
s=10**18
for i in range(2**n):
    x=bin(i)[2:];c=0
    x='0'*(n-len(x))+x
    for i in range(n):
        c+=a[i] if x[i]=='1' else -a[i]
    s=min(s,abs(c))

print(s)
