import pygame
from controllers.game import Game
from controllers.botgame import BotGame
from views.indexview import IndexView
from views.endview import EndView
from time import sleep

menu = IndexView()
mode, difficulty = menu.run()

if mode == 0 or (mode == 1 and difficulty == 0):
    pygame.quit()
    exit()
if mode == 1:
    game = BotGame(difficulty, 600)
else:
    game = Game(600)

running = True
while running:
    game.view.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            is_end = game.play(x, y)
            if is_end:
                sleep(0.5)
                running = False
end_view = EndView(len(game.board.black), len(game.board.white))
end_view.run()
pygame.quit()
