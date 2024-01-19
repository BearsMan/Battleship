import random

# board variable
board = []
for x in range(6):
  board.append(["0"] * 6)

# functions
def print_board(board):
  for row in board:
    print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
  return random.randint(0, len(board) - 1)
def random_col(board):
  return random.randint(0, len(board[0]) - 1)

# ship position variables
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row, ship_col)