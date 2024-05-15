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

    def expand_move(self, x, y, disc):
        self.grid[x][y] = disc
        self.black.add((x, y)) if disc == Disc.BLACK else self.white.add((x, y))
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

    def add_move(self, xc, yc, opponent_disc, direction):
        x, y = direction.next_position(xc, yc)
        is_opponent_disc_found = False
        while 0 <= x < 8 and 0 <= y < 8 and self.grid[x][y] == opponent_disc:
            is_opponent_disc_found = True
            x, y = direction.next_position(x, y)
        if 0 <= x < 8 and 0 <= y < 8 and (self.grid[x][y] == Disc.EMPTY or self.grid[x][y] == Disc.GREY) and is_opponent_disc_found:
            if not(self.grey.get((x, y))):
                self.grey[(x, y)] = []
            self.grey[(x, y)].append((xc, yc, direction))
            self.grid[x][y] = Disc.GREY

    def create_next_moves(self, opponent_disc):
        li = self.white if opponent_disc == Disc.BLACK else self.black
        for xc, yc in li:
            for direction in Direction:
                self.add_move(xc, yc, opponent_disc, direction)

    def apply_move(self, row, col, disc):
        if self.get_disc(row, col) != Disc.GREY:
            return
        self.expand_move(row, col, disc)
        self.create_next_moves(disc)

    def get_disc(self, row, col):
        return self.grid[row][col]

    def is_full(self):
        black_cnt = len(self.black)
        white_cnt = len(self.white)
        return black_cnt == 0 or white_cnt == 0 or black_cnt + white_cnt == 64

    def has_moves(self):
        return len(self.grey) != 0
