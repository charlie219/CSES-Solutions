F=lambda:[int(i) for i in input().split()]
n,t=F()
a=F()
l=0
r=sum(a)+1
x=max(a)
while r>l+1:
    m=(l+r)//2
    c=0;s=0
    for i in a:
        if s+i>=m:
            c+=1
            s=0 if s+i==m else i
        else:
            s+=i
    c+=1 if s>0 else 0
    if c<=t and x<=m:
        r=m
    else:
        l=m
print(r)
