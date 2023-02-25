# Returns an empty board containing only single spaces at start of game
def new_board():
	return [' ' for i in range(9)]

# Renders the board based on what moves have been made
def render(board):
  print('  1 2 3')
  print(' +-----+')
  print('1|{} {} {}|\n2|{} {} {}|\n3|{} {} {}|'.format(*board))
  print(' +-----+')

def get_move():
  return int(input("What is your move ? "))

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

def is_valid_move(board, move):
  if board[move-1] == ' ':
    return True
  else:
    return False

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

def is_board_full(board):
  if ' ' not in board:
    return True
  else:
    return False

board = new_board()
player = 'X'

render(board)

while True:
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