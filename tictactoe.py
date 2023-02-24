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
  return input("What is your move ? ")

board = new_board()

render(board)
move = get_move()

# Loop through turns until the game is over
'''
loop forever:
  # TODO: hmm I'm not sure how best to do this
  # right now. No problem, I'll come back later.
  current_player = ???

  # Print the current state of the board
  render(board)

  # Get the move that the current player is going
  # to make.
  move_co_ords = get_move()

  # Make the move that we calculated above
  make_move(board, move_co_ords, current_player)

  # Work out if there's a winner
  winner = get_winner(board)

  # If there is a winner, crown them the champion
  # and exit the loop.
  if winner is not None:
    print "WINNER IS %s!!" % winner
    break

  # If there is no winner and the board is full,
  # exit the loop.
  if is_board_full(board):
    print "IT'S A DRAW!!"
    break

  # Repeat until the game is over
'''