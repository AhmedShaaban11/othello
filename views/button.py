import pygame


class Button:
    def __init__(self, canvas, x, y, width, height, text, font_color, background_color, command=None):
        self.text = text
        self.width = width
        self.height = height
        self.font_color = font_color
        self.background_color = background_color
        self.command = command
        self.x = x
        self.y = y
        self.canvas = canvas
        self.draw()

    def draw(self):
        pygame.draw.rect(self.canvas, self.background_color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, self.font_color)
        self.canvas.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))

    def collide_point(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def click(self):
        return self.command()
