import pygame

WIDTH = 600
HEIGHT = WIDTH
ROWS = 8
COLS = ROWS
SQUARE_SIZE = WIDTH // ROWS
PADDING = 10
BORDER = 2
RADIUS = SQUARE_SIZE // 2 - PADDING
FPS = 60
CAPTION = 'Checkers'

# RGB colors
DARK = (60, 42, 33)
LIGHT = (229, 229, 203)
PLAYER_TWO_COLOR = (105, 105, 105)  # up
PLAYER_ONE_COLOR = (255, 0, 0)  # bottom
BLUE = (0, 0, 255)
DARK_GRAY = (60, 60, 60)

CROWN = pygame.transform.scale(pygame.image.load('util/crown.png'), (50, 25))

MAX_DEPTH = 3
