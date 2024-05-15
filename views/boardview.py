import pygame
from enums.disc import Disc
from time import sleep


class BoardView:
    def __init__(self, board, game, canvas, width=900, height=600):
        self.canvas = canvas
        self.game = game
        self.board = board
        self.length = width - 300
        self.tile_length = self.length / 8

    def center(self, row, col):
        return col * self.tile_length + self.tile_length / 2, row * self.tile_length + self.tile_length / 2

    def draw_players_states(self):
        font = pygame.font.Font(None, 24)
        text = font.render(f"{self.game.player1.name} ({self.game.player1.disc.name}): {self.game.player1.moves} moves, {len(self.board.black)} discs", True, "#000000")
        self.canvas.blit(text, (self.length + 10, 10))
        text = font.render(f"{self.game.player2.name} ({self.game.player2.disc.name}): {self.game.player2.moves} moves, {len(self.board.white)} discs", True, "#000000")
        self.canvas.blit(text, (self.length + 10, 40))
        text = font.render(f"Turn: {self.game.turn.name}", True, "#000000")
        self.canvas.blit(text, (self.length + 10, 70))

    def draw(self):
        # Draw background
        self.canvas.fill("#009067")
        # Draw lines
        for i in range(9):
            # Horizontal line
            pygame.draw.line(self.canvas, "#000000", (i * self.tile_length, 0), (i * self.tile_length, self.length), 1)
            # Vertical line
            pygame.draw.line(self.canvas, "#000000", (0, i * self.tile_length), (self.length, i * self.tile_length), 1)
        # Draw discs
        radius = self.tile_length / 2 - 5
        for row in range(8):
            for col in range(8):
                disc = self.board.get_disc(row, col)
                pygame.draw.circle(self.canvas, disc.color(), self.center(row, col), radius)
        # Draw players states
        self.draw_players_states()
        pygame.display.update()
        sleep(0.5)

    def get_row_col(self, screen_x, screen_y):
        return int(screen_y // self.tile_length), int(screen_x // self.tile_length)

    def run(self):
        self.draw()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.game.play(x, y)
                else:
                    is_end = self.game.check_and_update_state()
                    if is_end:
                        running = False
                        sleep(1)
