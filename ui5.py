import pygame

#settings

class UI5:
    def __init__(self,game):
        self.game=game
        self.suf1_rect=self.back_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',50)
        self.suf1=pygame.Surface((200,400))
        self.suf1.fill((252,232,55))
        self.suf1_text=font1.render('用户',True,(0,0,0),None)

        font2=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        self.back = font2.render('«返回', True, (0, 0, 0), None)

    def display(self):
        self.suf1_rect=self.game.blit_to_sc(self.suf1,(342,320),0)
        self.game.blit_to_sc(self.suf1_text,(300,480),0)
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)

    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=1
        elif self.suf1_rect.collidepoint(press_pos):
            self.game.st=10
