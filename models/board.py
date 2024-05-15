from enums.disc import Disc
from enums.direction import Direction


# Square Board 8*8
class Board:
    def __init__(self):
        self.grid = [[Disc.EMPTY for _ in range(8)] for _ in range(8)]
        self.black = {(3, 4), (4, 3)}
        self.white = {(3, 3), (4, 4)}
        self.grey = {(3, 2): [(3, 4, Direction.LEFT)], (2, 3): [(4, 3, Direction.UP)], (5, 4): [(3, 4, Direction.DOWN)], (4, 5): [(4, 3, Direction.RIGHT)]}
        for x, y in self.black:
            self.grid[x][y] = Disc.BLACK
        for x, y in self.white:
            self.grid[x][y] = Disc.WHITE
        for x, y in self.grey.keys():
            self.grid[x][y] = Disc.GREY

    def clear_grey(self):
        for x, y in self.grey.keys():
            self.grid[x][y] = Disc.EMPTY
        self.grey.clear()

    def expand(self, x, y, disc):
        self.grid[x][y] = disc
        if disc == Disc.BLACK:
            self.black.add((x, y))
        elif disc == Disc.WHITE:
            self.white.add((x, y))
        li = self.grey.pop((x, y))
        self.clear_grey()
        for row, col, direction in li:
            row, col = direction.next_position(row, col)
            while (row, col) != (x, y):
                if self.grid[row][col] == Disc.WHITE:
                    self.white.discard((row, col))
                    self.black.add((row, col))
                elif self.grid[row][col] == Disc.BLACK:
                    self.black.discard((row, col))
                    self.white.add((row, col))
                self.grid[row][col] = disc
                row, col = direction.next_position(row, col)

    def check_grey_in_one_direction(self, xc, yc, opposite_disc, direction):
        x, y = direction.next_position(xc, yc)
        is_opposite_disc_found = False
        while 0 <= x < 8 and 0 <= y < 8 and self.grid[x][y] == opposite_disc:
            is_opposite_disc_found = True
            x, y = direction.next_position(x, y)
        if 0 <= x < 8 and 0 <= y < 8 and (self.grid[x][y] == Disc.EMPTY or self.grid[x][y] == Disc.GREY) and is_opposite_disc_found:
            if not(self.grey.get((x, y))):
                self.grey[(x, y)] = []
            self.grey[(x, y)].append((xc, yc, direction))
            self.grid[x][y] = Disc.GREY

    def update_grey(self, opposite_disc):
        li = self.white if opposite_disc == Disc.BLACK else self.black
        for xc, yc in li:
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.LEFT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.RIGHT)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.UP)
            self.check_grey_in_one_direction(xc, yc, opposite_disc, Direction.DOWN)

    def update(self, row, col, disc):
        self.expand(row, col, disc)
        self.update_grey(disc)

    def get(self, row, col):
        return self.grid[row][col]

    def is_full(self):
        black_cnt = len(self.black)
        white_cnt = len(self.white)
        return black_cnt == 0 or white_cnt == 0 or black_cnt + white_cnt == 64

    def has_grey(self):
        return len(self.grey) != 0
