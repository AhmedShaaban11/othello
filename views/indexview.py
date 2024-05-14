import pygame
from views.button import Button
from enums.difficulty import Difficulty


class IndexView:
    def __init__(self, width=600, height=600):
        pygame.init()
        pygame.display.set_caption("Othello")
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((width, height))

    def set_heading(self, heading):
        font = pygame.font.Font(None, 36)
        text = font.render(heading, True, "#000000")
        self.canvas.blit(text, ((self.width - text.get_width()) // 2, 25))

    def set_index_view(self):
        self.canvas.fill("#ffffff")
        self.set_heading("Othello")
        btn1 = Button(self.canvas, 150, 250, 300, 75, "1 Player", "#ffffff", "#000000", lambda: (1, self.run_choose_difficulty()))
        btn2 = Button(self.canvas, 150, 350, 300, 75, "2 Players", "#ffffff", "#000000", lambda: (2, None))
        pygame.display.flip()
        return [btn1, btn2]

    def set_difficulty_view(self):
        self.canvas.fill("#ffffff")
        self.set_heading("Choose Difficulty")
        btn1 = Button(self.canvas, 150, 200, 300, 75, "Easy", "#ffffff", "#000000", lambda: Difficulty.EASY)
        btn2 = Button(self.canvas, 150, 300, 300, 75, "Medium", "#ffffff", "#000000", lambda: Difficulty.MEDIUM)
        btn3 = Button(self.canvas, 150, 400, 300, 75, "Hard", "#ffffff", "#000000", lambda: Difficulty.HARD)
        pygame.display.flip()
        return [btn1, btn2, btn3]

    def run_btn_list(self, btn_list):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for btn in btn_list:
                        if btn.collide_point(x, y):
                            return btn.click()
        pygame.quit()
        return 0

    def run_choose_difficulty(self):
        btn_list = self.set_difficulty_view()
        return self.run_btn_list(btn_list)

    def run(self):
        btn_list = self.set_index_view()
        ret = self.run_btn_list(btn_list)
        if type(ret) is int:
            return ret, None
        return ret
