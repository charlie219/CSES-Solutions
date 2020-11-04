F= lambda :map(int,input().split())
n,x=F()
a=sorted(F())
c,l=[1],0
for i in range(x+1):
    c+=[0]
    for j in a[l:]:
        if i<j:
            l-=1
        else:
            c[i]=(c[i]+c[i-j])%(10**9+7)            
print(c[x])
