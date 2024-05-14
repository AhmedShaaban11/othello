from models.board import Board, Disc
from models.player import Player
from views.boardview import View


class Game:
    def __init__(self, screen_size=600):
        self.board = Board()
        self.player1 = Player(Disc.BLACK)
        self.player2 = Player(Disc.WHITE)
        self.turn = self.player1
        self.view = View(self.board, screen_size)

    def play(self, x, y):
        x, y = self.view.get_row_col(x, y)
        if self.board.get(x, y) != Disc.GREY and len(self.board.grey) != 0:
            return
        if len(self.board.grey) == 0:
            self.board.update_grey(self.turn.disc)
            if len(self.board.grey) == 0:
                return True
        else:
            self.board.update(x, y, self.turn.disc)
        self.turn = self.player1 if self.turn == self.player2 else self.player2
        self.view.draw()
        if self.board.is_full():
            return True
        return False
