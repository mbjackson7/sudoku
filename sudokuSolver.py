from copy import deepcopy
import time

from bruteForceSudoku import initialize_inkala_board


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


def get_custom_board():
    board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 7, [1, 2, 3,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
    return board


def get_zero_board(board=None):
    if not board:
        board = [
            [8, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 3,  6, 0, 0,  0, 0, 0],
            [0, 7, 0,  0, 9, 0,  2, 0, 0],

            [0, 5, 0,  0, 0, 7,  0, 0, 0],
            [0, 0, 0,  0, 4, 5,  7, 0, 0],
            [0, 0, 0,  1, 0, 0,  0, 3, 0],

            [0, 0, 1,  0, 0, 0,  0, 6, 8],
            [0, 0, 8,  5, 0, 0,  0, 1, 0],
            [0, 9, 0,  0, 0, 0,  4, 0, 0]
        ]

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                board[row][col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def initialize_counts():
    counts = {
        "rows": {},
        "cols": {},
        "boxes": {},
    }
    for i in range(9):
        counts["rows"][i] = {}
        counts["cols"][i] = {}
        counts["boxes"][i] = {}
        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            counts["rows"][i][j] = 0
            counts["cols"][i][j] = 0
            counts["boxes"][i][j] = 0
    return counts


def initialize_pairs():
    pairs = {
        "rows": {},
        "cols": {},
        "boxes": {},
    }
    for i in range(9):
        pairs["rows"][i] = []
        pairs["cols"][i] = []
        pairs["boxes"][i] = []
    return pairs


def print_board(board, debug=False):
    print("\n---------------------")
    for row in range(9):
        for col in range(9):
            if board == False or board == None:
                print("Unsolvable")
                return
            elif type(board[row][col]) == int or debug:
                print(board[row][col], end=" ")
            else:
                print(" ", end=" ")
            if col == 2 or col == 5:
                print("|", end=" ")
        print()
        if row == 2 or row == 5 or row == 8:
            print("---------------------")


def get_box(row, col):
    boxRow = row//3
    boxCol = col//3
    box = -1
    if boxRow == 0 and boxCol == 0:
        box = 0
    elif boxRow == 0 and boxCol == 1:
        box = 1
    elif boxRow == 0 and boxCol == 2:
        box = 2
    elif boxRow == 1 and boxCol == 0:
        box = 3
    elif boxRow == 1 and boxCol == 1:
        box = 4
    elif boxRow == 1 and boxCol == 2:
        box = 5
    elif boxRow == 2 and boxCol == 0:
        box = 6
    elif boxRow == 2 and boxCol == 1:
        box = 7
    elif boxRow == 2 and boxCol == 2:
        box = 8
    return box


def get_box_coords(box):
    if box == 0:
        return 0, 0
    elif box == 1:
        return 0, 3
    elif box == 2:
        return 0, 6
    elif box == 3:
        return 3, 0
    elif box == 4:
        return 3, 3
    elif box == 5:
        return 3, 6
    elif box == 6:
        return 6, 0
    elif box == 7:
        return 6, 3
    elif box == 8:
        return 6, 6


def initialize_possibilities():
    board = []
    for i in range(9):
        board.append([])
        for _ in range(9):
            board[i].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

    return board


def set_value(board, value, row, col):
    for i in range(9):
        if type(board[i][col]) != int and value in board[i][col]:
            board[i][col].remove(value)
        if type(board[row][i]) != int and value in board[row][i]:
            board[row][i].remove(value)
    rowModifier = row//3 * 3
    colModifier = col//3 * 3
    for boxRow in range(3):
        for boxCol in range(3):
            if type(board[boxRow+rowModifier][boxCol+colModifier]) != int and value in board[boxRow+rowModifier][boxCol+colModifier]:
                board[boxRow+rowModifier][boxCol+colModifier].remove(value)
    board[row][col] = value
    # print_board(board)
    return board


def only_spot_validation(board, setList):
    counts = initialize_counts()
    for row in range(9):
        for col in range(9):
            if type(board[row][col]) == list:
                box = get_box(row, col)
                for num in board[row][col]:
                    counts["rows"][row][num] += 1
                    counts["cols"][col][num] += 1
                    counts["boxes"][box][num] += 1
    # print(counts)
    for row in range(9):
        for col in range(9):
            if type(board[row][col]) == list:
                box = get_box(row, col)
                for num in board[row][col]:
                    if counts["rows"][row][num] == 1:
                        board = set_value(board, num, row, col)
                        setList[row][col] = 1
                    elif counts["cols"][col][num] == 1:
                        board = set_value(board, num, row, col)
                        setList[row][col] = 1
                    elif counts["boxes"][box][num] == 1:
                        board = set_value(board, num, row, col)
                    setList[row][col] = 1
    return board, setList


def naked_pair(board):
    pairs = initialize_pairs()
    for row in range(9):
        for col in range(9):
            pair = board[row][col]
            if type(pair) == list and len(pair) == 2:
                box = get_box(row, col)
                # check if there is a pair in any rows
                if pair in pairs["rows"][row]:
                    for i in range(9):
                        value = board[row][i]
                        if type(value) == list and value != pair:
                            for num in pair:
                                if num in value:
                                    board[row][i].remove(num)
                else:
                    pairs["rows"][row].append(pair)
                # check if there is a pair in any columns
                if pair in pairs["cols"][col]:
                    for i in range(9):
                        value = board[i][col]
                        if type(value) == list and value != pair:
                            for num in pair:
                                if num in value:
                                    board[i][col].remove(num)
                else:
                    pairs["cols"][col].append(pair)
                if pair in pairs["boxes"][box]:
                    x, y = get_box_coords(box)
                    for i in range(3):
                        for j in range(3):
                            value = board[x+i][y+j]
                            if type(value) == list and value != pair:
                                for num in pair:
                                    if num in value:
                                        board[x+i][y+j].remove(num)
                else:
                    pairs["boxes"][box].append(pair)
    return board


def hidden_triple(board):
    pairs = initialize_pairs()
    for row in range(9):
        for col in range(9):
            pair = board[row][col]
            if type(pair) == list and len(pair) == 2:
                box = get_box(row, col)
                # check if there is a pair in any rows
                if pair in pairs["rows"][row]:
                    for i in range(9):
                        value = board[row][i]
                        if type(value) == list and value != pair:
                            for num in pair:
                                if num in value:
                                    board[row][i].remove(num)
                else:
                    pairs["rows"][row].append(pair)
                # check if there is a pair in any columns
                if pair in pairs["cols"][col]:
                    for i in range(9):
                        value = board[i][col]
                        if type(value) == list and value != pair:
                            for num in pair:
                                if num in value:
                                    board[i][col].remove(num)
                else:
                    pairs["cols"][col].append(pair)
                if pair in pairs["boxes"][box]:
                    x, y = get_box_coords(box)
                    for i in range(3):
                        for j in range(3):
                            value = board[x+i][y+j]
                            if type(value) == list and value != pair:
                                for num in pair:
                                    if num in value:
                                        board[x+i][y+j].remove(num)
                else:
                    pairs["boxes"][box].append(pair)
    return board


def bifurcate(board):
    #print("Bifurcating!")
    #print_board(board, True)
    for row in range(9):
        for col in range(9):
            pair = board[row][col]
            if type(pair) == list and len(pair) == 2:
                board1 = deepcopy(board)
                set_value(board1, board[row][col][0], row, col)
                board1 = solve_sudoku(board1)
                if board1:
                    return board1
                board2 = deepcopy(board)
                set_value(board2, board[row][col][1], row, col)
                board2 = solve_sudoku(board2)
                if board2:
                    return board2
    return False


def test_placement(board, row, col, value):
    for x in range(9):
        if board[row][x] == value:
            return False
    for x in range(9):
        if board[x][col] == value:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == value:
                return False
    return True


def backtracking(board, row, col):
    blank = [1,2,3,4,5,6,7,8,9]
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if type(board[row][col]) != list:
        return backtracking(board, row, col + 1)
    for value in range(1, 10): 
        if test_placement(board, row, col, value):
            board[row][col] = value
            if backtracking(board, row, col + 1):
                return True
        board[row][col] = blank
    return False


def solve_sudoku(board, generationMode=False):
    unsolved = True
    setList = initialize_possibilities()
    repetitions = 0
    while(unsolved):
        unsolved = False
        for row in range(9):
            for col in range(9):
                if setList[row][col] != 1 or type(board[row][col]) == list:
                    unsolved = True
                    if type(board[row][col]) == list and len(board[row][col]) == 0:
                        return False
                    if repetitions > 80:
                        if not generationMode:
                            backtracking(board, 0, 0)
                            if board:
                                return board
                        return False
                    value = board[row][col]
                    if type(value) != int and len(value) == 1:
                        board = set_value(board, value[0], row, col)
                        setList[row][col] = 1
                    elif type(value) == int:
                        board = set_value(board, value, row, col)
                        setList[row][col] = 1

        board, setList = only_spot_validation(board, setList)
        board = naked_pair(board)
        repetitions += 1
    return board


def main():
    start = time.time()
    board = initialize_possibilities()
    board = initialize_expert_board(board)
    print_board(board)
    board = solve_sudoku(board)
    print_board(board)
    end = time.time()
    print("Elapsed Time:" + str(end - start))


if __name__ == "__main__":
    main()
