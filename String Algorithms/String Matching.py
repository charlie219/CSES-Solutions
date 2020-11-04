t = input()
s = input()
n = len(s)
 
s = s + '$' + t
p = [0] * len(s)
r = 0
for i in range(1, len(s)):
    k = p[i - 1]
    while k > 0 and s[i] != s[k]:
        k = p[k - 1]
    p[i] = k + (s[i] == s[k])
    if p[i] == n: r += 1
print(r)
