from collections import defaultdict as t
F=lambda:[int(i) for i in input().split()]
n,x=F()
a=F()
d=t(int)
s=0
c=0
for i in a:
    s+=i
    if s==x:    c+=1
    if s-x in d:
        c+=d[s-x]
    d[s]+=1
print(c)
