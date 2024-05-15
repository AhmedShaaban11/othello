from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def next_position(self, x, y):
        if self == Direction.UP:
            return x - 1, y
        elif self == Direction.DOWN:
            return x + 1, y
        elif self == Direction.LEFT:
            return x, y - 1
        elif self == Direction.RIGHT:
            return x, y + 1
        return x, y
