import pygame
from game import Game
SCREEN_LENGTH = 600

pygame.init()
pygame.display.set_caption("Othello")
canvas = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_LENGTH))
game = Game(canvas, SCREEN_LENGTH)
game.board.draw()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            game.play(x, y)
            if game.board.grey == {}:
                game.board.update_grey(game.turn.disc)
                game.turn = game.player1 if game.turn == game.player2 else game.player2
                if game.board.grey == {}:
                    running = False
black_disks_cnt = len(game.board.black)
white_disks_cnt = len(game.board.white)
if black_disks_cnt > white_disks_cnt:
    print("Black wins")
elif black_disks_cnt < white_disks_cnt:
    print("White wins")
else:
    print("Draw")
pygame.quit()
