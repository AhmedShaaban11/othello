from models.board import Board, Disc
from models.player import Player
from views.boardview import BoardView


class Game:
    def __init__(self, canvas, screen_size=600):
        self.board = Board()
        self.player1 = Player(Disc.BLACK, 30)
        self.player2 = Player(Disc.WHITE, 30)
        self.turn = self.player1
        self.view = BoardView(self.board, self, canvas, screen_size)

    def check_and_update_state(self):
        if self.board.is_full() or not self.player1.has_moves() or not self.player2.has_moves():
            return True
        # If current player hasn't a valid move, go to the next player
        if not self.board.has_moves():
            self.board.create_next_moves(self.turn.disc)
            if not self.board.has_moves():
                return True
            self.turn = self.player1 if self.turn == self.player2 else self.player2
        return False

    def play(self, x, y):
        x, y = self.view.get_row_col(x, y)
        if self.board.get_disc(x, y) != Disc.GREY:
            return
        self.board.apply_move(x, y, self.turn.disc)
        self.turn.decrease_moves()
        self.turn = self.player1 if self.turn == self.player2 else self.player2
