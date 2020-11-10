n=input()
s=['A','C','G','T']
m=len(n)
c=''
for i in s:
    x=n.count(i)
    if m>x:
        m=x
        c=i
print(c*(m+1))
