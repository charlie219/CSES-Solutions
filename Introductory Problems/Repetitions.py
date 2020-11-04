s=input()+'+'
a=s[0];m=0;c=0
for i in s:
    if i==a: c+=1
    else:
        if c>m:    m=c
        c=1
        a=i
print(m)
        
