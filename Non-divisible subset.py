from itertools import combinations
n = 4
k = 7
S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
list_=combinations(S, 2)
list_=list(list_)
results=[]
for a in list_:
    if (a[0]+a[1])%k!=0:
        results+=[a[0]]
        results+=[a[1]]
final_results=len(set(results))


print(list_)