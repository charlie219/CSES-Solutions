f=[1];m=10**9+7
I=lambda a:pow(a,m-2,m)
for i in range(1,10**6+1):
    f+=[(f[-1]*i)%m]
s=input()
a=f[len(s)]
for i in range(26):
    x=s.count(chr(97+i))
    if(x>1):
        a=(a*I(f[x]))%m
print(a)
