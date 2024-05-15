import pygame
from controllers.game import Game
from controllers.botgame import BotGame
from views.indexview import IndexView
from views.endview import EndView


def main():
    pygame.init()
    pygame.display.set_caption("Othello")
    canvas = pygame.display.set_mode((600, 600))
    menu = IndexView(canvas)
    mode, difficulty = menu.run()
    if mode == 0 or (mode == 1 and difficulty == 0):
        pygame.quit()
        exit()
    if mode == 1:
        game = BotGame(difficulty, canvas)
    else:
        game = Game(canvas)
    board_view = game.view
    board_view.run()
    end_view = EndView(len(game.board.black), len(game.board.white), canvas)
    end_view.run()
    pygame.quit()


if __name__ == "__main__":
    main()
