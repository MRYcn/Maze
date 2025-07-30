import pygame
import pygame.transform as pt

#suspend page

class UI11:
    def __init__(self,game):
        self.game=game

        font1 = pygame.font.Font('res/font/DFPGB_Y5.ttf', 95)
        font2 = pygame.font.Font('res/font/DFPGB_Y5.ttf', 45)
        self.title=font1.render(' 删除所有数据？',True,(0,0,0),None)

        self.back_rect=None
        self.back_text=font2.render('<<返回',True,(0,0,0),None)

        self.confirm_rect=None
        self.confirm_suf=pt.scale(pygame.image.load('res/pic/ui0_suf.png'),(200,70))
        self.confirm_suf.set_alpha((150))
        self.confirm_text=font2.render('确认',True,(0,0,0),None)


    def display(self):
        self.game.blit_to_sc(self.title,(642,200),0)
        self.back_rect=self.game.blit_to_sc(self.back_text,(125,80),0)
        self.confirm_rect=self.game.blit_to_sc(self.confirm_suf,(642,450),0)
        self.game.blit_to_sc(self.confirm_text,(642,450),0)

    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=10
        elif self.confirm_rect.collidepoint(press_pos):
            self.game.data=self.game.dm.DEF_DATA
            self.game.st=10
