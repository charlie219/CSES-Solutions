n=int(input())
a=[int(i) for i in input().split()]
d=[a[0]]
for i in range(1,n):
    x=a[i]
    if x>d[-1]: d+=[x]
    elif d[0]>=x:    d[0]=x
    else:
        l,r=0,len(d)
        while(r>l+1):
            m=(l+r)//2
            if(d[m]<x): l=m
            else:   r=m
        d[r]=x
print(len(d))        
