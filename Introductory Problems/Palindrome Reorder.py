n=input()
l=[];a=[];z=''
for i in set(n):
    c=n.count(i)
    l+=[i]*(c%2)
    a+=[i]*(c//2)
if(len(l)>1):  z='NO SOLUTION'
else:   z="".join(a+l+a[::-1])
print(z)
