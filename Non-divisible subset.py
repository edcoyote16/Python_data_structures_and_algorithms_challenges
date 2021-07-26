from itertools import combinations
n = 4
k = 3
S = [1, 7, 2, 4]
list_=combinations(S, 2)
list_=list(list_)
results=[]
for a in list_:
    if (a[0]+a[1])%k!=0:
        results+=[a[0]]
        results+=[a[1]]
final_results=len(set(results))


print(list_)