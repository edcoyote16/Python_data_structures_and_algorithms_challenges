def pokerNim(k, c):
    # Write your code here

    res = 0
    for i in c:
        res ^= i
    if (res):
        return ("First")
    else:
        return ("Second")
    
k=5
c=[2, 1, 3]
pokerNim(k,c)