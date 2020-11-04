import sys
F=lambda: sys.stdin.readline().rstrip()
n=int(F())
a=c=0
for i in sorted([[int(i) for i in F().split()][::-1] for j in range(n)]):
    y,x=i
    if x>=a:
        a=y
        c+=1
print(c)
        
