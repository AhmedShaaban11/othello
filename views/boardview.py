import pygame
from enums.disc import Disc
from time import sleep


class BoardView:
    def __init__(self, board, game, canvas, screen_length=600):
        self.canvas = canvas
        self.game = game
        self.board = board
        self.tile_length = screen_length / 8
        self.length = screen_length

    def center(self, row, col):
        return col * self.tile_length + self.tile_length / 2, row * self.tile_length + self.tile_length / 2

    def draw(self):
        # Draw background
        self.canvas.fill("#009067")
        # Draw lines
        for i in range(9):
            # Horizontal line
            pygame.draw.line(self.canvas, "#000000", (i * self.tile_length, 0), (i * self.tile_length, self.length), 1)
            # Vertical line
            pygame.draw.line(self.canvas, "#000000", (0, i * self.tile_length), (self.length, i * self.tile_length), 1)
        # Draw discs
        radius = self.tile_length / 2 - 5
        for row in range(8):
            for col in range(8):
                disc = self.board.get(row, col)
                pygame.draw.circle(self.canvas, disc.color(), self.center(row, col), radius)
        pygame.display.update()

    def get_row_col(self, screen_x, screen_y):
        return int(screen_y // self.tile_length), int(screen_x // self.tile_length)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.draw()
                sleep(0.2)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.game.play(x, y)
                else:
                    is_end = self.game.update_state()
                    if is_end:
                        running = False
