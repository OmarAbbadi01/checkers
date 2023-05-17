import random

import pygame

from gray_player import GrayPlayer
from model.turn import Turn
from util.constants import SQUARE_SIZE, ROWS, COLS


class EventHandler:

    def __init__(self, board, drawer):
        self.board = board
        self.drawer = drawer
        self.last_valid_moves = []
        self.last_clicked_piece = ()
        self.turn = Turn.MIN
        self.gray_player = GrayPlayer()

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
            # gray player turn
            try:
                move = self.gray_player.play(self.board.matrix)
                old_row, old_col, new_row, new_col = move[0][0], move[0][1], move[1][0], move[1][1]
                # self.board.get_valid_moves(old_row, old_col, Turn.MIN)
                self._move_piece(old_row, old_col, new_row, new_col)
            except Exception as e:
                self._move_randomly()

    def _get_coordinates(self, position):
        return position[1] // SQUARE_SIZE, position[0] // SQUARE_SIZE

    def _draw_valid_spots(self, moves):
        for move in moves:
            self.drawer.draw_valid_spot(move[0], move[1])

    def _coordinate_contains_piece(self, row, col):
        return self.board.matrix[row][col] != 0

    def _move_piece(self, old_row, old_col, new_row, new_col):
        self.board.get_valid_moves(old_row, old_col, self.turn)
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
        self.turn = Turn.MAX if self.turn == Turn.MIN else Turn.MIN

    def _move_randomly(self):
        valid_moves = {}
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.get_piece_at(row, col) in ('G', 'GK'):
                    valid_moves[(row, col)] = self.board.get_valid_moves(row, col, self.turn)
        keys = []
        for key in valid_moves.keys():
            if valid_moves[key]:
                keys.append(key)
        key = random.choice(keys)
        old_row, old_col, new_row, new_col = key[0], key[1], valid_moves[key][0][0], valid_moves[key][0][1]
        self._move_piece(old_row, old_col, new_row, new_col)
