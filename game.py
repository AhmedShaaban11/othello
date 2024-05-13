from board import Board, Disc
from player import Player


class Game:
    def __init__(self, canvas, board_length=400):
        self.board = Board(canvas, board_length)
        self.player1 = Player(Disc.BLACK)
        self.player2 = Player(Disc.WHITE)
        self.turn = self.player1

    def play(self, x, y):
        if self.board.get(x, y) != Disc.GREY:
            return
        self.board.update(x, y, self.turn.disc)
        self.turn = self.player1 if self.turn == self.player2 else self.player2
        self.board.draw()
