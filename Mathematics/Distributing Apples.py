f=[1];m=10**9+7
I=lambda a:pow(a,m-2,m)
for i in range(1,2*10**6):
    f+=[(f[-1]*i)%m]
N,M=map(int,input().split())
a=N+M-1;b=N-1
print((f[a]*I(f[b])*I(f[a-b]))%m)
