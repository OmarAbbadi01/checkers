from collections import deque

from model.direction import Direction
from model.turn import Turn
from util.constants import *


# from model.piece import Piece


class Board:

    def __init__(self):
        self.matrix = []
        self.gray_left = self.red_left = 12
        self.gray_kings = self.red_kings = 0
        self.initialize_board()

    def initialize_board(self):
        for row in range(ROWS):
            self.matrix.append([])
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    if row <= 2:
                        self.matrix[row].append('G')  # Draw gray pieces
                    elif row >= 5:
                        self.matrix[row].append('R')  # Draw red pieces
                    else:
                        self.matrix[row].append('-')

                else:
                    self.matrix[row].append('-')

    def kill_piece(self, row, col):
        self._validate_coordinate(row, col)
        self.matrix[row][col] = '-'

    def get_valid_moves(self, row, col, turn):
        self._validate_coordinate(row, col)
        valid_moves = []
        if self.matrix[row][col] in ('R', 'RK') and turn == Turn.PLAYER2 \
                or self.matrix[row][col] in ('G', 'GK') and turn == Turn.PLAYER1:
            return valid_moves
        player = self.matrix[row][col]
        opponent = 'G' if player == 'R' else 'R'
        direction = None
        if player in ('RK', 'GK'):
            direction = Direction.BOTH
        elif player == 'R':
            direction = Direction.UPWARD
        elif player == 'G':
            direction = Direction.DOWNWARD

    def _get_downward_moves(self, row, col, opponent):
        right, left = 1, -1
        moves = []
        if self._valid_down_coordinate(row + 1, col + 1):
            

        if self._valid_down_coordinate(row + 1, col - 1):

    def _valid_down_coordinate(self, row, col):
        return ROWS > row >= 0 and COLS > col >= 0

    def _get_opponent(self, row, col):
        self._validate_coordinate(row, col)
        if self.matrix[row][col] == 'R':
            return 'G'
        elif self.matrix[row][col] == 'G':
            return 'R'
        return '-'

    def move_piece(self, old_row, old_col, new_row, new_col):
        self._validate_coordinate(old_row, old_col)
        self._validate_coordinate(new_row, new_col)
        if self.matrix[old_row][old_col] == '-':
            raise Exception('No Move For Empty Piece!')
        self.matrix[old_row][old_col], self.matrix[new_row][new_col] = self.matrix[new_row][new_col], \
            self.matrix[old_row][old_col]

    def get_piece_at(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col]

    def piece_exists_at(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col] != '-'

    #
    # def get_piece_color_at(self, row, col):
    #     if not self.piece_exists_at(row, col):
    #         raise Exception('No Color For No Piece!')
    #     return self.matrix[row][col].color

    def is_piece_king(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col] == 'RK' or self.matrix[row][col] == 'GK'

    def _validate_coordinate(self, row, col):
        if row >= ROWS or col >= COLS or row <= -1 or col <= -1:
            raise Exception('Invalid Coordinate!')

    def get_piece_color_at(self, row, col):
        return PLAYER_ONE_COLOR if self.matrix[row][col] in ('R', 'RK') else PLAYER_TWO_COLOR
