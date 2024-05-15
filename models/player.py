class Player:
    def __init__(self, name, disc, moves=30):
        self.name = name
        self.disc = disc
        self.moves = moves

    def decrease_moves(self):
        self.moves -= 1

    def has_moves(self):
        return self.moves > 0

    def get_name(self):
        return self.name
