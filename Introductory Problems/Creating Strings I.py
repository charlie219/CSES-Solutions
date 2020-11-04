from itertools import permutations as per
s=sorted(list(map("".join,set(per(input()))))
print(len(s),*s,sep='\n')
