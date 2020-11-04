input()
a=sorted([int(i) for i in input().split()])
x=a[len(a)//2]
print(sum(abs(x-i) for i in a))
