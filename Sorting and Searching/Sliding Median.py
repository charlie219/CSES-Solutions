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
    return r
 
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
c=sorted(a[:k])
m=(k-1)//2
x=[c[m]]
print(c)
for i in range(k,n):
    u=a[i-k]
    v=a[i]
    p=b(u)
    q=b(v)
    print(p,q)
    if p>q:
        c=c[:q]+[v]+c[q:p-1]+c[p:]
    else:
        c=c[:p-1]+c[p:q]+[v]+c[q:]
    print(c)
    x+=[c[m]]
print(*x)
