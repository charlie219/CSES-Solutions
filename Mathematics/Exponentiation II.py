n=int(input())
while n:
    n-=1
    x,y,z=map(int,input().split())
    m=10**9+7
    print(pow(x,pow(y,z,m-1),m))

