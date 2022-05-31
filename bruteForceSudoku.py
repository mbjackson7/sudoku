# This solution was found online for comparison against my own
# https://www.askpython.com/python/examples/sudoku-solver-in-python
# It has significantly less code, but uses brute force and recursion
# My own grid generation function has been added so the same puzzle may be easily compared
import time


def get_board():
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(0)
    
    return board

def initialize_board(board):
    board[0][0] = 5
    board[0][1] = 3
    board[0][4] = 7
    board[1][0] = 6
    board[1][3] = 1
    board[1][4] = 9
    board[1][5] = 5
    board[2][1] = 9
    board[2][2] = 8
    board[2][7] = 6
    board[3][0] = 8
    board[3][4] = 6
    board[3][8] = 3
    board[4][0] = 4
    board[4][3] = 8
    board[4][5] = 3
    board[4][8] = 1
    board[5][0] = 7
    board[5][4] = 2
    board[5][8] = 6
    board[6][1] = 6
    board[6][6] = 2
    board[6][7] = 8
    board[7][3] = 4
    board[7][4] = 1
    board[7][5] = 9
    board[7][8] = 5
    board[8][4] = 8
    board[8][7] = 7
    board[8][8] = 9
    return board

def initialize_expert_board(board):
    board[0][2] = 5
    board[0][6] = 2
    board[0][8] = 3
    board[1][1] = 6
    board[1][2] = 8
    board[1][3] = 7
    board[2][0] = 1
    board[2][2] = 9
    board[3][3] = 9
    board[3][6] = 3
    board[3][8] = 5
    board[4][1] = 1
    board[4][4] = 5
    board[4][7] = 4
    board[4][8] = 2
    board[6][3] = 6
    board[6][4] = 4
    board[6][6] = 5
    board[7][1] = 8
    board[7][7] = 7
    board[8][0] = 6
    board[8][3] = 1
    board[8][4] = 2
    return board

def initialize_inkala_board(board):
    board[0][0] = 8
    board[1][2] = 3
    board[1][3] = 6
    board[2][1] = 7
    board[2][4] = 9
    board[2][6] = 2
    board[3][1] = 5
    board[3][5] = 7
    board[4][4] = 4
    board[4][5] = 5
    board[4][6] = 7
    board[5][3] = 1
    board[5][7] = 3
    board[6][2] = 1
    board[6][7] = 6
    board[6][8] = 8
    board[7][2] = 8
    board[7][3] = 5
    board[7][7] = 1
    board[8][1] = 9
    board[8][6] = 4
    return board


M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''

start = time.time()
grid = get_board()
grid = initialize_expert_board(grid)
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")
end = time.time()
print("Elapsed Time:" + str(end - start))
