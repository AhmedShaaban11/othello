import pygame


class EndView:
    def __init__(self, blacks_count, whites_count, canvas, width=600, height=600):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.blacks_count = blacks_count
        self.whites_count = whites_count

    def set_heading(self, heading, y=25):
        font = pygame.font.Font(None, 36)
        text = font.render(heading, True, "#000000")
        self.canvas.blit(text, ((self.width - text.get_width()) // 2, y))

    def run(self):
        self.canvas.fill("#ffffff")
        if self.blacks_count > self.whites_count:
            heading = "Black Wins with " + str(self.blacks_count) + " discs!"
        elif self.blacks_count < self.whites_count:
            heading = "White Wins with " + str(self.whites_count) + " discs!"
        else:
            heading = "Draw!"
        self.set_heading(heading, self.height // 2 - 25)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
