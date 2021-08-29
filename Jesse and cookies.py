#  1. INTEGER k
#  2. INTEGER_ARRAY A
def cookies(k, A):
    A=list(set(A))
    #sweetness = 1 X Least sweet cookie + 2 X 2nd least sweet cookie)
    iterations=0
    while min(A) <= k and len(A)>=2:

        first_least_sweet_cookie = A.pop(A.index(min(A)))
        second_least_sweet_cookie = A.pop(A.index(min(A)))
        new_member=first_least_sweet_cookie + (2 * second_least_sweet_cookie)
        if len(A)==1 and A[0]<k:
            return -1
        if new_member not in A:
            A+=[new_member]
        iterations+=1


    return iterations

print(cookies(8467293,[13, 47, 74 ,12, 89, 74, 18, 38]))
