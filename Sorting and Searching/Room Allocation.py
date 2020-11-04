from bisect import bisect_right as br
F=input
n = int(F())
a=[[int(i) for i in F().split()]for j in range(n)]
l=[]
an=[]
r=0
for i in a:
    x,y=i
    p=br(l,x)
    if p>=r:
        l+=[y]
        r+=1
    else:
        l[p]=y
    an+=[p+1]
    print(l) 
print(*an)
