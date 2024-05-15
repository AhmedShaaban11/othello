import pygame
from controllers.game import Game
from controllers.botgame import BotGame
from views.indexview import IndexView
from views.endview import EndView


def main():
    width = 900
    height = 600
    pygame.init()
    pygame.display.set_caption("Othello")
    canvas = pygame.display.set_mode((width, height))
    menu = IndexView(canvas, width, height)
    mode, difficulty = menu.run()
    if mode == 0 or (mode == 1 and difficulty == 0):
        pygame.quit()
        exit()
    if mode == 1:
        game = BotGame(difficulty, canvas, width, height)
    else:
        game = Game(canvas, width, height)
    game.view.run()
    end_view = EndView(len(game.board.black), len(game.board.white), canvas, width, height)
    end_view.run()
    pygame.quit()


if __name__ == "__main__":
    main()
