import pygame
from disc import Disc
from direction import Direction


# Square Board 8*8
class Board:
    def __init__(self, canvas, length=400):
        self.canvas = canvas
        self.board = [[Disc.EMPTY for _ in range(8)] for _ in range(8)]
        self.black = {(3, 4), (4, 3)}
        self.white = {(3, 3), (4, 4)}
        self.grey = {(3, 2): [(3, 4, Direction.LEFT)], (2, 3): [(4, 3, Direction.UP)], (5, 4): [(3, 4, Direction.DOWN)], (4, 5): [(4, 3, Direction.RIGHT)]}
        for x, y in self.black:
            self.board[x][y] = Disc.BLACK
        for x, y in self.white:
            self.board[x][y] = Disc.WHITE
        for x, y in self.grey.keys():
            self.board[x][y] = Disc.GREY
        self.length = length
        self.tile_length = length / 8
        self.radius = self.tile_length / 2 - 5

    def get_center(self, row, col):
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
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == Disc.BLACK:
                    pygame.draw.circle(self.canvas, "#000000", self.get_center(row, col), self.radius)
                elif self.board[row][col] == Disc.WHITE:
                    pygame.draw.circle(self.canvas, "#ffffff", self.get_center(row, col), self.radius)
                elif self.board[row][col] == Disc.GREY:
                    pygame.draw.circle(self.canvas, "#888888", self.get_center(row, col), self.radius)
        pygame.display.flip()

    def clear_grey(self):
        for x, y in self.grey.keys():
            self.board[x][y] = Disc.EMPTY
        self.grey.clear()

    def expand(self, x, y, disc):
        self.board[x][y] = disc
        if disc == Disc.BLACK:
            self.black.add((x, y))
        elif disc == Disc.WHITE:
            self.white.add((x, y))
        li = self.grey.pop((x, y))
        self.clear_grey()
        for row, col, direction in li:
            row, col = self.next_position(row, col, direction)
            while (row, col) != (x, y):
                if self.board[row][col] == Disc.WHITE:
                    self.white.discard((row, col))
                    self.black.add((row, col))
                elif self.board[row][col] == Disc.BLACK:
                    self.black.discard((row, col))
                    self.white.add((row, col))
                self.board[row][col] = disc
                row, col = self.next_position(row, col, direction)

    def next_position(self, x, y, direction):
        if direction == Direction.UP:
            return x - 1, y
        elif direction == Direction.DOWN:
            return x + 1, y
        elif direction == Direction.LEFT:
            return x, y - 1
        elif direction == Direction.RIGHT:
            return x, y + 1
        elif direction == Direction.UP_LEFT:
            return x - 1, y - 1
        elif direction == Direction.UP_RIGHT:
            return x - 1, y + 1
        elif direction == Direction.DOWN_LEFT:
            return x + 1, y - 1
        elif direction == Direction.DOWN_RIGHT:
            return x + 1, y + 1

    def check_grey_in_one_direction(self, xc, yc, opposite_disc, direction):
        x, y = self.next_position(xc, yc, direction)
        is_opposite_disc_found = False
        while 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == opposite_disc:
            is_opposite_disc_found = True
            x, y = self.next_position(x, y, direction)
        if 0 <= x < 8 and 0 <= y < 8 and (self.board[x][y] == Disc.EMPTY or self.board[x][y] == Disc.GREY) and is_opposite_disc_found:
            if not(self.grey.get((x, y))):
                self.grey[(x, y)] = []
            self.grey[(x, y)].append((xc, yc, direction))
            self.board[x][y] = Disc.GREY

    def update_grey(self, opposite_disc):
        li = self.white if opposite_disc == Disc.BLACK else self.black
        for xc, yc in li:
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.LEFT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.RIGHT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.UP)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.DOWN)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.UP_LEFT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.UP_RIGHT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.DOWN_LEFT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.DOWN_RIGHT)

    def update(self, screen_x, screen_y, disc):
        row = int(screen_y // self.tile_length)
        col = int(screen_x // self.tile_length)
        self.expand(row, col, disc)
        self.update_grey(disc)

    def get(self, screen_x, screen_y):
        row = int(screen_y // self.tile_length)
        col = int(screen_x // self.tile_length)
        return self.board[row][col]
