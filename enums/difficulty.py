from enum import Enum


class Difficulty(Enum):
    EASY = 1,
    MEDIUM = 2,
    HARD = 3,

    def depth(self):
        if self == self.EASY:
            return 1
        elif self == self.MEDIUM:
            return 3
        elif self == self.HARD:
            return 5
        return 0
