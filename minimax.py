# import copy
#
# # Board constants
# EMPTY = '-'
# PLAYER_X = 'x'
# PLAYER_O = 'o'
#
#
# # Function to print the board
# def print_board(board):
#     print("   0 1 2 3 4 5 6 7")
#     for i, row in enumerate(board):
#         print(i, end='  ')
#         for cell in row:
#             print(cell, end=' ')
#         print()
#
#
# # Function to check if a move is valid
# def is_valid_move(board, player, start, end):
#     x1, y1 = start
#     x2, y2 = end
#
#     if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
#         return False
#
#     if board[x2][y2] != EMPTY:
#         return False
#
#     if player == PLAYER_X:
#         if board[x1][y1] == PLAYER_X and x2 == x1 + 1 and abs(y2 - y1) == 1:
#             return True
#         elif board[x1][y1] == PLAYER_X.upper() and abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
#             return True
#     elif player == PLAYER_O:
#         if board[x1][y1] == PLAYER_O and x2 == x1 - 1 and abs(y2 - y1) == 1:
#             return True
#         elif board[x1][y1] == PLAYER_O.upper() and abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
#             return True
#
#     return False
#
#
# # Function to make a move
# def make_move(board, player, start, end):
#     new_board = copy.deepcopy(board)
#     x1, y1 = start
#     x2, y2 = end
#
#     if player == PLAYER_X and x2 == 7:
#         new_board[x2][y2] = PLAYER_X.upper()
#     elif player == PLAYER_O and x2 == 0:
#         new_board[x2][y2] = PLAYER_O.upper()
#     else:
#         new_board[x2][y2] = new_board[x1][y1]
#
#     new_board[x1][y1] = EMPTY
#     return new_board
#
#
# # Function to evaluate the board
# def evaluate(board):
#     x_count = 0
#     o_count = 0
#
#     for row in board:
#         for cell in row:
#             if cell == PLAYER_X or cell == PLAYER_X.upper():
#                 x_count += 1
#             elif cell == PLAYER_O or cell == PLAYER_O.upper():
#                 o_count += 1
#
#     return x_count - o_count
#
#
# # Minimax algorithm
# def minimax(board, depth, maximizing_player):
#     if depth == 0:
#         return evaluate(board)
#
#     if maximizing_player:
#         max_eval = float('-inf')
#         moves = get_valid_moves(board, PLAYER_O)
#         for move in moves:
#             new_board = make_move(board, PLAYER_O, move[0], move[1])
#             eval = minimax(new_board, depth - 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = float('inf')
#         moves = get_valid_moves(board, PLAYER_X)
#         for move in moves:
#             new_board = make_move(board, PLAYER_X, move[0], move[1])
#             eval = minimax(new_board, depth - 1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval
#
#         # Function to get valid moves for a player
#
#
# def get_valid_moves(board, player):
#     moves = []
#     for i in range(8):
#         for j in range(8):
#             if board[i][j] == player or board[i][j] == player.upper():
#                 start = (i, j)
#                 if player == PLAYER_X or player == PLAYER_X.upper():
#                     end1 = (i + 1, j - 1)
#                     end2 = (i + 1, j + 1)
#                     if is_valid_move(board, player, start, end1):
#                         moves.append((start, end1))
#                     if is_valid_move(board, player, start, end2):
#                         moves.append((start, end2))
#                 else:
#                     end1 = (i - 1, j - 1)
#                     end2 = (i - 1, j + 1)
#                     if is_valid_move(board, player, start, end1):
#                         moves.append((start, end1))
#                     if is_valid_move(board, player, start, end2):
#                         moves.append((start, end2))
#     return moves
#
#     # Main game loop
#
#
# def play_game():
#     board = [
#         ['-', 'o', '-', 'o', '-', 'o', '-', 'o'],
#         ['o', '-', 'o', '-', 'o', '-', 'o', '-'],
#         ['-', 'o', '-', 'o', '-', 'o', '-', 'o'],
#         ['-', '-', '-', '-', '-', '-', '-', '-'],
#         ['-', '-', '-', '-', '-', '-', '-', '-'],
#         ['x', '-', 'x', '-', 'x', '-', 'x', '-'],
#         ['-', 'x', '-', 'x', '-', 'x', '-', 'x'],
#         ['x', '-', 'x', '-', 'x', '-', 'x', '-']
#     ]
#
#     current_player = PLAYER_X
#
#     while True:
#         print_board(board)
#
#         if current_player == PLAYER_X:
#             print("Your turn (x)")
#             start = input("Enter start position (row, col): ")
#             end = input("Enter end position (row, col): ")
#             start = tuple(map(int, start.split(',')))
#             end = tuple(map(int, end.split(',')))
#
#             if is_valid_move(board, current_player, start, end):
#                 board = make_move(board, current_player, start, end)
#                 current_player = PLAYER_O
#             else:
#                 print("Invalid move. Try again.")
#
#         else:
#             print("Computer's turn (o)")
#
#             moves = get_valid_moves(board, current_player)
#             best_move = None
#             best_score = float('-inf')
#
#             for move in moves:
#                 new_board = make_move(board, current_player, move[0], move[1])
#                 score = minimax(new_board, 3, False)  # Adjust depth as needed
#                 if score > best_score:
#                     best_score = score
#                     best_move = move
#
#             board = make_move(board, current_player, best_move[0], best_move[1])
#             current_player = PLAYER_X
#
#         if not get_valid_moves(board, current_player):
#             print("Game over!")
#             print("Final board:")
#             print_board(board)
#             break
#
#     # Start the game
#
#
# play_game()
