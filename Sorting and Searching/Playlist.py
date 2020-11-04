n=int(input())
a=[int(i) for i in input().split()]
l=0
dic={}
for i in set(a):    dic[i]=0
dic[a[0]]=1
s=0
for r in range(1,n):
    if(dic[a[r]]==1):
        while(a[l]!=a[r]):
            dic[a[l]]=0
            l+=1
        dic[a[l]]=0
        l+=1
    dic[a[r]]=1
    r+=1
    s=max(s,r-l)
print(s)
