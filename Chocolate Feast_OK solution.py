# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:16:26 2021

@author: Compaq
"""
n=15
c=3
m=2

count = n//c
x = count
while x>=m:
    a,b = divmod(x,m)
    count+=a
    x = a+b
print( count)


# pasarlo a excel para ver funcionamiento