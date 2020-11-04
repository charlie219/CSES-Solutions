pri={};prime=[]
def Sieve():
    n=1000000
    prim=[True for i in range(n + 1)] 
    p=2
    while(p*p<=n): 
        if(prim[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prim[i] = False
        p += 1
    prim[0]= False
    prim[1]= False
    for p in range(n + 1): 
        if prim[p]: 
            pri[p]=1
            prime.append(p)
Sieve()

def prime_factors(n):
    ans=[]
    for i in prime:
        c=0
        if(n==1):
            break
        while(n%i==0):
            n//=i
            c+=1
        if(c>0):
            ans.append(c)
        if(n in pri.keys()):
            ans.append(1)
            break
    return ans

def count_fact(n):
    li=prime_factors(n)
    count=1
    for i in li:
        count*=(1+i)
    return int(count)

for _ in range(int(input())):
    n=int(input())
    print(count_fact(n))
    
