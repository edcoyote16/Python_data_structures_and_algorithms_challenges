# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:35:51 2021

@author: Compaq
"""
n=11
#def find_number(n):
three = n//3

while (n - 3*three)%5 != 0:
    print((n - 3*three))
    print((n - 3*three)%5)
    #
    three -= 1
    
if three > 0:
    res = [5] * 3 * three
    res += [3] * (n - 3*three)
elif three == 0 and n%5 == 0:
    res = [3] * n
else:
    res = [-1]
    
print(res)
    #return res
    