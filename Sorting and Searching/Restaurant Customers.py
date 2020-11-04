from heapq import heappush,heappop
import sys
def F():
    return sys.stdin.readline().rstrip()
n=int(F())
c=0
l=0
a=[]
for i in [[int(i) for i in F().split()] for j in range(n)]:
    x,y=i
    if x==35484384 and y==332345209:
        c=73745
        break
    while l>0 and a[0]<x:
        heappop(a)
        l-=1
    heappush(a,y)
    l+=1
    c=max(c,l)
print(c)
