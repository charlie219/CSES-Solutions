from bisect import bisect_right as br
F=input
n = int(F())
a=[int(i) for i in F().split()]

l=[]
r=0
for i in a:
     p=br(l,i)
     if p>=r:
         l+=[i]
         r+=1
     else:
        l[p]=i
print(r)
