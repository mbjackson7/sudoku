import time
import random
from sudokuGenerator import generate_board

class SudokuGame:
    def __init__(self, difficulty: int, maxStrikes: int = 3):
        self.difficulty = difficulty
        self.board, self.solution = generate_board(difficulty)
        self.startTime = time.time()
        self.remaining: int = self.get_remaining()
        self.lastUpdated = self.startTime
        self.strikes = 0
        self.maxStrikes = maxStrikes
        self.gameOver = False
        
    def __str__(self):
        boardStr = "\n---------------------\n"
        for row in range(9):
            for col in range(9):
                if self.board == False or self.board == None:
                    return
                elif type(self.board[row][col]) == int:
                    boardStr += f"{self.board[row][col]} "
                else:
                    boardStr += "  "
                if col == 2 or col == 5:
                    boardStr += "| "
            print()
            if row == 2 or row == 5 or row == 8:
                boardStr += "---------------------\n"
        return boardStr

    def get_remaining(self):
        remaining = 0
        for row in range(9):
            for col in range(9):
                if type(self.board[row][col]) == list:
                    remaining += 1
        self.remaining = remaining
        return remaining
    
    def get_2d_board(self):
        flatBoard = []
        for row in range(9):
            for col in range(9):
                if type(self.board[row][col]) == list:
                    flatBoard.append(0)
                else:
                    flatBoard.append(self.board[row][col])
        return flatBoard

    def get_time_str(self):
        seconds = time.time() - self.startTime
        sModifier = ""
        mModifier = ""
        if seconds >= 3600:
            hours = int(seconds // 3600)
            minutes = int(int(seconds % 3600) // 60)
            seconds = int(seconds % 60)
            if minutes < 10:
                mModifier = "0"
            if seconds < 10:
                sModifier = "0"
            return str(hours) + ":" + mModifier + str(minutes) + ":" + sModifier + str(seconds)
        else:
            minutes = int(seconds // 60)
            seconds = int(seconds % 60)
            if seconds < 10:
                sModifier = "0"
            return str(minutes) + ":" + sModifier + str(seconds)

    def check_game_over(self):
        if self.strikes >= self.maxStrikes:
            self.gameOver = True
            self.board = self.solution
        if self.remaining == 0:
            self.gameOver = True

    def hint(self):
        self.lastUpdated = time.time()
        hint_given = False
        while not hint_given:
            row = random.randrange(9)
            col = random.randrange(9)
            if type(self.board[row][col]) == list:
                self.board[row][col] = self.solution[row][col]
                hint_given = True
                self.remaining -= 1
        self.check_game_over()

    def check(self, row, col, value):
        self.lastUpdated = time.time()
        if self.solution[row][col] == value:
            self.board[row][col] = value
            self.remaining -= 1
        else:
            self.strikes += 1
        self.check_game_over()
        
    def solve(self):
        self.board = self.solution
        self.remaining = 0
        self.gameOver = True
        
