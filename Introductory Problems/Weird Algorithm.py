F=lambda x: 3*x+1 if(x%2) else x//2
a=[int(input())]
while(a[-1]!=1):
    a+=[F(a[-1])]
print(*a)
