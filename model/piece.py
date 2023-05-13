# from model.direction import Direction
# from util.constants import PLAYER_TWO_COLOR, PLAYER_ONE_COLOR, SQUARE_SIZE
#
#
# class Piece:
#
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#         self.king = False
#         if color == PLAYER_TWO_COLOR:
#             self.direction = Direction.DOWNWARD
#         elif color == PLAYER_ONE_COLOR:
#             self.direction = Direction.UPWARD
#         else:
#             raise Exception('Invalid Color!, it muse be either BOT_COLOR or PLAYER_COLOR')
#
#     def make_king(self):
#         self.king = True
#         self.direction = Direction.BOTH
#
#     def __repr__(self):
#         return f'<({self.row}, {self.col}), {self.color}>'
#
#     def __eq__(self, other):
#         if isinstance(other, Piece):
#             return self.row == other.row and self.col == other.col
#         return False
