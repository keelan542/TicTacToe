from colorama import Fore, Back, Style

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

# Checks if there is winner, based on current state of board
def is_winner(board):
  for i in range(0, 7):
    # Check for a horizontal win
    if i % 3 == 0 and all(x == board[i] and x != ' ' for x in board[i:i+3]):
      return board[i]

    # Check for a vertical win
    if i < 3 and all(x == board[i] and x != ' ' for x in board[i:i+7:3]):
      return board[i]

    # Check for first possible diagonal win
    if i == 0 and all(x == board[i] and x != ' ' for x in board[i::4]):
      return board[i]

    # Check for second possible diagonal win
    if i == 2 and all(x == board[i] and x != ' ' for x in board[2:7:2]):
      return board[i]

  return None

# Checks if the board is full
def is_board_full(board):
  if ' ' not in board:
    return True
  else:
    return False

# Asks the players if they want to play again
def play_again():
  play = input("Do you want to play again (y/n) ? ")
  if play == 'y':
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
    if play_again() == False:
      break
    else:
      print()
      board = new_board()
      render(board)

  if is_board_full(board):
    print("The game has ended in a draw!")
    if play_again() == False:
      break
    else:
      print()
      board = new_board()
      render()

  match player:
    case 'X':
      player = 'O'
    case 'O':
      player = 'X'