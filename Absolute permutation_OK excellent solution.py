# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:08:47 2021

@author: Edgar
"""

n=8
k=2
# results=[]
# bag=list(range(1,n+1))
# for index, element in enumerate(range(1,n+1)):
#     for my_bag in bag:
#         if abs(my_bag-element)==k:
#             results+=[my_bag]
#             bag.remove(my_bag)
#             #bag.sort(reverse=True)
# if len(results)==n:
#     print (results)
# else:
#     print ([-1])
#2 1 4 3 6 5 8 7 10 9

def max_permutation(n, k):
    #array = [x for x in range(1, n+1)]
    out = []
    switch = k
    if k == 0:
        return [x for x in range(1, n+1)]
    
    if n % (2*k) != 0:
        return [-1]
        
    for pos in range(1, n + 1):
        out.append(pos + switch)
        
        if pos % k == 0:
            switch *= -1
    return out
max_permutation(n, k)
