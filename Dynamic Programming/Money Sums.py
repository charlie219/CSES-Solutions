F=lambda:map(int,input().split())
n=F()
a=list(F())
d=[]
for i in a:
    x=[i]
    for j in dp:
        x.append(j+i)
    d.extend(x)
    d=list(set(d))
print(len(d))
print(*sorted(d))
