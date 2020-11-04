F=lambda:[int(i) for i in input().split()]
n,m,k=F()
p=sorted(F())
a=sorted(F())
c=x=y=0
d=len(p)
f=len(a)
while 1:
    if x>=d or y>=f:
        break
    s=p[x]
    t=a[y]
    if s>t+k:
        y+=1
    elif s<t-k:
        x+=1
    else:
        c+=1
        x+=1
        y+=1
print(c)
