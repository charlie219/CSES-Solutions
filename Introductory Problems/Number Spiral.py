for _ in range(int(input())):
    y,x=map(int,input().split())
    a=max(y,x);b=x+y-a-1
    if(a%2==0 and x==a) or (a%2==1 and y==a):
        a-=1;b=-b-1
    print(a*a-b)
