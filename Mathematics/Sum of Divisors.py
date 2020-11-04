def cal(n):
    ans=0;a=0
    if(n!=1):
        x=1;a=0
        if(n<=10):
            if(n>=7):
                ans+=2
                return ans
            if(n>=4):
                ans+=1
                return ans
            return ans
    
        while(n>=x):
            x*=10
            a+=1
        ans+=2**(a)-2
    b=1
    print(n,a)
    if(int(str(n)[0])>=7):
       b*=2
    elif(int(str(n)[0])>=4):
        b*=1
    else:
        b=0
    ans+=b*(2**a)
    return ans
for _ in range(int(input())):
    l,r=map(int,input().split())
    x,y=1,1
    a,b=0,0
    print(cal(r),cal(l))
    
