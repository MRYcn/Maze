import pygame

#mode selection page

class UI1:
    def __init__(self,game):
        self.game=game
        self.suf1_rect=self.suf2_rect=self.suf3_rect=self.back_rect=None
        font1=pygame.font.Font('res/font/DFPGB_Y5.ttf',50)
        self.suf1=pygame.image.load('res/pic/mode_suf1.png')
        self.suf1.set_alpha((150))
        self.suf1_text=font1.render('关卡',True,(0,0,0),None)
        self.suf2=pygame.image.load('res/pic/mode_suf2.png')
        self.suf2.set_alpha((150))
        self.suf2_text=font1.render('排位',True,(0,0,0),None)
        self.suf3=pygame.image.load('res/pic/mode_suf3.png')
        self.suf3.set_alpha((150))
        self.suf3_text=font1.render('设置',True,(0,0,0),None)
        
        font2=pygame.font.Font('res/font/DFPGB_Y5.ttf',45)
        self.back=font2.render('<<返回',True,(0,0,0),None)
    
    def display(self):
        self.suf1_rect=self.game.blit_to_sc(self.suf1,(342,320),0)
        self.game.blit_to_sc(self.suf1_text,(300,480),0)
        self.suf2_rect=self.game.blit_to_sc(self.suf2,(642,320),0)
        self.game.blit_to_sc(self.suf2_text,(600,480),0)
        self.suf3_rect=self.game.blit_to_sc(self.suf3,(942,320),0)
        self.game.blit_to_sc(self.suf3_text,(900,480),0)
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)
    
    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=0
        elif self.suf1_rect.collidepoint(press_pos):
            self.game.ui4.update_progress()
            self.game.st=4
        elif self.suf2_rect.collidepoint(press_pos):
            self.game.st=6
        elif self.suf3_rect.collidepoint(press_pos):
            self.game.st=5