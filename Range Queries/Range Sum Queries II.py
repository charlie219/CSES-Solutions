import os
import sys
from io import BytesIO, IOBase
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

class Seg:
    def __init__(self,n,arr):
        self.size=1
        while(self.size<n):
            self.size*=2
        self.seg=[0]*(2*self.size)
        for i in range(n):
            self.seg[self.size-1+i]=arr[i]
        temp=self.size//2-1
        while(temp>=0):
            for i in range(temp,2*temp+1):
                self.seg[i]=self.seg[2*i+1]+self.seg[2*i+2]
            temp=(temp+1)//2-1

            
    def update(self,x,y):
        pos=self.size-1+x
        self.seg[pos]=y
        temp=(pos-1)//2
        while(temp>=0):
            self.seg[temp]=self.seg[2*temp+1]+self.seg[2*temp+2]
            temp=(temp-1)//2

            
    def find(self,x,lx,rx,l,r):
        if(rx<=l) or (lx>=r):
            return 0
        if(l<=lx and rx<=r):
            return self.seg[x]
        ans=0;mid=(lx+rx)//2
        ans+=self.find(2*x+1,lx,mid,l,r)+self.find(2*x+2,mid,rx,l,r)
        return ans
F=lambda:[int(i) for i in input().split()]        
n,q=F()
a=F()
st=Seg(n,a)
for _ in range(q):
    t,x,y=F()
    if(t==1):
        st.update(x-1,y)
    else:
        #print(st.seg)
        print(st.find(0,0,st.size,x-1,y))
