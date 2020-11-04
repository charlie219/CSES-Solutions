for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    if(a==0 and b==0):
        print('YES')
        continue
    x=(2*a-b)//3;y=(2*b-a)//3
    ans='YES' if(abs(2*a-b)%3==0 and abs(2*b-a)%3==0) and x>=0 and y>=0 else 'NO'
    print(ans)
