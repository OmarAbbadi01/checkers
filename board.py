from model.direction import Direction
from model.turn import Turn
from util.constants import *


class Board:

    def __init__(self):
        self.matrix = []
        self.gray_left = self.red_left = 12
        self.gray_kings = self.red_kings = 0
        self.to_be_killed = {}
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
        self.to_be_killed = {}
        valid_moves = []
        if self.matrix[row][col] in ('R', 'RK') and turn == Turn.PLAYER2 \
                or self.matrix[row][col] in ('G', 'GK') and turn == Turn.PLAYER1:
            return valid_moves
        player = self.matrix[row][col]
        opponents = self._get_opponent(row, col)
        direction = None
        if player in ('RK', 'GK'):
            direction = Direction.BOTH
        elif player == 'R':
            direction = Direction.UPWARD
        elif player == 'G':
            direction = Direction.DOWNWARD
        valid_moves = self._get_all_moves(row, col, direction, opponents)
        print(self.to_be_killed)
        return valid_moves

    def _get_all_moves(self, row, col, direction, opponents):
        moves = []
        can_be_killed = []
        if direction == Direction.DOWNWARD:
            self._get_most_deep_move(row + 1, col + 1, 1, 1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

            self._get_most_deep_move(row + 1, col - 1, 1, -1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

        elif direction == Direction.UPWARD:
            self._get_most_deep_move(row - 1, col + 1, -1, 1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

            self._get_most_deep_move(row - 1, col - 1, -1, -1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

        elif direction == Direction.BOTH:
            self._get_most_deep_move(row + 1, col + 1, 1, 1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

            self._get_most_deep_move(row + 1, col - 1, 1, -1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

            self._get_most_deep_move(row - 1, col + 1, -1, 1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

            self._get_most_deep_move(row - 1, col - 1, -1, -1, opponents, row, col, moves, can_be_killed)
            can_be_killed = self._add_move_to_be_killed_dictionary(moves, can_be_killed)

        return moves

    def _add_move_to_be_killed_dictionary(self, moves, can_be_killed):
        if moves:
            if moves[-1] in self.to_be_killed:
                old_array = self.to_be_killed[moves[-1]]
                can_be_killed.extend(old_array)
                self.to_be_killed[moves[-1]] = can_be_killed
            else:
                self.to_be_killed[moves[-1]] = can_be_killed
        return []

    def _get_most_deep_move(self, row, col, row_direction, col_direction, opponents, current_row, current_col, moves,
                            can_be_killed):
        if not self._valid_coordinate(row, col):
            return

        elif self.matrix[row][col] in opponents:
            if self.matrix[row - row_direction][col - col_direction] in opponents:
                return
            self._get_most_deep_move(row + row_direction, col + col_direction, row_direction, col_direction,
                                     opponents, current_row, current_col, moves, can_be_killed)

        elif self.matrix[row][col] == '-':
            if self.matrix[row - row_direction][col - col_direction] == '-':
                return
            elif row - row_direction == current_row and col - col_direction == current_col:
                moves.append((row, col))
                return
            else:
                if self.matrix[row - row_direction][col - col_direction] in opponents:
                    can_be_killed.append((row - row_direction, col - col_direction))
                current_move = (row, col)
                length = len(moves)
                self._get_most_deep_move(row + row_direction, col + col_direction, row_direction,
                                         col_direction, opponents, current_row, current_col, moves, can_be_killed)
                self._get_most_deep_move(row + row_direction, col - col_direction, row_direction,
                                         col_direction * -1, opponents, row, col, moves, can_be_killed)
                if len(moves) == length:
                    moves.append(current_move)

    def _valid_coordinate(self, row, col):
        return ROWS > row >= 0 and COLS > col >= 0

    def _get_opponent(self, row, col):
        self._validate_coordinate(row, col)
        if self.matrix[row][col] in ('R', 'RK'):
            return 'G', 'GK'
        elif self.matrix[row][col] in ('G', 'GK'):
            return 'R', 'RK'
        return '-'

    def move_piece(self, old_row, old_col, new_row, new_col):
        self._validate_coordinate(old_row, old_col)
        self._validate_coordinate(new_row, new_col)
        if self.matrix[old_row][old_col] == '-':
            raise Exception(f'No Move For Empty Piece at: {old_row}, {old_col}')
        self.matrix[old_row][old_col], self.matrix[new_row][new_col] = self.matrix[new_row][new_col], \
            self.matrix[old_row][old_col]

    # def _get_reverse_path(self, old_row, old_col, new_row, new_col):

    def get_piece_at(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col]

    def piece_exists_at(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col] != '-'

    def is_piece_king(self, row, col):
        self._validate_coordinate(row, col)
        return self.matrix[row][col] == 'RK' or self.matrix[row][col] == 'GK'

    def _validate_coordinate(self, row, col):
        if row >= ROWS or col >= COLS or row <= -1 or col <= -1:
            raise Exception(f'Invalid Coordinate! at: {row}, {col}')

    def get_piece_color_at(self, row, col):
        return PLAYER_ONE_COLOR if self.matrix[row][col] in ('R', 'RK') else PLAYER_TWO_COLOR
