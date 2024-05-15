from enum import Enum


class Disc(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    GREY = 3

    def color(self):
        if self == self.EMPTY:
            return "#009067"
        elif self == self.BLACK:
            return "#000000"
        elif self == self.WHITE:
            return "#ffffff"
        elif self == self.GREY:
            return "#888888"
        return "#000000"
