input()
a=[int(i) for i in input().split()]
s=0
for i in range(1,len(a)):
    if(a[i-1]>a[i]):
        s+=a[i-1]-a[i]
        a[i]=a[i-1]
print(s)
    
