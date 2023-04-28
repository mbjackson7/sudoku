import sys
import string
from turtle import back
import requests
import time
from bs4 import BeautifulSoup
from sudokuSolver import initialize_possibilities, solve_sudoku, print_board, backtracking

def list_to_board(puzzleList: list):
    board = initialize_possibilities()
    for index in range(len(puzzleList)):
        if puzzleList[index] != 0:
            row = index // 9
            col = index - (row*9)
            board[row][col] = puzzleList[index]
    return board
        

def get_puzzle(difficulty: string):
    response = requests.get("https://www.nytimes.com/puzzles/sudoku")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.select('div[class=pz-game-screen] > script')

    lcls = locals()
    exec(data[0].string.replace("window.", ""), globals(), lcls)
    gameData = lcls["gameData"]

    puzzle = list_to_board(gameData[difficulty]['puzzle_data']['puzzle'])
    solution = list_to_board(gameData[difficulty]['puzzle_data']['solution'])
    return puzzle, solution

def main():
    difficulty = 'hard'
    if len(sys.argv) == 2:
        difficulty = str(sys.argv[1])

    start = time.time()
    puzzle, solution = get_puzzle(difficulty)
    print_board(puzzle)
    puzzle = solve_sudoku(puzzle)
    print_board(puzzle)
    end = time.time()
    if puzzle == solution:
        print("Success!")
    else:
        print("Something went wrong...")
    print("Elapsed Time:" + str(end - start))


if __name__ == "__main__":
    main()
