n = 4
m = 4
k = 3
track = [[2, 2, 3], [3, 1, 4], [4, 4, 4]]
my_cells=[]
for a in track:
    for b in range(a[1], a[2]+1):
        my_cells+=[[a[0], b]]
#my_cells=set(my_cells)
counter=0
array=[]
for c in range(1,n+1):
    for d in range(1, m + 1):
        if [c,d] not in my_cells:
            counter+=1


print(counter)