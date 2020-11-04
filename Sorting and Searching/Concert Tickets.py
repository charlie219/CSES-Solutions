from collections import defaultdict
f=lambda:list(map(int,input().split()))
n,m=f()
h=f()
a=f();s=[]
d=defaultdict(int)
for i in h:
    d[i]+=1
h=sorted(list(d.keys()))
n=len(h)
for i in a:
    l=-1;r=n
    while(r>l+1):
        mid=(l+r)//2
        if(h[mid]<=i):
            l=mid
        else:
            r=mid
    while(d[h[l]]==0 and l>-1):
        l-=1
       
    s=h[l] if l>=0 else -1
    print(s)
    d[h[l]]-=1
