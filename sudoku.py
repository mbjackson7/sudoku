
def get_board():
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(' ')
    
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

def print_board(board):
    print("---------------------")
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5 or i == 8:
            print("---------------------")

def initialize_possibilities():
    possibleVals = []
    for i in range(9):
        possibleVals.append([])
        for _ in range(9):
            possibleVals[i].append([1,2,3,4,5,6,7,8,9])

    return possibleVals

def solve_sudoku(board):
    possibleVals = initialize_possibilities()
    unsolved = True
    while(unsolved):
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value != ' ':
                    #print(value, row, col)
                    for i in range(9):
                        if type(possibleVals[i][col]) != int and value in possibleVals[i][col]:
                            possibleVals[i][col].remove(value)
                        if type(possibleVals[row][i]) != int and value in possibleVals[row][i]:
                            possibleVals[row][i].remove(value)
                    rowModifier = row//3 * 3
                    colModifier = col//3 * 3
                    for boxRow in range(3):
                        for boxCol in range(3):
                            if type(possibleVals[boxRow+rowModifier][boxCol+colModifier]) != int and value in possibleVals[boxRow+rowModifier][boxCol+colModifier]:
                                possibleVals[boxRow+rowModifier][boxCol+colModifier].remove(value)
                    possibleVals[row][col] = value
        unsolved = False
        for row in range(9):
            for col in range(9):
                if type(possibleVals[row][col]) != int and len(possibleVals[row][col]) == 1:
                    unsolved = True
                    possibleVals[row][col] = board[row][col] = possibleVals[row][col][0]
        print_board(possibleVals)
    return board



def main():
    board = get_board()
    board = initialize_board(board)
    print_board(board)
    board = solve_sudoku(board)
    print_board(board)


if __name__ == "__main__":
    main()