import pygame

#checkout page

class UI9:
    def __init__(self,game):
        self.game=game

        font1 = pygame.font.Font('res/font/DFPGB_Y5.ttf', 95)
        font2 = pygame.font.Font('res/font/DFPGB_Y5.ttf', 45)
        self.result=font1.render(' 过关！',True,(0,0,0),None)

        self.back_rect=None
        self.back_suf=pygame.Surface((200,70))
        self.back_suf.fill((255,255,255))
        self.back_suf.set_alpha(150)
        self.back_font=font2.render('返回',True,(0,0,0),None)

    def display(self):
        self.game.blit_to_sc(self.result,(642,200),0)
        self.back_rect=self.game.blit_to_sc(self.back_suf,(642,450),0)
        self.game.blit_to_sc(self.back_font,(642,450),0)

    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=4