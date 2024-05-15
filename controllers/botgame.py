from enums.difficulty import Difficulty
from models.player import Player
from views.boardview import BoardView
from models.board import Board, Disc
from controllers.game import Game
from copy import deepcopy
from time import sleep


class BotGame(Game):
    def __init__(self, difficulty, canvas, screen_size=600):
        super().__init__(canvas, screen_size)
        self.depth = difficulty.depth()

    def check_and_update_state(self):
        if super().check_and_update_state():
            return True
        if self.turn == self.player2:
            self.play_bot()
        return False

    def play(self, x, y):
        if self.turn == self.player1:
            super().play(x, y)

    def play_bot(self):
        self.board = self.alpha_beta_root(self.depth)
        self.view.board = self.board
        self.turn.decrease_moves()
        self.turn = self.player1

    def alpha_beta_root(self, depth, alpha=-100, beta=100):
        max_val = -101
        best_board = None
        for x, y in self.board.grey.keys():
            board = deepcopy(self.board)
            board.apply_move(x, y, self.player2.disc)
            val = self.alpha_beta(board, depth - 1, alpha, beta, False)
            if max_val < val:
                best_board = board
                max_val = val
            alpha = max(alpha, val)
            if beta <= alpha:
                return best_board
        return best_board

    def alpha_beta(self, root_board, depth, alpha, beta, is_max):
        if depth == 0:
            return len(root_board.white)
        ret_val = -100 if is_max else 100
        for x, y in root_board.grey.keys():
            board = deepcopy(root_board)
            if is_max:
                board.apply_move(x, y, self.player2.disc)
                val = self.alpha_beta(board, depth - 1, alpha, beta, not is_max)
                ret_val = max(ret_val, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    return ret_val
            else:
                board.apply_move(x, y, self.player1.disc)
                val = self.alpha_beta(board, depth - 1, alpha, beta, not is_max)
                ret_val = min(ret_val, val)
                beta = min(beta, val)
                if beta <= alpha:
                    return ret_val
        return ret_val
