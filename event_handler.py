import pygame

from model.turn import Turn
from util.constants import SQUARE_SIZE


class EventHandler:

    def __init__(self, board, drawer):
        self.board = board
        self.drawer = drawer
        self.last_valid_moves = []
        self.last_clicked_piece = ()
        self.turn = Turn.PLAYER1

    def handle(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        self.drawer.clear_valid_spots(self.last_valid_moves)

        row, col = self._get_coordinates(pygame.mouse.get_pos())

        if self.board.piece_exists_at(row, col):
            moves = self.board.get_valid_moves(row, col, self.turn)
            self._draw_valid_spots(moves)
            self.last_valid_moves = moves
            self.last_clicked_piece = (row, col)

        elif (row, col) in self.last_valid_moves:
            self._move_piece(self.last_clicked_piece[0], self.last_clicked_piece[1], row, col)
            self.last_clicked_piece = ()
            self.last_valid_moves = []

    def _get_coordinates(self, position):
        return position[1] // SQUARE_SIZE, position[0] // SQUARE_SIZE

    def _draw_valid_spots(self, moves):
        for move in moves:
            self.drawer.draw_valid_spot(move[0], move[1])

    def _coordinate_contains_piece(self, row, col):
        return self.board.matrix[row][col] != 0

    def _move_piece(self, old_row, old_col, new_row, new_col):
        killed = self.board.move_piece(old_row, old_col, new_row, new_col)
        self._redraw_piece(old_row, old_col, new_row, new_col)
        self.swap_turn()
        for coordinate in killed:
            self.drawer.draw_blank(coordinate[0], coordinate[1])

    def _redraw_piece(self, old_row, old_col, new_row, new_col):
        self.drawer.draw_piece(new_row, new_col, self.board.get_piece_color_at(new_row, new_col),
                               self.board.is_piece_king(new_row, new_col))
        self.drawer.draw_blank(old_row, old_col)

    def swap_turn(self):
        self.turn = Turn.PLAYER1 if self.turn == Turn.PLAYER2 else Turn.PLAYER2
