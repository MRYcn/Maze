import pygame

#level selection page

class UI7:
    def __init__(self,game):
        self.game=game
        font = pygame.font.Font('res/font/DroidSansChinese.ttf', 45)
        self.back_text = font.render('«返回', True, (0, 0, 0), None)

    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back_text,(125,80),0)

    def update(self,press_pos=False,mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            pass