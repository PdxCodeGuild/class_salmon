player1 = {'name': 'Pete', 'token': 'X'}
player2 = {'name': 'Matthew', 'token': 'Y'}
players = [player1, player2]

player1_name = input('What\'s Player1\'s name? ')
player2_name = input('What\'s Player2\'s name? ')

player1['name'] = player1_name
player2['name'] = player2_name

# print(players)

def display_board(board):
  print(' X 0 1 2')
  print('Y')
  print('0  ' + '|'.join(board[0]))
  print('1  ' + '|'.join(board[1]))
  print('2  ' + '|'.join(board[2]))

def take_turn(board, player):
  turnX = int(input(f"{player['name']}, where do you want to place a token (X-coordinate)? "))
  turnY = int(input(f"{player['name']}, where do you want to place a token (Y-coordinate)? "))
  if board[turnY][turnX] == ' ':
    board[turnY][turnX] = player['token']
    return True
  else:
    print('Spot\'s taken!')
    return False

def check_game_state(board, player, counter):
  # check win conditions
  for row in board:
    if set(row) == {player['token']}:
      display_board(board)
      print(f"{player['name']} wins!")
      return True
  for i in range(3):
    column = [board[0][i], board[1][i], board[2][i]]
    if set(column) == {player['token']}:
      display_board(board)
      print(f"{player['name']} wins!")
      return True
  
  diagonal1 = [board[0][0], board[1][1], board[2][2]]
  diagonal2 = [board[0][2], board[1][1], board[2][0]]
  if set(diagonal1) == {player['token']} \
    or set(diagonal2) == {player['token']}:
    display_board(board)
    print(f"{player['name']} wins!")
    return True

  # check board full draw
  # for row in board:
  #   for space in row:
  #     if space == ' ':
  #       display_board(board)
  #       print("cat's game")
  #       return False
  if counter == 8:
    display_board(board)
    print("cat's game")
    return True
  return False

board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
]

counter = 0
while True:
  player = players[counter % 2]
  print()
  print('----------------------')
  print()
  print(f"{player['name']}'s turn. Token: {player['token']}")
  display_board(board)
  valid_move = take_turn(board, player)
  game_over = check_game_state(board, player, counter)
  if valid_move:
    counter += 1
  if game_over:
    break