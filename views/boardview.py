import pygame
from enums.disc import Disc


class View:
    def __init__(self, board, length=600):
        pygame.init()
        pygame.display.set_caption("Othello")
        self.canvas = pygame.display.set_mode((length, length))
        self.board = board
        self.length = length
        self.tile_length = length / 8
        self.radius = self.tile_length / 2 - 5

    def center(self, row, col):
        return col * self.tile_length + self.tile_length / 2, row * self.tile_length + self.tile_length / 2

    def draw(self):
        # Draw background
        pygame.draw.rect(self.canvas, "#009067", (0, 0, self.length, self.length))
        # Draw lines
        for i in range(9):
            # Horizontal line
            pygame.draw.line(self.canvas, "#000000", (i * self.tile_length, 0), (i * self.tile_length, self.length), 1)
            # Vertical line
            pygame.draw.line(self.canvas, "#000000", (0, i * self.tile_length), (self.length, i * self.tile_length), 1)
        # Draw discs
        if type(self.board) is None:
            return
        for row in range(8):
            for col in range(8):
                if self.board.grid[row][col] == Disc.BLACK:
                    pygame.draw.circle(self.canvas, "#000000", self.center(row, col), self.radius)
                elif self.board.grid[row][col] == Disc.WHITE:
                    pygame.draw.circle(self.canvas, "#ffffff", self.center(row, col), self.radius)
                elif self.board.grid[row][col] == Disc.GREY:
                    pygame.draw.circle(self.canvas, "#888888", self.center(row, col), self.radius)
        pygame.display.update()

    def get_row_col(self, screen_x, screen_y):
        return int(screen_y // self.tile_length), int(screen_x // self.tile_length)
