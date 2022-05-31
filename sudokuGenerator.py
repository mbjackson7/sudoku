import time, random, copy
from sudokuSolver import initialize_possibilities, print_board, set_value, solve_sudoku

def populate_board():
    broken = True
    while broken:
        broken = False
        board = initialize_possibilities()
        for row in range(9):
            for col in range(9):
                if len(board[row][col]) == 0:
                    broken = True
                    break
                value = random.choice(board[row][col])
                board = set_value(board, value, row, col)
            if broken:
                break
    return board

def reduce_board(board, remainingGoal):
    trueSolution = copy.deepcopy(board)
    repetitions = 0
    remaining = 81
    while repetitions < 60 and remaining > remainingGoal:
        row = random.randrange(9)
        col = random.randrange(9)
        removedVal = board[row][col]
        if type(removedVal) == list:
            continue
        board[row][col] = [1,2,3,4,5,6,7,8,9]
        newBoard = copy.deepcopy(board)
        #exportBoard = copy.deepcopy(board)
        genSolution = solve_sudoku(board)
        #importSolution = test_imported_board(exportBoard)
        board = newBoard
        if genSolution != trueSolution:
            board[row][col] = removedVal
            repetitions += 1
        else:
          remaining -= 1
    #print("Remaining: " + str(remaining))
    return board

def generate_board(remainingGoal=0):
    solution = populate_board()
    board = copy.deepcopy(solution)
    board = reduce_board(board, remainingGoal)
    return board, solution

def main():
    start = time.time()
    board, solution = generate_board()
    print_board(solution)
    print_board(board)
    end = time.time()
    print("Elapsed Time:" + str(end - start))

if __name__ == "__main__":
    main()