from collections import Counter

s='aaabbbb'
s=Counter(s)
#a=Counter(s.values())
results=[]
for n in s.values():
    if n%2!=0:
        results+=[n%2]
if not results or len(results)==1:
    print('YES')
else:
    print('NO')
