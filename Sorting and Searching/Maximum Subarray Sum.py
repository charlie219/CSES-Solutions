input()
a=list(map(int,input().split()))
x=-10e9
y=0
for i in a:
    y+=i
    if x<y: x=y
    if(y<0):    y=0
print(x)
