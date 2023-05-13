import pygame

from util.constants import DARK, ROWS, COLS, LIGHT, SQUARE_SIZE, DARK_GRAY, RADIUS, BORDER, CROWN, BLUE, \
    PLAYER_TWO_COLOR, PLAYER_ONE_COLOR


class Drawer:

    def __init__(self, window):
        self.window = window

    def draw_board(self, matrix):
        self.window.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.window, LIGHT, (
                    row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                ))
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] != '-':
                    king = matrix[row][col] == 'RK' or matrix[row][col] == 'GK'
                    color = PLAYER_ONE_COLOR if matrix[row][col] == 'R' or matrix[row][
                        col] == 'RK' else PLAYER_TWO_COLOR
                    self.draw_piece(row, col, color, king)

    def draw_piece(self, row, col, color, king):
        y, x = row * SQUARE_SIZE + SQUARE_SIZE // 2, col * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(self.window, DARK_GRAY, (x, y), RADIUS + BORDER)
        pygame.draw.circle(self.window, color, (x, y), RADIUS)
        if king:
            self.window.blit(CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))

    def draw_blank(self, row, col):
        y, x = row * SQUARE_SIZE, col * SQUARE_SIZE
        pygame.draw.rect(self.window, DARK, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    def draw_valid_spot(self, row, col):
        y, x = row * SQUARE_SIZE + SQUARE_SIZE // 2, col * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(self.window, BLUE, (x, y), RADIUS // 2)

    def clear_valid_spots(self, moves):
        for move in moves:
            self.draw_blank(move[0], move[1])
