F={-1:0,0:1,1:1}
M=10**9+7
def c(n):
    if n in F:
        return F[n]
    k=n//2
    if n%2:
        F[n]=(c(k)*c(k+1)+c(k-1)*c(k))
    else:
        F[n]=pow(c(k),2,M)+pow(c(k-1),2,M)
    return F[n]%M
print(c(int(input())-1))
