grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
length=len(grid)
grid = [sorted(n) for n in grid]
grid_vertically=[]
grid_vertically_whole=[]
for index_a, a in enumerate(range(length)):
    # if grid_vertically:
    #     grid_vertically_whole+=[grid_vertically]
    #     grid_vertically=[]
    for index_b, b in enumerate(range(len(grid[0]))):
        grid_vertically+=[grid[b][a]]
    if grid_vertically:
        grid_vertically_whole+=[grid_vertically]
        grid_vertically=[]
grid_vertically_whole2=grid_vertically_whole[::]
grid_vertically_whole2=[sorted(n) for n in grid_vertically_whole2]
if grid_vertically_whole2==grid_vertically_whole:
    check='YES'
else:
    check='NO'

print(check)