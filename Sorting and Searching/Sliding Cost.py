from sys import stdin, stdout

def input():
    return stdin.readline().rstrip()

def b(a):
    l=0
    r=k
    while(r>l+1):
        m=(l+r)//2
        if(c[m]<=a):
            l=m
        else:
            r=m
    return l

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
c=sorted(a[:k])
m=(k-1)//2
x=[c[m]]
for i in range(k,n):
    u=a[i-k]
    v=a[i]
    p=b(u)
    c[p]=v
    t=p
    while t-1>=0 and c[t]<c[t-1]:
        c[t],c[t-1]=c[t-1],c[t]
        t-=1
    while p<k-1 and c[p]>c[p+1]:
        c[p],c[p+1]=c[p+1],c[p]
        p+=1
    e=[abs(xx-c[m]) for xx in c]
    print(e)
    x+=[sum(e)]
print(*x)
    
    
