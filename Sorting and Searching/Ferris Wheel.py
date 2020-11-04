t=lambda:map(int,input().split())
n,x=t()
a=sorted(t())
l=s=0
r=n-1
while r>=l:
    if a[l]+a[r]<=x:
        l+=1
    s+=1
    r-=1
print(s)
