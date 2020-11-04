n=int(input())
while n:
    n-=1
    print(pow(*map(int,input().split()),10**9+7))

