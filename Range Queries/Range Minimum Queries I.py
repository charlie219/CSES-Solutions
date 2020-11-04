from sys import stdin, stdout
import sys
range = xrange
input = raw_input
def input():
    return stdin.readline().rstrip()
class Seg:
    def __init__(self,n,arr):
        self.size=1
        self.MAX=10e9
        while(self.size<n):
            self.size*=2
        self.seg=[self.MAX]*(2*self.size)
        for i in range(n):
            self.seg[self.size-1+i]=arr[i]
        temp=self.size//2-1
        while(temp>=0):
            for i in range(temp,2*temp+1):
                self.seg[i]=min(self.seg[2*i+1],self.seg[2*i+2])
            temp=(temp+1)//2-1
            
    def find(self,x,lx,rx,l,r):
        if(rx<=l) or (lx>=r):
            return self.MAX
        if(l<=lx and rx<=r):
            return self.seg[x]
        ans=0;mid=(lx+rx)//2
        ans+=min(self.find(2*x+1,lx,mid,l,r),self.find(2*x+2,mid,rx,l,r))
        return ans
       
n,q=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
st=Seg(n,a)
for _ in range(q):
    x,y=[int(i) for i in input().split()]
    x-=1
    print st.find(0,0,st.size,x,y)
