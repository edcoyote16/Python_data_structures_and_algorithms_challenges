class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = []
        columns = []
        cells = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(9):
            row = []
            for j in range(9):
                if (board[i][j] != 0):
                    row.append(board[i][j])
            rows.append(row)
        for j in range(9):
            column = []
            for i in range(9):
                if (board[i][j] != 0):
                    column.append(board[i][j])
            columns.append(column)
        for i in range(9):
            for j in range(9):
                if (board[i][j] != 0):
                    cells[i // 3][j // 3].append(board[i][j])

        def solveOne(i, j):
            while (board[i][j] != 0):
                if (j < 8):
                    j += 1
                elif (i < 8):
                    i += 1
                    j = 0
                else:
                    return True

            for k in range(1,10):
                k_str = int(k)
                if (not ((k_str in rows[i]) or (k_str in columns[j]) or (k_str in cells[i // 3][j // 3]))):
                    board[i][j] = k_str
                    rows[i].append(k_str)
                    columns[j].append(k_str)
                    cells[i // 3][j // 3].append(k_str)

                    if (solveOne(i, j)):
                        return True
                    else:
                        board[i][j] = 0
                        rows[i].pop()
                        columns[j].pop()
                        cells[i // 3][j // 3].pop()
            return False

        solveOne(0, 0)
        for n in board:
            print(*n)

grid=[]
mysolution=Solution()
for _ in range(int(input())):
    #mat.append(list(map(str, input().rstrip().split())))
    for n in range(9):
        #grid+= [[int(x) for x in input().rstrip().split()]]
        grid+= [[int(i) for i in input().strip().split()]]
    #print(grid)
    mysolution.solveSudoku(grid)