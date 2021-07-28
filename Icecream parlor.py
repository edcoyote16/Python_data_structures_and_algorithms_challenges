

n = 4
cost = [2, 2,4, 3]
def icecreamParlor(n, cost):
    # Write your code here
    results=[]
    for index_a, a in enumerate(cost):
        for index_b, b in enumerate(cost):
            if a + b == n and index_a!=index_b:
                results+=[sorted([index_a+1,index_b+1])]

    return results[0]
