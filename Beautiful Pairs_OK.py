# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:52:47 2021

@author: Compaq
"""

a=[3, 5, 7, 11, 5, 8]
b=[5, 7, 11, 10, 5, 8]
new_list=[]
left_a=[]
left_b=[]
for n in a:
    #for m in b:
    if n in b:
        new_list+=[n]
    if n not in new_list:
        left_a+=[n]
        #b.remove(n)

for m in b:
    if m not in new_list:
        left_b+=[m]
    

print(new_list)
print(left_a)
print(left_b)