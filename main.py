import random

# game board variables
while (True):
  board = []
  for x in range(5):
      board.append(["O"] * 5)
  
  def print_board(board):
      for row in board:
          print (" ".join(row))
  
  print ("Let's play Battleship!")
  print_board(board)
  
  # randomly select the ship location
  def random_row(board):
      return random.randint(0, len(board) - 1)
  
  def random_col(board):
      return random.randint(0, len(board[0]) - 1)
  
  ship_row = random_row(board)
  ship_col = random_col(board)
  
  # Game loop!
  for turn in range(4):
      print ("Turn", turn)
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
  
      if guess_row == ship_row and guess_col == ship_col:
          print ("Congratulations! You sank my battleship!")
          break
      else:
          if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col):
              print ("Oops, that's not even in the ocean.")
          elif(board[guess_row][guess_col] == "X"):
              print ("You guessed that one already.")
          else:
              print ("You missed my battleship!")
              board[guess_row][guess_col] = "X"
          if (turn == 3):
              print ("Game Over")
              print ("The ship was at row", ship_row, "and column", ship_col)
          turn += 1
          print_board(board)

          # if (guess_row - ship_row, ship_col - guess_col) == (0, 1):
             # print ("You're close!")

        # Asks the user if they want to play again.
  confirm = input("Would you like to play again? (y/n): ")
  if confirm == "N" or confirm == "n":
    break