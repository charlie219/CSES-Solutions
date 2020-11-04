m=10**9+7
F=[[16],[8],[4],[2],[1],[1]]
A=[[1]*6]
for i in range(1,6):
    A+=[[0]*(i-1)+[1]+[0]*(6-i)]
def mul(A,B):
    return [[sum(A[i][k] * B[k][j] for k in range(6))%m for j in range(len(B[0]))] for i in range(len(A))]

def p(A,n):
    R=[[1]*6 for i in range(6)]
    while n:
        if n&1:
            R=mul(R,A)
        n//=2
        A=mul(A,A)
    return R

n=int(input())
if n<6:
    print(F[-n-1][0])
else:
    M=p(A,n-6)
    print(mul(M,F)[0][0]%m)

