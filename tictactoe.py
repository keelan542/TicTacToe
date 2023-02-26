# Returns an empty board containing only single spaces at start of game
def new_board():
	return [' ' for i in range(9)]

# Renders the board based on what moves have been made
def render(board):
  print('\n   1   2   3')
  print(' +-----------+')
  print('1| {} | {} | {} |\n -------------\n2| {} | {} | {} |\n -------------\n3| {} | {} | {} |'.format(*board))
  print(' +-----------+')

# Gets move input from user
def get_move():
  try:
    return int(input("What is your move ? "))
  except ValueError:
    print("", end='')

# Makes move after checking with is_valid_move() first
def make_move(board, player):
  while True:
    move = get_move()
    if is_valid_move(board, move):
      break
    else:
      print("Invalid move, try again!")

  updated_board = board
  updated_board[move-1] = player
  return updated_board

# Checks is move is valid and returns to make_move()
def is_valid_move(board, move):
  if move in range(1, 10) and board[move-1] == ' ':
    return True
  else:
    return False

# Checks if there is winner, following the previous move
def is_winner(board):
  for i in range(0, 7, 3):
    if board[i] == board[i+1] == board[i+2] == 'X':
      return 'X'
    elif board[i] == board[i+1] == board[i+2] == 'O':
      return 'O'

  for i in range(3):
    if board[i] == board[i+3] == board[i+6] == 'X':
      return 'X'
    elif board[i] == board[i+3] == board[i+6] == 'O':
      return 'O'

  if board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
    return 'X'
  elif board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'Y':
    return 'O'

  return None

# Checks if the board is full
def is_board_full(board):
  if ' ' not in board:
    return True
  else:
    return False

# Start of main program
board = new_board()
player = 'X'

# Welcome message
print("Welcome to TicTacToe")
print("Below you will see the game board")
print("In order to make a valid move, you must enter an integer from 1-9")
print("Each integer corresponds to a place on the board\n")
render([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nTHE GAME HAS NOW STARTED!")

# Render empty board
render(board)

# Main game loop until draw or winner
while True:
  print("It is {}'s turn".format(player))
  make_move(board, player)
  render(board)

  if is_winner(board) != None:
    print("{} has won the game!".format(player))
    break

  if is_board_full(board):
    print("The game has ended in a draw!")
    break

  match player:
    case 'X':
      player = 'O'
    case 'O':
      player = 'X'