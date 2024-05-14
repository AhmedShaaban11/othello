from enums.difficulty import Difficulty
from models.player import Player
from views.boardview import View
from models.board import Board, Disc
from copy import deepcopy
from time import sleep


class BotGame:
    def __init__(self, difficulty, screen_size=600):
        self.board = Board()
        self.depth = self.calculate_depth(difficulty)
        self.screen_size = screen_size
        self.player = Player(Disc.BLACK)
        self.bot = Player(Disc.WHITE)
        self.turn = self.player
        self.view = View(self.board, screen_size)

    def calculate_depth(self, difficulty):
        if difficulty == Difficulty.EASY:
            return 1
        elif difficulty == Difficulty.MEDIUM:
            return 3
        elif difficulty == Difficulty.HARD:
            return 5
        return 0

    def play(self, x, y):
        x, y = self.view.get_row_col(x, y)
        if self.board.get(x, y) != Disc.GREY and len(self.board.grey) != 0:
            return
        if len(self.board.grey) == 0:
            self.board.update_grey(self.player.disc)
            if len(self.board.grey) == 0:
                return True
        else:
            self.board.update(x, y, self.player.disc)
        self.view.draw()
        sleep(0.25)
        if len(self.board.grey) == 0:
            self.board.update_grey(self.bot.disc)
            if len(self.board.grey) == 0:
                return True
        else:
            self.board = self.bot_play_root(self.depth)
            self.view.board = self.board
        self.view.draw()
        if self.board.is_full():
            return True
        return False

    def bot_play_root(self, depth, alpha=-100, beta=100):
        max_val = -101
        best_board = None
        for x, y in self.board.grey.keys():
            board = deepcopy(self.board)
            board.update(x, y, self.bot.disc)
            val = self.bot_play(board, depth - 1, alpha, beta)
            if max_val < val:
                best_board = board
                max_val = val
            alpha = max(alpha, val)
            if beta <= alpha:
                return best_board
        return best_board

    def bot_play(self, root_board, depth, alpha, beta):
        if depth == 0:
            return len(root_board.white)
        is_max = depth % 2 == 1
        ret_val = -100 if is_max else 100
        for x, y in root_board.grey.keys():
            board = deepcopy(root_board)
            if is_max:
                board.update(x, y, self.bot.disc)
                val = self.bot_play(board, depth - 1, alpha, beta)
                ret_val = max(ret_val, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    return ret_val
            else:
                board.update(x, y, self.player.disc)
                val = self.bot_play(board, depth - 1, alpha, beta)
                ret_val = min(ret_val, val)
                beta = min(beta, val)
                if beta <= alpha:
                    return ret_val
        return ret_val
