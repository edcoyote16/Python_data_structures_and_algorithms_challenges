# Function to check if two queens threaten each other or not
def isSafe(mat, r, c):
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the same \ diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # return false if two queens share the same / diagonal
    (i, j) = (r, c)
    while i >= 0 and j < N:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def nQueen(mat, r):
    # if N queens are placed successfully, print the solution
    if r == N:
        for i in range(N):
            for column1 in range(N):
                print(mat[i][column1], end=' ')
            print()
        print()

        return

    # place Queen at every square in current row r
    # and recur for each valid movement
    for column in range(N):

        # if no two queens threaten each other
        if isSafe(mat, r, column):
            # place queen on current square
            mat[r][column] = 'Q'

            # recur for next row
            nQueen(mat, r + 1)

            # backtrack and remove queen from current square
            mat[r][column] = '-'


#if __name__ == '__main__':

# N x N chessboard
N = 4

# mat[][] keeps track of position of Queens in
# the current configuration
mat = [['-' for x in range(N)] for y in range(N)]

nQueen(mat, 0)