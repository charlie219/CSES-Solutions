from collections import defaultdict as t
F=input
n=int(F())
a=[int(i) for i in F().split()]
d=t(int)
s=0
c=0
for i in a:
    s+=i
    if s%n==0:    c+=1
    if s%n in d:
        c+=d[s%n]
    d[s%n]+=1
print(c)
