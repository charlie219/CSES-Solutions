t=lambda:[int(i) for i in input().split()]
n,q=t()
a=t()
s=[0]
for i in a:
    s+=[s[-1]+i]

for i in range(q):
    l,r=t()
    print(s[r]-s[l]+a[l-1])
