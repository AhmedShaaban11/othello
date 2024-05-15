class Player:
    def __init__(self, disc, moves=30):
        self.disc = disc
        self.moves = moves

    def decrease_moves(self):
        self.moves -= 1

    def has_moves(self):
        return self.moves > 0
