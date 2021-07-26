from itertools import combinations
n = 5
k = 5
#S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
#S=[422346306, 940894801, 696810740, 862741861, 85835055, 313720373]
S=[2, 7, 12, 17, 22]
from collections import Counter
def nonDivisibleSubset(a):
    c = Counter((i%k for i in a))
    count = 0
    blacklist = set()
    for x,y in c.most_common():
        if x == k/2 or x==0:
            count+=1
        elif k-x not in blacklist:
            count+=y
            blacklist.add(x)
    return count

#n,k = map(int,input().split())
#a = list(map(int,input().split()))
print(nonDivisibleSubset(S))


#print(final_results)