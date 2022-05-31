import time, random, copy
from sudokuSolver import print_board, set_value
from sudokuGenerator import generate_board

def splash_screen():
  print("==============================================")
  print("  _____  _    _  _____    ____   _  __ _    _ ")
  print(" / ____|| |  | ||  __ \  / __ \ | |/ /| |  | |")
  print("| (___  | |  | || |  | || |  | || ' / | |  | |")
  print(" \___ \ | |  | || |  | || |  | ||  <  | |  | |")
  print(" ____) || |__| || |__| || |__| || . \ | |__| |")
  print("|_____/  \____/ |_____/  \____/ |_|\_\ \____/ ")
  print()
  print("            PRESS ENTER TO BEGIN")
  print()
  print("==============================================")

def print_controls():
  board, solution = generate_board(81)
  print("A board looks likes this, with row and column labels on the sides")
  print_guided_board(solution)
  input("Press Enter To Continue...")
  print("\nControls:")
  print("   To enter an answer, type it in the format")
  print("   \"<row>,<col>,<value>\"")
  print("   then press enter.")
  print()
  print("   If you get stuck, you can type \"solve\" to get the solution")

def print_guided_board(board):
    print("\n    1 2 3   4 5 6   7 8 9")
    print()
    for row in range(9):
      print(str(row+1) + "  ", end=" ")
      for col in range(9):
          if board == None:
            print("Unsolvable")
            return
          elif type(board[row][col]) == int:
            print(board[row][col], end=" ")
          else:
            print(" ", end=" ")
          if col == 2 or col == 5:
              print("|", end=" ")
      print()
      if row == 2 or row == 5:
          print("    ------|-------|------")
    print()

def get_remaining(board):
  remaining = 0
  for row in range(9):
    for col in range(9):
      if type(board[row][col]) == list:
        remaining += 1
  return remaining

def main():
    strikes = 0
    splash_screen()
    input()
    print_controls()
    difficulty = input("Minimum Known Spaces (Skip For Max Difficulty): ")
    if difficulty.isdigit():
        difficulty = int(difficulty)
    else:  
        difficulty = 0
    print("Generating Board...")
    board, solution = generate_board(difficulty)
    print("Go!")
    start = time.time()
    while get_remaining(board) > 0 and strikes < 3:
      print_guided_board(board)
      print("Remaining: " + str(get_remaining(board)) + "\n")
      print("Strikes: " + str(strikes) + "\n")
      answer = input("Next Answer: ")
      if answer == "solve":
        break
      else:
        answer = answer.split(',')
        if type(answer) != list or len(answer) != 3 or not answer[0].isdigit() or not answer[1].isdigit() or not answer[2].isdigit():
          print("Invalid Entry")
          continue
        row = int(answer[0]) - 1
        col = int(answer[1]) - 1
        value = int(answer[2])
        if row not in range(9) or col not in range(9) or value-1 not in range(9):
          print("Invalid Number")
          continue

        if solution[row][col] == value:
          print("Correct!")
          board[row][col] = value
        else:
          print("Miss!")
          strikes += 1

    print_guided_board(solution)
    if get_remaining(board) > 0:
      print("Here's the solution, better luck next time and keep practicing!")
    else:
      print("You did it, congratulations!")

    end = time.time()
    print("Elapsed Time:" + str(end - start))

if __name__ == "__main__":
    main()