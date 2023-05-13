import pygame.time

from board import Board
from drawer import Drawer
from event_handler import EventHandler
from util.constants import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)


def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()
    drawer = Drawer(window)
    handler = EventHandler(board, drawer)
    drawer.draw_board(board.matrix)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                handler.handle(event)

            pygame.display.update()

    pygame.quit()


main()
