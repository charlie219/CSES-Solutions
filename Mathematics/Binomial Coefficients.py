f=[1];m=10**9+7
I=lambda a:pow(a,m-2,m)
for i in range(1,10**6+10):
    f+=[(f[-1]*i)%m]
for _ in range(int(input())):
    a,b=map(int,input().split())
    print((f[a]*I(f[b])*I(f[a-b]))%m)
