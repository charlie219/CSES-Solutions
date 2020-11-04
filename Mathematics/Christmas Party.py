a=0
b=1
for i in range(int(input())):    a,b=b,(a+b)*i%(10**9+7)
print(b)
