import copy

from board import Board
from model.turn import Turn
from util.constants import MAX_DEPTH, ROWS, COLS


class GrayPlayer:
    def __init__(self):
        self.board = Board()
        pass

    def play(self, matrix):
        best_move = self.minimax(matrix, MAX_DEPTH, True)[1]
        return best_move

    def minimax(self, matrix, depth, maximizing_player):
        if depth == 0 or self.is_game_over(matrix):
            return self.evaluate(matrix), None

        turn = self._get_turn(maximizing_player)
        valid_moves = self.get_all_valid_moves(matrix, turn)
        old_matrix = copy.deepcopy(matrix)
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for old_coordinate in valid_moves:
                new_coordinates = valid_moves[old_coordinate][0]
                for option in new_coordinates:
                    old_row, old_col = old_coordinate[0], old_coordinate[1]
                    new_row, new_col = option[0], option[1]
                    new_matrix = self.make_move(matrix, old_row, old_col, new_row, new_col,
                                                valid_moves[old_coordinate][1])
                    evaluation = self.minimax(new_matrix, depth - 1, False)[0]
                    new_matrix = copy.deepcopy(old_matrix)
                    if evaluation > max_eval:
                        max_eval = evaluation
                        best_move = ((old_row, old_col), (new_row, new_col))
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for old_coordinate in valid_moves:
                new_coordinates = valid_moves[old_coordinate][0]
                for option in new_coordinates:
                    old_row, old_col = old_coordinate[0], old_coordinate[1]
                    new_row, new_col = option[0], option[1]
                    new_matrix = self.make_move(matrix, old_row, old_col, new_row, new_col,
                                                valid_moves[old_coordinate][1])
                    evaluation = self.minimax(new_matrix, depth - 1, True)[0]
                    new_matrix = copy.deepcopy(old_matrix)
                    if evaluation < min_eval:
                        min_eval = evaluation
                        best_move = old_coordinate
            return min_eval, best_move

    def evaluate(self, matrix):
        normal = 'G'
        king = 'GK'
        evaluation = 0
        for row in matrix:
            for element in row:
                if element == normal:
                    evaluation += 1
                elif element == king:
                    evaluation += 2
        return evaluation

    def is_game_over(self, matrix):
        reds, grays = 0, 0
        for row in matrix:
            for element in row:
                if element in ('R', 'RK'):
                    reds += 1
                elif element in ('G', 'GK'):
                    grays += 1
        return reds == 0 or grays == 0

    def get_all_valid_moves(self, matrix, turn):
        self.board.set_matrix(matrix)
        valid_moves = {}
        for row in range(ROWS):
            for col in range(COLS):
                moves = self.board.get_valid_moves(row, col, turn)
                if moves:
                    valid_moves[(row, col)] = (moves, self.board.to_be_killed)

        return valid_moves

    def make_move(self, matrix, old_row, old_col, new_row, new_col, to_be_killed):
        self.board.set_matrix(copy.deepcopy(matrix))
        self.board.to_be_killed = to_be_killed
        self.board.move_piece(old_row, old_col, new_row, new_col)
        return copy.deepcopy(self.board.matrix)

    # def roll_back(self, matrix, old_row, old_col, new_row, new_col, was_killed, old):
    #     self.board.set_matrix(matrix.deepcopy())
    #     self.board.

    def _get_turn(self, maximizing_player):
        return Turn.MAX if maximizing_player else Turn.MIN
