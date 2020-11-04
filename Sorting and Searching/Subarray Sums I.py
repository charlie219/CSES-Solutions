F=lambda:[int(i) for i in input().split()]
n,x=F()
a=F()
c=l=0
s=a[l]
r=1
while l<=r<=n:
    if s>=x:
        if s==x:    c+=1
        s-=a[l]
        l+=1
    elif r<n:
        s+=a[r]
        r+=1
    else:
        break
print(c)
