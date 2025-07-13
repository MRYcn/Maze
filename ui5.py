import pygame

#settings

class UI5:
    def __init__(self,game):
        self.game=game
        self.back_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        self.back=font1.render('«返回',True,(0,0,0),None)
    
    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)
    
    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=1