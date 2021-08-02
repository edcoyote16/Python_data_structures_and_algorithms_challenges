n = 6
k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
zeros=[]
ones=[]
for index_a, a in enumerate(contests):
    if a[1]==0:
        zeros+=[a]
    else:
        ones+=[a]

zeros= sorted(zeros)
ones= sorted(ones, reverse=True)

counter=0
my_results=0
for b in ones:
    if counter < k:
        my_results+=b[0]
        counter+=1
    elif counter >= k:
        my_results -= b[0]
        counter += 1
for c in zeros:
    my_results+=c[0]
print(my_results)

print(contests)