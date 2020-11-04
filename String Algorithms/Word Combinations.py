import sys
sys.setrecursionlimit(1500000)
def cal(st,li):
    c=0
    for i in range(0,len(st)+1):
        temp=st[:i]
        if(st[:i] in dic):
            cal(st[i:],li+[temp])
    if(st in dic):
        ans.append(li+[st])
    
        
s=input()
n=int(input())
ans=[]
a=[input() for i in range(n)]
dic={}
for i in a: dic[i]=1
cal(s,[])

print(len(ans))
