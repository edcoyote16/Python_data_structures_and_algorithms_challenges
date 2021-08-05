# -*- coding: utf-8 -*-
"""
"""
grid = ['1112', '1912', '1892', '1234']

# def maxRegion(grid):

for row in range(len(grid)):
    for col in range(len(grid[0])):
        try:
                
            if grid[row-1][col]<grid[row][col] and grid[row+1][col]<grid[row][col] and grid[row][col-1]<grid[row][col] and grid[row][col+1] <grid[row][col]:
                
                temp=[n for n in grid[row]]
                temp[col]='X'
                grid[row]=''.join(temp)
                
        except IndexError:
            continue
print(grid)
#    return max_cell_counter




# =============================================================================
# 
# def count_region_cells(grid, row, col):
#     if any([row<0, col<0, row>=len(grid), col>=len(grid[0])]):
#         return 0
#     if grid[row][col]==0:
#         return 0
#     cell_count=1
#     grid[row][col]=0
#     
#     for r in range(row-1, row+2):
#         for c in range(col-1, col+2):
#             if any([r!=row, c!=col]):
#                 cell_count+=count_region_cells(grid, r, c)
#                 
#             
#     return cell_count
# 
# 
# 
# =============================================================================
