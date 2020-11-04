
n=int(input())
sum=n*(n+1)//2
if(sum%2):
    print('NO')
else:
    c=sum//2
    ans1=[]
    tem=n+1
    if(n%2==1):
        c-=n
        ans1=[n]
        tem-=1
    i=1
    while(c>0):
        ans1.extend([tem-i,i])
        c-=tem
        i+=1
    ans2=[ii for ii in range(i,tem-i+1)]
    print('YES')
    l=tem-2*i+1
    print(l)
    print(*ans2)
    print(n-l)
    print(*ans1)
    
    
