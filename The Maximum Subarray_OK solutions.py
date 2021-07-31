# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:59:28 2021

@author: Compaq
"""


def max_mid_sum(arr,l,m,h):
    #take minimum value
    sm=0
    left_sum= -10000
    for i in range(m,l-1,-1):
        sm+=arr[i]
        if sm>left_sum:
            left_sum=sm
        
    sm=0
    right_sum= -10000
    for i in range(m+1,h+1):
        sm+=arr[i]
        if sm>right_sum:
            right_sum=sm
    return left_sum+right_sum

#def maxSubarray(arr):
def max_subArray_sum(arr,l,h):
    #base
    if l==h:
        return arr[l]
    #get the mid
    m=(l+h)//2
    
    return max(max_subArray_sum(arr, l, m),
               max_subArray_sum(arr, m+1, h),
               max_mid_sum(arr,l,m,h))

    # Write your code here
def get_sub(arr):
    for index, p in enumerate(arr):
        if max(arr)<0:
            return max(arr)
        elif index==0:
            my_number=p
        else:
            if my_number + p > my_number:
                my_number += p
    return my_number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#####################
    for _ in range(int(input())):
        _, arr = input(), [int(n) for n in input().split()]
        h = m = t = arr[0]
        for ind, n in enumerate(arr):
            if ind == 0: continue
            t = max(t, n, t + n)
            h = max(n, h + n)
            m = max(m, h)
        print(m, t)

######################
    #t = int(input().strip())

    #for t_itr in range(t):
    #    n = int(input().strip())

    #    arr = list(map(int, input().rstrip().split()))
     
    #    l=0

    #    result = max_subArray_sum(arr,l,n-1)
     
    #    result2= get_sub(arr)
    #    fptr.write(' '.join(map(str, (result, result2))))

        fptr.write(' '.join(map(str, (m,t))))
        #print(' '.join(str(result)))
        
        fptr.write('\n')

    fptr.close()
